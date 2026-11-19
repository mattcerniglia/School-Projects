#Matthew Cerniglia
#Dictionary
#Complete

#This program counts the number of times each letter appears in a text file ignoring any non-alphabetic characters
#It then returns a dictionary with the letter as the key and the count as the value.
#The dictionary is sorted in descending order based on the count.

#Not exactly a necesary compoenent, more for cleaner UI so the user can read that the program is wanting the file to be converted to .txt.
import time 


#file_path is the variable used that holds the input from the user as the path to the file.
#Quotes and whitespace are stripped from the input to ensure a clean file path.
file_path = input("Copy & Paste or type in the file path: ").strip('"').strip("'").strip()

#text is the variable that holds the contents of the file after it is checked to be a .txt file and read.
#Python can only read .txt without further libraries,  to ensure the program runs correctly, it checks if the file path ends with .txt.
#If not, it prompts the user to change the file type. If it does, it opens the file and reads the text into a variable called text.
if not file_path.endswith('.txt'):
    print('This program does not support this file type. Please change to a .txt file.')
    time.sleep(20)
else:
    with open(file_path, 'r') as file:
        text = file.read()

#letter_count is the list that holds the count of each letter in the text. It is initialized as an empty dictionary.
#The program iterates through each character in the text, checking if it is an alphabetic character using the isalpha() method.
#The program then checks if the character is already a key in the letter_count dictionary.
#If it is, it adds it to the count for that character. If it is not, it adds the character as a new key with a count of 1.
def count_letters(text):      
    letter_count = {}
    for char in text:
        if char.isalpha():

#If it is an alphabetic character, it converts it to lowercase to ensure that the count is case-insensitive.
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
   
#the letter_count dictionary is then sorted in descending order based on the count using the sorted() function and a lambda function as the key.  
    letter_count = dict(sorted(letter_count.items(), key=lambda x: x[1], reverse=True))
    return letter_count

if file_path.endswith('.txt'):
    letter_count = count_letters(text)
    print(letter_count)
