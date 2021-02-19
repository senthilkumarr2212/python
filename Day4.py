#Task 1 
"""
Create a class that implements __iter__ and __next__ methods.
It should accept a string and provide an iterator that traverses every other character in the string i.e. given hello, provide h, l, o and StopIteration on consecutive next calls. 
"""
class Jumper:

     def __init__(self, chars):
         self.n = 0
         self.chars = chars

     def __iter__(self):
         return self

     def __next__(self):
         if self.n < len(self.chars):
            result = self.chars[self.n]
            self.n += 2
            return result
         else:
            raise StopIteration

j = Jumper('python')
it = iter(j)
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) #StopIteration hits



#Task 2 
"""
create a CSV file containing names and experience of the participants. Note: Not xls, just a comma separated plain text file.
"""
import csv

with open('participants.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Name', 'Experience'])
    writer.writerow(['Ramesh', 3])
    writer.writerow(['Naveen', 5])
    writer.writerow(['Suresh', 2])
    writer.writerow(['Elango', 4])



#Task 3
"""
write a program to traverse the current directory (recursively) and print only python file names.
"""
import pathlib

path = pathlib.Path.home() / 'C:\PythonFiles'
for p in path.glob('*.py'):
    print(p.name)



#Task 4
"""
write a program to traverse the current directory (recursively) and print only python file names.
"""
import sys
print(f"List of Command Line Arguments : {list(sys.argv)}")



#Task 5 & 6
"""
Rewrite the guessing game program to throw a custom error when the user is out of tries.
accept input from a user and handle type, value errors
"""
import random
number = random.randint(1, 100)

print("Hello, Welcome to the guessing game !")
print("The number is between 1 and 100")

number_of_tries = 0

 while number_of_tries < 3:
      try:
      guess = int(input("Please enter your guess: "))
      number_of_tries += 1
      if guess < number:
          print("Your guess is too low")
      if guess > number:
          print("Your guess is too high")
      if guess == number:
       print("Congratulations! You guessed the number in " + str(number_of_tries) + " tries!")
       break
    except TypeError:
       print("The type of guess should be an Integer")
    except ValueError:
        print('error')
    if number_of_tries >=3:
     print("End of the game! You did not guess the number, The number was " + str(number))


#Task 7
"""
demonstrate key and index errors in an example
"""

try:
    cnt = {'country':'india','capital':'delhi','citizen':'indian'}
    print(cnt['name'])
except KeyError:
    print("Key Error Triggered")

try:
    list = [1,2,3,4,5]
    print(list[6])
except IndexError:
    print("Index Error Triggered")
