#!/usr/bin/python3
""" Python script that, using this REST API """


if __name__ == "__main__":
    """code should not be executed when imported"""
    import requests
    from sys import argv
    import json

    if len(argv) == 2:
        usr = argv[1]
        if usr.isdigit():
            api_user = "https://jsonplaceholder.typicode.com/users/{}" \
                .format(usr)
            resp = requests.get(api_user)
            usr_name = resp.json().get("username")
            aptodo = 'https://jsonplaceholder.typicode.com/todos/?userId={}' \
                .format(usr)
            todos = requests.get(aptodo).json()
            usr_todo = []
            todo_dict = {}
            for todo in todos:
                todo_dict.update({"username": usr_name})
                todo_dict.update({"task": todo.get('title')})
                todo_dict.update({"completed": todo.get('completed')})
                usr_todo.append(todo_dict)
            new = {usr: usr_todo}
            with open(usr + '.json', mode='w') as f:
                f.write(json.dumps(new))
