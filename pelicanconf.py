#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'm157q'
SITENAME = u'Just for noting'
SITEURL = u'https://m157q.github.io'
PATH = 'content'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
TWITTER_USERNAME = u'M157q'
THEME = 'themes/plumage'
#THEME = 'themes/gum'
USE_FOLDER_AS_CATEGORY = False


# URLs and Paths
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
MENUITEMS = [
    #('home', '/index'),
    ('tags', '/tags'),
    ('categories', '/categories'),
    ('archives', '/archives'),
    #('search', 'search'),
    #('authors', 'authors'),
    #('about', 'about'),
]
DIRECT_TEMPLATES = (
    'index',
    'tags',
    'categories',
    'archives',
    #'search',
    #'authors',
    #'about',
)

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
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'related_posts']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1.0,
        'indexes': 0.7,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'yearly'
    }
}
RELATED_POSTS_MAX = 5
