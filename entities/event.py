from datetime import datetime, timedelta

def weekday_string_to_int(day_string):
    weekdays = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}
    return weekdays[day_string]

class Event:

    def __init__(self, day, timeslot, participants):
        self.participants = participants
        self.day = day
        self.timeslot = timeslot
        self.participants_rejected = False
        self.num_accepted = 0

    def participant_reject(self, participant):
        self.participants.remove(participant)
        self.participants_rejected = True
        # This is now invalid
        for participant in self.participants:
            participant.event_requests.remove(self)
    
    def participant_accept(self, participant):
        self.num_accepted += 1
        self.participants.append(participant)
        if self.num_accepted == len(self.participants):
            # everyone has accepted, thus send to everyone's calendar
            participant.add_event_to_calendar(self)
            # Also update everyones last talked to
            for participant in self.participants:
                for friend in participant.friends:
                    if friend in self.participants:
                        curr_day = datetime.now().weekday()
                        target_day = weekday_string_to_int(self.day)
                        days_diff = (target_day - curr_day) % 7
                        friend.last_talked_to = datetime.now() + timedelta(days=days_diff)