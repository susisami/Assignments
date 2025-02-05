#4.1
x = 0

while x<1000:
    print(x)
    x+=3

#4.2
inch = float(input('Inch to centimeter converter: '))
inches = []

while inch > 0:
   inches.append(inch*2.54)
   print('The converted value: ' + str(inches))
   inch = float(input('Inch to centimeter converter: ')) 
print("Negative value given to the program, all operations suspended") 

#4.3

numbers1 = []
numbers2 = []

number =int((input('Give me a number: ')))

while number !="":
   numbers1.append(int(number))
   numbers2.append(int(number))
   numbers1.sort()
   numbers2.sort(reverse=True)
   print(numbers1,numbers2)
   number = input('Give me a number: ')
print('Biggest of the given numbers: ' + str(numbers2[0]) + '\nSmallest of the given numbers: ' + str(numbers1[0]))

#4.4
import random

computernumber = int(random.randint(1,10))
print(computernumber)
playerguess = int(input('Player guess (1-10): '))

while playerguess != computernumber:
         
         if(playerguess < computernumber):
            print("The guessed number was too small, try again")
            playerguess = int(input('Player guess (1-10): '))
         
         elif (playerguess > computernumber):
            print("The guessed number was too big, try again")
            playerguess = int(input('Player guess (1-10): '))

print("The number was: " + str(computernumber) + "\nYou won the game by guessing the computer's number.")

#4.5
import secrets


username = [x for x in (input('Give a Username: ').split(","))]

password = [x for x in (input('Give a Password: ').split(","))]

print(username, password)

logincounter = 0

while username[0]!='python' or password[0]!='rules':
   
   if logincounter == 5:
      print("Access denied from system.")
      username[0] = secrets.token_urlsafe(32)
      password[0] = secrets.token_urlsafe(32) 
   else: 
         logincounter += 1
         print('Wrong password or username, please retry login: \n')
         username = [x for x in (input('Give a Username: ').split(","))]
         password = [x for x in (input('Give a Password: ').split(","))]
print('\bAccess  \bgranted to the system.')

#4.6
import random, math

pi = math.pi

N = int(input('Give a number from 0 to a million: '))

counter = 0
circlecounter = 0
while counter < N:
   x = random.uniform(1,-1)
   y = random.uniform(1,-1)
   if (x**2 + y**2 < 1):
       circlecounter += 1

answer = 4 * int(circlecounter)/N
print("Pi is approximately: " + str(answer))
