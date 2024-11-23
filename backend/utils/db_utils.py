import sqlite3

def db_connection():
    conn = sqlite3.connect('projects.db')
    conn.row_factory = sqlite3.Row  
    c = conn.cursor()
    return c, conn