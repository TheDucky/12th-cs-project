import mysql.connector as db
from dotenv import load_dotenv
from os import getenv
from datetime import datetime

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
    print("switching to database [notes_app_db]")
    controller.execute("use notes_app_db")
else:
    print("unable to connect to database")
    exit()

def get_notes():
    controller.execute('select * from note_logs')
    notes = controller.fetchall()
    return notes

def add_note(author, note):
    raw_date = datetime.now()
    created = raw_date.strftime('%Y-%m-%d %H:%M:%S') # formated date
    query = "insert into note_logs (author, note, created) values('{0}', '{1}', '{2}')".format(author, note, created)
    controller.execute(query)
    connection.commit()
    print('new note added')

def delete_note(sno):
    try:
        query = "delete from note_logs where sno = {}".format(sno)
        controller.execute(query)
        connection.commit()
        print('deleted note')
    except:
        print('error unable to delete selected note')

#def edit_note():