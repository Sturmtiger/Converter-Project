import sqlite3 as db
import datetime as dt
import json

def db_write(num, converted_num):
    conn = db.connect('database.db')
    cursor = conn.cursor()
    time_info = dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M:%S")
    data = [(time_info, num, converted_num)]
    cursor.executemany("INSERT INTO queries VALUES (?,?,?)", data)
    conn.commit()
    cursor.close()
    conn.close()

def db_read():
    conn = db.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM queries")
    return cursor.fetchall()