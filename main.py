from datetime import datetime
from gps_message import GpsMessage
from alarm_indications import validate_alarm_indications

if __name__ == '__main__':
    gps_message = GpsMessage(start_date=datetime.now())

    if not validate_alarm_indications(gps_message):
        print('Alarm indications are invalid')
    else:
        print(gps_message)
