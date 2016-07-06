#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'm157q'
SITENAME = u'Just for noting'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'zh'
DEFAULT_PAGINATION = 10
TWITTER_USERNAME = u'M157q'
THEME = 'themes/plumage'
USE_FOLDER_AS_CATEGORY = False
SUMMARY_MAX_LENGTH = 20

# Directories for Pelican processing
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
ARTICLE_EXCLUDES = ['drafts']

# URLs and Paths
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

STATIC_PATHS = ['files', 'extra/favicon.ico', 'extra/CNAME']

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
}

MENUITEMS = [
    # ('home', '/index'),
    ('Categories', '/categories'),
    ('Archives', '/archives'),
    ('Tags', '/tags'),
    # ('search', 'search'),
    # ('authors', 'authors'),
    # ('about', 'about'),
]

DIRECT_TEMPLATES = (
    'index',
    'tags',
    'categories',
    'archives',
    'search',
    # 'authors',
    # 'about',
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
    ('LinkedIn', 'https://www.linkedin.com/in/shunyi'),
)

# Debug
CACHE_PATH = 'cache'
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
GZIP_CACHE = True
RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'neighbors',
    'pin_to_top',
    'related_posts',
    'render_math',
    'sitemap',
    'share_post',
    'tipue_search',
]
TIPUE_SEARCH = True

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
MATH_JAX = {
    'color': 'blue',
    'linebreak_automatic': True,
    'responsive': True,
    'tex_extensions': ['color.js']
}
