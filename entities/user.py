from datetime import datetime
from calendar_parser import parse_ics
from friend import Priority
from event import Event
from friend import Friend
from scheduling import manual_schedule_event, recommend_event

def int_to_weekday_string(day_int):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[day_int]


class User:
    #

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.friends = []
        self.calendar = {"Saturday":[], "Sunday":[], "Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
        self.friends_requests = []
        self.event_requests = []
        self.events_attended = []

    def change_friend_priority(self, friend, priority):
        # assume friend is a User object
        for fr in self.friends:
            if fr.get_user().get_userid == friend.id:
                fr.change_priority(priority)

    def add_friend_request(self, user):
        user.friends_requests.append(self)

    def send_friend_request(self, friend):
        friend.add_friend_request(self)

    def accept_friend_request(self, friend):
        friend_obj = Friend(friend, Priority.LOW)
        self_obj = Friend(self, Priority.LOW)
        self.friends.append(friend_obj)
        friend.friends.append(self_obj) # potentially problematic
        self.friends_requests.remove(friend)    

    def reject_friend_request(self, friend):
        self.friends_requests.remove(friend)
    
    def add_event_request(self, event):
        self.event_requests.append(event)

    def add_event_to_calendar(self, event):
        self.calendar[event.day].append(event)
        self.events_attended.append(event)
    
    def modify_calendar_ics(self, event):
        # need to implement
        pass

    def read_calendar_ics(self, path='./entities/calendar.ics'):
        # need to implement
        events = parse_ics(path)
        for event in events:
            dtstart_str = event["dtstart"].strftime('%Y-%m-%d %H:%M:%S')
            dt_start = datetime.strptime(dtstart_str, '%Y-%m-%d %H:%M:%S')
            dtend_str = event["dtend"].strftime('%Y-%m-%d %H:%M:%S')
            dt_end = datetime.strptime(dtend_str, '%Y-%m-%d %H:%M:%S')
            day = int_to_weekday_string(dt_start.weekday())
            self.calendar[day].append((dt_start.hour, dt_end.hour))
        # now determine overlaps and combine
        for day in self.calendar:
            sorted_list = sorted(self.calendar[day], key=lambda x: x[0])
            n = len(sorted_list)
            if n == 0 or n == 1:
                continue
            i = 0
            j = 1
            while j < n:
                if sorted_list[j][0] < sorted_list[i][1]:
                    sorted_list[i] = (sorted_list[i][0], max(sorted_list[i][1], sorted_list[j][1]))
                    sorted_list.pop(j)
                    n -= 1
                i += 1
                j += 1
            self.calendar[day] = sorted_list

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

    

    
   
    
    

        
