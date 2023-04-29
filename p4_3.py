import re
import requests
import mysql.connector

from bs4 import BeautifulSoup
r= requests.get("https://www.hamrah-mechanic.com/carprice/")

soup = BeautifulSoup(r.text, 'html.parser')
data = []

regex = re.compile('.*carsBrandPriceList_price.*')
for EachTable in soup.find_all("table", {"class" : regex}):
    table_body = EachTable.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

# Set up a database connection, using a try-except block to handle errors
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user='root',
        password='1234',
        database='car'
    )
    print("Database connection successful.")

    # Define a list of tuples to be inserted into the car_price table
    for d in data :
        print("Name: %s , Price: %s" %(d[0],d[1]))
        with mydb.cursor() as mycursor:
            sql = "INSERT INTO car_price (name,price) VALUES (%s, %s)"
            val = (d[0],d[1])
            mycursor.execute(sql, val)
            mydb.commit()
            print('Car Price record inserted successfully!')
    # Close the cursor and database connections
    mycursor.close()
    mydb.close()
    print("Database connections closed.")

# Handle errors that may arise during database connections
except mysql.connector.Error as error:
    print("Failed to connect to database: {}".format(error))