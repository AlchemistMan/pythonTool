
import jaydebeapi

'''
因为 cx_Oracle 不支持 Apple M1 的 ARM 架构 （ARM 才是YYDS）
所以oracle数据库链接分成两种
使用 jaydebeapi 链接oracle
'''


user =''
password = ''
OracleConnectifo = 'jdbc:oracle:thin:@host:port/servicename'
dirver = 'oracle.jdbc.OracleDriver'
jarFile = '.. /ojdbc8.jar'


class oracleDB:
    def execute(sql):
        conn = jaydebeapi.connect(dirver, OracleConnectifo, [user, password], jarFile)
        curs = conn.cursor()
        curs.execute(sql)
        for row in curs.fetchall():
            return row

    def executeone(sql):
        conn = jaydebeapi.connect(dirver, OracleConnectifo, [user, password], jarFile)
        curs = conn.cursor()
        curs.execute(sql)
        for row in curs.fetchone():
            return row

    def pers(table):
        sql = "SELECT * FROM  table  p WHERE p.ID =" + table
        data = oracleDB.execute(sql)
        return data