import mysql.connector
import numpy

db = mysql.connector.connect(user='root', password='1234',
                             host='127.0.0.1', database='new_database')

# code_1 = 'CREATE DATABASE `new_database_1`'
# code_2 = 'DROP DATABASE `new_database_1`'
code_3 = "ALTER TABLE `new_database_1`.`food` " \
         "ADD COLUMN `minh` VARCHAR(45) NULL AFTER `ban`;"
# code_4 = "DROP TABLE `new_database_1`.`food_t2`"
#
# # đổi tên table
code_5 = "ALTER TABLE `new_database`.`distances` " \
         "RENAME TO  `new_database`.`distance` ;"
# tim kiếm tất cả databases hiện có
# code_6 = 'SHOW DATABASES'
# # tìm kiếm tất cả table trong database được chọn
# code_7 = 'SHOW TABLES'
# tìm kiếm dữ liệu trong table
code_8 = 'SELECT * FROM customer'
# # tìm một dữ liệu đơn lẻ
# code_9 = 'SELECT * FROM customer WHERE id = "A5"'
# # tìm ra một dữ liệu tương tự
# code_10 = 'SELECT * FROM customer WHERE name LIKE "%g%"'
code_11 = "UPDATE `new_database`.`distances` SET `km` = '2' WHERE (`ID` = 'A1');"


# lệnh chạy code
mycursor = db.cursor()
mycursor.execute(code_5)  # make database
db.commit()
#
# in ra kết quả có trong mycursor
result = mycursor.fetchall()
b = numpy.array(result)
print(b)
# for x in result:
#     print(x)
#
# kết thúc lệnh
# mycursor.close()
# db.close()