# -*- coding: utf-8 -*-

import datetime

"""
Tarbell project configuration
"""

# Google spreadsheet key
SPREADSHEET_KEY = "1kKTcr1m2HirJoMM7-Jq23qkcl8SkSc6k0cncllfiWmo"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Spreadsheet cache lifetime in seconds. (Default: 4)
# SPREADSHEET_CACHE_TTL = 4

# Create JSON data at ./data.json, disabled by default
CREATE_JSON = True

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
    "production": "cloud.registerguard.com/discovery",
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
    'title': 'Discovery 2016',
    'map_height': '380px',
    'GOOGLE_ANALYTICS_ID': 'UA-882065-1',
    'datetime_now': datetime.datetime.now(),
}

# Blueprint
from flask import Blueprint, Response, g, render_template, request

blueprint = Blueprint('discovery', __name__)

@blueprint.route('/breweries/print/')
def breweries_indesign_tagged_text():
    id_file_timestamp = '%s' % datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')

    context = g.current_site.get_context()
    context['os'] = 'WIN'
    the_text = render_template('breweries/print.html', **context)
    # make the line endings Windows
    the_text = the_text.replace(u'\n', u'\r\n')
    # make it utf-16le, what Windows calls 'Unicode'
    the_text = the_text.encode('utf-16-le')
    the_response = Response(the_text, mimetype='text/plain')
    the_response.headers['Content-Disposition'] = 'attachment; filename=breweries-%s.txt' % id_file_timestamp
    return the_response

@blueprint.route('/campgrounds/print/')
def campgrounds_indesign_tagged_text():
    id_file_timestamp = '%s' % datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')

    context = g.current_site.get_context()
    context['os'] = u'WIN'
    the_text = render_template('campgrounds/print.html', **context)
    # make the line endings Windows
    the_text = the_text.replace(u'\n', u'\r\n')
    # make it utf-16le, what Windows calls 'Unicode'
    the_text = the_text.encode('utf-16-le')
    the_response = Response(the_text, mimetype='text/plain')
    the_response.headers['Content-Disposition'] = 'attachment; filename=campgrounds-%s.txt' % id_file_timestamp
    return the_response

@blueprint.route('/festivals/print/')
def festivals_indesign_tagged_text():
    id_file_timestamp = '%s' % datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')

    context = g.current_site.get_context()
    context['os'] = 'WIN'
    the_text = render_template('festivals/print.html', **context)
    # make the line endings Windows
    the_text = the_text.replace(u'\n', u'\r\n')
    # make it utf-16le, what Windows calls 'Unicode'
    the_text = the_text.encode('utf-16-le')
    the_response = Response(the_text, mimetype='text/plain')
    the_response.headers['Content-Disposition'] = 'attachment; filename=festivals-%s.txt' % id_file_timestamp
    return the_response

@blueprint.route('/festivals/json/')
def festivals_json():
    context = g.current_site.get_context()
    callback_name = request.args.get('callback', '%s' % datetime.datetime.now().strftime('%Y%m%d'))
    context['callback'] = callback_name
    the_json = render_template('festivals/json.html', **context)
    the_json = the_json.encode('windows-1252')
    the_response = Response(the_json, mimetype='application/json', content_type='application/json; charset=windows-1252')
    return the_response

@blueprint.route('/golf/print/')
def golf_indesign_tagged_text():
    id_file_timestamp = '%s' % datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')

    context = g.current_site.get_context()
    context['os'] = 'WIN'
    the_text = render_template('golf/print.html', **context)
    # make the line endings Windows
    the_text = the_text.replace(u'\n', u'\r\n')
    # make it utf-16le, what Windows calls 'Unicode'
    the_text = the_text.encode('utf-16-le')
    the_response = Response(the_text, mimetype='text/plain')
    the_response.headers['Content-Disposition'] = 'attachment; filename=golf-%s.txt' % id_file_timestamp
    return the_response

@blueprint.route('/museums/print/')
def museums_indesign_tagged_text():
    id_file_timestamp = '%s' % datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')

    context = g.current_site.get_context()
    context['os'] = 'WIN'
    the_text = render_template('museums/print.html', **context)
    # make the line endings Windows
    the_text = the_text.replace(u'\n', u'\r\n')
    # make it utf-16le, what Windows calls 'Unicode'
    the_text = the_text.encode('utf-16-le')
    the_response = Response(the_text, mimetype='text/plain')
    the_response.headers['Content-Disposition'] = 'attachment; filename=museums-%s.txt' % id_file_timestamp
    return the_response

@blueprint.route('/wineries/print/')
def wineries_indesign_tagged_text():
    id_file_timestamp = '%s' % datetime.datetime.now().strftime('%Y-%m-%d-%I-%M-%S-%p')

    context = g.current_site.get_context()
    context['os'] = 'WIN'
    the_text = render_template('wineries/print.html', **context)
    # make the line endings Windows
    the_text = the_text.replace(u'\n', u'\r\n')
    # make it utf-16le, what Windows calls 'Unicode'
    the_text = the_text.encode('utf-16-le')
    the_response = Response(the_text, mimetype='text/plain')
    the_response.headers['Content-Disposition'] = 'attachment; filename=wineries-%s.txt' % id_file_timestamp
    return the_response
