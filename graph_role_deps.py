#!/usr/bin/python
'''Graphs role dependencies in roles/ as a graphviz digraph'''

import os
import yaml
import sys

print 'digraph {'

for role in os.listdir('./roles'):
    try:
        with open('./roles/%s/meta/main.yml' % role) as meta:
            data = yaml.load(meta)
    except Exception as exc:
        print >>sys.stderr, 'Skipping %s: %r' % (role, exc) 
        continue

    try:
        deps = data['dependencies']
    except Exception as exc:
        print >>sys.stderr, 'Skipping %s: %r' % (role, exc)
        continue

    print '\t"%s" -> {' % role,
    for dep in deps:
        print >>sys.stderr, 'dep:', dep
        name = dep['role']
        print '"%s"' % name,
    print '}'

print '}'
