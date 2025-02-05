import math

#2.1
kayttaja = input('State your name: ')
print("Nice to meet you, " + kayttaja + "!") 

#2.2
sade = input('What is the radius of the circle: ')
luku = float(sade)
area = math.pi*luku**2
print("This is the area of the circle: " + str(area))

#2.3

rectanglebase = input("Type rectangle base : ")
rectangleheight = input ("Type rectangle height: ")

floatedcircle = float(rectanglebase)
rectanglecircle = floatedcircle * 4

rectanglearea = int(rectangleheight) * int(rectanglebase)
rectanglearea1 = str(rectanglearea)

print("The rectangle area is : " + rectanglearea1 + " and the circle: " + str(rectanglecircle))
number1, number2, number3 = input("Give three numbers with a space between them: ").split()

product = float(number1) * float(number2) * float(number3)
sum = float(number1) + float(number2) + float(number3)
average = sum/3
print("Here are the numbers: " + number1, number2, number3)
print('Here is the product of the three numbers: ' + str(product) + '  #sum: ' + str(sum) + ' average: ' + str(average))

#2.5
x = [float(x) for x in input('Give the amount of nails, bread and bullets separated by a comma: ').split(",")]

print('You have ' + str(x[0]) + ' nails ' + str(x[1]) + ' breads, and ' + str(x[2]) + ' bullets.') 

totalsum = sum(x)
print('Total item count: ' + str(totalsum))

access = float(input('Type the total of your items to continue: '))

if access == float(totalsum):
    b = float(x[2]*13.3)
    n = float(b/x[2]*32*x[0])
    B = float(n/x[0]*20*x[1])
print("The total mass of each item you chose: " + str(n) + ' grams of nails ,', str(B) + ' grams of bread and ,', str(b) + ' grams of bullets')

total = b + n + B

inttotal = total/1000

totalkg = (int(inttotal))

totalgrams = int((inttotal - totalkg)*1000)

print('Total mass comes to : '+ str(totalkg) + ' kilograms and ' + str(totalgrams) + ' grams.')

#2.6
import random

#Three digit code pushed into a list, numbers between the following digits (0-6)
code = []
for i in range(0,3):
    randomnumber = random.randint(0,6)
    code.append(randomnumber)
else: print(code)

#Four digit code pushed into a list, numbers between the following digits (0-9)

code2 = []
for i in range(0,4):
    randomnumber2 = random.randint(0,9)
    code2.append(randomnumber2)
else: print(code2)
