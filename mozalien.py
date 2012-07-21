#!/usr/bin/env python
# -*- coding: utf-8-*-
import praw
import json
import feedparser

def configure():
    with open('settings.json') as f:
        json_data = f.read()
        settings = json.loads(json_data)
        return settings
    return None

def login(reddit, settings):
    reddit.login(settings['username'], settings['password'])


def submit(reddit, subreddit, url, title):
    sub = r.get_subreddit(subreddit)
    sub.submit(title=title, url=url)


def main():
    r = praw.Reddit(user_agent='mozalien by /u/nigelbabu')
    login(r)
    submissions = r.get_subreddit('mozillamemes').get_hot(limit=5)
    print [str(x) for x in submissions]


if __name__ == '__main__':
    main()
