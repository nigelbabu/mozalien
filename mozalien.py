#!/usr/bin/env python

import praw
import json

def login(reddit):
    with open('settings.json') as f:
        json_data = f.read()
        settings = json.loads(json_data)
        reddit.login(settings['username'], settings['password'])


def main():
    r = praw.Reddit(user_agent='mozalien by /u/nigelbabu')
    submissions = r.get_subreddit('mozillamemes').get_hot(limit=5)
    print [str(x) for x in submissions]


if __name__ == '__main__':
    main()
