#!/usr/bin/python3
"""
0-subs module.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the total number of subscribers for \
    a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:advanced-api:v1.0 (by /u/username)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    return response.json().get("data").get("subscribers")
