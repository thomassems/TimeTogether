import psycopg2

hostname = 'localhost'
database = 'timetogether'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = None
cur = None
try:
        conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
        cur = conn.cursor()
        def add_user(uID, username):
                try:
                        cur.execute("INSERT INTO users (uID, username, friend, lastTalkedTo, priority) VALUES (%s, %s, NULL, NULL, 0)", (uID, username))
                        conn.commit()
                        print("User added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add user")
        def add_friend(uID, username, friend, priority):
                try:    
                        cur.execute("INSERT INTO users (uID, username, friend, lastTalkedTo, priority) VALUES (%s, %s, %s, NULL, %s)", (uID, username, friend, priority))
                        # cur.execute("UPDATE users SET friend = %s WHERE uID = %s", (friend, uID))
                        conn.commit()
                        print("Friend added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add friend")
        def invite_to_event(eID, uID, friendID, eventName, eventTime, eventLocation, eventDescription):
                try:
                        cur.execute("INSERT INTO invites (eID, uID, friendID, response) VALUES (%s, %s, %s, False)", (eID, uID, friendID))
                        #cur.execute("INSERT INTO invites (eID, uID, response) VALUES (%s, %s, NULL)", (eID, uID))
                        conn.commit()
                        cur.execute("INSERT INTO events (eID, eventName, eventTime, eventLocation, eventDescription) VALUES (%s, %s, %s, %s, %s)", (eID, eventName, eventTime, eventLocation, eventDescription))
                        conn.commit()
                        print("Invitation sent successfully")
                except Exception as e:
                        print(e)
                        print("Failed to send invitation")
        def update_event(eID, eventName, eventTime, eventLocation, eventDescription):
                try:
                        cur.execute("UPDATE events SET eventName = %s, eventTime = %s, eventLocation = %s, eventDescription = %s WHERE eID = %s", (eventName, eventTime, eventLocation, eventDescription, eID))
                        conn.commit()
                        print("Event updated successfully")
                except Exception as e:
                        print(e)
                        print("Failed to update event")
        def add_participant_to_event(eID, uID):
                try:
                        cur.execute("INSERT INTO event_participants (eID, uID) VALUES (%s, %s)", (eID, uID))
                        conn.commit()
                        print("Participant added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add participant")
        def accept_invite(eID, friendID): # MAYBE DO A COUPLE EXTRA TRY-CATCH BLOCKS
                try:
                        oID = "SELECT uID FROM invites WHERE eID = %s AND friendID = %s", (eID, friendID)
                        conn.commit()
                        add_participant_to_event(eID, oID)
                        add_participant_to_event(eID, friendID)
                        # other person's ID
                        # cur.execute("UPDATE invites SET response = True WHERE eID = %s AND uID = %s", (eID, uID))
                        print("Invite accepted successfully")
                except Exception as e:
                        print(e)
                        print("Failed to accept invite")

# GETTERS

        def get_user_events(uID):
                try:
                        cur.execute("SELECT eID, eventName, eventTime, eventLocation, eventDescription FROM events WHERE eID IN (SELECT eID FROM event_participants WHERE uID = %s)", (uID))
                        conn.commit()
                        print("Events retrieved successfully")
                        events = []
                        for event in cur:
                                subevents = []
                                subevents.append(event['eID'])
                                subevents.append(event['eventName'])
                                subevents.append(event['eventTime'])
                                subevents.append(event['eventLocation'])
                                subevents.append(event['eventDescription'])
                                events.append(subevents)
                        return events
                except Exception as e:
                        print(e)
                        print("Failed to retrieve events")

        def get_user_friends(uID):
                try:
                        cur.execute("SELECT uID, username, priority FROM users WHERE uID IN (SELECT friend FROM users WHERE uID = %s)", (uID))
                        conn.commit()
                        print("Friends retrieved successfully")
                        friends = []
                        for friend in cur:
                                subfriends = []
                                subfriends.append(friend['uID'])
                                subfriends.append(friend['username'])
                                subfriends.append(friend['priority'])
                                friends.append(subfriends)
                except Exception as e:
                        print(e)
                        print("Failed to retrieve friends")

        def get_user_invites(friendID):
                try:
                        cur.execute("SELECT e.eID, e.eventName, e.eventTime, e.eventLocation, e.eventDescription, i.uID, u.username FROM events e JOIN invites i ON e.eID = i.eID JOIN users u ON i.uID = u.uID WHERE i.friendID = %s", (friendID,))
                        conn.commit()
                        print("Invites retrieved successfully")
                        invites = []
                        for invite in cur:
                                subinvites = []
                                subinvites.append(invite['eID'])
                                subinvites.append(invite['eventName'])
                                subinvites.append(invite['eventTime'])
                                subinvites.append(invite['eventLocation'])
                                subinvites.append(invite['eventDescription'])
                                subinvites.append(invite['uID'])
                                subinvites.append(invite['username'])
                                invites.append(subinvites)
                except Exception as e:
                        print(e)
                        print("Failed to retrieve invites")
        # Example usage:
        cur.close()
        conn.close()
except Exception as e:
        print(e)
        print('Unable to connect to the database')
        exit()