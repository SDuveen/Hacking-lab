from datetime import datetime, timedelta

ZERO_POINT = datetime.strptime('1980-01-06T00:00Z', '%Y-%m-%dT%H:%MZ')
TOTAL_LEAP_SECONDS_UNTIL_NOW = 18
MAX_GPS_WEEK = 1024

def gps_time(date = datetime.now()):
    begin_of_week = (date - timedelta(days=date.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    begin_of_gps_week = begin_of_week - timedelta(seconds=TOTAL_LEAP_SECONDS_UNTIL_NOW)

    week_number = int((begin_of_gps_week - ZERO_POINT).total_seconds() / (7 * 24 * 3600)) % MAX_GPS_WEEK
    time_of_week = int((date - begin_of_gps_week).total_seconds() // 1.5)

    return week_number, time_of_week

if __name__ == '__main__':
    week, time_of_week = gps_time()

    print(f'GPS week: {week}, time of week: {time_of_week}')
