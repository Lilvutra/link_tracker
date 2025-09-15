#View saved links

import sqlite3

db_name = "links.db"

def list_links():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()   
    c.execute("SELECT url, created_at FROM links") #change later after design the database 
    links = c.fetchall()
    conn.close()
    return links

if __name__ == "__main__":
    list_links