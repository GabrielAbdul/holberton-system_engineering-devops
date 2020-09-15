#!/usr/bin/python3
'''returns info about employees based on input id number'''


if __name__ == '__main__':

    import csv
    import requests
    from sys import argv

    u_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(u_id)
    url_for_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(u_id)
    r = requests.get(url)
    name = requests.get(url_for_name).json().get('username')

    with open('{}.csv'.format(u_id), mode='w') as f:
        w = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

        for task in r.json():
            w.writerow([u_id, name, task.get('completed'), task.get('title')])
