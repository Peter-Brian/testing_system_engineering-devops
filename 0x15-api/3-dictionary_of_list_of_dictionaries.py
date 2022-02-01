#!/usr/bin/python3
"""Gather data from API"""

from requests import get
from sys import argv, exit
import json

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users"
    url_todo = url + "todos"

    request_user = get(url_user)
    request_todo = get(url_todo)
    # Connection and have an access to the json
    try:
        jsuser = request_user.json()
        jstodo = request_todo.json()
    except ValueError:
        print("No Json")

    # Assign values
    if jsuser and jstodo:
        jsresult = {}
        for user in jsuser:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            jsresult[USER_ID] = []

            # create the value of the dict of the final json file
            # jslist = jsresult[USER_ID]
            for task in jstodo:
                TASK_TITLE = task.get('title')
                TASK_COMPLETED_STATUS = task.get('completed')
                # write the internal dict
                taskdict = {"task": TASK_TITLE,
                            "completed": TASK_COMPLETED_STATUS,
                            "username": USERNAME}
                if jsresult[USER_ID] is not None:
                    jsresult[USER_ID].append(taskdict)

                # create the final dictionary
                # js_result = {USER_ID: jslist}

        # generate the jsonfile
        with open('todo_all_employees.json', 'w', newline='') as jsonfile:
            json.dump(jsresult, jsonfile)
