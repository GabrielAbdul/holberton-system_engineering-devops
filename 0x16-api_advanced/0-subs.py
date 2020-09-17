#!/usr/bin/python3
'''Function that queries the Reddit API'''


def number_of_subscribers(subreddit):
    '''Gets number of subscribers from subreddit'''
    import requests
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': ''}
    subreddit_info = requests.get\
    (url, allow_redirects=False, headers=headers).json()
    try:
        subscriber_count = subreddit_info.get('data').get('subscribers')
    except AttributeError:
        return 0
    return subscriber_count
