#!/usr/bin/python3
""" Python script that, using this REST API """


if __name__ == "__main__":
    """code should not be executed when imported"""
    import requests
    from sys import argv

    if len(argv) == 2:
        usr = argv[1]
        if usr.isdigit():
            api_user = "https://jsonplaceholder.typicode.com/users/{}"\
                .format(usr)
            resp = requests.get(api_user)
            usr_name = resp.json().get("name")
            api_todo = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
                .format(usr)
            todos = requests.get(api_todo)
            todos_title = todos.json()
            total = 0
            done = 0
            usr_todo = []
            for todo in todos_title:
                total += 1
                completed = todo.get('completed')
                if completed is True:
                    usr_todo.append(todo['title'])
                    done += 1
            print("Employee {} is done with tasks({}/{}):"
                  .format(usr_name, done, total))
            for to in usr_todo:
                print("\t {}".format(to))
