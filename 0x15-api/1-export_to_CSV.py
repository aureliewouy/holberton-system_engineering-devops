#!/usr/bin/python3
""" Python script to export data in the CSV format """


if __name__ == "__main__":
    """code should not be executed when imported"""
    import requests
    from sys import argv
    import csv

    if len(argv) == 2:
        usr = argv[1]
        if usr.isdigit():
            api_user = "https://jsonplaceholder.typicode.com/users/{}"\
                .format(usr)
            resp = requests.get(api_user)
            usr_name = resp.json().get("username")
            api_todo = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
                .format(usr)
            todos = requests.get(api_todo).json()
            with open(usr + '.csv', mode='w') as csv_file:
                wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
                for todo in todos:
                    wr.writerow([usr, usr_name, todo.get('completed'),
                                 todo.get('title')])
