#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://site.douban.com/205387/widget/notes/12693315/'

def main():
    """docstring for main"""
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    i = 0 
    for note in soup.findAll('div', {'class': 'note-item'}):
        note_url = note.find('a', href = True)
        print note_url['href']

if __name__ == '__main__':
    main()
