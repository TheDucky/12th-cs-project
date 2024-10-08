# script to generate sql table structure

import mysql.connector as db
from dotenv import load_dotenv
from os import getenv

load_dotenv()

cn_conf = {
    "host": "localhost",
    "user": getenv('MYSQL_USER'),
    "passwd": getenv('MYSQL_PASSKEY')
}

connection = db.connect(**cn_conf)

if connection.is_connected():
    print("handshake successful")
    controller = connection.cursor()
else:
    print("unable to connect to database")
    exit()

try:
    controller.execute("create database notes_app_db")
    print("database [notes_app_db] created")

    print("switching to database [notes_app_db]")
    controller.execute("use notes_app_db")

    controller.execute("""create table notes( 
                        sno int primary key auto_increment,
                        title varchar(150) not null,
                        note varchar(10000) not null,
                        created varchar(20) not null )""")
    print("table [notes] created")

    # auto increment: attribute can be used to generate a unique identity for new rows.
    # this removes the need to rowcount or pass in any search queries before adding the next sno
except:
    print("unable to generate database and/or table")
finally:
    print("closing connection")
    controller.close()
    connection.close()