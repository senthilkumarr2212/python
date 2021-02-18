#Task 1
#dictionaries
#Task 1 - a
"""
given a list of numbers (nums = [1, 2, 3]) use dict comprehension to create a dict of squares { 1: 1, 2: 4, 3: 9}
"""
nums = [1, 2, 3]
num = {x: x**2 for x in nums}
print(num)



#Task 1 - b
"""
make a list of values alone from the above dictionary [1, 4, 9] using list comprehension
"""
nums = [1, 2, 3]
num = {x**2 for x in nums}
print(num)



#set comprehension
#Task 2
"""
given a list [1, 2, 5, 2, 3, 1, 4, 5], create squares of unique items using set comprehension. {1, 4, 9, 16, 25}
"""
n = [1, 2, 5, 2, 3, 1, 4, 5]
num = {x**2 for x in n}
print(num)



#Task 3
"""
Given a list of tuples with current and min balances: [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)] use comprehensions to get the below:
"""
#Task 3 - a
"""
dict of those with proper balances (above or equal min bal) {"Guido": 2000, "Brandon": 2000}
"""
tList = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
print("Given list : \n" ,tList)

proper_balances = {name : cur_balance for (name, cur_balance, min_balance) in tList if cur_balance >= min_balance}
print(proper_balances)

#Task 3 - b
"""
set of all balances {2000, -52, 900}
"""
set_of_all_balances = {cur_balance for (name, cur_balance, min_balance) in tList}
print(set_of_all_balances)

#Task 3 - c
"""
list of account holders ["Guido", "Raymond", "Jack", "Brandon"]
"""
list_of_account_holders = [name for (name, cur_balance, min_balance) in tList]
print(list_of_account_holders)

#Task 3 - d
"""
dict of user and money each need to fulfill the min balance requirement (those who already have enough bal should not be in the dict) {"Raymond": 1052, "Jack": 100}
"""
min_balance_requirement = {name : min_balance-cur_balance for (name, cur_balance, min_balance) in tList if cur_balance < min_balance}
print(min_balance_requirement)

#Task 3 - e
"""
list of tuples with name and current balance if the balance is above 0 [("Guido", 2000), ("Jack", 900), ("Brandon", 2000)]
"""
list_name_cur_balance = [(name, cur_balance) for (name, cur_balance, min_balance) in tList if cur_balance > 0]
print(list_name_cur_balance)



#Task 4
"""
Write a Developer class that has a code function and a languages list.
"""

#Task 4 - a
"""
code function should accept a language param and if the language is in the languages list it should print code in <language>.
"""

class Developer :

     def __init__(self, devlanguages):
         self.devlanguages= ["C","C++","Java","Php","Python"]
     def code(self,devlanguage): 
            if(devlanguage in list(map(lambda x: x.upper(), self.devlanguages ))): 
                  print(f"code in {devlanguage}")
            else:
                 print(f"You entered code {devlanguage} is not in the list")          

     def resume(self):
        print(self.devlanguages) 
        
inputlanguage = input("Please enter the coding language: ")
devlanguage = inputlanguage.upper()
s = Developer("")
s.code(devlanguage)
print(devlanguage.__repr__())
print(devlanguage.__str__())

#Task 4 - b
"""
resume function that prints languages of the developer.
"""
s.resume()

#Task 4 - C
"""
Write a SrDeveloper class that inherits Developer and adds review function. review should also be limited to languages list.
"""
class SrDeveloper(Developer):
    def __init__(self):
        Developer.__init__(self)
        self.reviews = []
    def review(self,review):            
        if(len(self.reviews)<=len(self.devlanguages)):
            self.reviews.append(review)   
            print(self.reviews)

srdevrev = SrDeveloper()
srdevrev.review("Good")

#Task 4 - C
"""
Write a TechLead class that inherits from SrDeveloper and adds design function
"""
class TechLead(SrDeveloper):
    def __init__(self):
        SrDeveloper.__init__(self)

    def design(self):
        print("Design for TechLead")

tlead = TechLead()
tlead.design()



#Task 5
"""
create a class that provides the factorials for the list of numbers provided.
"""
import math
L = [1, 2, 3, 4, 5, 6]
class Factorial:
    def factorial(self, fact):
         for num in fact:
            print(math.factorial(num))


fact = Factorial()
fact.factorial(L)



#Task 6
"""
import a func from a module and call it to print some output
"""
from ImportProgram import callFunction
callFunction()



#Task 7
"""
import a func and rename it to use in your module from another
"""
from ImportProgram import callFunction as changeFunc
changeFunc()



#Task 8
"""
create a module that prints "I'm running" only when it's ran as a script (not as a module using import)
"""

def imrunning():
    if __name__ == "__main__":
        print("I'm Running")

imrunning()
