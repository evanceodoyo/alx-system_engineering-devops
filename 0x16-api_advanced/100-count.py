#!/usr/bin/python3
"""
100-count module.
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Queries the Reddit API, parses the title of all hot articles, \
    and prints a sorted count of given keywords (case-insensitive, \
    delimited by spaces. Javascript should count as javascript, \
    but java should not)
    """
    if word_counts is None:
        word_counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:advanced-api:v1.0 (by /u/username)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        print()

    data = response.json().get("data")
    if data and "children" in data:
        for post in data["children"]:
            post_data = post.get("data")
            if post_data and "title" in post_data:
                title = post_data["title"].lower()
                for word in word_list:
                    if word in title:
                        word_counts[word] = word_counts.get(word, 0) + 1

        after = data.get("after")
        if after is not None:
            return count_words(subreddit, word_list, after=after,
                               word_counts=word_counts)
        else:
            sorted_counts = sorted(word_counts.items(),
                                   key=lambda item: (-item[1], item[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
    else:
        print()
