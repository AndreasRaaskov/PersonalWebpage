from pathlib import Path

# Basic site information
AUTHOR = 'Your Name'
SITENAME = 'Your Name - Personal Website'
#SITEURL = "https://andreasraaskov.github.io/PersonalWebpage"
RELATIVE_URLS = False


SITEURL = 'http://localhost:8000'

# Time and Date
TIMEZONE = 'Europe/Copenhagen'  # Adjust this to your timezone
DEFAULT_LANG = 'en'

# Site generation settings
PATH = 'content'  # Directory containing your content
OUTPUT_PATH = 'output'  # Directory where Pelican will put the generated site

# URL settings
ARTICLE_PATHS = ['articles']  # Directory for blog posts, if you plan to have a blog
PAGE_PATHS = ['pages']  # Directory for static pages

# Theme settings
THEME = Path(__file__).parent / 'themes' / 'custom_theme'

# Static files
STATIC_PATHS = ['images']  # For your profile picture and other static assets

# Plugins and extensions
PLUGINS = []  # Add any plugins you want to use

# Disable some default pages we don't need right now
ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

# Custom settings for your homepage
TEMPLATE_PAGES = {'index.html': 'index.html'}