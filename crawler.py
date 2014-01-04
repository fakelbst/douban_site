#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import os
from BeautifulSoup import BeautifulSoup

url = 'http://site.douban.com/205387/widget/notes/12693315/'

def main():
    """docstring for main"""
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)

    start = soup.findAll('span', {'class': 'next'});
    page_url = start[0].find('a', href=True)
    notes(page_url['href'])

def notes(page_url):
    html = urllib2.urlopen(page_url).read()
    soup = BeautifulSoup(html)
    for note in soup.findAll('div', {'class': 'note-item'}):
        note_url = note.find('a', href = True)
        get_note(note_url['href'])

def get_note(note_url):
    html = urllib2.urlopen(note_url).read()
    soup = BeautifulSoup(html)
    for note_c in soup.findAll('div', {'class': 'note-content'}):
        image_url = note_c.find('img', src = True)
        print image_url['src']


def downloads():
    pass

if __name__ == '__main__':
    main()
