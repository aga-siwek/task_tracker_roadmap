import sys
from pathlib import Path
import os
import datetime
import sqlite3


# def create_data_base():
#     # check if  directory exist
#     check_path = Path.cwd() / Path("task_management_sql")
#     if not os.path.exists(check_path):
#         os.mkdir("task_management_sql")
#
#     # check if DATA BASE file exist
#     check_path = Path.cwd() / Path("task_management_sql", "task_tracker.db")
#     if not os.path.exists(check_path):
#         con = sqlite3.connect("task_management_sql/task_tracker.db")
#         cursor_obj = con.cursor()
#         cursor_obj.execute("DROP TABLE IF EXISTS TRACKER")
#         statement = """
#         CREATE TABLE TRACKER (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         description VARCHAR(50) NOT NULL,
#         created_at TEXT NOT NULL,
#         updated_at TEXT NOT NULL,
#         status VARCHAR(20) NOT NULL);
#         """
#         cursor_obj.execute(statement)
#         con.commit()
#         cursor_obj.close()
#         con.close()
#
#
# def add_task(description, currently_data):
#     conn = sqlite3.connect("task_management_sql/task_tracker.db")
#     cursor_obj = conn.cursor()
#     statement = """
#     INSERT INTO TRACKER (description, created_at, updated_at, status)
#     VALUES (?, ?, ?, 'todo')"""
#     cursor_obj.execute(statement, (description, currently_data, currently_data))
#     conn.commit()
#     cursor_obj.close()
#     conn.close()
#     print("Task added successfully")
#
#
# # UPDATE description
# def update_file(id_for_task, change_text, currently_date):
#     conn = sqlite3.connect("task_management_sql/task_tracker.db")
#     cursor_obj = conn.cursor()
#     cursor_obj.execute("SELECT id FROM TRACKER WHERE id=?", (id_for_task,))
#     select_data = cursor_obj.fetchall()
#     if select_data is not None:
#         statement = """
#         UPDATE TRACKER
#         SET description = ?, updated_at = ?
#         WHERE id = ?"""
#         cursor_obj.execute(statement, (change_text, currently_date, id_for_task))
#         conn.commit()
#         cursor_obj.close()
#         conn.close()
#         print(f"Task ID: {id_for_task} was updated")
#     else:
#         print(f"Task ID: {id_for_task} does not exist")
#
#
# # MARK status
# def mark_status(id_for_task, commend, currently_date):
#     conn = sqlite3.connect("task_management_sql/task_tracker.db")
#     cursor_obj = conn.cursor()
#     cursor_obj.execute("SELECT id FROM TRACKER WHERE id=?", (id_for_task,))
#     select_data = cursor_obj.fetchone()
#     if select_data is not None:
#         if "todo" in commend:
#             cursor_obj.execute("""
#             UPDATE TRACKER
#             SET status = 'todo', updated_at = ?
#             WHERE id = ?;
#             """, (currently_date, id_for_task))
#             print("Status has been successfully changed")
#         elif "in-progress" in commend:
#             cursor_obj.execute("""
#             UPDATE TRACKER
#             SET status = 'in-progress', updated_at = ?
#             WHERE id = ?
#             """, (currently_date, id_for_task))
#             print("Status has been successfully changed")
#         elif "done" in commend:
#             cursor_obj.execute("""
#             UPDATE TRACKER
#             SET status = 'done', updated_at = ?
#             WHERE id = ?
#             """, (currently_date, id_for_task))
#             print("Status has been successfully changed")
#         else:
#             print("status doesn't exist")
#             return False
#     else:
#         print("ID doesn't exist")
#         return False
#     conn.commit()
#     cursor_obj.close()
#     conn.close()
#
#
# # DELETE task
# def delete_file(id_for_task):
#     conn = sqlite3.connect("task_management_sql/task_tracker.db")
#     cursor_obj = conn.cursor()
#     cursor_obj.execute("SELECT id FROM TRACKER WHERE id=?", (id_for_task,))
#     select_data = cursor_obj.fetchone()
#     if select_data is not None:
#         cursor_obj.execute("""
#         DELETE FROM TRACKER
#         WHERE id=?
#         """, (id_for_task,))
#     conn.commit()
#     cursor_obj.close()
#     conn.close()
#
#
# # LIST tasks
# # ||' '||  break between
# def list_status(status):
#     conn = sqlite3.connect("task_management_sql/task_tracker.db")
#     cursor_obj = conn.cursor()
#     if status == "all":
#         cursor_obj.execute("SELECT CAST(id AS VARCHAR(10))||'. '|| description FROM TRACKER ORDER BY description;")
#         output = cursor_obj.fetchall()
#         for row in output:
#             print("".join(row))
#     else:
#         cursor_obj.execute("SELECT CAST(id AS VARCHAR(10))||'. '|| description FROM TRACKER WHERE status=? ORDER BY description;", (status,))
#         output = cursor_obj.fetchall()
#         for row in output:
#             print("".join(row))


def process_task():
    commend = sys.argv[1].lower()
    today_data = str(datetime.datetime.now())
    create_data_base()
    try:
        if commend == "add":
            task_description = sys.argv[2]
            add_task(task_description, today_data)

        elif commend == "update":
            task_id = sys.argv[2]
            update_text = sys.argv[3]
            update_file(task_id, update_text, today_data)

        elif "mark" in commend:
            task_id = int(sys.argv[2])
            mark_status(task_id, commend, today_data)

        elif commend == "delete":
            task_id = sys.argv[2]
            delete_file(task_id)

        elif commend == "list":
            if len(sys.argv) == 2:
                status_name = "all"
            else:
                status_name = sys.argv[2]
            list_status(status_name)

        else:
            print("commend doesn't exist \n "
                  "You can use a few commends: "
                  "\n ADD: python task_sql.py add 'task description'"
                  "\n UPDATE: python task_sql.py update 'task id' 'update text'"
                  "\n MARK: python task_sql.py mark+'task id' 'status name'"
                  "\n LIST: python task_sql.py list for all or python task.py list 'status name'"
                  "\n DELETE: python task_sql.py delete 'task id'")

    except IndexError:
        print("You can use a few commends: "
              "\n ADD: python task_sql.py add 'task description'"
              "\n UPDATE: python task_sql.py update 'task id' 'update text'"
              "\n MARK: python task_sql.py mark+'task id' 'status name'"
              "\n LIST: python task_sql.py list for all or python task.py list 'status name'"
              "\n DELETE: python task_sql.py delete 'task id'")


if __name__ == '__main__':
    process_task()
