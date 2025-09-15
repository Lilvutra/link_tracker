#Database functions(init, insert, delete)

import sqlite3
from datetime import datetime

db_name = "links.db"

#Is it neccessary to use sqlite_master query to inspect the database
def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links
                 (id INTEGER PRIMARY KEY, url TEXT, title TEXT, detected_at TIMESTAMP)''')
    conn.commit()
    conn.close()

#Currently just stores URL and timestamp, title is placeholder for future use
def add_link(url, title):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO links (url, title, detected_at) VALUES (?, ?, ?)", (url, title, datetime.now()))
    conn.commit()
    conn.close()

def remove_link(url):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM links WHERE url = ?", (url,))
    conn.commit()
    conn.close()






















