import datetime
class User:
    id
    name
    friends
    calendar
    friends_requests
    event_requests
    password

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.friends = []
        self.calendar = {"Saturday":[], "Sunday":[], "Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
        self.friends_requests = []
        self.event_requests = []

    def change_friend_priority(self, friend, priority):
        friend.change_priority(priority)

    def add_friend_request(self, user):
        self.friends_requests.append(user)

    def send_friend_request(self, friend):
        friend.add_friend_request(self)

    def accept_friend_request(self, friend):
        self.friends.append(friend)
        friend.friends.append(self) # potentially problematic
        self.friends_requests.remove(friend)
        friend.friends_requests.remove(self)

    def reject_friend_request(self, friend):
        self.friends_requests.remove(friend)
    
    def add_event_request(self, event):
        self.event_requests.append(event)

    def add_event_to_calendar(self, event):
        self.calendar[event.day].append(event)
    
    def modify_calendar_ics(self, event):
        # need to implement
        pass

    def read_calendar_ics(self):
        # need to implement
        pass
    
    def accept_event_request(self, event):
        self.event_requests.remove(event)
        event.participant_accept(self)
    
    def get_calendar(self):
        return self.calendar
    
    def get_friends(self): 
        return self.friends
    
    def get_userid(self):    
        return self.id

    def add_event_to_calendar(self, event):
        self.add_event_to_calendar(event)

    def reject_event_request(self, event):
        self.event_requests.remove(event)
        # need to add a way to show the message this to Event
        event.participant_reject(self)
    
    def _get_top_friend(self):
        last_talked_to = None
        top_friend = None
        for friend in self.friends:
            if friend.last_talked_to is None:
                return friend
            if last_talked_to is None:
                last_talked_to = top_friend.last_talked_to
            if friend.last_talked_to < last_talked_to:
                last_talked_to = friend.last_talked_to
                top_friend = friend
        return top_friend

    def get_top_three(self):
        top_three = []
        for i in range(3):
            top_friend = self._get_top_friend()
            top_three.append(top_friend)
            self.friends.remove(top_friend)
        self.friends = top_three + self.friends
        return top_three

    

    
   
    
    

        
