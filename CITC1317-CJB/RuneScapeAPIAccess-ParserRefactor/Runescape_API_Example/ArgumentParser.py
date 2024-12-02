"""
Project Name: ArgParseDemonstration
File Name: ArgumentParser.py
Date Created: 11/11/2024
Author: Edgar Wallace Bowlin III
Class: CSCI 1317 Introduction to Scripting Languages
Instructor: Edgar Wallace Bowlin III
Date Last Edited: 11/11/2024
"""

import argparse

from typing import Type

class ArgumentParser:
    def __init__(self, **kwarg):
        # Initialize the parser
        self.parser = argparse.ArgumentParser(**kwarg)

        self.args = None


        # created with the help of ChatGPT
    def AddArgumentTypes(self,parserArgs:dict):
        NameOrFlag = parserArgs.pop("name_or_flags")
        self.parser.add_argument(*NameOrFlag, **parserArgs)



    def ParseArgs(self):

        self.args = self.parser.parse_args()