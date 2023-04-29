import mysql.connector
import re

name= input("Enter your name: ")
email= input("Enter your email: ")

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
while not re.fullmatch(regex, email):
        email= input("Enter your email again : ")

print(name,email)
#email=email.split("@")
#email= email[0] + "\@" + email[1]
#print(email)
# Establishing a connection with the MySQL database
with mysql.connector.connect(
    host="localhost",
    user='root',
    password='79413161',
    database='employee'
) as mydb:
    
    # Creating a cursor object to execute MySQL queries
    with mydb.cursor() as mycursor:
        sql = "INSERT INTO mail_list (name,email) VALUES (%s, %s)"
        val = (name,email)
        mycursor.execute(sql, val)
        mydb.commit()
        print('User record inserted successfully!')
    # Closing the database connection
    mydb.close()       