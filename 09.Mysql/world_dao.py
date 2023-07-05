# world database를 액세스하는 라이브러리
import json
import pymysql

with open('./mysql.json') as f:
    config_str =f.read()
config = json.loads(config_str)


#어떤 국가의 인구수 Top n개 도시 정보
def get_citylist_by_country(countrycode,num):
    conn = pymysql.connect(**config)
    cur =conn.cursor()
    sql ="SELECT * FROM city  where countrycode=%s order by population LIMIT %s;"
    cur.execute(sql,(countrycode,num))          # 파라메터는 반드시 튜플로 전달해야함
    rows=cur.fetchall()
    cur.close
    conn.close
    return rows


# 어떤 도시의 정보
def get_city_by_name(name):
    conn = pymysql.connect(**config)
    cur =conn.cursor()
    sql ="SELECT * FROM city  where name=%s;"
    cur.execute(sql,(name,))          # 파라메터는 반드시 튜플로 전달해야함
    row=cur.fetchone()                     # 하나의 레코드
    cur.close()
    conn.close
    return row


#데이터 삽입
def insert_city(params):
    conn = pymysql.connect(**config)
    cur =conn.cursor()
    sql ="INSERT INTO city VALUES(DEFAULT,%s,%s,%s,%s);"
    cur.execute(sql,params)         
    conn.commit()                    
    cur.close()
    conn.close()


# 데이터 갱신
def update_city(params):
    conn = pymysql.connect(**config)
    cur =conn.cursor()
    sql = "UPDATE city SET name=%s, countrycode=%s, district=%s, population=%s WHERE id=%s;"
    cur.execute(sql,params)         
    conn.commit()                    
    cur.close()
    conn.close()

#데이터 삭제
def delete_city(id):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "DELETE FROM city where id >%s;"
    cur.executemany(sql,(id,))
    conn.commit() 
    cur.close()
    conn.close()
    
