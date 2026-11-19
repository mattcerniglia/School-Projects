#Matthew Cerniglia - Complete Project
#LF298.CSC.221.100V.SP26.14W
#Pizza Pie

import time #it was just closing immediately for me running on cmd

print('Calculator For price per square inch of a pizza')
def get_area(): #asks the user to type the size of their pizza and uses that innput to calculate the area of the pizza, returns the area to be used in the next function
    dia = int(input('Enter the size of the pizza in inches: '))
    print(f"The area of the pizza is: {3.14159*(dia/2)**2:.2f} square inches.")
    r = dia/2   
    area = 3.14159*(r**2)
    return area
area = get_area() #calls the function for gathering the area and saves it as the variable "area" so it can be used in the last function

def price_per_sqinch(): #asks the user for the price of the pizza, takes in the area that was previously defined, and divides the price by that. lastly, it prints/displasys the price per square inch.
    price = float(input('Enter the price of the pizza in dollars: '))
    price_per_square_inch = price / area
    print(f"The price per square inch of the pizza is: ${price_per_square_inch:.2f}")
price_per_sqinch()
time.sleep(30)