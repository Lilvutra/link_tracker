#Database functions(init, inset, delete)

import sqlite3
from datetime import datetime
db_name = "links.db"

def init_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS links
                 (id INTEGER PRIMARY KEY, url TEXT, created_at TIMESTAMP)''')
    conn.commit()
    conn.close()

def add_link(url):
    conn = sqlite3.connect("db_name")
    c = conn.cursor()
    c.execute("INSERT INTO links (url, created_at) VALUES (?, ?)", (url, datetime.now()))
    conn.commit()
    conn.close()

def remove_link(url):
    conn = sqlite3.connect("db_name")
    c = conn.cursor()
    c.execute("DELETE FROM links WHERE url = ?", (url,))
    conn.commit()
    conn.close()






















