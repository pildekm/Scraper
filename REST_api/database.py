import psycopg2
from psycopg2 import *

def initialize():
    conn = psycopg2.connect(host="127.0.0.1", database="db_pelud", user="encode", password="100", port=5432)
    if conn:
        print('Povezan s bazom!')
        return conn

