#
# member table 대한 DAta Access Object(DAO)
#
import sqlite3 as sq
# member table에 있는 데이터 모두 읽기
def get_members():
    conn = sq.connect('test.db')
    cur =conn.cursor()

    sql ='SELECT * FROM member;'
    cur.execute(sql)
    rows =cur.fetchall()

    cur.close()
    conn.close()
    return rows

# 성별로 가져오기
def get_members_by_gender(gender):
    conn = sq.connect('test.db')
    cur =conn.cursor()

    sql ='SELECT * FROM member where gender =?;'
    cur.execute(sql,(gender,))   #parameter는 반드시 tuple 형태라야 함
    rows =cur.fetchall()

    cur.close()
    conn.close()
    return rows

#mid에 해당하는 데이터 한 건만 가져오기
def get_member_by_mid(mid):
    conn = sq.connect('test.db')
    cur =conn.cursor()

    sql ='SELECT * FROM member where mid =?;'
    cur.execute(sql,(mid,))   #parameter는 반드시 tuple 형태라야 함
    row =cur.fetchone()       # 한건의 데이터만 가져오는 경우에는 fetchone()사용

    cur.close()
    conn.close()
    return row

# 데이터 추가하기
def inset_member(params):
    conn = sq.connect('test.db')
    cur =conn.cursor()

    sql ='insert into member(mname,gender) values (?,?);'
    cur.execute(sql,params)
    conn.commit()      # 데이터 수정하면 꼭 conn.commit() 하기
    cur.close()
    conn.close()

# 데이터 수정하기 - 파라메터 순서에 주의할것
def update_member(params):
    conn = sq.connect('test.db')
    cur =conn.cursor()

    sql ='update member set mname=?,gender=? where mid=?;'
    cur.execute(sql,params)
    conn.commit()      # 데이터 수정하면 꼭 conn.commit() 하기
    cur.close()
    conn.close()

# 데이터 삭제하기
def delete_member(mid):
    conn = sq.connect('test.db')
    cur =conn.cursor()

    sql ='delete from member where mid=?;'
    cur.execute(sql,(mid,))
    conn.commit()      # 데이터 수정하면 꼭 conn.commit() 하기
    cur.close()
    conn.close()