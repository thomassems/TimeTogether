from flask import Flask, jsonify, request
from web3 import Web3

app = Flask(__name__)

# Connect to Ethereum node (e.g., Infura, local node)
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.is_connected():
    print("Connected to Ethereum")
else:
    print("Failed to connect to Ethereum")

# Example endpoint: Get balance of an address
@app.route('/balance/<address>', methods=['GET'])
def get_balance(address):
    try:
        if not web3.isAddress(address):
            return jsonify({"error": "Invalid Ethereum address"}), 400
        balance = web3.eth.get_balance(address)
        ether_balance = web3.fromWei(balance, 'ether')
        return jsonify({"address": address, "balance": ether_balance})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to send a transaction
@app.route('/send', methods=['POST'])
def send_transaction():
    try:
        data = request.get_json()
        from_address = data['from']
        to_address = data['to']
        value = web3.toWei(data['value'], 'ether')
        private_key = data['private_key']
        transaction = {
            'to': to_address,
            'value': value,
            'gas': 21000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.get_transaction_count(from_address),
            'chainId': 1
        }
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return jsonify({"transaction_hash": txn_hash.hex()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get transaction details
@app.route('/transaction/<txn_hash>', methods=['GET'])
def get_transaction(txn_hash):
    try:
        txn = web3.eth.get_transaction(txn_hash)
        return jsonify({
            "hash": txn.hash.hex(),
            "from": txn['from'],
            "to": txn['to'],
            "value": web3.fromWei(txn['value'], 'ether'),
            "gas": txn['gas'],
            "gasPrice": web3.fromWei(txn['gasPrice'], 'gwei'),
            "nonce": txn['nonce'],
            "blockHash": txn['blockHash'].hex() if txn['blockHash'] else None,
            "blockNumber": txn['blockNumber']
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
