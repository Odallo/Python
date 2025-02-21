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