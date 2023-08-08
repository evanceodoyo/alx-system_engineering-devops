#!/usr/bin/python3
"""
2-recurse module.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a \
    list of hot article titles.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:advanced-api:v1.0 (by /u/username)"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    if data and "children" in data:
        for post in data["children"]:
            post_data = post.get("data")
            if post_data and "title" in post_data:
                hot_list.append(post_data["title"])

        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
