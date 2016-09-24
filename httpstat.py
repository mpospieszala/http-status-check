# coding:utf-8
__author__ = 'Magdum'

import urllib
import csv

def openFile():
    urlArray = []
    openF = open('URLlist.txt', 'r')
    for line in openF:
        urlArray.append(line)
    return urlArray

def checkStatusCode():
    urls = openFile()
    for url in urls:
        try:
            a = urllib.urlopen(url)
        except IOError:
            print 'Error', url
        else:
            yield a.getcode(), url


gen = checkStatusCode()

with open('output.csv', 'wb') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar = '\n', lineterminator = '\n') #TODO: Zlikwidować potrójne entery
    writer.writerows(gen)