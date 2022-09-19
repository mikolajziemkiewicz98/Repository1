"""

print("Hello World!")
wiek = 30
print(f'Wiek: {wiek}')


VAT = 21

cnj = 10
cna = 20

cbj = cnj * (1 + VAT / 100)
cba = cna * (1 + VAT / 100)

x = 5
y = 3
z = 4
a,b,c = 6,7,8
f=g=h = 1

imie = 'arek'
imie_Nowe = imie.capitalize()

print(imie)
print(imie_Nowe)

#Instrukcje warunkowe#

liczba = -90
if liczba < 0:
    print(liczba + (2 * (- (liczba))))
elif liczba == 0:
    print(0)
else:
    print(liczba)

#Pętle#

liczba = 0

while liczba <= 5:
    print(liczba)
    liczba += 1

liczba = 10

while liczba >= 0:
    print(liczba)
    liczba -= 1


wynik = 0


i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1

print("Wynik doawania licz to: ", wynik)

"""


"""
for i in range(0, 4):
    x = int(input("Podaj liczbę: "))
    wynik += x


print("Wynik doawania licz to: ", wynik)



for i in range(200):
    if (i % 5 == 0) and (i % 7 == 0):
        print("Liczba", i, " jest podzielna przez 5 i 7")


wynik = 0

i = 0
while i < 3:
    x = int(input("Podaj dowolną liczbę: "))
    if (x> 0):
        wynik += x
    else:
        print("Liczba musi być dodatnia!")
        continue
    print("Obecny wynik dodawania to: ", wynik)
    i += 1

"""

"""

wynik = 0

i = 0
while i < 3:
    x = int(input("Podaj dowolną liczbę: "))
    if (x % 2 == 0) and (x > 0):
        wynik += x
    else:
        print("Liczba musi być *jEDNOCZEŚNIE* parzysta i dodatnia!")
        continue
    print("Obecny wynik dodawania to: ", wynik)
    i += 1

"""

"""

szukana_liczba = 40

while x != szukana_liczba:
    x = int(input("Podaj dowolną liczbę: "))
    if x == szukana_liczba:
        print("Brawo! Odgadłeś liczbę!")
    else:
        print("Niepoprawna liczba. Sprubój ponownie!")
        continue


print("Szukana liczba to: ", szukana_liczba)


"""

"""

szukana = 40
i =5


while x != szukana and i > 0:
    x = int(input("Podaj liczbę: "))
    if x == szukana:
        print("Brawo! Odgadłeś liczbę!")
    elif x < szukana:
        print("Za mała liczba. "
              "Zostało prób: ", (i - 1))
        i -= 1
    elif x > szukana:
        print("Za duża liczba. "
              "Zostało prób: ", (i - 1))
        i -= 1
    if i == 0:
        print("Wyczerpałeś próby.")
        continue

"""

"""

#listy, krotki, słowniki, zbiory#

list = [4, 5, 6, 7]

for lel in list:
    print(lel)

tuple = (8, 9, 0, 1)

for tel in tuple:
    print(tel)

dict = {1: 'A',
        2: 'B',
        3: 'C',
        4: 'D'}

for key in dict:
    print(key,":",dict[key])


people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}
          ]


for dictionary in people2:
         for key in dictionary:
             print(key, dictionary [key])



people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
         }


for id in people:
    print("\n")
    for key in dictionary:
        print(key, ":", dictionary[key])


definicje = {}

while True:

    print("1: Dodaj definicji")
    print("2: Znajdź definicji")
    print("3: Usun definicji")
    print("4: Zakończ")

    wybor = input("Co chcesz zrobić?: ")

    if wybor == "1":
        klucz = input("Podaj słowo do zdefiniowania: ")
        definicja = input("Podaj definicję: ")
        definicje[klucz] = definicja
        print("Definicja dodana pomyślnie!")
    elif wybor == "2":
        klucz = input("Czego szukasz?: ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie ma szukanego hasła")
    elif wybor == "3":
        klucz = input("Jaką definicę chcesz usunąć?: ")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja: ", [klucz],"została usunięta pomyślnie")
        else:
            print("Nie ma takiego hasła")
    elif wybor == "4":
        print("Działanie programu zakończone")
        break
    else:
        print("Niewłaściwa wartość.")

"""

"""

raised_100_gen = (el**2
                  for el in range(100))


print(sum(raised_100_gen))


numbers = [1, 2, 3, 4, 5, 6]


multinumbers = {number: number*number
               for number in numbers}


celcius = {'T1': 20,'T2': -15,'T3': 0,'T4': 12,'T5': 24}


farenheitT = {key: (celcius*1.8) + 32
              for key, celcius in celcius.items()}



numbers_gen = (
                el
                for el in range(2, 471)
                if el % 7 == 0
                if el % 5 != 0
                )

for el in numbers_gen:
    print(el)

"""

"""

#Funkcje#


def pole_prostokata(a, b):
    return a * b


print(5 * pole_prostokata(2, 8))

"""

"""

print("Witamy w programie liczącym pola figur!
W celu obliczenia pola figury, wybierz
numer jej odowiadający, a następnie naciśnij
klawisz ENTER, aby wyświetlić następne istrukcje
Miłej zabawy!")

from cmath import pi as pi

while True:
    print("\n")
    print("Menu:")

    print("1: prostokąt")
    print("2: kwadrat")
    print("3: trójkąt")
    print("4: trapez")
    print("5: koło")
    print("6: zakończ")
    print("\n")

    opcja = input("Pole jakiej figury chcesz policzyć?: ")

    if opcja == "1":
        pbok1 = int(input("Podaj długość pierwszego boku prostokąta: "))
        pbok2 = int(input("Podaj długość drugiego boku prostokąta: "))
        def prostokat(pbok1, pbok2):
            return pbok1 * pbok2
        print("Pole prostokąta wynosi:", prostokat(pbok1, pbok2))

    elif opcja == "2":
        kbok = int(input("Podaj długość boku kwadratu: "))
        def kwadrat(kbok):
            return kbok**2
        print("Pole kwadratu wynosi:", kwadrat(kbok))

    elif opcja == "3":
        ptroj = int(input("Podaj długość podstawy trójkąta: "))
        htroj = int(input("Podaj długość wysokości trójkąta: "))
        def trojkat(ptroj, htroj):
            return (0.5 * ptroj) * htroj
        print("Pole trójkąta wynosi:", trojkat(ptroj, htroj))

    elif opcja == "4":
        p1trap = int(input("Podaj długość dolnej podstawy trapezu: "))
        p2trap = int(input("Podaj długość górnej podstawy trapezu: "))
        htrap = int(input("Podaj długość wysokości trapezu: "))
        def trapez(p1trap, p2trap, htrap):
            return ((p1trap + p2trap)* htrap) / 2
        print("Pole trapezu wynosi:", trapez(p1trap, p2trap, htrap))

    elif opcja == "5":
        rkolo = int(input("Podaj długość promienia koła: "))
        def kolo(rkolo, pi):
            return (pi * rkolo) **2
        print("Pole koła wynosi:", round(kolo(rkolo, pi), 3))

    elif opcja == "6":
        print("Działane programu zakończone.")
        break
    else:
        print("\nWybrałeś niewłaściwą wartość.\nWybierz spośród 1 -6.")

"""

"""

#Funkcje - zaawansowane#



while True:
    x = int(input("Podaj liczbę: "))
    print("Suma liczb od 1 do", x, "wynosi: ", sum(range(1, (x + 1))))
    continue





while True:
    x = int(input("Podaj liczbę: "))

    numbers_gen = (el
                   for el in range(1, (x + 1)))

    print("Suma liczb od 1 do", x, "wynosi: ",sum(numbers_gen))
    continue





import time

def sumuj_do1(liczba):
    suma = 0
    for liczba in range(1, (liczba + 1)):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1, (liczba + 1))])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1, (liczba + 1))})

def sumuj_do4(liczba):
    return sum(liczba for liczba in range(1, (liczba + 1)))

def sumuj_do5(liczba):
    return((1 + liczba) / 2 ) * liczba

def finish_timer(start):
    end = time.perf_counter()
    return end - start



def function_perf(func, arg, how_many_times = 1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum



print(function_perf(sumuj_do1, 5000000, 25))
print(function_perf(sumuj_do2, 5000000))
print(function_perf(sumuj_do3, 5000000))
print(function_perf(sumuj_do4, 5000000))
print(function_perf(sumuj_do5, 5000000))



start = time.perf_counter()
print("1: ",sumuj_do1(256))
end = time.perf_counter()
print(finish_timer(start))
print("\n")

start = time.perf_counter()
print("2: ",sumuj_do2(256))
end = time.perf_counter()
print(finish_timer(start))
print("\n")

start = time.perf_counter()
print("3: ",sumuj_do3(256))
end = time.perf_counter()
print(finish_timer(start))
print("\n")

start = time.perf_counter()
print("4: ",sumuj_do4(256))
end = time.perf_counter()
print(finish_timer(start))
print("\n")

start = time.perf_counter()
print("5: ",sumuj_do5(256))
end = time.perf_counter()
print(finish_timer(start))

"""

"""

import time

set_container = (i for i in range(1000))
list_container = [i for i in range(1000)]


def exist_check (liczba, container):
    if liczba in container:
        return "Tak"
    else:
        return "Nie"


def function_perf(func, how_many_times = 1, *arg):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end - start)
    return sum


wynik1 = (function_perf(exist_check, 10000000, 50000, set_container))
wynik2 = (function_perf(exist_check, 10000000, 50000, list_container))

print("Set: ", exist_check(50000, set_container))
print(round(wynik1, 3))

print("List: ", exist_check(50000, list_container))
print(round(wynik2, 3))

"""

"""

def sum_arg(*liczba):
    suma = sum(liczba)
    return suma
print(sum_arg(1, 2, 3))

"""
'''

import random

def hit_chance(hit_probab):
    hitting_chance = random.uniform(0, 100)
    if hitting_chance < hit_probab:
        return("Hit")
    else:
        return("Not hit")


x = 0

hitlist = []

while x < 100:
    x = x + 1
    hitlist.append(hit_chance(50))

from collections import Counter

dicthit = Counter(hitlist)
'''
"""
import random

nagroda = ["Zielony", "Niebiseki", "Fioletowy", "Złoty" ,"Czarny"]

from collections import Counter

x = 0
while x < 100:
    x = x + 1
    print(Counter(random.choices
              (nagroda, [0.500, 0.350, 0.125, 0.024, 0.001], k = 100)))

"""


"""
import random

def lotto(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))


lotto(6, 49)

"""

"""
try:
    file = open("Test", "w")
    file.write("Hello!")
    print(0/0)
    file.write("Hello World!")
finally:
    file.close()
    a = 5
    print(a)

"""

"""

with open("oceany.txt", "r", encoding = "UTF-8") as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(0)
    print(file.readline())
    print(file.tell())

"""

"""

namesandsurnames = []

with open("imionanazwiska.txt", "r", encoding = "UTF-8") as file:
    for line in file:
        namesandsurnames.append((tuple(line.replace("\n", "").split(" "))))

with open("imiona.txt", "w", encoding = "UTF-8") as file:
    for item in namesandsurnames:
        file.write(item[0] + "\n")

with open("nazwiska.txt", "w", encoding = "UTF-8") as file:
    for item in namesandsurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")

"""

"""

import json



film = {
    "title" : "Ale ja nie będę tego robił!",
    "release_year" : 1969,
    "won_oscar" : True,
    "actors": ("Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"),
    "budget" : None,
    "credits" : {
            "director" : "Arkadiusz Włodarczyk",
            "writer" : "Alan Burger",
            "animator" : "Anime Animatrix"
            }
}

with open("sample.json", "w",encoding = "UTF-8") as file:
    json.dump(film, file, ensure_ascii = False)




import json


retrieved_movie = '{"title": "Ale ja nie będę tego robił!", "release_year": 1969, "won_oscar": true, "actors": ["Arkadiusz Włodarczyk", "Wiolleta Włodarczyk"], "budget": null, "credits": {"director": "Arkadiusz Włodarczyk", "writer": "Alan Burger", "animator": "Anime Animatrix"}}'

decoded_movie = json.loads(retrieved_movie)

with open("sample.json", "r", encoding = "UTF-8") as file:
    wynik = json.load(file)

pretty_film = json.dumps(film, ensure_ascii = False,
                         indent = 4, sort_keys =  True)

print(pretty_film)




import requests

import json

siteslist1 = ["http://videokurs.pl", "http://lego.com", "http://wp.pl",
             "http://lego.com/lkjh", "http://wp.pl/jhgfdsr", "http://airbus.com/mnbvc"]
opened_sites = []
sites_not_found = []

for site_name in siteslist1:
    def open_check(site_name):
        response = requests.get(site_name)
        if response.status_code == 200:
            return (opened_sites.append(site_name), print((site_name, "Site has been opened correctly!")))
        else:
            return (sites_not_found.append(site_name), print((site_name, "Site not found!")))

for site_name in siteslist1:
    print(open_check(site_name))

with open("opened_sites.txt", "w", encoding = "UTF-8") as file:
    json.dump(opened_sites, file, ensure_ascii = False)

"""

"""

import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")



tasks = json.loads(r.text)



def count_tasks_frequency(tasks):
    completedTaskFrequencyByUser = dict ()
    for entry in tasks:
        if (entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

    return completedTaskFrequencyByUser

def user_with_top_completed_tasks(completedTaskFrequencyByUser):
    userIDWithMaxAmountOfComletedTasks = []
    maxAmountOfComletedTasks = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTasks == maxAmountOfComletedTasks):
            userIDWithMaxAmountOfComletedTasks.append(userId)

    return userIDWithMaxAmountOfComletedTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format!")
else:
    completedTaskFrequencyByUser = count_tasks_frequency(tasks)
    usersWithTopCompletedTasks = (
        user_with_top_completed_tasks(completedTaskFrequencyByUser))

r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    if (user["id"] in usersWithTopCompletedTasks):
        print("Ciastko węddruje do: ", user["name"])

"""

"""

import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta

timeBefore = (timedelta(days = 7))

searchDate = datetime.today() - timeBefore



params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(searchDate.timestamp()),
    "tagged" : "python",
    "min" : 15
    }


r = requests.get("https://api.stackexchange.com/2.3/questions", params)



try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format!")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])

"""

"""

def generate_even_numbers():
    print("Start")
    for element in range(400):
        print("Przed yield")
        if element % 2 == 0:
            yield element
            print("Po yield")

a = generate_even_numbers()

"""

"""

def gen_10_numbers():
    x = 0
    while x < 10:
        yield x
        x = x + 1



print(list(gen_10_numbers()))

"""

"""

print("Hello World!")

"""

"""
class User:

    def __init__(self, age, name):
        print("I'm an initializer")

        self.age = age
        self.name = name

    def print_age(self):
        print("Age: ", self.age, self.name)


user1 = User(30, "Arek")
user2 = User(24, "Mirek")

user1.print_age()
user2.print_age()
"""

"""
class Rocket():
    def __init__(self, speed=1):
        self.altitude = 0
        self.speed = speed

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rocket is on altitude: " + str(self.altitude) \
            + " and has speed: " + str(self.speed)


class RocketBoard():
    pass

"""
