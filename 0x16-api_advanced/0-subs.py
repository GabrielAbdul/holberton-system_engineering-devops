#!/usr/bin/python3
'''Function that queries the Reddit API'''


def number_of_subscribers(subreddit):
    '''Gets number of subscribers from subreddit'''
    import requests
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {'User-Agent': ''}
    subreddit_info = requests.get(url, allow_redirects=False, headers=h).json()
    try:
        subscriber_count = subreddit_info['data']['subscribers']
    except AttributeError:
        return 0
    return subscriber_count
