from API.src._MainAPI import _API
from util.My_URL_Templates import DUSK_DAWN_URL

class Dusk_Dawn_API_Accessor(_API):

    def __init__(self):
        #initializes
        super().__init__()
        #initializes child class

    def Get_duskdawn_from_date(self, latitude:float or str, longitude: float or str, date:str = "today", tzid : float or str = "America/New_York"):
        #as per bowlin ARGs are in lists
       return super()._request_and_decode_API_response(DUSK_DAWN_URL, "Can-I-See-The-ISS-Midterm", [tzid, latitude, longitude, date])