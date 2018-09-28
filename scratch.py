#!/usr/bin/env python
'''
Assignment 1:

First create a script file called scratch.py

Go ahead and make a request to the JSONPlaceholder API for the /todos endpoint

Ref: https://jsonplaceholder.typicode.com/todos

Add required code and calculations to find the user/users who have completed most number of tasks.
Can you determine which users have completed the most tasks?

Return output like :

==========
User 20 completed 12 TODOs
or
User 20 and 15 completed 12 TODOs
==========
'''
import requests
import json

def get_top_users(url):
    '''
    Function to find users with completed most number of tasks
    url - url to json data
    '''
    r = requests.get(url)
    todos = r.text
    todo_list = json.loads(todos)
    completed_todos = []
    # Loop through todo list
    for todo in todo_list:
        # Check if task completed
        if todo['completed'] is True:
            completed_todos.append(todo)

    todos_by_user = {}
    # Fetch user ids of completed todos
    for completed_todo in completed_todos:
        user_id = completed_todo['userId']
        try:
            todos_by_user[user_id] += 1
        except KeyError:
            todos_by_user[user_id] = 1
    items = [(v, k) for k, v in todos_by_user.items()]
    items = sorted(items, reverse=True)
    items = [(k, v) for v, k in items]
    c = items[0][1]
    users = []
    # Fetch users having most no. of completed tasks
    for k, v in items:
        if v == c:
            users.append(k)

    top_users = ', '.join(str(x) for x in users)
    result = "Users {} completed {} ToDos".format(top_users, c)
    return result

if __name__ == '__main__':
    url = 'http://poornamlabs.com/todos'
    print get_top_users(url)
