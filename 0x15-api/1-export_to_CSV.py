#!/usr/bin/python3
""" Python script to export data in the CSV format """
import requests
from sys import argv
import csv


if __name__ == "__main__":
    """code should not be executed when imported"""
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

                with open(usr + '.csv', mode='a+') as csv_file:
                    wr = csv.writer(csv_file, delimiter=',',
                                    quoting=csv.QUOTE_ALL)
                    wr.writerow([usr, usr_name, completed, todo['title']])
