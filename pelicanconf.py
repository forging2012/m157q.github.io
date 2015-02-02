#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'm157q'
SITENAME = u'Just for noting'
SITESUBTITLE = u'note everything worth noting for me'
SITEURL = u'https://m157q.github.io'
PATH = 'content'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
DISQUS_SITENAME = "m157q-logdown"
GOOGLE_ANALYTICS = "UA-45367183-1"
GITHUB_URL = 'https://github.com/M157q'
TWITTER_USERNAME = u'M157q'


# URLs and Paths
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
STATIC_PATHS = ['images']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/M157q'),
    ('Twitter', 'https://twitter.com/M157q'),
    ('Google+', 'https://plus.google.com/u/0/+SYJheng/posts'),
)

# Debug
LOAD_CONTENT_CACHE = False
