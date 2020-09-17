#!/usr/bin/python3
'''Function that queries the Reddit API'''


def top_ten(subreddit):
    '''Gets number of subscribers from subreddit'''
    import requests
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': ''}
    info = requests.get(url, allow_redirects=False, headers=h).json()
    if info.get('message') == 'Not found':
        print(None)
        return
    if info.get('data') and info['data'].get('children') is not None:
        list_of_children = info.get('data').get('children')[:10]
        [print(title['data']['title']) for title in list_of_children]
    else:
        print(None)
