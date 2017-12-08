#coding: utf-8

from bs4 import BeautifulSoup
import requests
import os

urls = []
headers = {"User-Agent":"Mozilla/5.0"}

if os.path.isfile('url-list.txt'):
    with open('url-list.txt') as f:
        for line in f:
            urls.append(line)
else:
    print 'No "url-list.txt" file found. Create file "url-list.txt" to run the program'

for url in urls:
    html = requests.get(url.strip(), allow_redirects=False, headers=headers)
    if html.status_code != 200:
        print html.url,'\t', html.status_code
    else:
        print html.url, '\t', html.status_code
