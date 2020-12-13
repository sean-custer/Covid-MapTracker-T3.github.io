import csv
import MySQLdb
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='prisoncovid')

cursor = mydb.cursor()

csv_data = csv.reader(open('states.csv'), delimiter = ',')
for row in csv_data:
    print("Here?")
    cursor.execute('INSERT INTO state(date, state, cases, deaths )''VALUES("%s", "%s", "%s", "%s")', row)
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")