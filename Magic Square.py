#This contains two programs, one that takes user input to create a 3x3 grid of numbers, and another that checks if the grid is a valid Lo Shu Magic Square. 
#A Lo Shu Magic Square is a 3x3 grid of numbers from 1 to 9 where each row, column, and both main diagonals sum to 15, and no number is repeated.
#The program will keep asking the user to input a grid until a valid Lo Shu Magic Square is entered, at which point it will print the square and confirm its validity.

#Nums is the variable that takes the user input and splits it into a list of strings. 
#The program then checks if the input is valid (9 numbers between 1 and 9, no repeats) and constructs a 3x3 grid (square) from the input. 
#Square is a 2D list that represents the 3x3 grid of numbers. 
#K is a variable used to keep track of the index while filling the square with the user input numbers.
def create_lo_shu_magic_square():
    while True:
        nums = input("Enter 9 numbers between 1 and 9, separated by spaces: ").split()
        try:
             nums = [int(x) for x in nums]
        except ValueError: 
            print("Please enter integers only.")
            continue
        if len(nums) != 9: 
            print("Please enter exactly 9 numbers.")
            continue
        square = [[0]*3 for _ in range(3)]
        k = 0
        for i in range(3):
            for j in range(3):
                square[i][j] = nums[k]
                k += 1
        return square

#The magic_square_check function verifies if the grid is a valid Lo Shu Magic Square by checking the sums of rows, columns, and diagonals, as well as ensuring all numbers are unique and within the specified range.
#Correct_sum is the variable that holds the value 15, which should be the sum for each row, column, and diagonal.
#Nums is the variable that flattens the 3x3 grid into a single list for easier validation of uniqueness and range.
#X is the variable that represents each number in the grid, which is checked to ensure it is between 1 and 9.
def magic_square_check(square):
    nums = [x for row in square for x in row]
    if any(not (1 <= x <= 9) for x in nums):
        print("All numbers must be between 1 and 9.")
        return False
    if len(set(nums)) != 9:
        print("Numbers must not repeat.")
        return False
    correct_sum = 15
    for i, row in enumerate(square):
        if sum(row) != correct_sum:
            print(f"Row {i} does not sum to {correct_sum}.")
            return False
    for column in range(3):
        if sum(square[row][column] for row in range(3)) != correct_sum:
            print(f"Column {column} does not sum to {correct_sum}.")
            return False
    if (square[0][0] + square[1][1] + square[2][2] != correct_sum or
        square[0][2] + square[1][1] + square[2][0] != correct_sum):
        print("Diagonals do not sum to 15.")
        return False
    return True

#Keeps having user input new numbers until a correct Magic square is made then it will print the square and confirm its validity.
#Square is the variable that holds the 3x3 grid of numbers from the user input.
while True:
    square = create_lo_shu_magic_square()
    for row in square:
        print(row)
    if magic_square_check(square):
        print("Valid Lo Shu Magic Square.")
        break
    else:
        print("Not a valid magic square. Try again.")

print(magic_square_check(square)) 

magic_square_check(square)
