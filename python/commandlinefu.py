# Copyright (c) 2009 Olivier Hervieu <olivier.hervieu@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from sys     import version_info
from base64  import encodestring
from json    import loads

#Check for python version
if version_info[0] == 2:
    from httplib import HTTPConnection as HTTP
    from urllib  import urlencode
if version_info[0] == 3:
    from http.client import HTTPConnection as HTTP
    from urllib.parse import urlencode

API_DOMAIN    = 'www.commandlinefu.com'
SORT_BY_VOTES = 'sort-by-votes'
SORT_BY_DATES = 'sort-by-dates'

__version__      = '0.1'
__author__       = 'Olivier Hervieu'
__author_email__ = 'olivier.hervieu@gmail.com'
__url__          = 'http://github.com/ohe/commandlinefu/'

__doc__="""
Python CommandLineFu.

CommandLineFu is a python class that implements CommandLineFu API and more.
You can :
- browse current posts sorted by dates or votes,
- get commands from a specified user,
- match everythings that contains a search word,
- search commands that contains a search word.

This modules do not required special dependencies (it use only standard python
modules). So it can be used easily on many platforms.

This modules can't post new commands on commandlinefu since there is no API to
authenticate users and post new tips and tricks on CommandLineFu.
"""

class CommandLineFu(object):
    def __init__(self):
        self._h = HTTP(API_DOMAIN)

    def _operate(self, action, search_limit):
        index = 0
        search_result = []

        while True:
            if search_limit != None and index > search_limit:
                break
            self._h.request("GET", action)
            index = index + 25

            res = loads(self._h.getresponse().read())
            if res == []:
                break
            else: search_result += res

        return search_result

    def browse(self, sort_order=SORT_BY_DATES, index = 0):
        """
        Browse Commandlinefu history, sorted by dates or by votes.
        By default, CLF has 25 results per page, so index can be used
        to see others 25 results.
        """
        self._h.request("GET","/commands/browse/%s/json/%d"%(sort_order,index))
        return self._h.getresponse().read()

    def matching(self, match, sort_order = SORT_BY_DATES, search_limit = None):
        """
        Search from history commands that match the "match" string.
        By default, it returns all result, sort by dates with no search limit.
        """
        match64 = encodestring(match)[:-1]
        action = "/commands/matching/%s/%s/%s/json/%d"%(match, match64, sort_order, index)
        return self._operate(action, search_limit)

    def using(self, match, sort_order = SORT_BY_DATES, search_limit = None):
        """
        Returns commands that implements the search word "match'.
        By default, it returns all result, sort by dates with no search limit.
        """
        action = "/commands/using/%s/%s/json/%d"%(match, sort_order, index)
        return self._operate(action, search_limit)

    def by(self, match, sort_order = SORT_BY_DATES, search_limit = None):
        """
        Returns commands from a specified user.
        By default, it returns all result, sort by dates with no search limit.
        """
        action = "/commands/by/%s/%s/json/%d"%(match, sort_order, index)
        return self._operate(action, search_limit)

