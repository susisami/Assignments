import mysql.connector
from math import sin, cos, sqrt, atan2, radians

def math(list):
    #Haversine kaava
    rad = 6373.0

    lat1 = radians(list[0][0])
    lon1 = radians(list[0][1])
    lat2 = radians(list[1][0])
    lon2 = radians(list[1][1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = rad * c

    print("Result: ", distance, "kilometers.")

def distance(x, y):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{x}'"
    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{y}'"
    
    builder = connection.cursor()
    builder.execute(sql)
    result1 = builder.fetchall()

    builder.execute(sql2)
    result2 = builder.fetchall()

    if len(result1) > 0 and len(result2) > 0:
        list = [result1, result2]
        math(list)
    else:
        print("One or both ICAO codes were not found.")
    return

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='',
    autocommit=True
)

def prequestion():
    while True:
        x, y = input("Give two ICAO-codes separated by a comma: ").split(',')
        x = x.strip()
        y = y.strip()

        if (len(x) == 4 and len(y) == 4 and x.isalnum() and y.isalnum()  and x.isupper() and y.isupper()):        
            distance(x, y)
            break
        else: 
            print("Invalid input. Both ICAO codes must be 4 characters long, contain only uppercase letters and numbers. Please try again.")
prequestion()
