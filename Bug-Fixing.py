            # Day 1. Exercise 1 - pronaci i ispraviti greske
answers = ['Yes', 'No', 'Yes', 'No', 'No'
# RESENJE - nedostajala je uglasta zagrada na kraju liste!!

            # Day 1. Exercise 2 - pronaci i ispraviti greske
my_answer = input("What is your answer?")
answers = ['Yes', 'No', 'Yes' 'No' my_answer]
 # RESENJE - nedostajala 2 zareza (ispred i iza 'No')!!

            # Day 1. Exercise 3 - pronaci i ispraviti greske
my_answer = input(What is your answer?)
answers = ['Yes', 'No', 'Yes', 'No', my_answer]
# RESENJE - nedostajali znaci navoda pre uglaste zagrade!!

            # Day 1. Exercise 4 - pronaci i ispraviti greske
my_answer = input["What is your answer?"]
answers = ['Yes', 'No', 'Yes', 'No', my_answer]
# RESENJE #bile su uglaste zagrade umesto obicnih!!



            # Day 2. Exercise 1 - pronaci i ispraviti greske
while True
print("Hello")
#RESENJE - trebalo je odvojiti PRINT tabom!!

            # Day 2. Exercise 2 - pronaci i ispraviti greske
greeting = "hello"
print(upper(greeting))
#RESENJE - zamenjena mesta UPPER i GREETING!!

            # Day 2. Exercise 3 - pronaci i ispraviti greske
countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)
# RESENJE - trebalo je odvojiti PRINT tabom!!



            # Day 3. Exercise 1 - pronaci i ispraviti greske
for i in buttons:
    print(i.capitalize())

buttons = ["cancel", "reply", "submit"]
# RESENJE - definisanje LISTe treba uraditi pre FOR LOOP funkcije!!

            # Day 3. Exercise 2 - pronaci i ispraviti greske
buttons = ["cancel", "reply", "submit"]

for i in buttons:
print(i.capitalize())
# RESENJE - treba odvojiti PRINT tabom!!

            # Day 3. Exercise 3 - pronaci i ispraviti greske

for item in ["sandals", "glasses", "trousers"):
    print(item.capitalize)
# RESENJE - iza CAPITALIZE nedostaju zagrade!!


            # Day 4. Exercise 1 - pronaci i ispraviti greske
elements = ['a', 'b', 'c']
print(elements(1))
# RESENJE - treba obicne zameniti uglastim zagradama!!

            # Day 4. Exercise 2 - pronaci i ispraviti greske
elements = ['a', 'b', 'c']
new = 'x'
new = elements[1]
print(elements)
#RESENJE - elements[1] = new


            # Day 5. Exercise 1 - pronaci i ispraviti greske
menu = ["pasta", "pizza", "salad"]
user_choice = input("Enter the index of the item: ")
message = f"You chose {menu[user_choice]}."
print(message)
#RESENJE - mora se input definisati kao INT jer samo tako moze da se koristi za indexiranje!!

            # Day 5. Exercise 2 - pronaci i ispraviti greske
menu = ["pasta", "pizza", "salad"]
for i, j in enumerate[menu]:
    print(f"{i}.{j}")
#RESENJE - posle ENUMERATE idu obicne zagrade, ne uglaste!

            # Day 5. Exercise 3 - pronaci i ispraviti greske
menu = ["pasta", "pizza", "salad"]
for i, j in enumerate(menu):
    print("f{i}.{j}")
#RESENJE - oznaku F (f-string) treba napisati ispred znaka navoda (") a ne iza

            # Day 6. Exercise 1 - pronaci i ispraviti greske
file = open("data.txt", 'w')

file.write("100.12") + "\n"
file.write("111.23")

file.close()
#RESENJE - oznaku "\n" treba napisati ispred znaka navoda (npr. "100.12\n")

            # Day 6. Exercise 2 - pronaci i ispraviti greske
file = open("data.txt", 'r')
file.write("100.12")
file.close()
#RESENJE - ukoliko zelimo da ispisemo neku stvar, potrebno je da otvorimo WRITE MODE ('w') a ne READ MODE ('r')

            # Day 7. Exercise 1 - pronaci i ispraviti greske
temperatures = [10, 12, 14]

file = open("file.txt", 'w')
file.writelines(temperatures)
#RESENJE
temperatures = [10, 12, 14]
temperatures = [str(i) + '\n' for i in temperatures]

file = open("file.txt", 'w')
file.writelines(temperatures)

            # Day 7. Exercise 2 - pronaci i ispraviti greske
numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for item in numbers]
print(numbers)
#RESENJE - INT(NUMBER) > INT(ITEM)
numbers = [10.1, 12.3, 14.7]
numbers = [int(item) for item in numbers]
print(numbers)

            # Day 8. Exercise 1 - pronaci i ispraviti greske
with open("file.txt", 'r') as file:
    print(file.read())
    print(len(file.read()))
#RESENJE - INT(NUMBER) > INT(ITEM)
with open("file.txt", 'r') as file:
    content = file.read()
print(content)
print(len(content))

            # Day 9. Exercise 1 - pronaci i ispraviti greske
ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
if '_' in id:
x = x + 1
print(x)
#RESENJE - fale tabovi u IF loopu
ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
    if '_' in id:
        x = x + 1
print(x)

            # Day 9. Exercise 2 - pronaci i ispraviti greske
ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
    if '_' in id:
        x = x + 1
    print(x)
#RESENJE - greska je u tome sto ispred PRINTA stoji tab a ne bi trebalo jer ovako ispisuje rezultat za svaku iteraciju
ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
    if '_' in id:
        x = x + 1
print(x)

            # Day 9. Exercise 3 - pronaci i ispraviti greske
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area > 10:
    print("OK")
else:
    print("NOT OK")
# RESENJE -
length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")

    # Day 10. Exercise 1 - pronaci i ispraviti greske
waiting_list = ["john", "marry"]
name = input("Enter name: ")

number = waiting_list.index(name)
print(f"{name}'s turn is {number}")
# RESENJE - potrebno je dodati TRY-EXCEPT funkciju koja ce ispisivati trazeno obavestenje u slucaju ValueError-a
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"{name} is not in the list")


    # Day 11. Exercise 1 - pronaci i ispraviti greske
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    print(maximum)


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
# RESENJE
def get_maximum():
    celsius_local = [14, 15.1, 12.3, 42]
    maximum = max(celsius_local)
    return maximum


print(get_maximum())

fahrenheit = get_maximum() * 1.8 + 32
print(fahrenheit)

            # Day 12. Exercise 1 - pronaci i ispraviti greske
def speed(distance, time):
    return distance / time


print(speed([200, 4]))
#RESENJE - potrebno je samo obrisati uglaste zagrade u printu!
def speed(distance, time):
    return distance / time


print(speed(200, 4))

            # Day 12. Exercise 2 - pronaci i ispraviti greske
def speed(distance, time):
    return distance / time


print(speed(5, 300))
#RESENJE - treba obrnuti 5 i 300
def speed(distance, time):
    return distance / time


print(speed(300, 5))

            # Day 13. Exercise 1 - pronaci i ispraviti greske
def calculate_time(g=9.80665, h):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)
#RESENJE - POTREBNO JE NAVESTI H ispred DEFAULT VALUE G.
def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)

            # Day 14. Exercise 1 - pronaci i ispraviti greske
#main.py:
import functions
nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)

#functions.py:
def count(phrase):
    return phrase.count('.')
#RESENJE - neophodno je navesti FUNCTIONS ispred count("...")
import functions
nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)

#functions.py:
def count(phrase):
    return phrase.count('.')

    # Day 14. Exercise 2 - pronaci i ispraviti greske
#main.py:
import functions.py

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)

#functions.py:
def count(phrase):
    return phrase.count('.')
#RESENJE - u nazivu funckije ne treba da stoji .PY
#main.py:
import functions

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)

#functions.py:
def count(phrase):
    return phrase.count('.')

    # Day 14. Exercise 2 - pronaci i ispraviti greske
#main.py:
from functions import count

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)

#functions.py:
def count(phrase):
    return phrase.count('.')

#RESENJE - ispred COUNT ne treba da stoji FUNCTIONS !
#main.py:
from functions import count

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)

#functions.py:
def count(phrase):
    return phrase.count('.')