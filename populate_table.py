import csv
import psycopg2

conn = psycopg2.connect(database="CompanyXDB", user = "postgres", password = "password", host = "127.0.0.1", port = "5432")
cursor = conn.cursor()

csv_data = csv.reader(open('C:\Users\dimitri\Desktop\Unbabel_project\data-science-challenge\database.csv', 'rb'))

next(csv_data, None)
for row in csv_data:
    if row[2] != '' and row[3] != '': 
	    cursor.execute(
	    "insert into invoice (Transaction_ID, Created_at, Start_Date, End_Date, Amount_USD, Status, Revenue_Type) values ('" + row[0] + "', '" + row[1]
	    + "', '" + row[2] + "', '" + row[3] + "', '" + row[4] + "', '" + row[5] + "', '" + row[6] + "')" 	
	    )
    else:
	    cursor.execute(
	    "insert into invoice (Transaction_ID, Created_at, Start_Date, End_Date, Amount_USD, Status, Revenue_Type) values ('" + row[0] + "', '" + row[1]
	    + "', null, null, '" + row[4] + "', '" + row[5] + "', '" + row[6] + "')")	    

conn.commit()
conn.close()