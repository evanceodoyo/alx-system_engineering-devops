#!/usr/bin/python3
"""
1-top_ten module.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot \
    posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:advanced-api:v1.0 (by /u/username)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")

    data = response.json().get("data")
    if data and "children" in data:
        for post in data["children"]:
            post_data = post.get("data")
            if post_data and "title" in post_data:
                print(post_data["title"])
            else:
                print("No title available")
