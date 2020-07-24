from settings import *
import pandas as pd
import pymysql
from sqlalchemy import create_engine


db = pymysql.connect(host = host,user = user,password = password,port = port)  
cursor = db.cursor()
cursor.execute('USE football_prices_project')
cursor.execute('DROP TABLE players_prices')
cursor.execute('CREATE TABLE players_prices (name VARCHAR(20), price DECIMAL(10,2))')
data = pd.read_sql_query('SELECT * FROM football_prices_project.players_prices', db)
print(data.head())