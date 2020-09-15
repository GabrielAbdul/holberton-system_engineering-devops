#!/usr/bin/python3
'''returns info about employees based on input id number'''


if __name__ == '__main__':

    import json
    import requests
    from sys import argv

    u_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(u_id)
    url_for_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(u_id)
    r = requests.get(url)
    name = requests.get(url_for_name).json().get('name')

    task_dict = {u_id: [{'task': i.get('title'),
                 'completed': i.get('completed'),
                        'username': name} for i in r.json()]}
    file_name = u_id + '.json'
    with open(file_name, mode='w') as f:
        json.dump(task_dict, f)
