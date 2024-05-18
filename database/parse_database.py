# first loop through all of the users
from database_methods import get_user_info, get_user_friend_invites

def get_user(uID):
    lst = get_user_info(uID)
    lst.append(get_user_friend_invites(uID))

