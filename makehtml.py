#! /usr/bin/env python

# Transforms an API documentation file, written in reStructuredText
# (http://docutils.sourceforge.net/rst.html), to a Django template.
# This script is just a thin wrapper around the Docutils rst2html.py
# tool, which is assumed to be in the caller's path.
#
# Usage: make-apidoc-html apidoc.{version}.rst
#
# Output is written to apidoc.{version}.html.
#
# Greg Janee <gjanee@ucop.edu>
# September 2015

import re
import subprocess
import sys
import tempfile

def error (message):
  sys.stderr.write("makehtml: %s\n" % message)
  sys.exit(1)

if len(sys.argv) != 2:
  sys.stderr.write("Usage: makehtml {page_slug}.rst\n")
  sys.exit(1)

infile = sys.argv[1]
slug = infile[:-4] 
outfile = slug + ".html"

t = tempfile.NamedTemporaryFile()
if subprocess.call(["rst2html.py", infile, t.name]) != 0:
  error("subprocess call failed")
m = re.search("//BEGIN//</p>\n(.*)<p>//END//", t.read(), re.S)
if not m: error("error parsing rst2html.py output")
body = m.group(1)
t.close()

# Note the hack below: the extra </div> is needed to close the
# preceding section.

f = open(outfile, "w")
f.write(
"""<!DOCTYPE html>
<html lang="en">
<!--#include virtual="prelim.html" -->
<body>
<!--#include virtual="header.html" -->
<!--#include virtual="breadcrumb_%s.html" -->
<div class="container-narrowest">%s</div>
<!--#include virtual="footer.html" -->
</div>
</body>
</html>
""" % (slug, body))
f.close()
