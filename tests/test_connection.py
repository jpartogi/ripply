#!/usr/bin/env python

import sys

sys.path.append('../ripply')

from ripply.connection import Connection

connection = Connection()
print connection.client

print Connection().client()