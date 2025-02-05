#7.1 

def seasonteller(monthnumber):
    seasons = ("Spring", "Summer", "Autumn", "Winter")
    print(monthnumber)

    if (335 <= monthnumber <= 365) or (1 <= monthnumber <= 59):
        print("The day of the month is a day of " + f"{seasons[3]}" + " day.")

    elif (60 <= monthnumber <= 151  ):
        print("The day of the month is a day of " + f"{seasons[0]}" + " day.")

    elif (152 <= monthnumber <= 243):
        print("The day of the month is a day of " + f"{seasons[1]}" + " day.")

    elif (244 <= monthnumber <= 334):
        print("The day of the month is a day of " + f"{seasons[2]}" + " day.")
    
    else: print("The program ran into a problem, computer runs the program again.")
    prequestion()

def prequestion():
    monthnumber = int(input("Write a day of a year from 1 to 365: "))
    seasonteller(monthnumber)

prequestion()

#7.2

namelist = set()

def prenamer(name): 
      
    if name != '':
        namemachine(name)
    elif name == '': 
        print("First list: " + str(namelist))
    

def namemachine(name):
            if name in namelist:
                  print("Name already in the list.")
                  prenamer(name=str(input("Give a name to be added to the list: ")))            
            elif  name not in namelist:
                  namelist.add(name)
                  print("New name added to the list.") 
                  prenamer(name=str(input("Give a name to be added to the list: ")))
            else: 
                print("Something went wrong, running the program again.")
                prenamer(name=str(input("Give a name to be added to the list: ")))      
            
prenamer(name=str(input("Give a name to be added to the list: ")))            

#7.3

codesafe ={}

def search ():
    searchengine = str(input("Input (Search) or (Save) to confirm the ICAO-mode or type (Delete) to delete all stored data: "))
    
    if searchengine != '':
        searchenginestart(searchengine)
    
    else: 
        print("Something went wrong, trying to run the program again.")
        search()

def searchenginestart(searchengine):

    if (searchengine == 'Search'):
        
        print('[You chose search mode]')
        searchmode = str(input("Give an airport ICAO code or press enter to go back: "))
        if (searchmode == ''):
           search() 
        elif (searchmode != '' and searchmode in codesafe):
                print(f"The ICAO -code you wrote corresponds to the International Airport of: " + str({codesafe[searchmode]}))  
        else: print("Could not find an airport with this code.\nRemember that the program does not have ANY presaved airports or codes in its memory.")
        search()

    elif (searchengine == 'Save'):
        
        airportname, airportcode = str(input("1. Airport name and ICAO-code you want to save\n2. Input the code in the following order of [Name, code], both values separated by a comma: ")).split(', ') 

        codesafe.update({airportcode : airportname})
        print(*codesafe, sep='\n')
        print("New [ICAO-Code] and [Airport] added, running the program again.")
        search() 
    
    elif searchengine == 'Delete':
            codesafe.clear()
            print('All stored data deleted.')
            search()
search()
