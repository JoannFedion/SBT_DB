from faker import Faker
import random
import pymysql


#docker run --name my_manticore -p 9306:9306 -p 9312:9312 -d manticoresearch/manticore - предваритель запустить этот скрипт в терминале,чтобы поднять БД

fake = Faker()

connection = pymysql.connect(host='localhost',
                             port=9306,
                             user='root',
                             password='',
                             db='')

cursor = connection.cursor()


for i in range(1, 101):
    content = fake.text()
    sql = f"INSERT INTO my_index (id, content) VALUES ({i}, '{content}');"
    cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()