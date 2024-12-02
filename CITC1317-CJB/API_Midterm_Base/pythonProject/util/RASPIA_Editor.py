from enum import Enum, auto
import API
from API.util.API_NAME_ENUM import APINameEnums
from API.util.Runescape_HiScores_URL_Templates import REVERSED_API_ENDPOINTS_NEEDING_JSON_PARSE

# this is necessary as one of your restrictions will be to NOT edit A N Y source code in RASPIA
class RASPIA_Editor():
    def __init__(self):
        pass

    def add_enum_to_API_NAME_ENUM(self,list_of_names: list[str]):
        # Dynamically creating an extended Enum at runtime
        for name in list_of_names:
            API.util.API_NAME_ENUM.APINameEnums = Enum('ExtendedEnum', {**APINameEnums.__members__, name :auto()})

    def add_enum_to_API_NAME_ENUM_same_value(self, list_of_enums: list[str], value: int):
        # Dynamically creating an extended Enum at runtime, used when just taking a previously defined strategy.
        for name in list_of_enums:
            API.util.API_NAME_ENUM.APINameEnums = Enum('ExtendedEnum', {**APINameEnums.__members__, name :value})

    def add_to_SEARCHABLE_API_ENDPOINTS(self,url_to_fit_in_enum: list[str], list_of_URL_names: list[str]):
        # This one is really important if you're lucky enough to have an API that outputs JSONs
        # I use this in this example to add new apis and assign parsers to them.
        for url, name_of_url in zip(url_to_fit_in_enum, list_of_URL_names):
            REVERSED_API_ENDPOINTS_NEEDING_JSON_PARSE[url] = name_of_url
"""
    example code snippet for the aboce function
    
    # edit raspia settings to accept new arguments
    # here, we are actually just "hacking" it to force the API parser to use
    # the json parsing method
    raspia_editor = RASPIA_Editor()
    raspia_editor.add_to_SEARCHABLE_API_ENDPOINTS([URL_TEMPLATES.DUSK_DAWN_URL,URL_TEMPLATES.ISS_LOCATION_URL,URL_TEMPLATES.DAILY_WEATHER_URL],["get-sunset-sunrise","get-ISS-location","get-cloud-cover"])

"""