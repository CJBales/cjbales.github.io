from API.src._MainAPI import _API
from util.My_URL_Templates import DAILY_WEATHER_URL

class Weather_API_Accessor(_API):
    def __init__(self):
        #initializes
        super().__init__()
        #initializes child
    def CloudCover(self):
        return super()._request_and_decode_API_response(DAILY_WEATHER_URL,"Can-I-See-The-Sky-Midterm",[])