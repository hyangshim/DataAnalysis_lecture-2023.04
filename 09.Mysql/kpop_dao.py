# World database의 song, girl_group를 액세스하는 라이브러리
# Connection Pool 사용
# 설치: pip install mysql-connector-python

import json
from mysql.connector import pooling

with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

def get_song_list_by_debut(year):
    conn = pool.get_connection()
    cur = conn.cursor()
#   sql = """SELECT r.name, r.debut, l.title FROM song AS l
#               JOIN girl_group AS r
#               ON l.sid = r.hit_song_id
#               WHERE r.debut BETWEEN %s AND %s;"""
#   cur.execute(sql, (str(year)+'-01-01', str(year)+'-12-31'))
    sql = """SELECT r.name, r.debut, l.title FROM song AS l
                JOIN girl_group AS r
                ON l.sid = r.hit_song_id
                WHERE r.debut like CONCAT(%s, '%%');"""
    cur.execute(sql, (year, ))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_song_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM song LIMIT %s OFFSET %s;"
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_girl_group_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM girl_group LIMIT %s OFFSET %s;"
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insert_song(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO song VALUES(default, %s, %s)"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def insert_girl_group(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO girl_group VALUES(default, %s, %s, %s)"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()