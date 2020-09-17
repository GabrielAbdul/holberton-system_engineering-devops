#!/usr/bin/python3
'''Function that queries the Reddit API'''


def recurse(subreddit, hot_list=[], a=''):
    '''Gets number of subscribers from subreddit'''
    import requests
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': ''}
    p = {'after': a}
    info = requests.get(url, allow_redirects=False, headers=h, params=p).json()
    if info.get('message') == 'Not found':
        return None
    if info.get('data') and info['data'].get('children') is not None:
        children = info.get('data').get('children')
        hot_list += [title['data']['title'] for title in children]
        a = info['data']['after']
        return recurse(subreddit, hot_list, a) if a is not None else hot_list
    else:
        return None
