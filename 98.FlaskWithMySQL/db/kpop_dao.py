# World database의 song, girl_group를 액세스하는 라이브러리
# Connection Pool 사용
# 설치: pip install mysql-connector-python

import json
from mysql.connector import pooling

with open('./mysql.json') as f:
    config_str = f.read()
config = json.loads(config_str)
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

def get_song_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM song LIMIT %s OFFSET %s"
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_song(sid):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM song WHERE sid=%s"
    cur.execute(sql, (sid, ))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def insert_song(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO song VALUES(default, %s, %s)"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def update_song(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "UPDATE song set title=%s, lyrics=%s WHERE sid=%s"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def delete_song(sid):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM song WHERE sid=%s"
    cur.execute(sql, (sid,))
    conn.commit()
    cur.close()
    conn.close()

def get_girl_group_list(num, offset=0):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = """SELECT l.gid, l.name, l.debut, r.title FROM girl_group as l
                JOIN song AS r ON l.hit_song_id = r.sid
                ORDER BY l.debut LIMIT %s OFFSET %s"""
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_girl_group(gid):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM girl_group WHERE gid=%s"
    cur.execute(sql, (gid, ))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def insert_girl_group(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO girl_group VALUES(default, %s, %s, %s)"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def update_girl_group(params):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "UPDATE girl_group SET name=%s, debut=%s, hit_song_id=%s WHERE gid=%s"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

def delete_girl_group(gid):
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "DELETE FROM girl_group WHERE gid=%s"
    cur.execute(sql, (gid, ))
    conn.commit()
    cur.close()
    conn.close()