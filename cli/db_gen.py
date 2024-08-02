# script to generate sql table structure

import mysql.connector as db

cn_conf = {
    "host": "localhost",
    "user": "root",
    "passwd": ""
}

connection = db.connect(cn_conf);

if connection.is_connected():
    print("handshake successful")
    controller = connection.cursor()
else:
    print("unable to connect to database")
    exit()

try:
    controller.exicute("create database notes_app_db")
    print("database [notes_app_db] created")

    print("switching to database [notes_app_db]")
    controller.exicute("use notes_app_db")

    controller.exicute("""create table note_logs( 
                        sno int primary key,
                        author varchar(50) not null default 'unknown',
                        note varchar(5000) not null default '-',
                        created date not null );""")
    print("table [note_logs] created")
except:
    print("unable to generate database and/or table")
finally:
    print("all jobs done")
    controller.close()
    connection.close()