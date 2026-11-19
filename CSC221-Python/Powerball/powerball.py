#Matthew Cerniglia
#LF298.CSC.221.100V.SP26
#Powerball
#Complete Program
#This program is reading a file containing past powerball winners, and sorting through a few parameters.
#The program is designed to analyze the frequency of numbers drawn in past Powerball lottery tickets. 
#It reads the ticket data from a text file, counts the occurrences of each number, and provides insights such as the most common numbers, least common numbers, overdue numbers, and the frequency of numbers within specific ranges.
#The Powerball is a lottery game where players select five numbers from 1-69 white balls and one number 1-26 red balls (the Powerball). 

import os 
#downloads_dir sets a variable as the path to the user's Downloads folder, and 
#file_path takes downloads_dir and adds the full path to the "tickets.txt" file within that folder. 
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(downloads_dir, "tickets.txt")

#Provides the path to the "tickets.txt" file, which is expected to be located in the user's Downloads folder.
#The code then opens the file in read mode.
#tickets is the variable created to store the contents of the file line by line.
with open(file_path, "r") as file:
    tickets = file.readlines()
    
#number_count is a dictionary that will be used to count the occurrences of each number in the tickets.
#numbers is a list of the first five numbers in each ticket, which would be the main plays.
#sorted_numbers is the returned variable storing the most common numbers sorted in descending order based on their count, and the function returns the top 14 most common numbers.
#This code block is taking the input from the tickets, going through the first five numbers and sorting them based on how many times they appear in the tickets
#It  then returns the 15 most common numbers.
def most_common_numbers(tickets):
    number_count = {}
    for ticket in tickets:
        numbers = ticket.strip().split()[0:5]
       
        #strip and split are used to remove any whitespace and split the ticket into individual numbers. The [0:5] slice is used to get only the first five numbers of each ticket, which are the main numbers.
        for number in numbers:
            if number in number_count:
                number_count[number] += 1
            else:
                number_count[number] = 1
    sorted_numbers = sorted(number_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_numbers[:15]

#Same as the previous block, number_count is a dictionary that will be used to count the occurrences of each number in the tickets.
#numbers is a list of the first five numbers in each ticket, which would be the main plays.
#sorted_numbers is the returned variable storing the least common numbers sorted in ascending order based on their count.
#This code block is taking the input from the tickets, going through the first five numbers and sorting them based on how many times they appear in the tickets in ascending order.
#It then returns the 15 least common numbers.
def least_common_numbers(tickets):
    number_count = {}
    for ticket in tickets:
        numbers = ticket.strip().split()[0:5]
            
        #strip and split are used to remove any whitespace and split the ticket into individual numbers. The [0:5] slice is used to get only the first five numbers of each ticket, which are the main numbers.
        for number in numbers:
            if number in number_count:
                number_count[number] += 1
            else:
                number_count[number] = 1
    sorted_numbers = sorted(number_count.items(), key=lambda x: x[1])
    return sorted_numbers[:15]

#Same as the previous block, number_count is a dictionary that will be used to count the occurrences of each number in the tickets.
#numbers is a list of the first five numbers in each ticket, which would be the main plays.
#sorted_numbers is the returned variable storing the overdue numbers sorted in ascending order based on their count.
#This code  block is taking the input from the tickets, going through the first five numbers and sorting them based on how many times they appear in the tickets in ascending order.
#It then returns the 5 least common numbers, which are considered overdue.
def overdue_numbers(tickets):
    number_count = {}
    for ticket in tickets:
        numbers = ticket.strip().split()[0:5]
        
        #strip and split are used to remove any whitespace and split the ticket into individual numbers. The [0:5] slice is used to get only the first five numbers of each ticket, which are the main numbers.
        for number in numbers:
            if number in number_count:
                number_count[number] += 1
            else:
                number_count[number] = 1
    sorted_numbers = sorted(number_count.items(), key=lambda x: x[1])
    return sorted_numbers[:5]

#Same as the previous block, number_count is a dictionary that will be used to count the occurrences of each number in the tickets.
#numbers is a list of the first five numbers in each ticket, which would be the main plays.
#numbers_to_20 is a list of the numbers from the ticket that are between 1 and 20, using list comprehension to filter out any numbers that are not in this range.
#frequency_of_numbers_thru20 is returned storing the frequency of numbers 1-20 in order.
#This code block is taking the input from the tickets, going through the first five numbers and filtering out any numbers that are not between 1 and 20. 
#It then counts how many times each number between 1 and 20 appears in the tickets and returns the frequency of these numbers in order.
def frequency_of_numbers_thru20(tickets):
    number_count = {}
    for ticket in tickets:
        numbers = ticket.strip().split()[0:5]
        
        #strip and split are used to remove any whitespace and split the ticket into individual numbers. The [0:5] slice is used to get only the first five numbers of each ticket, which are the main numbers.
        numbers_to_20 = [int(num.lstrip('0') or 0) for num in numbers if num.lstrip('0').isdigit() and 1 <= int(num.lstrip('0') or 0) <= 20]
        for number in numbers_to_20:
            if number in number_count:
                number_count[number] += 1
            else:
                number_count[number] = 1
    # Sort numbers by their value (1-20) and return their frequencies
    return [(num, number_count.get(num, 0)) for num in range(1, 21)]

#powerball_count is a dictionary that will be used to count the occurrences of each Powerball number in the tickets.
#powerball is the variable that stores the Powerball number from each ticket, which is assumed to be at index 5, the 6th item.
#The code checks if the Powerball number is between 1 and 15, and if so, it adds to the count for that Powerball number in the powerball_count dictionary.
#frequency_of_powerball is returned storing the frequency of Powerballs 1-15 in order
def frequency_of_powerball(tickets):
    powerball_count = {i: 0 for i in range(1, 16)}  # Initialize count for Powerballs 1-15
    for ticket in tickets:
        powerball = int(ticket.strip().split()[5])  # Assuming the Powerball number is the 6th element (index 5)
        
        #strip and split are used to remove any whitespace and split the ticket into individual numbers. The [5] index is used to get the Powerball (6th) number from each ticket.
        if 1 <= powerball <= 15:
            powerball_count[powerball] += 1
    return list(powerball_count.items())

#main function is defined to execute the complilation of functions and print the results for most common numbers, least common numbers, overdue numbers, frequency of numbers 1-20, and frequency of Powerball numbers.
def main():
    print("Most Common Numbers:")
    for number, count in most_common_numbers(tickets): #This uses the most_common_numbers function to get the returned list of tuples (number, count). It then prints each number and its count.
        print(f"Number: {number}, Count: {count}")

    print("\nLeast Common Numbers:")
    for number, count in least_common_numbers(tickets): #This uses the least_common_numbers function to get the returned list of tuples (number, count). It then prints each number and its count.
        print(f"Number: {number}, Count: {count}")
    
    print("\nOverdue Numbers:")
    for number, count in overdue_numbers(tickets): #This uses the overdue_numbers function to get the returned list of tuples (number, count). It then prints each number and its count.
        print(f"Number: {number}, Count: {count}")
    
    print("\nFrequency of Numbers 1-20:")
    for number, count in frequency_of_numbers_thru20(tickets): #This uses the frequency_of_numbers_thru20 function to get the returned list of tuples (number, count). It then prints each number and its count.
        print(f"Number: {number}, Count: {count}")
    
    print("\nFrequency of Powerball Numbers:")
    for powerball, count in frequency_of_powerball(tickets): #This uses the frequency_of_powerball function to get the returned list of tuples (powerball, count). It then prints each Powerball number and its count.
        print(f"Powerball Number: {powerball}, Count: {count}")
    
main()