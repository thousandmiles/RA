import MySQLdb

# Create the connection object
connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    db="RA_WEB",

)

# Create cursor and use it to execute SQL command
cursor = connection.cursor()
cursor.execute("select @@version")
version = cursor.fetchone()

if version:
    print('Running version: ', version)
else:
    print('Not connected.')
