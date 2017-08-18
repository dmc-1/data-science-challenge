# Data Science Challenge

Hello there,

Welcome to our Data Science Challenge repository. This README will guide you on how to participate in this challenge.

Please fork this repo before you start working on the challenge. We will evaluate the code on the fork.

**FYI:** Please understand that this challenge is not decisive if you are applying to work at [Unbabel](https://unbabel.com/jobs). There are no right and wrong answers. This is just an opportunity for us both to work together and get to know each other in a more technical way. 

## Walkthrough

### Chapter A - Database creation
***Task:*** 

```
Create a Postgres database.

This database will be used throughout the rest of the exercise.
```
### Chapter B - Database initialization
***Task:*** 

```
Create a Python script that initializes the database with an empty table.  

The table should have the following columns:
- “Transaction-ID”: unique identifier
- “Created at”: date when the invoice was issued
- “Start Date”: start date of the period covered by the invoice
- “End Date”: end date of the period covered by the invoice
- “Amount USD”: total amount of the invoice
- “Status”: can be “issuable”, “issued”, “paid”, “not_invoiced”, “overdue”, “voided”
- “Revenue Type”: can be Subscription plan (SPC), Subscription plan Extra (SPE), One-time services (OTS), Top-up (TOP), Refunds (REF), Trial (TRI), Discounts (DIS)


```
Note: You'll populate this table later.

### Chapter C - Populate the database
***Task:*** 

```
In this repo you can find a .CSV with the contents that should be used populate the database.

Create a Python script that loads the data from CSV and populates the database.
```

### Chapter D - Revenue

***Task:***

```
The data you populated the database with is actually the revenue of Company X. 

Please write an SQL query that determines and shows the daily revenue of company X according to the following rules:

1. Calculate the daily revenue for 2017 (i.e. split the invoices in the corresponding days covered by the invoice);
2. When there is no “start-date” or “end-date”, please consider the “created date” (for both cases);
3. Status not to be considered as Revenue: “voided” and “overdue”. All others can be considered as revenue.

```

Note: 
You can use any SQL client to write and test the SQL query (Postico, PGAdmin, etc.) We're only interested in the SQL query itself.