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

from flask import Flask, jsonify
import json
from database_methods import get_user_info, get_user_friend_invites, get_user_event_invites

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


# Handle favicon request
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)
