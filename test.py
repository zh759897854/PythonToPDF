# coding=utf-8

from __future__ import unicode_literals
import logging
import os
import re
import time
from fake_useragent import UserAgent

try:
	from urllib.parse import urlparse  # py3
except:
	from urlparse import urlparse  # py2

import pdfkit
import requests
from bs4 import BeautifulSoup

def get_url_list():
    """
    获取所有URL目录列表
    :return:
    """
    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html.parser")

    # menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    menu_tag = soup.find_all(class_="x-wiki-index-item")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls