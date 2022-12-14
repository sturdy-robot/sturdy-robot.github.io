AUTHOR = 'Sturdy Robot'
SITENAME = 'Sturdy Robot'
SITEURL = 'https://sturdyrobot.net'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Blogroll
LINKS = (('GitHub', 'https://github.com/sturdy-robot'),
         ('eSports Manager', 'https://github.com/sturdy-robot/esports-manager'),
         ('Openfoot Manager', 'https://github.com/sturdy-robot/openfootmanager'),
        )

GITHUB_URL = 'https://github.com/sturdy-robot'

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True