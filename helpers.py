import datetime
import crud
from flask import app



def get_available_appts(user_id, existing_appts, appt_date, start_time, end_time):
    """Returns all available appt slots within time frame"""
    result = []

    # get set of all unavailable appt slots
    unavailable_slots = get_booked_appts(existing_appts)

    # get start and end time for appointment slot range
    start = get_start_time(appt_date, start_time)
    end = datetime.datetime.combine(appt_date, end_time)

    # get all user's appts to check that user can't have 2 appts on same day
    user_appts = crud.get_appts_by_user_id(user_id)
    user_appt_dates = {appt.date.date() for appt in user_appts}

    appointment_slot = start
    
    while appointment_slot <= end:
        if appointment_slot not in unavailable_slots and appointment_slot.date() not in user_appt_dates:
            result.append(appointment_slot)
        appointment_slot = appointment_slot + datetime.timedelta(minutes=30)

    return result

def get_booked_appts(existing_appts):
    """Return set with unavailable appointment slots"""
    unavailable = set()

    for appt in existing_appts:
        unavailable.add(appt.date)

    return unavailable

def get_start_time(appt_date, start_time):
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
    return datetime.datetime.combine(appt_date, start_time)