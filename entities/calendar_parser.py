from icalendar import Calendar
from datetime import datetime

def parse_ics():
    with open('calendar.ics', 'rb') as f:
        gcal = Calendar.from_icalendar(f.read())

    events = []

    for component in gcal.walk():
        if component.name == "VEVENT":
            event = {}
            event['dtstart'] = component.get('DTSTART').dt
            event['dtend'] = component.get('DTEND').dt
            events.append(event)
    return events