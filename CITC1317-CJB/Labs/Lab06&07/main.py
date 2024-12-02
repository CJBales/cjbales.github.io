#C. J. Bales
#cbales6@stumail.northeaststate.edu
#CITC1317 Intro to Scripting
#Edgar Bowlin III
#10/2/24
import os
import datetime
import argparse
import RuneScapeAPIAccess

class Players(RuneScapeAPIAccess):
    def LoadPlayerNamesToBeSearch(self):
        print("HI")
        return
    #Takes input files, loads them into your program, and puts them into a Python data structure that
    # allows the strings to be easily accessible. A List, perhaps?
    def GetPlayerData(self):

        return
    #Utilizes RASPIA to get play data from RuneScape Official servers and place it in an
    # easy-to-use Python built-in data structure or one of your own design
    def FormatPlayerData(self):

        return
    #take the available data and format the strings in an easy-to-read format that can be present to the user
    def PrintDataToScreen(self):

        return
    #prints the data in a pretty-print format to the console (mainly for testing purposes)
    def SaveDataToFile(self):

        return
    #saves the formatted text data to a file named (something along the lines of)
    # “PLAYERNAME-Skills-Report-DATE_RETRIEVED-TIME_RETRIEVED.txt”.
    #You wouldreplace all-caps words with the relevant player and the date and time it was retrieved.
    #The exact name does not matter if it gives the same information as the one given in the above example.
    # I want INDIVIDUAL FILES for each of the players