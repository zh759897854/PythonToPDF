# coding=utf-8
from __future__ import unicode_literals

import logging
import os
import re
import time
import sys
import threading
import datetime

from fake_useragent import UserAgent
import requests


def download_txt(host, begin_numbers, end_numbers):

    headers = {'User-Agent': UserAgent().random,
               'Host': 'www.shubao77.com',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Pragma': 'no-cache',
               'DNT': '1',
               'Upgrade-Insecure-Requests': '1',
               'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               'Accept-Encoding': "gzip, deflate",
               'Accept-Language': "zh-CN,zh;q=0.9",
               }

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(begin_numbers, end_numbers+1):  # 20298
        try:
            url = "http://www.shubao77.com/modules/article/txtarticle.php?id=" + \
                str(i)
            print('----------------------------------------------------------------')
            print(datetime.datetime.now(),'begin downloading books, id='+("%05d" % i))
            print(' ## url:'+url)

            response = R_SESSION.get(url, headers=headers)
            response.encoding = 'gbk'
            search_object = re.match(".*《(.*)》.*", response.text)
            f_name = search_object.group(
                1).replace(r'/', '-')+'.txt' if search_object else 'tmp'+("%05d" % i)+'.txt'

            with open('/'.join([directory, f_name]), 'w') as f:
                f.write(response.text)
            print(datetime.datetime.now(),'end downloading books, id='+("%05d" % i)+'name='+f_name)
        except :
            print('error for downloading ',url)
        


def run_with_threading(host, books_total, threading_cnt=20):
    threadpool = []
    cut = int(books_total/threading_cnt)
    for i in range(0, threading_cnt):
        if i == 0:
            begin_numbers, end_numbers = 1, cut
        else:
            begin_numbers, end_numbers = begin_numbers+cut, end_numbers+cut

        #threading.Thread(target=download_txt(   host, begin_numbers, end_numbers)).start()

        th = threading.Thread(target=download_txt, args=(
            host, begin_numbers, end_numbers))
        threadpool.append(th)
        print('===============================================================')
        print('append theading for download books in ' + str(begin_numbers)+'--'+str(end_numbers))

    #add theading for last cut 
    th = threading.Thread(target=download_txt, args=(
        host, end_numbers+1, books_total))
    threadpool.append(th)
    print('===============================================================')
    print('append theading for download books in ' + str(end_numbers+1)+'--'+str(books_total))


    for th in threadpool:
        th.start()

    for th in threadpool:
        threading.Thread.join(th)

    print('all Done at:', datetime.datetime.now())


if __name__ == '__main__':
    R_SESSION = requests.session()  # 20289
    directory = host = sys.argv[1]
    books_total = int(sys.argv[2])
    threading_max = int(sys.argv[3])
    run_with_threading(host, books_total, threading_max)
