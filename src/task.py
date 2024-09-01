import sys
from pathlib import Path
import os
import json
import datetime

# general variables
tracker_path = Path.cwd()
commend = sys.argv[1]
today_data = str(datetime.datetime.now())


# function for commend ADD

# for 1 task
def add_first_task(description, status, currently_data):
    task = {"0": {"description": description, "status": status,
                  "created_at": currently_data, "updated_at": "NO DATA"}}
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, "w") as file:
        json.dump(task, file, indent=4)


# create id for 2,3,4 etc. tasks
def next_id_create():
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
        number_of_dicts = int(max(data.keys())) + 1
        return number_of_dicts


# create 2,3,4 etc. tasks
def add_next_task(description, status, currently_data):
    task = {str(next_id_create()): {"description": description, "status": status,
                                    "created_at": currently_data, "updated_at": "NO DATA"}}

    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
        data.update(task)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


# check if folder for management  task exist, if not add 1 task if yes add next task
def task_adder(add_path, description, status, currently_data):
    # check if folder exist
    check_path = add_path / Path("task_management")
    if not os.path.exists(check_path):
        os.mkdir("task_management")
        add_first_task(description, status, currently_data)
    else:
        add_next_task(description, status, currently_data)


# function for commend UPDATE

def update_file(id_for_task, what_change, change_text, currently_date):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
    if id_for_task in data:
        data[id_for_task][what_change] = change_text
        data[id_for_task]["updated_at"] = currently_date
    else:
        print("wrong id")

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def mark_status(id_for_task, status, currently_date):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r+') as file:
        data = json.load(file)
    if id_for_task in data:
        data[id_for_task]["status"] = status
        data[id_for_task]["updated_at"] = currently_date
    else:
        print("wrong id")

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# function for commend DELETE
def delete_file(id_for_task):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    if id_for_task in data:
        del data[id_for_task]
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# function for commend LIST
def list_status(status):
    file_path = Path.cwd() / Path("task_management", "data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)

        for key, value in data.items():
            if status == "all":
                print(value["description"])
            if value["status"] == status:
                print(value["description"])


if __name__ == '__main__':
    if commend == "add":
        task_description = sys.argv[2]
        task_status = sys.argv[3]
        task_adder(tracker_path, task_description, task_status, today_data)

    if commend == "update":
        task_id = sys.argv[2]
        changed_position = sys.argv[3]
        update_text = sys.argv[4]
        update_file(task_id, changed_position, update_text, today_data)

    if commend == "mark":
        task_id = sys.argv[2]
        status_name = sys.argv[3]
        mark_status(task_id, status_name, today_data)

    if commend == "delete":
        task_id = sys.argv[2]
        delete_file(task_id)

    if commend == "list":
        status_name = sys.argv[2]
        list_status(status_name)
