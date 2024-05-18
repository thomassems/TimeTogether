# from flask import Flask, jsonify
# import json
# from database_methods import get_user_info, get_user_friend_invites
# # from user import User

# # def get_user(uID):
# #     lst = get_user_info(uID)
# #     lst.append(get_user_friend_invites(uID))


# # Define a Python list

# my_list = [1, 2, 3, "four", {"five": 5}, [6, 7]]
# json_string = jsonify(my_list)
# print(type(json_string))
# print(json_string)

# # print(get_user(5))

# from flask import Flask, jsonify
# import json
# from database_methods import get_user_info, get_user_friend_invites

# app = Flask(__name__)

# # Example route to use jsonify
# @app.route('/json')
# def get_json():
#     # Define a Python list
#     my_list = [1, 2, 3, "four", {"five": 5}, [6, 7]]
#     return jsonify(my_list)

# # Example function to get user info and friend invites
# @app.route('/user/<int:uID>')
# def get_user(uID):
#     user_info = get_user_info(uID)
#     user_friend_invites = get_user_friend_invites(uID)
#     response_data = {
#         'user_info': user_info,
#         'friend_invites': user_friend_invites
#     }
#     return jsonify(response_data)

# if __name__ == '__main__':
#     app.run(debug=True)

import uuid
from flask import Flask, jsonify, request
import json
from database_methods import accept_invite, accept_req, add_user, friend_req, get_user_info, get_user_friend_invites, get_user_event_invites, invite_to_event, update_priority

app = Flask(__name__)

# Route for the root URL
@app.route('/')
def home():
    return 'Welcome to the Flask Application!'

# Example route to use jsonify
@app.route('/json')
def get_json():
    # Define a Python list
    my_list = [1, 2, 3, "four", {"five": 5}, [6, 7]]
    return jsonify(my_list)

# Example function to get user info and friend invites
@app.route('/user/<int:uID>')
def get_user(uID):
    user_info = get_user_info(uID)
    user_friend_invites = get_user_friend_invites(uID)
    user_event_invites_list = get_user_event_invites(uID)
    
    
    # Parse JSON strings back to Python dictionaries
    user_info_dict = json.loads(user_info) if user_info else None
    user_friend_invites_list = json.loads(user_friend_invites) if user_friend_invites else None
    user_event_invites_list = json.loads(user_event_invites_list) if user_event_invites_list else None
    
    response_data = {
        'user_info': user_info_dict,
        'friend_invites': user_friend_invites_list,
        'event_invites': user_event_invites_list
    }
    return jsonify(response_data)

@app.route('/add', methods=['POST']) ## NOT SURE IF IT WORKS
def add_user_to_db():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Generate a unique identifier for the user
    uID = uuid.uuid4()

    # Call the helper function to add the user to the database
    response, status = add_user(str(uID), username, password)
    return jsonify(response), status

@app.route('/friend_request', methods=['POST'])
def send_friend_request():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    uID = data.get('uID')
    username = data.get('username')
    friend = data.get('friend')
    priority = data.get('priority')

    if not username or not friend or priority is None:
        return jsonify({"error": "Username, friend, and priority are required"}), 400

    # Call the friend_req function
    response, status = friend_req(str(uID), username, friend, priority)
    return jsonify(response), status

@app.route('/accept_friend_request', methods=['POST'])
def accept_friend_request():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    uID = data.get('uID')
    username = data.get('username')
    friend = data.get('friend')

    if not uID or not username or not friend:
        return jsonify({"error": "uID, username, and friend are required"}), 400

    # Call the helper function to accept the friend request
    response, status = accept_req(uID, username, friend)
    return jsonify(response), status

@app.route('/update_priority', methods=['POST'])
def update_friend_priority():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    uID = data.get('uID')
    friend = data.get('friend')
    priority = data.get('priority')

    if not uID or not friend or priority is None:
        return jsonify({"error": "uID, friend, and priority are required"}), 400

    # Call the helper function to update priority
    response, status = update_priority(uID, friend, priority)
    return jsonify(response), status

@app.route('/invite_to_event', methods=['POST'])
def invite_to_event_db():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    eID = data.get('eID')
    uID = data.get('uID')
    friendID = data.get('friendID')
    eventName = data.get('eventName')
    eventTime = data.get('eventTime')
    eventLocation = data.get('eventLocation')
    eventDescription = data.get('eventDescription')

    if not eID or not uID or not friendID or not eventName or not eventTime or not eventLocation or not eventDescription:
        return jsonify({"error": "Incomplete event details"}), 400

    # Call the helper function to invite friends to the event
    response, status = invite_to_event(eID, uID, friendID, eventName, eventTime, eventLocation, eventDescription)
    return jsonify(response), status

@app.route('/accept_invite_to_event', methods=['POST'])
def accept_invite_to_event():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid input"}), 400

    eID = data.get('eID')
    friendID = data.get('friendID')

    if not eID or not friendID:
        return jsonify({"error": "eID and friendID are required"}), 400

    # Call the helper function to accept the invitation
    response, status = accept_invite(eID, friendID)
    return jsonify(response), status

# Handle favicon request
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)
