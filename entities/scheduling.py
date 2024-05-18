def _find_longest_consecutive_timeslot(available_times):
    # Find the longest consecutive timeslot in the available times
    longest_timeslot_len = 0
    longest_timeslot_start = -1
    current_timeslot_len = 0
    current_timeslot_start = -1
    for i in range(24):
        if i in available_times:
            if current_timeslot_len == 0:
                current_timeslot_start = i
            current_timeslot_len += 1
        else:
            if current_timeslot_len > longest_timeslot_len:
                longest_timeslot_len = current_timeslot_len
                longest_timeslot_start = current_timeslot_start
            current_timeslot_len = 0
    return longest_timeslot_start, longest_timeslot_len

def _find_master_available_times(user_schedule, friend_schedule):
    master_available_times = {day: set([i for i in range(24)]) for day in user_schedule}
    for day in user_schedule:
        master_available_times[day] = set(friend_available_times[day]).intersection(set(user_available_times[day]))
        master_available_times[day] = list(master_available_times[day])
        master_available_times[day].sort()
    
    largest_timeslot_len = 0
    largest_timeslot_day = None
    largest_timeslot_start = -1

    for day in master_available_times:
        start, length = _find_longest_consecutive_timeslot(master_available_times[day])
        if length > largest_timeslot_len:
            largest_timeslot_len = length
            largest_timeslot_day = day
            largest_timeslot_start = start
    return largest_timeslot_day, largest_timeslot_start, largest_timeslot_len

def _modify_available_times(available_times, schedule):
    for day in schedule:
        for timeslot in schedule[day]:
            for i in range(timeslot[0], timeslot[1] + 1):
                available_times[day].remove(i)

def recommend_event(user_requesting, friend_requested):
    # Find a time that works for all participants and return Event object or return if not possible
    # Search for times depending on priority of friends to user_requesting and user_requesting to friends
    # Example if S req event for high N mid T low E, but say S is low to N, then S may skip their events for N and 
    # N will not skip their events for S

    # For each person, get their free times

    # For each person start with own list of [0, 1, ... 23]
    # Then based on prio and availability we change this to reflect only stasrt times they are available, 

    user_schedule = user_requesting.get_calendar()
    friend_schedule = friend_requested.get_user().get_calendar()

    # first check without needing priority (only day time so 9am to 10pm)

    user_available_times = {day: [i for i in range(9, 22)] for day in user_schedule}
    friend_available_times = {day: [i for i in range(9, 22)] for day in friend_schedule}
    
    _modify_available_times(user_available_times, user_schedule)
    _modify_available_times(friend_available_times, friend_schedule)
    
    largest_timeslot_day, largest_timeslot_start, largest_timeslot_len = _find_master_available_times(user_available_times, friend_available_times)

    if largest_timeslot_len == 0:
        # No time available, now determine if we can skip stuff in the timetable (based on priority)
        user_friends = user_requesting.get_friends()
        friend_prio = friend_requested.get_priority()
        user_prio = -1
        for friend in friend_requested.get_user().get_friends():
            if friend.get_userid() == user_requesting.get_userid():
                user_prio = friend.get_priority()
                break
                
        ltd = None
        lts = 0
        ltl = 0
        if user_prio == Priority.LOW and (friend_prio == Priority.MEDIUM or friend_prio == Priority.HIGH):
            # You priortize them but they don't prioritize you
            user_available_times = {day: [i for i in range(24)] for day in user_schedule}
            _modify_available_times(user_available_times, user_schedule)
            ltd, lts, ltl = _find_master_available_times(user_available_times, friend_schedule)
            if ltl == 0:
                if friend_prio == Priority.HIGH:
                    user_available_times = {day: [i for i in range(24)] for day in user_schedule}
                    ltd, lts, ltl = _find_master_available_times(user_available_times, friend_schedule)  
                    if largest_timeslot_len == 0:
                        # No available times
                        return None
                    else:
                        return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
            else:
                return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
            
        if user_prio == Priority.MEDIUM:
            friend_available_times = {day: [i for i in range(24)] for day in friend_schedule}
            _modify_available_times(friend_available_times, friend_schedule)
            user_available_times = {day: [i for i in range(9, 22)] for day in user_schedule}
            _modify_available_times(user_available_times, user_schedule)
            ltd, lts, ltl = _find_master_available_times(user_available_times, friend_available_times)
            if ltl != 0:
                return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
            if friend_prio == Priority.MEDIUM or friend_prio == Priority.HIGH:
                user_available_times = {day: [i for i in range(24)] for day in user_schedule}
                _modify_available_times(user_available_times, user_schedule)
                ltd, lts, ltl = _find_master_available_times(user_available_times, friend_available_times)
                if ltl != 0:
                    return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
            if friend_prio == Priority.HIGH:
                user_available_times = {day: [i for i in range(24)] for day in user_schedule}
                ltd, lts, ltl = _find_master_available_times(user_available_times, friend_available_times)
                if ltl != 0:
                    return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
                

        if user_prio == Priority.HIGH:
            friend_available_times = {day: [i for i in range(24)] for day in friend_schedule}
            user_available_times = {day: [i for i in range(9, 22)] for day in user_schedule}
            _modify_available_times(user_available_times, user_schedule)
            ltd, lts, ltl = _find_master_available_times(user_available_times, friend_available_times)
            if ltl != 0:
                return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
            if friend_prio == Priority.MEDIUM or friend_prio == Priority.HIGH:
                user_available_times = {day: [i for i in range(24)] for day in user_schedule}
                _modify_available_times(user_available_times, user_schedule)
                ltd, lts, ltl = _find_master_available_times(user_available_times, friend_available_times)
                if ltl != 0:
                    return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
            if friend_prio == Priority.HIGH:
                user_available_times = {day: [i for i in range(24)] for day in user_schedule}
                ltd, lts, ltl = _find_master_available_times(user_available_times, friend_available_times)
                if ltl != 0:
                    return manual_schedule_event(user_requesting, [friend_requested], ltd, (lts, lts + ltl))
        if ltl == 0:
            return None # No available times

    else:
        return manual_schedule_event(user_requesting, [friend_requested], largest_timeslot_day, (largest_timeslot_start, largest_timeslot_start + largest_timeslot_len)) # maybe -1 here?
    


def manual_schedule_event(user_requesting, friends_requested, day, timeslot):
    created_event = Event(day, timeslot, [user_requesting] + friends_requested)
    for friend in friends_requested:
        friend.add_event_request(created_event)
    return created_event