#!/usr/bin/python3
"""Top ten"""
import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """Return a list of titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    params = {'after': after}

    if not word_dict:
        for word in word_list:
            word_dict[word] = 0

    if after is None:
        word_list = [[k, v] for k, v in word_dict.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0].lower(), w[1]))
        return None

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data")
            after = data.get("after", None)
            children = data.get("children", None)
            for each in children:
                title = each.get("data").get("title", None)
                lower = [s.lower() for s in title.split(' ')]

                for w in word_list:
                    word_dict[w] += lower.count(w.lower())
        except Exception as e:
            return None
    else:
        return None

    return recurse(subreddit, hot_list, after)
