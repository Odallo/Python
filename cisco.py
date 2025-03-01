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

def is_year_leap(year):
   if year % 4 != 0:
        return False
   elif year % 100 != 0:
        return True
   elif year % 400 != 0:
        return False
   else:
        return True

def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 6, 9, 10, 12]:
        return 31
   

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
