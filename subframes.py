from datetime import datetime
from gps_message import GpsMessage

if __name__ == '__main__':
    gps_message = GpsMessage(start_date=datetime.now())

    print(gps_message)
