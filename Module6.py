#6.1

import random

randomnumberlist = []

def dicethrower (): 
        randomnumber = random.randint(1,6)
        print("The dice landed on the number: " + str(randomnumber))

def sixermachine():
        randomnumber = random.randint(1,6)
        if randomnumber < 6:
            print("You threw the number: " + str(randomnumber))
            randomnumberlist.append(randomnumber)
            sixermachine()
            
        elif randomnumber >= 6:
            print("It took " + str(len(randomnumberlist) + 1) + " throws to get the number (6).")

key = int(input('Input the number (1) to start the dicethrower or number (2) to start the sixermachine: '))

if key == int(1):
    dicethrower()
elif key == int(2):
    sixermachine()

#6.2

throws = []

def dicethrow(maxamount):
        
        randomnum = random.randint(1, maxamount)
        
        if randomnum != int(maxamount):
           throws.append(randomnum)
           print("You threw: (" + str(randomnum) + "), Throwing again...")
           dicethrow(maxamount)
        
        elif randomnum == int(maxamount):
            print("You got the maximum number of: (" + str(randomnum) + ") which took you (" + str(int(len(throws)) + 1) + ") throws.")

def halfamount():
    maxamount = int(input('Write the total number of halves of the dice: '))
    if (maxamount >= int(1)):
        dicethrow(maxamount)

halfamount()

#6.3
def converter(gallons):
    unitchanged = (gallons * 3.785)
    print("The amount of gallons you gave is equal to: " + str(unitchanged) + " liters.")
    startconverter()


def startconverter():
    gallons = float(input('Give an amount of gallons to be converted to liters: '))
    if (gallons > int(0)):
        converter(gallons)
    
    else: print("The converter has stopped, you gave a negative amount or wrote something the computer did not understand.") 

startconverter()

#6.4
def sumlist (listofintegers):

    sum = 0

    for x in listofintegers:
        sum += int(x)
    
    print("The sum of the list you gave came to: " + str(sum)) 

sumlist(listofintegers=input("Give a list (2 or more) of integers separated by a comma: ").split(','))

#6.5
def evenlist(integerlist):
    evenlist2 = []
    oddlist = []
    for integer in integerlist:
        if (int(integer) % 2 == 0):
            evenlist2.append(integer)
        
        elif (0 < int(integer) % 2 < 0):
           oddlist.append(integer)
    
    evenlist2.sort()
    print(evenlist2)

evenlist(integerlist=input("Give a list (2 or more) of integers separated by a comma: ").split(','))

#6.6

#Pizzafunktio 1
def pizzalator(p_diameter, p_price):
    
    diameterinm2 = float(p_diameter) / 100**2
    priceconverted = float(p_price) / 100**2

    print("Pizza costs: " + str(priceconverted) + "€'s of " + str(diameterinm2) + " m² of pizza.")


def prequestions():
    p_diameter, p_price = input("Give the diameter of a pizza in (cm) and price in (€): ").split(", ")

    pizzalator(p_diameter, p_price)

prequestions()
    
#Pizzafunktio v2
def pizzalator2(p_diameter1, p_diameter2, p_price1, p_price2):
    
    diameterinm2_1 = float(p_diameter1) / 100**2
    priceconverted_1 = float(p_price1) / 100**2
    diameterinm2_2 = float(p_diameter2) / 100**2
    priceconverted_2 = float(p_price2) / 100**2

    if (priceconverted_1 < priceconverted_2):
        print("Pizza [1] costs: " + str(priceconverted_1) + "€'s of " + str(diameterinm2_1) + " m² of pizza and therefore is cheaper than the SECOND pizza.")
    
    elif (priceconverted_1 > priceconverted_2):
        print("Pizza [2]  costs: " + str(priceconverted_2) + "€'s of " + str(diameterinm2_2) + " m² of pizza and therefore is cheaper than the FIRST pizza.")
    
    else: print("SOMETHING went wrong with the calculations, the computer runs the program again...")
    prequestions1()


def prequestions1():
    p_diameter1, p_diameter2, p_price1, p_price2 = input("1. Give the diameter of the pizzas in (cm) and the prices of the pizzas in (€) separated by a comma.\n2. Make sure that the order corresponds to the following: (diam 1, diam 2, price 1, price, 2): ").split(", ")

    pizzalator2(p_diameter1, p_diameter2, p_price1, p_price2)

prequestions1()

