#!/usr/bin/python3
'''Function that queries the Reddit API'''


def count_words(subreddit, word_list):
    import requests
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': ''}
    p = {'limit': 100}
    count = 0
    for word in word_list:
        word = word.lower()
    info = requests.get(url, allow_redirects=False, headers=h, params=p).json()
    word_count_dict = {}
    if info.get('message') == 'Not found':
        return None
    if info.get('data') and info['data'].get('children') is not None:
        children = info.get('data').get('children')
        for dictionary in children:
            title = dictionary.get('data').get('title').lower()
            title = title.split()
            for word in word_list:
                if word in title:
                    count += 1
                    word_count_dict.update({word: count})
        a = info['data']['after']
        if a is not None:
            return count_words(subreddit, word_list)
        else:
            for word in word_count_dict:
                print('{}: {}'.format(word, word_count_dict[word]))
