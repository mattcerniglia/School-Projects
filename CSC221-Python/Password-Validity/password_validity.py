#Matthew Cerniglia -  Complete Project (extra credit attempted)
#LF298.CSC.221.100V.SP26.14W
#Password Validity
def check_password(): #the function that takes in input from the user as possible password and checks against the rules if it is a valid password
	special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
	max_attempts = 4 #extra credit - max 4 attempts to enter  a valid password.
	attempt = 0
	while attempt < max_attempts:
		if attempt == 0:
			password = input("Please Enter A Password: ")
		else:
			password = input("Please re-enter your password or close the program: ")
		attempt += 1

		if len(password) < 10: 
			print("Password must be at least 10 characters long.")
			if attempt < max_attempts:
				print(f"{max_attempts - attempt} attempts remaining.")
			continue
		if len(password) > 20:
			print("Password must be no more than 20 characters long.")
			if attempt < max_attempts:
				print(f"{max_attempts - attempt} attempts remaining.")
			continue
		if not any(char.isdigit() for char in password): #first three make sure there is more than 10, less than 20 & a number in password
			print("Password must contain at least one digit.")
			if attempt < max_attempts:
				print(f"{max_attempts - attempt} attempts remaining.")
			continue
		
		if not any(char in special_chars for char in password): #uses the special characters defined earlier in the function and checks if they are in the password
			print("Password must contain at least one special character.")
			if attempt < max_attempts:
				print(f"{max_attempts - attempt} attempts remaining.")
			continue
		print("Password is valid.")
		return True

	print("Too many attempts. Please try again later.") #extra crdit - if too many attempts are made, it will close the program.
	return False
check_password()