Bank Management System using Python & MySQL
Project Description

This project is a simple Bank Management System developed using Python and MySQL. It allows users to perform banking operations such as:

Create Account
Deposit Money
Withdraw Money
Check Balance
View Account Details

The project uses Python Database Connectivity (PDBC) with the mysql.connector module to connect Python with MySQL database.

Technologies Used
Python
MySQL
mysql.connector
VS Code
Features
Create new bank accounts
Deposit amount into account
Withdraw amount from account
Check account balance
Store account details in MySQL database
Database Table
CREATE TABLE accounts(
    acc_no INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    balance FLOAT
);
Installation Process
Step 1: Install MySQL Connector
pip install mysql-connector-python
Step 2: Import Module
import mysql.connector
Step 3: Create Database Connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="bankdb"
)
