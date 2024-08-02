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

connection = db.connect(**cn_conf);

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

    controller.execute("""create table note_logs( 
                        sno int primary key,
                        author varchar(50) not null,
                        note varchar(5000) not null,
                        created date not null );""")
    print("table [note_logs] created")
except:
    print("unable to generate database and/or table")
finally:
    print("all jobs done")
    controller.close()
    connection.close()