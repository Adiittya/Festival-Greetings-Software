import datetime
import database as db   

def get_upcoming_events():

    f_date=""
    f_name=""
    events=db.connection("SELECT fest_name,fest_date FROM fest_india")
    upcoming_events =[]
    dt=datetime.datetime.now()
    date=dt.date()
    for event in events:
        if event[1] > date:
            upcoming_events.append(event)
            break
    for i in upcoming_events:
        f_name=i[0]
        f_date=i[1]
    
    return f"Event:{f_name} \ndate:{f_date}"

