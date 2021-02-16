#Task 1
""" 
Improvise the guessing game from yesterday by providing 3 tries to the player
""" 
import random
number = random.randint(1, 100)

print("Hello, Welcome to the guessing game !")
print("The number is between 1 and 100")

number_of_tries = 0

 while number_of_tries < 3:
      guess = int(input("Please enter your guess: "))
      number_of_tries += 1
      if guess < number:
          print("Your guess is too low")
      if guess > number:
          print("Your guess is too high")
      if guess == number:
          break
 if guess == number:
     print("Congratulations! You guessed the number in " + str(number_of_tries) + " tries!")
 else:
     print("End of the game! You did not guess the number, The number was " + str(number))



#Task 2
"""
Given a list ['a', 'b', ...] print elements along with their position like 0: a, 1: b one per line
"""

charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
for index,char in enumerate(charList):
    print(f"{index}: {char}")



#Task 3
"""
Loop over a dict and print the value and key in the format value belongs to key
"""
cDict = {'Country': 'India', 'Capital': 'Delhi', 'Citizen': 'Indian'}
for key, value in cDict.items():
    print(key, value)



#Task 4
"""
Demonstrate the else clause being invoked in a while loop. try the opposite as well.
"""
#else clause being invoked
num = int(input("Please enter your number: "))
while num < 10:
    print("Num : " + num)
    num += 1
else:
    print("Please enter the number less than 10")

#else clause not being invoked
num = int(input("Please enter your number: "))
while num < 10:
    print("Num : " + num)
    num += 1
    if num == 10:
      break
else:
    print("Please enter the number less than 10")



#Task 5
"""
write an add function that accepts two numbers and returns their sum
"""
#type hints
def sum(num1: int, num2: int) -> int:
    """Adding two numbers based on user inputs""" #docstring
    sum = num1 + num2
    return num

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(sum(n1, n2))



#Task 6
"""
write a function that accepts any number of args and prints them to the screen one per line
"""
def countries(*args):  
    for clist in args:  
        print (clist) 
    
countries("India", "Canada", "Japan", "Germany", "Australia") 



#Task 7
"""
write a function that accepts any number of kwargs and prints the number of args
"""
def keywargs(**kwargs):
    print(len(kwargs))
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

keywargs(Country: "India", Capital: "Delhi", Citizen: "Indian")



#Task 8
"""
write a function that accepts any number of args and/or kwargs and prints the count of both
"""
def argskw(*args, **kwargs):
    print(len(args) + len(kwargs))

argskw("India", "Canada", "Japan", "Germany", "Australia", Country: "India", Capital: "Delhi", Citizen: "Indian")   



#Task 9
"""
Do a while loop with and without else block getting invoked
"""
#with else block
num = 10
while num > 4:
   print(num)
   num = num - 1
else:
   print("loop is completed")

#without else block
num = 10
while num > 4:
   print(num)
   num = num - 1



#Task 9
"""
Do list comprehension to get odd numbers' squares from this list: [1, 3, 3, 4, 5, 6]
"""
nList = [1,3,3,4,5,6]
numsq = [num**2 for num in nList if num%2 == 1]
for oddnumsq in numsq:
	print(oddnumsq)



#Task 10
"""
write a lambda expression to return average given a total and count
"""
total = int(input("Enter the total: "))
count = int(input("Enter the count: "))

average = lambda total, count : total/count
print(average(total, count))



#Bonus Challenges
#Task 11
"""
Try list comp to get keys that are longer than 4 chars in a dict
"""

cDict = {'Country': 'India', 'Capital': 'Delhi', 'Citizen': 'Indian'}
keyLonger = {key for key in cDict.items() if len(key)>4}
print(keyLonger)



#Task 12
"""
implement nested list comp in any use case
"""
num = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]] 

values = [val for numlist in num for val in numlist] 

"""Return all the values inside the numlist""
print(values)


