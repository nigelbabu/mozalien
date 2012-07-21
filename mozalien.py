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


def submit(subreddit, feed):
    submission = subreddit.submit(title=feed['title'], url=feed['url'])
    print submission.short_link


def get_feeds(url):
    feed = feedparser.parse(url)
    return [{'url': x.link, 'title': x.title} for x in feed.entries]


def main():
    settings = configure()
    r = praw.Reddit(user_agent='mozalien by /u/%s' % settings['username'])
    sub = r.get_subreddit(settings['subreddit'])
    login(r, settings)
    feeds = get_feeds(settings['feed_url'])
    feeds.reverse()
    for feed in feeds:
        if not len([x for x in r.info(feed['url'])]):
            print feed['title']
            submit(sub, feed)


if __name__ == '__main__':
    main()
