import math
import time
import random
import os
import threading

# Python Tutorial
#
# ----------

#--Variables = a container for a value

#String type:
name = "Matheus"
last_name = "Mota"
#Integer type:
age = 30
#Float type:
height = 220.5
#Boolean Type:
yes = True
no = False
#To make changes to int variable:
age += 2
age -= 4
#To make operations inside variables:
size_woman = 22 + 10
size_man = 4 * 4
size_kid = 20 / 10

#--Multiple Assignment

#Create multiple variables on the same line:
bob, mary, jon = 33, 36, 29

#--Output = Print on screen to the user

#Function print:
print("Hello World!")
print(name)

#To get the type of a var:
print(type(name))
print(type(age))
print(type(height))

#Ways to print different types in a same line:
print("My name is" + " " + name)
print("My age is " + str(age))
print(f"My height is {height}")
print("The man size is {}".format(size_man))

#Print method to display control
x = 1000
y = "Math"
print("The number is {:.3f}".format(x))
print("The number is {:,}".format(x))
print("The number is {:b}".format(x))
print("The number is {:o}".format(x))
print("The number is {:x}".format(x))
print("The number is {:E}".format(x))

#--String Methods

#Most used String methods:
print(len(name))
print(name.find("a"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.count("a"))
print(name.replace("a", "o"))
print(name * 3)

#--Input = Get something from the user

#Create a variable with the function input():
question = input("What is your name?: ")
your_age = int(input("What is your age?: "))
print("Your name is ", question, "and your age is ", str(your_age))

#--Math functions

#Helpful functions to manipulate numbers (import math)
pi = 3.14
x = 20
y = 50
#Print the next int:
print(round(pi))
#Print the upper int:
print(math.ceil(pi))
#Print the lower int:
print(math.floor(pi))
#Print absolute number:
print(abs(pi))
#Print the max number:
print(max(x, y))
#Print the min number:
print(min(x, y))

#--Slicing = Create substring by extracting elements

#Indexing[]
#[start:stop:step]
full_name = "Matheus Mota"
f_name = name[0:7]
reversed_name = name[::-1]
print(f_name)
print(reversed_name)

#Slice()
website = "http://google.com"
slicing = slice(7, -4)
print(website[slicing])

#--If Statement

#Block will execute only if condition is true
verification = int(input("How old are you?: "))
if verification < 18:
    print("Too young. Access denied!")
    if verification == 17:
        print("You can access next year!")
elif verification == 18:
    print("You can access now, Welcome!!")
else:
    print("Welcome!!")

#--Logical operators

#Use to check one or more conditional
#(and, or, not)
temp = int(input("What is the temperature?: "))
if temp not in (0, 90):
    print("Thank you!")
else:
    print("Extreme temperature.")

if temp >= 50 and temp <= 80:
    print("Temperature is great, go outside!")
elif temp < 49 or temp > 81:
    print("The temperature is bad today, stay inside!")

#--While loop

#Will execute as long as it's condition remains true
#To make sure the user will add at least 1 character
enter_name = ""
while len(enter_name) == 0:
    enter_name = input("Enter your name: ")
print(enter_name)

#Or
enter_name = ""
while not enter_name:
    enter_name = input("Enter your name: ")
print(enter_name)

#--Loop control
#(break, continue, pass)

#Break if name added
while True:
    name_user = input("Enter your name: ")
    if name_user != "":
        break

#Print number without "-"
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

#To jump a number
for i in range(1, 21):
    if i == 13:
        pass
    else:
     print(i, end=" ")

#--For loop

#Block will execute a limited amount of times
#for i in range(first number, last number, step)
for i in range(10):
    print(i)

#Make a multiplication table
for i in range(10):
    print(f"1 + {i} = {i+1}")

#Creating a timer (import time)
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    print("Good bye!")

#--Nested loop

#Will execute inner loop and than outer loop
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use?: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

#--Exception

#To detect errors (try, except, finally)
while True:
    try:
        x = int(input("Enter a number: "))
        print(x)
    except ValueError:
        print("Error, Enter number only.")
    finally:
        print("This will always print.")

#--List

#Used to store multiple items
food = ["Pizza", "Hamburger", "Pasta", "Fries",]
#To print 1 item at a list
print(food[1])
#Print a list in a loop for
for x in food:
    print(x)

#List Resources
food.append("Ice Cream")
food.remove("Fries")
food.pop() #Remove the last item
food.insert(0, "Cake")
food.sort()
food.clear()

#2D list
food = ["Pizza", "Hamburger", "Pasta", "Fries",]
drinks = ["Coffee", "Water", "Coke",]
lunch = [food, drinks]
food.extend(drinks)
print(food.index("Pizza"))
print(lunch)
print(food)
#To print 1 item of 1 item
print(lunch[0][0])

#--Tuple
#Collection unchangeable

#Create tuple
student = ("Alex", "Male", "20", "Biology",)
for x in student:
    print(x)

#--Set

#Create a unordered and not indexed items. No duplicate
dishes = {"Fork", "Spoon", "Knife"}
dishes.add("Napkin")
dishes.add("Fork")
print(dishes)

--Dictionary

#Items with unique key
capitals = {"USA": "Washington DC", "Brazil": "Brasilia"}
print(capitals["Brazil"])
print(capitals.get("Germany")) #Safe way to check keys
print(capitals.keys())
print(capitals.values())
#Method to print key and items:
for key,value in capitals.items():
    print(key, value)
capitals.update({"USA": "Las Vegas"})
capitals.update({"China": "Beijing"})
capitals.pop("Brazil")

-- Function

#Put functions on the top of the file
def main():
    print("Function")
#Call function
main()

#Using argument
def addiction(number1, number2):
    print(number1 + number2)
#Call
addiction(2, 2)

#Return value
def multiply(number1, number2):
    result = number1 * number2
    return result
print(multiply(5, 5))

#Keyword arguments
def name(first, middle, last):
    print("Hello" + first + middle + last)
#I use (first, middle, last)
name(last="Mota", first="Matheus", middle="Chaves")

#--Random Method

#Using random (import random)
x = random.randint(1, 10)
letter = ["A", "B", "C", "D"]
rand = random.choice(letter) #To get a random item on the list
print(x)
print(rand)

#--File

#Creating a file
#File exist verification:
try:
    f = open("text.txt", "r")
    print("File does exist!")
except:
    f=open("text.txt", "x")
    print("File does not exist!")
finally:
    f.close()

#Write a file
name = "Hello World!\n"
with open("text.txt", "a") as f:
    f.write(name)

#Read a file
with open("text.txt", "r") as f:
    print(f.read())

#Move a file (import os)
source = "text.txt"
destination = "C:\\Users\\mathe\\text.txt"
try:
    if os.path.exists(destination):
        print("File is there")
    else:
        os.replace(source, destination)
        print("Moved")
except:
    print(source + "was not found")

#Delete a file (import os)
try:
    os.remove(destination)
    print("Deleted")
except FileNotFoundError:
    print("File not found.")

#--Class
#Constructor
class Car:
    def __init__(self, make, model, year):
        self.make = make #Instance variable
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.model} is driving!")

car1 = Car("Toyota", "Corolla", 2020)
car1.drive()

#Inheritance
class Engine(Car):
    pass

car2 = Engine("Chevrolet", "Cruze", 2014)
car2.drive()

#Super function
class Tire(Car):
    def __init__(self, make, model, year, wheel):
        super().__init__(make, model, year)
        self.wheel = wheel

#- Lambda

double = lambda x:x * 2
multiply = lambda x, y: x * y
age_check = lambda age: True if age >= 18 else False
print(multiply(2, 4))
print(age_check(18))

#- Tuple, List, Dictionary manipulation
#Sort
names = ["Matt", "Luz", "Ana"]

names.sort()

for i in names:
    print(i)

#Map
store = [("Shirt", 20), ("Pants", 25), ("Jacket", 50)]

to_euros = lambda data: (data[0], data[1]* 0.80)
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

#Filter
friends = [("Rachel", 19), ("Monica", 18), ("Phoebe", 17)]

age = lambda data: data[1] >= 18

drink = list(filter(age, friends))

for i in drink:
    print(i)

#List Comprehension

squares = [i * i for i in range(1, 11)]
print(squares)

students = [100, 90, 80, 70, 50, 30, 0]

passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)

#Dictionary Comprehension

cities = {"New York0": 32, "Boston": 75, "Los Angeles": 100, "chicago": 50}

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}

#Zip

usernames = ["Mark", "Bro", "Mister"]
passwords = ("1234", "Abc123", "Main1")

users = zip(usernames, passwords)

for i in users:
    print(i)

#if __name__

def main():
    print("starting!")

if __name__ == "__main":
    main()

#- Module
#time

#import time

time.sleep(10)
print(time.ctime(0))
print(time.time())

time_now = time.localtime()
time.strftime("%B %d %Y %H:%M:%S", time_now)
print(time_now)

#Threading

# import threading

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(count)

threading.Thread(target=timer).start()

input("Press to quit")




-- 06:07:55
