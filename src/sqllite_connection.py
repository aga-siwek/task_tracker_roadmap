from pathlib import Path
import os
import sqlite3


def create_data_base():
    # check if  directory exist
    check_path = Path.cwd() / Path("db")
    if not os.path.exists(check_path):
        os.mkdir("db")

    # check if DATA BASE file exist
    check_path = Path.cwd() / Path("db", "data.db")
    if not os.path.exists(check_path):
        con = sqlite3.connect("db/data.db")
        cursor_obj = con.cursor()
        cursor_obj.execute("DROP TABLE IF EXISTS TRACKER")
        statement = """
        CREATE TABLE TRACKER (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description VARCHAR(50) NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL,
        status VARCHAR(20) NOT NULL);
        """
        cursor_obj.execute(statement)
        con.commit()
        cursor_obj.close()
        con.close()


def add_task(description, currently_data):
    create_data_base()

    conn = sqlite3.connect("db/data.db")
    cursor_obj = conn.cursor()
    statement = """
    INSERT INTO TRACKER (description, created_at, updated_at, status)
    VALUES (?, ?, ?, 'todo')"""
    cursor_obj.execute(statement, (description, currently_data, currently_data))
    conn.commit()
    cursor_obj.close()
    conn.close()
    print("Task added successfully")


# UPDATE description
def update_file(id_for_task, change_text, currently_date):
    create_data_base()

    conn = sqlite3.connect("db/data.db")
    cursor_obj = conn.cursor()
    cursor_obj.execute("SELECT id FROM TRACKER WHERE id=?", (id_for_task,))
    select_data = cursor_obj.fetchall()
    if bool(select_data):
        statement = """
        UPDATE TRACKER
        SET description = ?, updated_at = ?
        WHERE id = ?"""
        cursor_obj.execute(statement, (change_text, currently_date, id_for_task))
        conn.commit()
        cursor_obj.close()
        conn.close()
        print(f"Task ID: {id_for_task} was updated")
    else:
        print(f"Task ID: {id_for_task} does not exist")


# MARK status
def mark_status(id_for_task, commend, currently_date):
    create_data_base()

    conn = sqlite3.connect("db/data.db")
    cursor_obj = conn.cursor()
    cursor_obj.execute("SELECT id FROM TRACKER WHERE id=?", (id_for_task,))
    select_data = cursor_obj.fetchone()
    if select_data is not None:
        if "todo" in commend:
            cursor_obj.execute("""
            UPDATE TRACKER 
            SET status = 'todo', updated_at = ?
            WHERE id = ?;
            """, (currently_date, id_for_task))
            print("Status has been successfully changed")
        elif "in-progress" in commend:
            cursor_obj.execute("""
            UPDATE TRACKER 
            SET status = 'in-progress', updated_at = ?
            WHERE id = ?
            """, (currently_date, id_for_task))
            print("Status has been successfully changed")
        elif "done" in commend:
            cursor_obj.execute("""
            UPDATE TRACKER 
            SET status = 'done', updated_at = ?
            WHERE id = ?
            """, (currently_date, id_for_task))
            print("Status has been successfully changed")
        else:
            print("status doesn't exist")
            return False
    else:
        print("ID doesn't exist")
        return False
    conn.commit()
    cursor_obj.close()
    conn.close()


# DELETE task
def delete_file(id_for_task):
    create_data_base()

    conn = sqlite3.connect("db/data.db")
    cursor_obj = conn.cursor()
    cursor_obj.execute("SELECT id FROM TRACKER WHERE id=?", (id_for_task,))
    select_data = cursor_obj.fetchone()
    if select_data is not None:
        cursor_obj.execute("""
        DELETE FROM TRACKER
        WHERE id=?
        """, (id_for_task,))
    conn.commit()
    cursor_obj.close()
    conn.close()


# LIST tasks
# ||' '||  break between
def list_status(status):
    create_data_base()

    conn = sqlite3.connect("db/data.db")
    cursor_obj = conn.cursor()
    if status == "all":
        cursor_obj.execute("SELECT CAST(id AS VARCHAR(10)), description FROM TRACKER ORDER BY id;")
        output = cursor_obj.fetchall()
        for row in output:
            print(". ".join(row))
    else:
        cursor_obj.execute(
            "SELECT CAST(id AS VARCHAR(10)), description FROM TRACKER WHERE status=? ORDER BY id;", (status,))
        output = cursor_obj.fetchall()
        for row in output:
            print(". ".join(row))
