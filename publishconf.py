#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.m157q.tw'
RELATIVE_URLS = False

# atom feed
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# rss feed
FEED_RSS = 'feeds/rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "m157q-logdown"
GOOGLE_ANALYTICS = "UA-45367183-2"
GOOGLE_ANALYTICS_DOMAIN = "auto"
# GOOGLE_SEARCH = "005681925362179744994:3xdgt3w3iu0"
