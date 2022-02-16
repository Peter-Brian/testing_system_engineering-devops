#!/usr/bin/python3
"""Top ten"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return a list of titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    params = {'after': after}
    if after is None:
        return hot_list

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        try:
            after = response.json().get("after")
            data = response.json().get("data")
            children = data.get("children")
            for each in children:
                hot_list.append(each.get("data").get("title"))
        except Exception as e:
            return None
    else:
        return None
    return recurse(subreddit, hot_list, after)
