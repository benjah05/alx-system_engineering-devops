#!/usr/bin/python3
"""
find the number of subcribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        get the number of subs in a subreddit
    """
    try:
        users_api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
        headers = {'User-Agent': 'MyRedditApp/1.0'}

        user_requests = requests.get(users_api_url,
                             headers=headers, allow_redirects=False)
        user_requests.raise_for_status()
        if 'application/json' not in user_requests.headers.get('Content-Type', ''):
            return 0
        user_data = user_requests.json()
        if "data" not in user_data or "subscribers" not in user_data["data"]:
            print("Error: 'data' or 'subscribers' key not found in response")
            return 0
        return int(user_data["data"]["subscribers"])
    except requests.exceptions.HTTPError as err:
        if user_requests.status_code == 404:
            return 0
