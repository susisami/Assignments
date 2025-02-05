#3.1 
length = float(input("Input the pikeperch length in centimeters: "))

if length < 37:
    print('Please lay the fish back down to the lake as it is undersize')
else: print("Nice catch, eat it now")

#3.2

cabinclass = str(input("Please confirm your cabinclass(LUX, A, B, C): "))
if cabinclass == 'LUX':
       
        print("Your cabin is located upper deck and has a balcony")

elif cabinclass == 'A':
        
        print("Your cabin has a seaview and is located above the cardeck")

elif cabinclass == 'B':
        
        print("Your cabin is located above the cardeck and doesn't have a window")

elif cabinclass == 'C':
        
        print("Your cabin is a windowless room below the cardeck")
        
else: 
        
        print("Error in search of your cabin, please retry.")
#3.3

x = [str(x) for x in input('Sex (Female, Male) and hemoglobin separated by a comma: ').split(",")] 

sex = x[0]
hemoglobin = float(x[1])

print(sex, ' , ' + str(hemoglobin))

if hemoglobin < 134 and sex == 'Male':
    print("1m. You are a low hemoglobin: " + 'Male')

elif hemoglobin > 195 and sex == 'Male':
    print("2m. You are a high hemoglobin: " + 'Male')

elif 134 < hemoglobin < 195 and sex == 'Male':
    print("3m. You are a normal hemoglobin: " + 'Male')

elif hemoglobin < 117 and sex == 'Female':
    print("1f. You are a low hemoglobin: " + 'Female') 

elif hemoglobin > 175 and sex == 'Female':
    print("2f. You are a high hemoglobin: " + 'Female') 

elif 117 < hemoglobin < 175 and sex == 'Female':
    print("3f. You are a normal hemoglobin: " + 'Female')

else: print('Could not figure out your hemoglobin, please try again')

#3.4

year = int((input('Input a year to check if it is a leap year: ')))

if (year % 4 == 0 or (year % 400 == 0 and year % 4 == 0)):
    print(f"{year} is a leap year.")
else: print(f"{year} is not a leap year.")
