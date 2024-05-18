import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="your_dbname",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)
cur = conn.cursor()

# Insert or update calendar data
for calendar in calendar_list['items']:
    cur.execute("""
        INSERT INTO calendars (calendar_id, summary, description, time_zone)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (calendar_id) DO UPDATE
        SET summary = EXCLUDED.summary,
            description = EXCLUDED.description,
            time_zone = EXCLUDED.time_zone
    """, (calendar['id'], calendar['summary'], calendar.get('description'), calendar['timeZone']))

# Insert or update event data
for event in events:
    cur.execute("""
        INSERT INTO events (event_id, calendar_id, summary, description, start_time, end_time, location, status, created, updated)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (event_id) DO UPDATE
        SET calendar_id = EXCLUDED.calendar_id,
            summary = EXCLUDED.summary,
            description = EXCLUDED.description,
            start_time = EXCLUDED.start_time,
            end_time = EXCLUDED.end_time,
            location = EXCLUDED.location,
            status = EXCLUDED.status,
            created = EXCLUDED.created,
            updated = EXCLUDED.updated
    """, (
        event['id'], calendar_id, event.get('summary'), event.get('description'),
        event['start'].get('dateTime'), event['end'].get('dateTime'),
        event.get('location'), event['status'], event['created'], event['updated']
    ))

    # Insert or update attendee data
    for attendee in event.get('attendees', []):
        cur.execute("""
            INSERT INTO attendees (event_id, email, response_status)
            VALUES (%s, %s, %s)
            ON CONFLICT (event_id, email) DO UPDATE
            SET response_status = EXCLUDED.response_status
        """, (event['id'], attendee['email'], attendee['responseStatus']))

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
