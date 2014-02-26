#!/usr/bin/python
import urllib2

currentLink = 'http://en.wikipedia.org/wiki/D%27alembert%27s_principle'

print urllib2.urlopen(currentLink).read()
