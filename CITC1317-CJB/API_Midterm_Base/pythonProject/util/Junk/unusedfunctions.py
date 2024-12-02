from datetime import datetime, timezone, timedelta

from util.Junk.ISS_Info import ISS_Info


def convert_datetime_to_unix_time(date,time ):
    # Define your date and time
    combined_datetime_string = f'{date} {time}'  # Example date and time
    date_format = '%Y-%m-%d %H:%M:%S %p'

    # Convert the date string into a datetime object
    dt = datetime.strptime(combined_datetime_string, date_format)

    # Set the timezone to UTC
    dt_utc = dt.replace(tzinfo=timezone.utc)

    # Convert the datetime object to a Unix timestamp
    timestamp = int(dt_utc.timestamp())

    #print(f"The Unix timestamp for {combined_datetime_string} UTC is: {timestamp}")
    return timestamp

BMP_latitude = 36.3
BMP_longitude= -82.3

def is_iss_visible(lat1,lon1):
    temp = ISS_Info()
    distance_to_iss = temp.haversine(BMP_latitude, BMP_longitude, lat1, lon1)

    # Step 6: (ASSUMPTION) Define the visible horizon distance (assumed, based on typical ISS altitude)
    visible_horizon_distance = 2000  # in kilometers



    print(f"Distance to iss: {distance_to_iss} and visible horizon distance: {visible_horizon_distance}")
    return distance_to_iss <= visible_horizon_distance


    # Function to estimate ISS location for a time 45 minutes before sunrise and after sunset
def estimate_iss_location(start_lat, start_lng, end_lat, end_lng, factor):
    # Linear interpolation of latitude and longitude
    estimated_lat = start_lat + factor * (end_lat - start_lat)
    estimated_lng = start_lng + factor * (end_lng - start_lng)
    return estimated_lat, estimated_lng


def create_ISS_time_offsets(lat1,lon1):
    factor2 = (0.5)/45  # 1 minutes in a 90-minute orbit

    # Estimate 1 minutes before given time
    adjusted_iss_lat, adujust_iss_lng = estimate_iss_location(
        lat1, lon1, -factor2)


    return adjusted_iss_lat, adujust_iss_lng


# Function to check if the ISS is within the visible horizon distance during a time interval
def check_iss_visibility_during_interval(start_time, end_time, observer_lat, observer_lng,iss_lat,iss_lon, time_step_minutes=1,
                                         visible_horizon_distance=4000):
    iss_info = ISS_Info()
    current_time = start_time
    while current_time <= end_time:
        print(f"This is the current time {current_time} and iss lat {iss_lat} and long {iss_lon}")
        timestamp = int(current_time.timestamp())  # Convert to Unix timestamp


        # Check distance between ISS and observer
        distance_night = iss_info.haversine(observer_lat, observer_lng, iss_lat, iss_lon)

        if distance_night <= visible_horizon_distance:
            print(f"current time {current_time}, iss latitude: {iss_lat}  iss Longitude {iss_lon}")
            return True  # ISS is within visible horizon at some point

        # Increment time by time_step_minutes
        current_time += timedelta(minutes=time_step_minutes)
        iss_lat, iss_lon=create_ISS_time_offsets(iss_lat, iss_lon)

    return False  # ISS is never within visible horizon during the interval