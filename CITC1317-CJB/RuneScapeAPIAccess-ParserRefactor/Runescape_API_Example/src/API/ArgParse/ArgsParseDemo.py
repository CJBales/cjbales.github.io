"""
Project Name: ArgParseDemonstration
File Name: ArgsParseDemo.py
Date Created: 11/11/2024
Author: Edgar Wallace Bowlin III
Class: CSCI 1317 Introduction to Scripting Languages
Instructor: Edgar Wallace Bowlin III
Date Last Edited: 11/11/2024
"""


from ArgumentParser import ArgumentParser

if __name__ == "__main__":

    parsedArgs = ArgumentParser()

    dictArguments=[{"name_or_flags": "outputFile", "type": str, "help": "Input file path."},
                   {"name_or_flags":"--verbose", "action": "store_true", "help": "Saves a verbose save file"},
                   ]

    for arg in dictArguments:
        parsedArgs.AddArgumentTypes(arg)
    # Use the parsed arguments

    parsedArgs.ParseArgs()
    print(f"Processing file: {parsedArgs.args.outputFile}")
    if parsedArgs.args.verbose:
        print("Verbose mode enabled.")
