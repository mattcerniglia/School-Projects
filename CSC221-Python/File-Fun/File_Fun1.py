#Matthew Cerniglia
#File Fun - Complete
#LF298.CSC.221.100V.SP26.14W
#This is the inital program that is creating the file that will be read by the other program. 
#This file will contain a random number of lines, with each line containing a random number between 1 and 500. 
#The program also includes error handling for the file creation process.

import random

#This is the function that creates the file, with error handling for any potential issues that may arise during the file creation process.
#  Using the variable "makefiles" to call the function in the other program, to create the file that will be read by the other program. 
#  Using number as a variable to generate the random numbers that will be written to the file, with parameters of 1 - 500. Using a for loop to determine the number of lines that will be in the file, with parameters of 1 - 100.
#  Using a try-except block to handle any potential errors that may arise during the file creation process, including IOError, ValueError, and any other general exceptions.
def makefiles(): 
    try:
        with open(r"C:\Users\mattc\Documents\filefunnumbers.txt", "w") as f: #Designating where the file will be created, and using "w" to show that it will be wrote in.
                for _ in range(random.randint(1, 100)): #Using a "for" loop to determine the number of lines that will be in the file, with parameters of 1 - 100.
                    number = random.randint(1, 500) #Using number as a variable to generate the random numbers that will be written to the file, with parameters of 1 - 500.
                    f.write(f"{number}\n") 
    except IOError as e: #Checking for an I/O error during the file creation process, and printing an error message if one occurs.
        print("An I/O error occurred:", e)
    except ValueError as e: #Checking for a value error during the file creation process, and printing an error message if one occurs.
        print("A value error occurred:", e)
    except Exception as e: #Checking for any other general exceptions during the file creation process, and printing an error message if one occurs.
        print("An error occurred:", e)
    print("File creation complete.")

    makefiles()