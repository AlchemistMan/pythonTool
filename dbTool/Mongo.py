from pymongo import MongoClient

host = '' # 这是 MongoDB的地址，详情请咨询DEV
client = MongoClient(host, 27017)
#连接mydb数据库,账号密码认证
db = client.mydb    #  链接一个DB，这里是mydb只是举个栗子
db.authenticate("用户名", "密码")
collection = db.myset   #
collection.insert({"name":"zhangsan","age":18})   # 插入一条数据，如果没出错那么说明连接成功
