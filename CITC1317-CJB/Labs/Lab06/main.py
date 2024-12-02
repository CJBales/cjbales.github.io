#C. J. Bales
#cbales6@stumail.northeaststate.edu
#CITC1317 Intro to Scripting
#Edgar Bowlin III
#10/30/24
import os
import datetime
import RuneScapeAPIAccess.API.src.APIClient.BaseAPIClient

class Players:
    def __init__(self, name):
        self.name = name
        self.skills_data = {}

    def set_skills_data(self, skills_data):
        self.skills_data = skills_data

    def get_skills_data(self):
        return self.skills_data

class PlayerData:
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = output_folder
        self.HighScoresApi = RuneScapeAPIAccess.API.src.APIClient.BaseAPIClient.BaseAPIClient()
    def LoadPlayerNamesToBeSearch(self):
        with open("Ten_Users_Names.txt", "r") as greenShoeWindows:
            text = greenShoeWindows.read()
            username_list = text.split("\n")

        for username in username_list:
            print(self.HighScoresApi.get_player_hiscore(username))
            print("\n\n")
        return
    #Takes input files, loads them into your program, and puts them into a Python data structure that
    # allows the strings to be easily accessible. A List, perhaps?

    def GetPlayerData(self, player_name):
        api = RuneScapeAPIAccess.API.src.APIClient.BaseAPIClient.BaseAPIClient()
        return api.get_player_skills(player_name)
    #Utilizes RASPIA to get play data from RuneScape Official servers and place it in an
    # easy-to-use Python built-in data structure or one of your own design

    def FormatPlayerData(self, player):
        formatted_data = f"Skills for {player.name}:\n"
        for skill, data in player.get_skills_data().items():
            formatted_data += f"{skill}: Experience - {data['experience']}, HiScore Rank - {data['rank']}\n"
        return formatted_data
    #take the available data and format the strings in an easy-to-read format that can be present to the user

    def PrintDataToScreen(self, players):
        print(self.FormatPlayerData(players))
        return
    #prints the data in a pretty-print format to the console (mainly for testing purposes)

    def SaveDataToFile(self, player):
        date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{player.name}-Skills-Report-{date_time}.txt"
        file_path = os.path.join(self.output_folder, file_name)
        with open(file_path, 'w') as file:
            file.write(self.FormatPlayerData(player))
        return
    #saves the formatted text data to a file named (something along the lines of)
    # “PLAYERNAME-Skills-Report-DATE_RETRIEVED-TIME_RETRIEVED.txt”.
    #You would replace all-caps words with the relevant player and the date and time it was retrieved.
    #The exact name does not matter if it gives the same information as the one given in the above example.
    # I want INDIVIDUAL FILES for each of the players

    def main(self, input_file, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        retriever = PlayerData(input_file, output_folder)
        player_names = retriever.LoadPlayerNamesToBeSearch()

        for name in player_names:
            player = Players(name)
            skills_data = retriever.GetPlayerData(name)
            player.set_skills_data(skills_data)

            # Display and save data
            retriever.PrintDataToScreen(player)
            retriever.SaveDataToFile(player)