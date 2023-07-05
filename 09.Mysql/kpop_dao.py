# world database의 song,girl_group를 액세스하는 라이브러리
# pip install mysql-connector-python

import json
from mysql.connector import pooling



with open('./mysql.json') as f:
    config_str =f.read()
config = json.loads(config_str)


def get_song_list_by_debut(year):
    pass

def get_song_list(num,offset=0):
    conn = pool.get_connection()
    cur =conn.cursor()
    sql ="SELECT * FROM song LIMIT %s OFFSET %s ;"
    cur.execute(sql(num,offset=0))          # 파라메터는 반드시 튜플로 전달해야함
    cur.close()
    conn.close
    


def get_girl_group_list(params):
    conn = pymysql.connect(**config)
    cur =conn.cursor()
    sql ="SELECT %s FROM girl_group ; ;"
    cur.execute(sql,params)          # 파라메터는 반드시 튜플로 전달해야함
    cur.close()
    conn.close

def insert_song(params):
    pass

def insert_girl_group(params):
    pass