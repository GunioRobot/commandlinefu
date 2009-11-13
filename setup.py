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

import sys
from distutils.core import setup

sys.path.append('python')

from commandlinefu import __version__
from commandlinefu import __url__
from commandlinefu import __author__
from commandlinefu import __author_email__
from commandlinefu import __doc__
from commandlinefu import __name__

classifiers = """Development Status :: 3 - Alpha
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Utilities
Topic :: Software Development :: Libraries""".split('\n')

#Github specific dl path
dl_path = 'downloads/tarball/'

dl_url  = __url__ + dl_path + __name__ + '-' + __version__ + '.tar.gz'

setup(name='python-commandlinefu',
      version          = __version__,
      packages         = ['commandlinefu'],
      package_dir      = { 'commandlinefu' : 'python'},
      description      = 'python implementation of commandlifu API',
      author           = __author__,
      author_email     = __author_email__,
      url              = __url__,
      download_url     = dl_url,
      license          = 'MIT',
      long_description = __doc__,
      classifiers      = classifiers)
 
