#n = int(input("Enter your number: "))
#print(n>=100)

first = int(input("Enter your number: "))
second = int(input("Enter your number: "))
third = int(input("Enter your number: "))

largestNumber = first

if second > largestNumber:
    largestNumber = second

elif third > largestNumber:
    largestNumber = third

print("largestNumber =", largestNumber)