import sys
from pathlib import Path
import os
import json
import datetime

import mysql_connection as db_connection



# def id_creator(data_from_json):
#     if bool(data_from_json):
#         next_id = int(max(data_from_json.keys())) + 1
#         return next_id
#     else:
#         return 0


def check_if_file_exist():
    # check if  directory exist
    check_path = Path.cwd() / Path("task_management")
    if not os.path.exists(check_path):
        os.mkdir("task_management")

    # check if JSON file exist
    check_path = Path.cwd() / Path("task_management", "data.json")
    if not os.path.exists(check_path):
        with open(check_path, "w") as file:
            json.dump({}, file)


def add_task(description, currently_data):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)

        task_id = id_creator(data)

        task = {str(task_id): {"description": description, "status": "todo",
                               "created_at": currently_data, "updated_at": currently_data, "id": task_id}}
        data.update(task)
        file.seek(0)
        json.dump(data, file, indent=4)

    print(f"Task added successfully (ID: {task_id})")


# UPDATE description
def update_file(id_for_task, change_text, currently_date):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
    if id_for_task in data:
        data[id_for_task]["description"] = change_text
        data[id_for_task]["updated_at"] = currently_date
    else:
        print("ID doesn't exist")
        return False

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Task ID: {id_for_task} was updated")


# MARK status
def mark_status(id_for_task, commend, currently_date):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
    if id_for_task in data:
        if "todo" in commend:
            data[id_for_task]["status"] = "todo"
            data[id_for_task]["updated_at"] = currently_date
            print(f"'todo' for task ID: {id_for_task}.")
        elif "in-progress" in commend:
            data[id_for_task]["status"] = "in-progress"
            data[id_for_task]["updated_at"] = currently_date
            print(f"'in progress' for task ID: {id_for_task}.")
        elif "done" in commend:
            data[id_for_task]["status"] = "done"
            data[id_for_task]["updated_at"] = currently_date
            print(f"'done' for task ID: {id_for_task}.")
        else:
            print("status doesn't exist")
            return False

    else:
        print("ID doesn't exist")
        return False

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print("Status has been successfully changed")


# DELETE task
def delete_file(id_for_task):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    if id_for_task in data:
        del data[id_for_task]
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Task ID: {id_for_task} was deleted")


# LIST tasks
def list_status(status):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)

        for key, value in data.items():
            if status == "all":
                print(str(value["id"]) + ". " + value["description"])
            if value["status"] == status:
                print(str(value["id"]) + ". " + value["description"])


def process_task():
    commend = sys.argv[1].lower()
    today_data = str(datetime.datetime.now())

    check_if_file_exist()

    try:
        if commend == "add":
            task_description = sys.argv[2]
            add_task(task_description, today_data)

        elif commend == "update":
            task_id = sys.argv[2]
            update_text = sys.argv[3]
            update_file(task_id, update_text, today_data)

        elif "mark" in commend:
            task_id = sys.argv[2]
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
                  "\n ADD: python task.py add 'task description'"
                  "\n UPDATE: python task.py update 'task id' 'update text'"
                  "\n MARK: python task.py mark+'task id' 'status name'"
                  "\n LIST: python task.py list for all or python task.py list 'status name'"
                  "\n DELETE: python task.py delete 'task id'")

    except IndexError:
        print("You can use a few commends: "
              "\n ADD: python task.py add 'task description'"
              "\n UPDATE: python task.py update 'task id' 'update text'"
              "\n MARK: python task.py mark+'task id' 'status name'"
              "\n LIST: python task.py list for all or python task.py list 'status name'"
              "\n DELETE: python task.py delete 'task id'")


if __name__ == '__main__':
    process_task()
