#!/usr/bin/python3
'''returns info about employees based on input id number'''


if __name__ == '__main__':

    import requests
    from sys import argv

    u_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(u_id)
    url_for_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(u_id)
    r = requests.get(url)
    name = requests.get(url_for_name).json().get('name')
    total_tasks = len(r.json())
    done_tasks = [task for task in r.json() if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format
          (name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
