"Paul Yang M06 Prg Assignment 13.1"
"This code will write the current date as a string to the text file today.txt"

import datetime

filename = datetime.datetime.now()

def create_file():

    with open(filename.strftime("%d %B %Y")+" .txt", "w") as file:
        file.write("")

create_file()