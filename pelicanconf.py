#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Claudio Marcial Pe\xf3n'
SITENAME = u'La Jungla de Bamb\xfa'
SITEURL = 'http://www.elpanda.com.ar'

PATH = 'content'

STATIC_PATHS = ['blog','downloads','images','pages']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'America/Argentina/Cordoba'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('#', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://www.twitter.com/caudio'),
          ('linkedin', 'http://ar.linkedin.com/in/claudiomarcial'),
          ('facebook', 'http://www.facebook.com/claudio.marcial'))

DEFAULT_PAGINATION = 10

#Disquss

DISQUS_SITENAME = 'pandaenlaselva'

#Twitter

TWITTER_USERNAME = 'caudio'

#Setting up new theme.

THEME = 'pelican-blueidea-master'

#Add some plugins

#PLUGINS = ['share_post',]
#PLUGIN_PATHS = [/Library/Python/2.7/site-packages/pelican/plugins]


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
