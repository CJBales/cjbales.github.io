from API.src._MainAPI import _API
from util.My_URL_Templates import ISS_LOCATION_URL
from datetime import datetime, timezone

class ISS_API_Accessor(_API):
    def __init__(self):
        super().__init__()

    def get_ISS_position(self,timestamp):
        return super()._request_and_decode_API_response(ISS_LOCATION_URL,"Can-I-See-The-ISS-Midterm", [timestamp])


    def convert_time_to_UTC(self, time: str):

        # define date format
        date_format = '%Y-%m-%d %H:%M:%S'

        # Convert the date string into a datetime object
        dt = datetime.strptime(time, date_format)

        # Set the timezone to UTC
        dt_utc = dt.replace(tzinfo=timezone.utc)

        # Convert the datetime object to a Unix timestamp
        timestamp = int(dt_utc.timestamp())

        return timestamp

if __name__ == "__main__":
    date_format = '%Y-%m-%d %H:%M:%S'
    test = ISS_API_Accessor()
    print(datetime.now().__str__())
    print(test.convert_time_to_UTC(datetime.now().strftime(date_format)))
