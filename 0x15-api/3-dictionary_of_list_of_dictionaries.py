#!/usr/bin/python3
""" Python script to export data in the JSON format """


if __name__ == "__main__":
    """code should not be executed when imported"""
    import requests
    from sys import argv
    import json

    api_user = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(api_user).json()
    new = {}
    for user in users:
        usr_id = user.get("id")
        aptodo = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
            .format(usr_id)
        todos = requests.get(aptodo).json()
        usr_todo = []
        for todo in todos:
            todo_dict = {"username": user.get("name"),
                         "task": todo.get('title'),
                         "completed": todo.get('completed')}
            usr_todo.append(todo_dict)
        new[usr_id] = usr_todo
    with open('todo_all_employees.json', mode='a+') as f:
        f.write(json.dumps(new))
