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
        if self.num_accepted == len(self.participants):
            # everyone has accepted, thus send to everyone's calendar
            participant.add_event_to_calendar(self)
        