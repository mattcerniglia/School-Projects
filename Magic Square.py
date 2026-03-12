#Matthew Cerniglia
# #Magic Square - Complete

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

def magic_square_check(square):
    nums = [x for row in square for x in row]
    # check numbers are 1..9 and no repeats
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

    # main loop: keep asking until a valid Lo Shu magic square is entered
while True:
    square = create_lo_shu_magic_square()
    for row in square:
        print(row)
    if magic_square_check(square):
        print("Valid Lo Shu Magic Square.")
        break
    else:
        print("Not a valid magic square. Try again.")

print(magic_square_check(square)) # Output: True

magic_square_check(square)