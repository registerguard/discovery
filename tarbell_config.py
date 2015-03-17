# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Google spreadsheet key
SPREADSHEET_KEY = "1CIiWvFX-ecB0oYDEhNcyw2pCsMrK2MUX04Bu33BqXKo"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# Get context from a local file or URL. This file can be a CSV or Excel
# spreadsheet file. Relative, absolute, and remote (http/https) paths can be
# used.
# CONTEXT_SOURCE_FILE = ""

# EXPERIMENTAL: Path to a credentials file to authenticate with Google Drive.
# This is useful for for automated deployment. This option may be replaced by
# command line flag or environment variable. Take care not to commit or publish
# your credentials file.
# CREDENTIALS_PATH = ""

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it

    "staging": "uploads.registerguard.com/discovery",
    "production":  "cloud.registerguard.com/discovery",
}

# Default template variables
DEFAULT_CONTEXT = {
    'data': [   {   'column1': u'row1, column1',
                    'column2': u'row1, column2'},
                {   'column1': u'row2, column1',
                    'column2': u'row2, column2'}],
    'headline': u'Test headline',
    'keyed_data': {   'key1': {   'column1': u'key1, column1',
                                  'column2': u'key1, column2',
                                  'key': u'key1'},
                      'key2': {   'column1': u'key2, column1',
                                  'column2': u'key2, column2',
                                  'key': u'key2'}},
    'name': 'discovery',
    'title': 'Discovery 2015'
}

# Blueprint
from flask import Blueprint, Response, g, render_template

blueprint = Blueprint('discovery', __name__)

@blueprint.route('/campgrounds/print/mac/')
def mac_stuff():
    context = g.current_site.get_context()
    context['os'] = 'MAC'
    the_text = render_template('campgrounds/print.html', **context)
    the_response = Response(the_text, mimetype='application/json')
    the_response.headers['Content-Disposition'] = 'attachment; filename=foo_bar.txt'
    return the_response

@blueprint.route('/campgrounds/print/win/')
def win_stuff():
    context = g.current_site.get_context()
    context['os'] = 'WIN'
    the_text = render_template('campgrounds/print.html', **context)
    the_response = Response(the_text, mimetype='application/json')
    the_response.headers['Content-Disposition'] = 'attachment; filename=foo_bar.txt'
    return the_response
