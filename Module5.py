#5.1

import random

dices = (int(input('Input the number of dices: ')))
sum = 0

for i in range(dices):
    randomnumber = random.randint(1,6)
    sum += randomnumber
    print(randomnumber)

print(str(sum))

#5.2

number = int(input('Give a number: '))
numbers2 = []
numbers1 = []

while number != '':
        
        numbers2.append(float(number))
        numbers1.append(float(number))
        numbers2.sort(reverse=True)
        numbers1.sort()
        print("Reversed numbers: " + str(numbers2) + "\nNormal numbers: " + str(numbers1))
        number = input('Give a number or press ENTER to exit: ')
(print("(5) of the biggest numbers: " + str(numbers2[0:4]) + "\n(5) of the smallest numbers: " + str(numbers1[0:4])))

#5.3
import math

integer = int(input('Input an integer: '))

if (integer <= 1):
    print(f"{integer} is not a prime number")
else:
    primenumber = True
    for i in range(2, int(math.sqrt(integer)) + 1):
        if (integer % i) == 0:
            primenumber = False
            break
    if primenumber:
        print(f"{integer} was a primenumber!")
    else:   print(f"{integer} was not a primenumber!") 

#5.4

num = [1]
cities = []
for x in num:
      city = input('Give me (5) city names across the world: ')
      number = 0
if city != '' and number < 5:
         cities.append(city)
         print(cities)
         num.append(1)
         number += 1
         pass

else: print("All city names stated.")

for y in range(1):
     print("List of city names in the given order: ")
     print(*cities, sep='\n')
