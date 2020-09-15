#!/usr/bin/python3
'''returns info about employees based on input id number'''


if __name__ == '__main__':

    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/users'
    r = requests.get(url)
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    def return_name(id):
        '''returns name'''
        url_for_names = 'https://jsonplaceholder.typicode.com/users'
        for i in requests.get(url_for_names).json():
            if i.get('id') == id:
                return i.get('username')

    list_ids = [id.get('id') for id in r.json()]
    return_dict = {}
    for ids in list_ids:
        task_dict = [{'username': return_name(ids),
                     'task': task.get('title'),
                        'completed': task.get('completed')} for task in tasks]
        print(task_dict)
        return_dict.update({ids: task_dict})
    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as f:
        json.dump(return_dict, f)
