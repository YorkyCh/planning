from utils.db_utils import db_connection

# from .task import create_task, get_all_tasks, get_task_by_id, del_task_by_id

def create_task(project_id, description, name):
    c, conn = db_connection()
    c.execute("INSERT INTO tasks (project_id, description, name) VALUES (?, ?, ?)", (project_id, description, name))
    conn.commit()
    conn.close()

def get_all_tasks(project_id):
    c, conn = db_connection()
    c.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id,))
    tasks = c.fetchall()
    conn.close()
    return [dict(task) for task in tasks]

def delete_task(task_id):
    c, conn = db_connection()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()