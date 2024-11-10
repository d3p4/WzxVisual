import pymysql


try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='sales',
        password='123456',
        db='sales',
        charset='utf8'
    )
except pymysql.MySQLError as e:
    print(f"数据库连接错误: {e}")
    conn = None
