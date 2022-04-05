import cx_Oracle

'''
因为 cx_Oracle 不支持 Apple M1 的 ARM 架构 （ARM 才是YYDS）
所以oracle数据库链接分成两种
一类是支持 cx_Oracle ，等待 Oracle 后续更新 支持arm的 ，这个脚本工具也能让 intel芯片的同学继续使用
'''
user =''
passwd = ''
OracleConnectifo = "host:port/servicename"

class oracleDB:
    def execute(sql):
        connect = cx_Oracle.connect(user,passwd,OracleConnectifo)
        cursor = connect.cursor()
        cursor.execute(sql)
        for row in cursor.fetchall():  # 返回全部行
            return row
    def executeone(sql):
        connect = cx_Oracle.connect(user, passwd, OracleConnectifo)
        cursor = connect.cursor()
        cursor.execute(sql)
        for row in cursor.fetchone():  # 返回一行
            return row

    def pers(table):
        sql = "SELECT * FROM  table  p WHERE p.ID =" + table
        data = oracleDB.execute(sql)
        return data