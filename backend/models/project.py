import sqlite3
from utils.db_utils import db_connection

def create_project(name, description):
    c, conn = db_connection()
    c.execute("INSERT INTO projects (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

def get_all_projects():
    c, conn = db_connection()
    c.execute('SELECT * FROM projects')
    projects = c.fetchall()
    conn.close()
    return [dict(project) for project in projects] 

def get_project_by_id(id):
    c, conn = db_connection()
    c.execute('SELECT * FROM projects WHERE id = ?', (id,))
    project = c.fetchone()
    conn.close()
    return dict(project) if project else None  

def del_project_by_id(id):
    c, conn = db_connection()
    c.execute('DELETE FROM projects WHERE id = ?', (id,))
    rows_affected = c.rowcount
    conn.commit()
    conn.close()
    return rows_affected > 0