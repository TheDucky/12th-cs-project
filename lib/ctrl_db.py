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

connection = db.connect(**cn_conf)

if connection.is_connected():
    print("handshake successful")
    controller = connection.cursor()
    print("switching to database [notes_app_db]")
    controller.execute("use notes_app_db")
else:
    print("unable to connect to database")
    exit()

def stage_note():
    file = open("lib/notes.txt", "w")
    notes = reversed(get_notes())
    for note in notes:
        file.write("{0}: {1} [{2}]\n".format(note[0], note[1], note[3]))
        file.write(note[2] + "\n")
        file.write("-"*70 + "\n")
    file.close()

def get_notes():
    controller.execute('select * from notes')
    notes = controller.fetchall()
    return notes

def get_one_note(sno):
    query = 'select * from notes where sno = {}'.format(sno)
    controller.execute(query)
    note = controller.fetchone()
    return note

def add_note(title, note):
    clean_title = title.replace("'", "") 
    clean_note = note.replace("'", "")
    # above two are used to prevent sql injection and crashing the site
    raw_date = datetime.now()
    created = raw_date.strftime('%Y-%m-%d %I:%M %p') # formated date
    query = "insert into notes (title, note, created) values('{0}', '{1}', '{2}')".format(clean_title, clean_note, created)
    controller.execute(query)
    connection.commit()
    print('new note added')

def delete_note(sno):
    try:
        query = "delete from notes where sno = {}".format(sno)
        controller.execute(query)
        connection.commit()
        print('note deleted')
    except:
        print('error unable to delete selected note')

def edit_note(sno, newnote):
    try:
        query = "update notes set note = '{0}' where sno = {1}".format(newnote, sno)
        controller.execute(query)
        connection.commit()
        print('note edited')
    except:
        print('error unable to edit note')