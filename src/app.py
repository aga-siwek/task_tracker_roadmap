import sys
from pathlib import Path
import os
import json
import datetime

import json_connection as db_connection


def process_task():
    commend = sys.argv[1].lower()
    today_data = str(datetime.datetime.now())


    try:
        if commend == "add":
            task_description = sys.argv[2]
            db_connection.add_task(task_description, today_data)

        elif commend == "update":
            task_id = sys.argv[2]
            update_text = sys.argv[3]
            db_connection.update_file(task_id, update_text, today_data)

        elif "mark" in commend:
            task_id = sys.argv[2]
            db_connection.mark_status(task_id, commend, today_data)

        elif commend == "delete":
            task_id = sys.argv[2]
            db_connection.delete_file(task_id)

        elif commend == "list":
            if len(sys.argv) == 2:
                status_name = "all"
            else:
                status_name = sys.argv[2]
            db_connection.list_status(status_name)

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
