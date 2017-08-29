# Notes on the Challenge
Here is a short task by task explanation. 

### Chapter A - Database creation
A database "CompanyXDB" is created by a command in **create_db.bat**. 

### Chapter B - Database initialization
A table "invoice" is created in "CompanyXDB" by the python script **create_table.py**.  
Note: Using the script requires setting parameters in the call to psycopg2.connect(...). 

### Chapter C - Populate the database
The table "invoice" is populated from database.csv by the python script **populate_table.py**. 
The missing values in the csv file are exported to the database table as "null". 
Note: Using the script requires setting parameters in the call to psycopg2.connect(...). 

### Chapter D - Revenue
Revenue by days is calculated in the SQL script ***calculate_revenue.sql***.
First, each invoice is split by days covered by it. This is done in two select statements. One for those invoices for which neither "Day of Start Date" nor "Day of End Date" is missing, and the other for those invoices for which either "Day of Start Date" or "Day of End Date" is missing. Then, a union of these select statements is taken. Finally, the revenue is aggregated as a sum by days.
