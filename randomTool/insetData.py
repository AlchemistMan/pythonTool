# 向Mysql数据库里插入100条数据


import pymysql
import random
NUM = 0
db = pymysql.connect(host='IP', user='', passwd='', db='', port=80, charset='utf8')
cursor = db.cursor()

for i in range(100):
    Ageint = 20 + random.randint(0, 40)
    IMCONME = 10000 + random.randint(0, 1000)
    NUM += 1
    NAME ='name'+str(NUM)
    Nation ='CHINA', 'JAPAN', 'UK', 'USA', 'GERMAN', 'FRANCE', 'KOREA', 'BRAZIL'
    Lastname = 'SMTH','KOBE', 'MICHEAEL', 'JASON', 'FUCK', 'STUPID'
    Hobby = 'FOOTBALL', 'BASKETBALL', 'VOLLEBALL'
    COME = random.choice(Nation)
    LASTNAME = random.choice(Lastname)
    HOBBY = random.choice(Hobby)
    sql ="INSERT  test1y(id, firstname, middlename, lastname, comefrom, age, income, hobby) VALUES ('%d', '%s','%s','%s', '%s', '%d', '%d' ,'%s')"% (NUM, NAME, COME, LASTNAME, COME, Ageint, IMCONME,HOBBY)
    cursor.execute(sql)
    db.commit()
cursor.close()
db.close()