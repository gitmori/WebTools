#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
from requests import get
from bs4 import BeautifulSoup
from os.path import basename

# CSSセレクタを用いてスクレイピングする関数
def GetInfo(url):

    # fake_useragentを使ったUA設定（今回はブラウザIEとしてランダム生成）
    ua = UserAgent()
    custom_headers = {'User-Agent': ua.ie}

    # UA設定した状態でリクエストする
    fake = get(url, timeout=3, headers=custom_headers)

    # html5libを用いてGETしたHTMLをパース
    soup = BeautifulSoup(fake.content, 'html5lib')

    # 文字列「事業者名」の取得
    jg = soup.select('#sctl_sign .hourei td.tb13')[0].text

    # 事業者名の取得
    co = soup.select('#sctl_sign .hourei td.tb14')[0].text

    # 代表者名の取得
    to = soup.select('#sctl_sign .hourei td.tb14')[1].text
    
    # このモジュール名を取得
    mod = basename(__file__)

    # 戻り値（coに関しては文字数をスライス指定）
    return jg, co[0:5], to, mod

if __name__ == '__main__':
    GetInfo(url)

