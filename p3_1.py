import mysql.connector

# Establishing a connection with the MySQL database
with mysql.connector.connect(
    host="localhost",
    user='root',
    password='79413161',
    database='employee'
) as mydb:
    
    # Creating a cursor object to execute MySQL queries
    with mydb.cursor() as mycursor:
        # Retrieving data from the table 'info'
        mycursor.execute("SELECT * FROM info")
        info = list(mycursor)
        
    # Sorting the retrieved data based on the second element of each record in descending order
    info.sort(key=lambda x: (x[1],-x[2]), reverse=True)
    
    # Displaying the sorted data
    print(info)
    
    # Closing the database connection
    mydb.close()
