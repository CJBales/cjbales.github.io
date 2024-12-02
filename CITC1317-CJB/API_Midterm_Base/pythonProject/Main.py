#CITC1317 Intro to Scripting
#Cecil Bales
#10/16/24
#10/22/24
from datetime import datetime, timedelta
from time import sleep

import util.My_URL_Templates as URL_TEMPLATES
from Dusk_Dawn_API_Accessor import Dusk_Dawn_API_Accessor as DNDA
from Weather_API import Weather_API_Accessor
from util.RASPIA_Editor import RASPIA_Editor

if __name__ == "__main__":

    BMP_latitude = 36.3
    BMP_longitude= -82.3

    Raspia_edit = RASPIA_Editor()
    Raspia_edit.add_to_SEARCHABLE_API_ENDPOINTS([URL_TEMPLATES.DUSK_DAWN_URL,URL_TEMPLATES.ISS_LOCATION_URL,URL_TEMPLATES.DAILY_WEATHER_URL],["get-sunset-sunrise","get-ISS-location","get-cloud-cover"])
    #Edits RASPIA

    Weather_tool = Weather_API_Accessor()
    Weather_data = Weather_tool.CloudCover()
    #utilizes the weather API
    Sunrise_Sunset_tool = DNDA()
    #Utilizes the other api

    Date_time = [datetime.fromisoformat(x).strftime("%Y-%m-%d %I:%M:%S %p") for x in Weather_data["hourly"]["time"]]
    #provides the date and time in a formatted way for the product
    Time_cloud = dict(zip(Date_time, Weather_data["hourly"]["cloud_cover_high"]))
    #zips Datetime and cloud coverage in a variable to be utilized

    Client_date = '2024-10-22'

    New_date = datetime.strptime(Client_date, "%Y-%m-%d").date()
    #create a datetime object from cli-supplied arguments

    Listdates_sunrise_sunset = [New_date + timedelta(days=days_after) for days_after in range(0, 7)]
    #creates a list of datetime objects for 7 days

class Visibility_Calculation():

    for day in Listdates_sunrise_sunset:
        sleep(2)
        print(day)
    Sunrise_set_data = Sunrise_Sunset_tool.Get_duskdawn_from_date(BMP_latitude, BMP_longitude, date=day.strftime("%Y-%m-%d"))
    # get sunrise/sunset data

    Sunrise = Sunrise_set_data.strptime(Sunrise_set_data['results']['sunrise'],'%I:%M:%S %p').time()
    Sunset = Sunrise_set_data.strptime(Sunrise_set_data['results']['sunset'],'%I:%M:%S %p').time()
    # extract time strings and conver to datetime
    # ASSUMES API OUTPUT IS CORRECT

    Rise_timestamp = datetime.combine(day, Sunrise)
    Set_timestamp = datetime.combine(day, Sunset)
    #make date and time datetime object via combine for easier manipulation

    Rounded_rise = Rise_timestamp.replace(minute=0, second=0)
    Rounded_set = Set_timestamp.replace(hour=Set_timestamp.hour + 1, minute=0, second=0)
    #round the datetimes either down or up, depending on sunrise or sunset

    Rounded_rise_str = Rounded_rise.strftime("%Y-%m-%d %I:%M:%S %p")
    Rounded_set_str = Rounded_set.strftime("%Y-%m-%d %I:%M:%S %p")
    #get a formatted string for easier, human reading

    CloudCover_rise = Time_cloud[Rounded_rise_str]
    CloudCover_set = Time_cloud[Rounded_set_str]
    #get the corresponding cloud coverage from the appropriate dict

    print(f"Sunrise Observation: {Rounded_rise_str}  Cloud Coverage Percentage: {CloudCover_rise}")
    if CloudCover_rise < 30:
        print("Nice time to observe!")
    elif CloudCover_rise < 75:
        print("it's very risky! Good luck")
    else:
        print("Do Not Even Try. Let's go inside!")
    print(f"Sunset Observation: {Rounded_set_str}  Cloud Coverage Percentage: {CloudCover_set}")

    if CloudCover_set < 30:
        print("Nice time to observe!")
    elif CloudCover_set < 75:
        print("it's very risky! Good luck")
    else:
        print("Do Not Even Try. Let's go inside!")