import pymysql


#打开数据库
db = pymysql.connect("localhost", "root", "root", "TESTDB")
#使用cursor（）方法创建一个游标对象cursor
cursor = db.cursor()

'''
#打印数据库版本信息:
#使用execute（）方法执行SQL语句
cursor.execute("select version()")
#使用fetchone（）方法获取单条数据
data = cursor.fetchone()
print("Database version:%s" % data)
'''

'''
#创建数据库表:
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE if EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
'''

#数据库插入操作：
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库执行
    db.commit()
except:
    #如果发生错误则回滚
    db.rollback()


    








#关闭数据库
db.close()
