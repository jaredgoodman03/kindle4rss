#!/usr/bin/python3
import os
import sys
import urllib
from urllib import request
from bs4 import BeautifulSoup

BASE_URL = 'http://kindle4rss.com/'
USERNAME = ''
PASSWORD = ''

# build opener
o = request.build_opener(request.HTTPCookieProcessor())
request.install_opener(o)

# login
p = bytes(urllib.parse.urlencode({'email_address': USERNAME, 'password': PASSWORD}), 'utf-8')
doc = BeautifulSoup(o.open(BASE_URL + '/login/',  p).read().decode('utf8', 'replace'), features='html.parser')

# get list of courses
doc = BeautifulSoup(o.open(BASE_URL,  p).read().decode('utf8', 'replace'), features='html.parser')


BeautifulSoup(o.open(BASE_URL + '/send_now/').read().decode('utf8', 'replace'))
