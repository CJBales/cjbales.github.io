"""
RunescapeHiscoresAPI.py
Runescape Experience Calculator
Edgar Bowlin III

This serves as an easy way to access each Runescape Hiscorces API endpoints
as seen at https://runescape.wiki/w/Application_programming_interface#Hiscores.
Credit for the information on how to access API_Accessors goes to the authors of
the above article

Some Endpoints have been left out. They will be added as their function is understood enough
to abstract the parameters like category and table seen in the util.Runescape_Hiscores_URL_Templates.py
file.

"""

from src.API.Runescape_API_Accessors import BaseAPIClient as API
from src.API.Runescape_API_Example.util.commonImports import User_Agent_Strings, URL_Templates


class RunescapeHiScoresAPIAccessor(API):

    def __init__(self):
        super().__init__()

    def get_rankings(self, current_activity: str = "3", skill_or_activity_name: str = "3", amount_of_ranks: str =
    '10') -> str:
        """

        :param current_activity: a string containing the int of the current skill, overall level, or activity
        :param skill_or_activity_name: a string containing the int of the skills or activities
        :param amount_of_ranks: a string containing the int of the amount of players requested, MAX 50
        :return:a list directly from Jagex that contains the name, score, and rank of the top amount_ranks
            players as seen at
            https://runescape.wiki/w/Application_programming_interface#ranking
        """

        return super().request_and_decode_api_response(URL_Templates.ranking_url,
                                                       User_Agent_Strings.runescape_hiscores,
                                                       [current_activity, skill_or_activity_name, amount_of_ranks])

    def _get_userRanking(self, current_session_id: str) -> str:
        """

        :param current_session_id: a string containing the session ID of the currently
        logged in player
        :return: a list with the player name and their overall rank
        """

        return super().request_and_decode_api_response(URL_Templates.userRanking_URL,
                                                       User_Agent_Strings.runescape_hiscores,
                                                       [current_session_id])

    def get_player_hiscore(self, player_name: str = "Zezima") -> str:
        """

        used to get the hiscores data for a given player, as described at
             https://runescape.wiki/w/Application_programming_interface#Hiscores_Lite
        :param player_name: the name of the user to look up
        :return: a list directly from Jagex that contains the information on that user as seen at
            https://runescape.wiki/w/Application_programming_interface#Hiscores_Lite
        """

        return super().request_and_decode_api_response(URL_Templates.hiscores_lite_URL,
                                                       User_Agent_Strings.runescape_hiscores,
                                                       [player_name])

    def get_ironman_hiscore(self, player_name: str = "Gecu") -> str:
        """

        :param player_name: a string containing the name of the player in question
        :return:  a list directly from Jagex that contains the information on that Ironman user as seen at
            https://runescape.wiki/w/Application_programming_interface#Ironman_Lite

        """
        return super().request_and_decode_api_response(URL_Templates.ironman_hiscores_lite_URL,
                                                       User_Agent_Strings.runescape_hiscores,
                                                       [player_name])

    def get_hardcore_ironman_hiscore(self, player_name: str = "J oris") -> str:
        """

        :param player_name: a string containing the name of the player in question
        :return:  a list directly from Jagex that contains the information on that Hardcore Ironman user as seen at
            https://runescape.wiki/w/Application_programming_interface#Hardcore_Ironman_Lite
        """
        return super().request_and_decode_api_response(URL_Templates.hardcore_ironman_hiscores_lite_URL,
                                                       User_Agent_Strings.runescape_hiscores,
                                                       [player_name])

    def get_boss_groups_data(self, size_of_group: str = "1", amount_of_entries_per_page: str = "10", boss_id: str = "3",
                             page_number: str = "1") -> str:
        """
        Provides the information on group boss kills (including solo)
        :param size_of_group: a str containing the int describing the number of players in the group
        MIN 1 and MAX varies depending on boss
        :param amount_of_entries_per_page: a str containing the int describing the number of entries
        per page
        :param boss_id: a str containing the int describing the boss being killed
        :param page_number: a str containing the int describing the page number of the hiscores list
        :return: a list containing the data described at
        https://runescape.wiki/w/Application_programming_interface#groups
        """

        return super().request_and_decode_api_response(URL_Templates.boss_groups_URL,
                                                       User_Agent_Strings.runescape_hiscores,
                                                       [size_of_group,
                                                                                               amount_of_entries_per_page,
                                                                                               boss_id, page_number])



