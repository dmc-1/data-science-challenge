import psycopg2

conn = psycopg2.connect(database="CompanyXDB", user = "postgres", password = "password", host = "127.0.0.1", port = "5432")
cursor = conn.cursor()

cursor.execute(
'''
CREATE TABLE invoice (
    Transaction_ID    char(40)   PRIMARY KEY,
    Created_at        date, 
    Start_Date        date, 
	End_Date          date, 
	Amount_USD        money, 
	Status            char(40), 
	Revenue_Type      char(40));
''')

conn.commit()
conn.close()

