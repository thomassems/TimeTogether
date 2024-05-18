import psycopg2
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
        def add_user(uID, username):
                try:
                        cur.execute("""INSERT INTO "User" ("uID", "username", "friend", "lastTalkedTo", "priority") VALUES (%s, %s, NULL, NULL, 0)""", (uID, username))
                        conn.commit()
                        print("User added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add user")

        # add_user(2, "Nick")
        # cur.execute("SELECT * FROM \"User\"")
        # result = cur.fetchall()
        # print(result)

        conn.commit()
        def friend_req(uID, username, friend, priority):
                try:    
                        cur.execute("""INSERT INTO "User" ("uID", "username", "friend", "lastTalkedTo", "priority") VALUES (%s, %s, %s, NULL, %s)""", (uID, username, friend, priority))
                        conn.commit()
                        print("Friend added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add friend")

        # friend_req(3, "Mike", 2, 3)
        # cur.execute("SELECT * FROM \"User\"")
        # result = cur.fetchall()
        # print(result)
        def accept_req(uID, username, friend): # Very similar to one above it, just set the priority value to 1
                try:    
                        cur.execute("""INSERT INTO "User" ("uID", "username", "friend", "lastTalkedTo", "priority") VALUES (%s, %s, %s, NULL, 1)""", (uID, username, friend))
                        conn.commit()
                        print("Friend added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add friend")

        def update_priority(uID, friend, priority): # check that they are friends before-hand
                try:
                        cur.execute("""UPDATE "User" SET "priority" = %s WHERE "uID" = %s AND "friend" = %s""", (priority, uID, friend))
                
                except Exception as e:
                        print(e)
                        print("Failed to update priority")

        current_timestamp = datetime.now()

        def invite_to_event(eID, uID, friendID, eventName, eventTime, eventLocation, eventDescription):
                try:
                        cur.execute("""INSERT INTO "events" ("eID", "eventName", "eventTime", "eventLocation", "eventDescription") VALUES (%s, %s, %s, %s, %s)""", (eID, eventName, eventTime, eventLocation, eventDescription))
                        conn.commit()
                        cur.execute("""INSERT INTO "invites" ("eID", "uID", "friendID") VALUES (%s, %s, %s)""", (eID, uID, friendID))
                        conn.commit()
                        print("Invitation sent successfully")
                except Exception as e:
                        print(e)
                        print("Failed to send invitation")

        # invite_to_event(2, 3, 2, "Hackathon", current_timestamp, "Milton", "Start coding")
        # cur.execute("SELECT * FROM \"invites\"")
        # cur.execute("SELECT * FROM \"events\"")
        # result = cur.fetchall()
        # print(result)

        def update_event(eID, eventName, eventTime, eventLocation, eventDescription):
                try:
                        cur.execute("""UPDATE "events" SET "eventName" = %s, "eventTime" = %s, "eventLocation" = %s, 
                                    "eventDescription" = %s WHERE "eID" = %s""", (eventName, eventTime, eventLocation, eventDescription, eID))
                        conn.commit()
                        print("Event updated successfully")
                except Exception as e:
                        print(e)
                        print("Failed to update event")

        # update_event(1, "Nick's soccer tourny", current_timestamp, "Etobicoke", "Watch Nick get hat trick")
        # cur.execute("SELECT * FROM \"events\"")
        # result = cur.fetchall()
        # print(result)
        
        def add_participant_to_event(eID, uID):
                try:
                        cur.execute("""INSERT INTO "event_participants" ("eID", "uID") VALUES (%s, %s)""", (eID, uID))
                        conn.commit()
                        print("Participant added successfully")
                except Exception as e:
                        print(e)
                        print("Failed to add participant")

        # add_participant_to_event(1, 1)
        # cur.execute("SELECT * FROM \"event_participants\"")
        # result = cur.fetchall()
        # print(result)

        def accept_invite(eID, friendID): 
                try:                        
                        cur.execute(
                        """SELECT "uID" FROM "invites" WHERE "eID" = %s AND "friendID" = %s""", (eID, friendID))
                        result = cur.fetchone()
                        if result is not None:
                                oID = result[0]
                        
                        add_participant_to_event(eID, oID)
                        add_participant_to_event(eID, friendID)
                        print("accepted")
                        
                except Exception as e:
                        print(e)
                        print("Failed to accept invite")

        # accept_invite(2, 2)
        # cur.execute("SELECT * FROM \"invites\"")
        # cur.execute("SELECT * FROM \"event_participants\"")
        # result = cur.fetchall()
        # print(result)

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
       
        # print(get_user_events(1))

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
        
        # print(get_user_friends(3))

        def get_user_invites(friendID):
                try:
                        cur.execute(
                        """
                        SELECT e."eID", e."eventName", e."eventTime", e."eventLocation", e."eventDescription", i."uID", u."username"
                        FROM "events" e JOIN "invites" i ON e."eID" = i."eID" JOIN "User" u ON i."uID" = u."uID"
                        WHERE i."friendID" = %s""", (friendID,))
                        conn.commit()
                        print("Invites retrieved successfully")
                        invites = []
                        for invite in cur:
                                subinvites = []
                                subinvites.append(invite[0])
                                subinvites.append(invite[1])
                                subinvites.append(invite[2])
                                subinvites.append(invite[3])
                                subinvites.append(invite[4])
                                subinvites.append(invite[5])
                                subinvites.append(invite[6])
                                invites.append(subinvites)
                        return invites
                except Exception as e:
                        print(e)
                        print("Failed to retrieve invites")
        
        # print(get_user_invites(2))

        # Create remove functions

        def update_last_talked_to(uID, friendID):
                try:
                        cur.execute("""UPDATE "User" SET "lastTalkedTo" = %s WHERE "uID" = %s AND "friend" = %s
                        """, (current_timestamp, uID, friendID))

                        # Second update query
                        cur.execute("""UPDATE "User" SET "lastTalkedTo" = %s
                        WHERE "uID" = %s AND "friend" = %s""", (current_timestamp, friendID, uID))
                except Exception as e:
                        print(e)
                        print("Failed to update last talked to")
        
        # update_last_talked_to(3, 2)
        # cur.execute("SELECT * FROM \"User\"")
        # result = cur.fetchall()
        # print(result)

        def clear_all():
                cur.execute("""DELETE FROM "event_participants" """)
                cur.execute("""DELETE FROM "User" """)
                cur.execute("""DELETE FROM "events" """)
                cur.execute("""DELETE FROM "invige" """)

        # DON'T UNCOMMENT
        # clear_all()

        # result = cur.fetchall()
        # print(result)

        cur.close()
        conn.close()

except Exception as e:
        print(e)
        print('Unable to connect to the database')
        exit()