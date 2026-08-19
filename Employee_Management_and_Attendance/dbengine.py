# db_engine.py
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="employee", #enter the database you have created
        user="postgres", #Enter the username you have chosen
        password="*******", #Enter your password  
        host="localhost",
        port="5432"

    )
