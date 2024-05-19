import icalendar
import os
from datetime import datetime

def parse_ics(path='./entities/calendar.ics'):
    with open(path, 'rb') as f:
        gcal = icalendar.Calendar.from_ical(f.read())

    events = []

    for component in gcal.walk():
        if component.name == "VEVENT":
            event = {}
            event['dtstart'] = component.get('DTSTART').dt
            event['dtend'] = component.get('DTEND').dt
            event['description'] = component.get('DESCRIPTION')
            events.append(event)
    return events