import mysql.connector

#8.1
def icaocode(code):
    sql = f"SELECT airport.name 
            FROM airport 
            WHERE airport.ident = '{code}';"
    print(sql)
    changer = connection.cursor()
    changer.execute(sql)
    result = changer.fetchall()
    if changer.rowcount > 0:
        print(result)
    return      
connection = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            database = '',
            user = 'root',
            password = '',
            autocommit = True     
)

code = input("Give an ICAO to have the airport information printed for you: ")
icaocode(code)

#8.2
def airportcode(namevariable):
    sql = f"SELECT airport.type, 
            COUNT(*) 
            FROM airport
            WHERE airport.iso_country = '{namevariable}'
            GROUP BY airport.type
            ORDER BY COUNT(*) ASC;"
    print(sql)
    updater = connection.cursor()
    updater.execute(sql)
    result = updater.fetchall()
    if updater.rowcount > 0:
        for rows in result:
            print('Airport-type: ' + str(rows[0]) + 'Number of airports: ' + str(rows[1]))
    return 
connection = mysql.connector.connect (
host = 'localhost',
port = 3306,
database = 'flight_game',
user = 'root',
password = '',
autocommit = True
)

airportcode(namevariable=str(input("Give a countrycode to have the country's airport type printed: ")))
