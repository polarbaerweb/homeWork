"""

    Создать таблицу для студентов ( Id(auto_increment primary key), ФИО, пол, обучение онлайн или офлайн, группа, адрес, почта  и номер телефона),

    заполните эту таблицу 15 студентами

    напишите select отдельно для каждого поля а также select *

    используйте вместе c select выражение where где в номере телефона есть 2

"""

from mysql import connector as connection
from random import randint
from faker import Faker

db = connection.connect(
    host="127.0.0.1",
    user="root",
    password="polarbear123_",
    database="polarbear"
)

cursor = db.cursor()

sql_table = """create table if not exists students (
            id integer primary key auto_increment,
            firstName varchar(20) not null,
            lastName varchar(20) not null,
            surname varchar(20) not null,
            sex varchar(1) default('n'), 
            typeOfEducation varchar(20) not null,
            team varchar(60),
            address varchar(90), 
            email varchar(50) not null, 
            phoneNumber varchar(30) )"""

cursor.execute(sql_table)
db.commit()

# values = []
# faker = Faker()
# sex = ("m", "f")
# type = ("online", "offline")
#
# for _ in range(15):
#     firstName = faker.first_name()
#     lastName = faker.last_name()
#     surname = faker.last_name()
#     gender = sex[randint(0, 1)]
#     typeOfEducation = type[randint(0, 1)]
#     group = faker.job()
#     addr = faker.address()
#     email = f"{firstName + lastName}@gmail.com"
#     phoneNumber = f"+998"
#     for _ in range(9):
#         number = randint(1, 9)
#         phoneNumber += str(number)
#
#     values.append((firstName, lastName, surname, gender, typeOfEducation, group, addr, email, phoneNumber))
#
#
# sql_insert = """
#     insert into students (firstName, lastName, surname, sex, typeOfEducation, team, address, email, phoneNumber) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
# """
#
# cursor.executemany(sql_insert, values)
# db.commit()


def getUserData(column):
    sql = f"select {column} from students"
    cursor.execute(sql)
    output = cursor.fetchall()
    return output


columns = "firstName", "lastName", "surname", "sex", "typeOfEducation", "team", "address", "email", "phoneNumber"

for column in columns:
    print(f"user {column} columns: {getUserData(column)}")


def userInfo():
    sql = "select * from students where sex='f' and phoneNumber like '%1%' order by id desc"
    cursor.execute(sql)
    output = cursor.fetchall()
    return output

print(f"user female {column} columns: {userInfo()}")