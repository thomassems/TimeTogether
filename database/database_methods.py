import psycopg2
import json
from datetime import datetime

hostname = 'localhost'
database = 'timetogether'
username = 'thomassems'
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
        def add_user(uID, username, password):
                try:
                        cur.execute("""INSERT INTO "User" ("uID", "username", "friend", "lastTalkedTo", "priority", "password") VALUES (%s, %s, NULL, NULL, 0, %s)""", (uID, username, password))
                        conn.commit()
                        print("User added successfully")
                        return {"message": "Friend added successfully"}, 201
                except Exception as e:
                        print(e)
                        print("Failed to add user")
                        return {"error": str(e)}, 400

        def friend_req(uID, username, friend, priority):
                try:    
                        cur.execute("""INSERT INTO "User" ("uID", "username", "friend", "lastTalkedTo", "priority") VALUES (%s, %s, %s, NULL, %s)""", (uID, username, friend, priority))
                        conn.commit()
                        print("Friend added successfully")
                        return {"message": "Friend added successfully"}, 201
                except Exception as e:
                        print(e)
                        print("Failed to add friend")
                        return {"error": str(e)}, 400

        def accept_req(uID, username, friend): # Very similar to one above it, just set the priority value to 1
                try:    
                        cur.execute("""INSERT INTO "User" ("uID", "username", "friend", "lastTalkedTo", "priority") VALUES (%s, %s, %s, NULL, 3)""", (uID, username, friend))
                        conn.commit()
                        print("Friend added successfully")
                        return {"message": "Friend added successfully"}, 201
                except Exception as e:
                        print(e)
                        print("Failed to add friend")
                        return {"error": str(e)}, 400

        def update_priority(uID, friend, priority): 
                try:
                        cur.execute("""UPDATE "User" SET "priority" = %s WHERE "uID" = %s AND "friend" = %s""", (priority, uID, friend))
                        print("Priority updated successfully")
                        return {"message": "Priority updated successfully"}, 200
                except Exception as e:
                        print(e)
                        print("Failed to update priority")
                        return {"error": str(e)}, 400

        current_timestamp = datetime.now()

        def invite_to_event(eID, uID, friendID, eventName, eventTime, eventLocation, eventDescription):
                try:
                        cur.execute("""INSERT INTO "events" ("eID", "eventName", "eventTime", "eventLocation", "eventDescription") VALUES (%s, %s, %s, %s, %s)""", (eID, eventName, eventTime, eventLocation, eventDescription))
                        conn.commit()
                        cur.execute("""INSERT INTO "invites" ("eID", "uID", "friendID") VALUES (%s, %s, %s)""", (eID, uID, friendID))
                        conn.commit()
                        print("Invitation sent successfully")
                        return {"message": "Invitation sent successfully"}, 201
                except Exception as e:
                        print(e)
                        print("Failed to send invitation")
                        return {"error": str(e)}, 400

        def update_event(eID, eventName, eventTime, eventLocation, eventDescription):
                try:
                        cur.execute("""UPDATE "events" SET "eventName" = %s, "eventTime" = %s, "eventLocation" = %s, 
                                    "eventDescription" = %s WHERE "eID" = %s""", (eventName, eventTime, eventLocation, eventDescription, eID))
                        conn.commit()
                        print("Event updated successfully")
                        return {"message": "Event updated successfully"}, 201
                except Exception as e:
                        print(e)
                        print("Failed to send invitation")
                        return {"error": str(e)}, 400
        
        def add_participant_to_event(eID, uID):
                try:
                        cur.execute("""INSERT INTO "event_participants" ("eID", "uID") VALUES (%s, %s)""", (eID, uID))
                        conn.commit()
                        print("Participant added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add participant")

        def accept_invite(eID, friendID): 
                try:                        
                        cur.execute(
                        """SELECT "uID" FROM "invites" WHERE "eID" = %s AND "friendID" = %s""", (eID, friendID))
                        result = cur.fetchone()
                        if result is not None:
                                oID = result[0]
                        
                        add_participant_to_event(eID, oID)
                        add_participant_to_event(eID, friendID)
                        print("Invitation accepted successfully")
                        return {"message": "Invitation accepted successfully"}, 201
                except Exception as e:
                        print(e)
                        print("Failed to accept invitation")
                        return {"error": str(e)}, 400

        def get_user_events(uID):
                try:
                        cur.execute(
                        """
                        SELECT "eID", "eventName", "eventTime", "eventLocation", "eventDescription" FROM "events" WHERE "eID" IN 
                        (SELECT "eID" FROM "event_participants" WHERE "uID" = %s)""", (uID,))
        
                        conn.commit()
                        print("Events retrieved successfully")
                        events = []
                        for event in cur:
                                subevents = []
                                subevents.append(event[0])
                                subevents.append(event[1])
                                subevents.append(event[2])
                                subevents.append(event[3])
                                subevents.append(event[4])
                                events.append(subevents)
                        return events
                except Exception as e:
                        print(e)
                        print("Failed to retrieve events")

        def get_user_friends(uID):
                try:
                        cur.execute(
                        """SELECT "uID", "username", "priority" FROM "User" WHERE "uID" IN (SELECT "friend" 
                        FROM "User" WHERE "uID" = %s)""", (uID,))
                        conn.commit()
                        print("Friends retrieved successfully")
                        friends = []
                        for friend in cur:
                                subfriends = []
                                subfriends.append(friend[0])
                                subfriends.append(friend[1])
                                subfriends.append(friend[2])
                                friends.append(subfriends)
                        return friends
                except Exception as e:
                        print(e)
                        print("Failed to retrieve friends")

        def get_user_info(uID):
                try:
                        # First query to get user information
                        cur.execute("""SELECT u1."uID", u1."username", u1."friend", u1."password" 
                                FROM "User" u1
                                WHERE u1."uID" = %s""", (uID,))
                        user_info = cur.fetchone()  # Fetch only one record
                        if user_info is None:
                                raise Exception("User not found")
                        # Extract user information
                        uID, username, friend, password = user_info
                        # Second query to get mutual friends
                        cur.execute("""SELECT u1."uID", u1."username", u1."friend" 
                                FROM "User" u1
                                JOIN "User" u2 ON u1."uID" = u2."friend" AND u1."friend" = u2."uID"
                                WHERE u1."uID" = %s""", (uID,))
                        results = cur.fetchall()
                        # Collect friends' uIDs
                        friends = [row[2] for row in results]

                        # Construct the list
                        lst = [uID, username, friends]

                        # Convert the list to a JSON string
                        json_result = json.dumps(lst)
                        return json_result

                except Exception as e:
                        print(e)
                        print("Failed to retrieve user info")
                        return None

        # print(get_user_info(2))
        # cur.execute("SELECT * FROM \"User\"")
        # result = cur.fetchall()
        # print(result)

        def get_user_event_invites(friend):
                try:
                        cur.execute("""
                        SELECT e."eID", e."eventName", e."eventTime", e."eventLocation", e."eventDescription", i."friendID"
                        FROM "events" e
                        JOIN "invites" i ON e."eID" = i."eID"
                        WHERE i."friendID" = %s
                        AND NOT EXISTS (
                                SELECT 1
                                FROM "event_participants" ep
                                WHERE ep."eID" = e."eID" AND ep."uID" = i."friendID"
                        )
                        """, (friend,))
                        invites = []
                        for invite in cur:
                                subinvites = []
                                subinvites.append(invite[0])
                                subinvites.append(invite[1])
                                subinvites.append(invite[2])
                                subinvites.append(invite[3])
                                subinvites.append(invite[4])
                                subinvites.append(invite[5])
                                invites.append(subinvites)
                        return invites

                except Exception as e:
                        print(e)
                        print("Failed at getting event invites")

        def get_user_friend_invites(friendID): 
                try:
                        cur.execute(
                        """
                        SELECT u1."uID", u1."friend"
                        FROM "User" u1
                        WHERE u1."friend" = %s
                        AND
                        NOT EXISTS(
                                SELECT 1 
                                FROM "User" u3 
                                WHERE u3."uID" = %s 
                                AND u1."uID" = u3."friend"
                        )
                        """, (friendID, friendID,)
                        )
                        conn.commit()
                        print("Invites retrieved successfully")
                        invites = []
                        for invite in cur:
                                subinvites = []
                                subinvites.append(invite[0])
                                subinvites.append(invite[1])
                                invites.append(subinvites)
                        return invites
                except Exception as e:
                        print(e)
                        print("Failed to retrieve invites")

        def update_last_talked_to(uID, friendID):
                try:
                        cur.execute("""UPDATE "User" SET "lastTalkedTo" = %s WHERE "uID" = %s AND "friend" = %s
                        """, (current_timestamp, uID, friendID))

                        cur.execute("""UPDATE "User" SET "lastTalkedTo" = %s
                        WHERE "uID" = %s AND "friend" = %s""", (current_timestamp, friendID, uID))
                except Exception as e:
                        print(e)
                        print("Failed to update last talked to")

        def clear_all():
                cur.execute("""DELETE FROM "event_participants" """)
                cur.execute("""DELETE FROM "User" """)
                cur.execute("""DELETE FROM "events" """)
                cur.execute("""DELETE FROM "invige" """)

        # UNCOMMENT TO DELETE DATABASE ENTRIES!!
        # def get_all_users():
        #         try:
        #                 cur.execute("""SELECT * FROM "User" """)
        #         except Exception as e:
        #                 print(e)
        def close():
                if cur is not None:
                        cur.close()
                if conn is not None:
                        conn.close()

except Exception as e:
        print(e)
        print('Unable to connect to the database')
        exit()

# finally:
#     if 'cur' in locals() and cur is not None and not cur.closed:
#         cur.close()
#     if 'conn' in locals() and conn is not None and not conn.closed:
#         conn.close()