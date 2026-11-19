#Matthew Cerniglia
#File Fun - Complete
#LF298.CSC.221.100V.SP26.14W
#This is the program that is reading the file that was created by the other program.
#It will read and print the file, then check if each character in the file is a digit, and 
#If it is a it will add it to a count of all the digits.


#This is the function that reads and prints, then checks if each character in the file is a digit, and if it is a it will add it to a count of all the digits. 
# Using the variable "readfiles" to call the function in the other program, to read the file that was created by the other program. 
# Using a with statement to open the file, with the "r" parameter to indicate that it is being read. 
# Using readlines() to read the file, and a for loop to print each line of the file.
# Using another for loop to iterate through each character in each line, with an if statement to check if the character is a digit using isdigit().
#If it is a digit, adding it to a total count using int() to convert the character to an integer.
def readfiles():
        with open(r"C:\Users\mattc\Documents\filefunnumbers.txt", "r") as h: #Designating where the file is located, and using "r" to indicate that it is being read.
            readfiles = h.readlines() #Using readlines() to read the file, and a for loop to print each line of the file.
        total = 0
        for line in readfiles:
            print(line.strip()) 
        for line in readfiles:
            for char in line: #Using another for loop to iterate through each character in each line, with an if statement to check if the character is a digit using isdigit().
                if char.isdigit(): 
                    total += int(char) #If it is a digit, adding it to a total count using int() to convert the character to an integer.
        print(f"The total of the numbers in the file is: {total}")

readfiles()
