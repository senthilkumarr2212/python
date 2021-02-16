# Task 1
names = ["john", "jake", "jack", "george", "jenny", "jason"]
for name in names:
    if len(name) < 5 and 'e' not in name:
        print('Printing Unique Names : ' +name)


# Task 2
str = 'python'
print('c' + str[1:])


# Task 3
dict = {"name": "python", "ext": "py", "creator": "guido"}
print(dict.keys())
print(dict.values())


# Task 4
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")   
    else:
        print("nothing")


# Task 5
guessnum = input("Enter your Guess Number :")
num = 20
if guessnum == num:
    print("You guessed correctly")
elif int(guessnum) > num:
    print("Your Guess value is greater than the actual number")
else:
    print("Your Guess value is less than the actual number")

