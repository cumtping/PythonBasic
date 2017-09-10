# http://www.runoob.com/python3/python3-mysql.html
# mysql study: http://www.runoob.com/mysql/mysql-administration.html

# 1. install mysql?
# 2. install pymysql(one mysql connector)
# 3. How to create mysql db?
#     http://database.51cto.com/art/200511/12524.htm
#       create database t1 / use t1; / show tables; / 
#       create table mytable (name VARCHAR(20), sex CHAR(1), birth DATE, birthaddr VARCHAR(20));
#       describe mytable;   /   select * from mytable;      /   
#       insert into mytable values('abc', 'f', '1977-07-07', 'china');
#       "mytable.txt" INTO TABLE pet; --> how to do this?

import pymysql

db = pymysql.connect("localhost","root","pige6666", "testdb" )

# insert one line
cursor = db.cursor()
sql = "INSERT INTO mytable(name, sex, birth, birthaddr) VALUES ('Mac', 'F', '1988-07-07', 'china')"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print (e)
    db.rollback()
#db.close()

# select from mytable
#cursor = db.cursor()
sql = "select * from mytable"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    
    for row in results:
        fname = row[0]
        sex = row[1]
        birth = row[2]
        birthaddr = row[3]
        
        print ('fname=', fname, ', sex=', sex, ', birth=', birth, ', birthaddr=', birthaddr)
except Exception as e:
    print (e)
    db.rollback()

# delete from mytable
sql = "delete from mytable where name='wenping'"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print (e)
    db.rollback()

# modify mytable
sql = "update mytable set name='wenping' where name='Mac'"

try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print (e)
    db.rollback()
    
db.close()
