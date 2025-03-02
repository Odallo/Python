#n = int(input("Enter your number: "))
#print(n>=100)

##
# first = int(input("Enter your number: "))
#second = int(input("Enter your number: "))
#third = int(input("Enter your number: "))

#largestNumber = first

#if second > largestNumber:
    #largestNumber = second

#elif third > largestNumber:
    #largestNumber = third

#print("largestNumber =", largestNumber)

# conditional execution
# text = input("Please enter a name: ")
# if text == "Alice":
#     print("Welcome Alice")
# elif text == "Bob":
#     print("Welcome Bob")
# else:
#     print("You are not Alice or Bob")


# tax scenario
# income = float(input("Enter your income: "))
# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
#     tax = 14839.02 + (income/85528) * 0.32 

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")



# loops
# while True:
#     print("Hello, world!")



#Counter
# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)


# #Magic number
# secretNumber = 777
# guess = int(input("Enter a number: "))
# while guess != secretNumber:
#     print("Ha ha! You're stuck in my loop!")
#     guess = int(input("Enter a number: "))
    
# print("Well done, muggle! You are free now.")


# For loop with the break and continue statements
# break - example
# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# # continue - example

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")


# while True:
#     word = input("Enter your word: ")
#     if word == "Chupacabra":
#         print("You have successfully entered your word")
#         break

# Vowel eater
# word = input("Enter your word: ")
# word = word.upper()
# for i in word:
#     if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         continue
#     print(i)
    

# word_without_vowel = ""
# word = input("Enter your word: ")
# word = word.upper()
# for i in word:
#     if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
#         continue
#     word_without_vowel += i
# print(word_without_vowel)

# x = 4
# y = 1
 
# a = x & y
# b = x | y
# c = ~x  # tricky!
# d = x ^ 5
# e = x >> 2
# f = x << 2
 
# print(a, b, c, d, e, f)

# hat_list = [1, 2, 3, 4, 5]  
# intNumber = int(input("Enter an integer number: "))
# hat_list[2] = intNumber
# hat_list.pop(-1)
# print(hat_list.__len__())
# print(hat_list)


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break

# if found:
#     print("Element found at index", i)
# else:
#     print("absent")

# my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# my_list = list(dict.fromkeys(my_list))

# print("The list with unique elements only:")
# print(my_list)



# def greetings():
#     return "Gutene Morgen"
# print(greetings())

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
   

# test_data = [1900, 2001, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")

# def is_year_leap(year):
#    if year % 4 != 0:
#         return False
#    elif year % 100 != 0:
#         return True
#    elif year % 400 != 0:
#         return False
#    else:
#         return True

# def days_in_month(year, month):
#     if month == 2:
#         if is_year_leap(year):
#             return 29
#         else:
#             return 28
#     elif month in [1, 3, 5, 7, 8, 6, 9, 10, 12]:
#         return 31
   

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr, mo, "->", end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Failed")


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates)    # outputs: 4

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}
 
# for item in (d1, d2):
#     d3.update(item)
#     tuple(d3)
 
# print(d3)
 
# my_list = ["car", "Ford", "flower", "Tulip"]

# t =  tuple(my_list)
# print(t)

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)

# print(colors_dictionary)

from random import randrange


def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square


def make_list_of_free_fields(board):
	free = []	
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in ['O','X']: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free


def victory_for(board,sgn):
	if sgn == "X":	# are we looking for X?
		who = 'me'	# yes - it's computer's side
	elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")


