# install mysql-connector-python
# install mysql
# install mysql-Connector

import mysql.connector 

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Beaver791",
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE Scorptech")

print("Database created successfully !!")
# Database configuration in settings.py