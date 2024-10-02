from pathlib import Path
import os
import json


def check_if_file_exist():
    # check if  directory exist
    check_path = Path.cwd() / Path("db")
    if not os.path.exists(check_path):
        os.mkdir("db")

    # check if JSON file exist
    check_path = Path.cwd() / Path("db", "data.json")
    if not os.path.exists(check_path):
        with open(check_path, "w") as file:
            json.dump({}, file)


def id_creator(data_from_json):
    if bool(data_from_json):
        next_id = int(max(data_from_json.keys())) + 1
        return next_id
    else:
        return 0


def add_task(description, currently_data):
    check_if_file_exist()
    file_path = Path.cwd() / Path("db", "data.json")
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
    check_if_file_exist()

    file_path = Path.cwd() / Path("db", "data.json")
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
    check_if_file_exist()

    file_path = Path.cwd() / Path("db", "data.json")
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
    check_if_file_exist()

    file_path = Path.cwd() / Path("db", "data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    if id_for_task in data:
        del data[id_for_task]
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Task ID: {id_for_task} was deleted")


# LIST tasks
def list_status(status):
    check_if_file_exist()

    file_path = Path.cwd() / Path("db", "data.json")
    with open(file_path, 'r') as file:
        data = json.load(file)

        for key, value in data.items():
            if status == "all":
                print(str(value["id"]) + ". " + value["description"])
            if value["status"] == status:
                print(str(value["id"]) + ". " + value["description"])
