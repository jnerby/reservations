import datetime


def get_available_appts(existing_appts, appt_date, start_time, end_time):
    """Returns all available appt slots within time frame"""
    result = []

    # get set of all unavailable appt slots
    unavailable_slots = get_booked_appts(existing_appts)

    # extract minutes from start time
    start_minutes = start_time.minute
    start_hour = start_time.hour
    
    # round minutes to nearest half hour or top of hour
    if start_minutes == 0:
        start_minutes = 0
    elif start_minutes <= 30:
        start_minutes = 30
    else: 
        start_hour += 1
        start_minutes = 00
    
    start_time = datetime.time(start_hour, start_minutes, 00)
    start = datetime.datetime.combine(appt_date, start_time)
    end = datetime.datetime.combine(appt_date, end_time)

    appointment_slot = start
    while appointment_slot <= end:
        if appointment_slot not in unavailable_slots:
            result.append(appointment_slot)
        appointment_slot = appointment_slot + datetime.timedelta(minutes=30)

    return result

def get_booked_appts(existing_appts):
    """Return set with unavailable appointment slots"""
    unavailable = set()

    for appt in existing_appts:
        unavailable.add(appt.date)

    return unavailable