from datetime import datetime, timedelta

def estimate_time(token):
    start = datetime.strptime("10:00", "%H:%M")
    return (start + timedelta(minutes=10 * (token - 1))).strftime("%H:%M")
