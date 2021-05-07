#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config.site_url import SiteUrl
from fake_useragent import UserAgent
from requests import get
from bs4 import BeautifulSoup
from random import randint
from time import sleep

# 要素からテキストを取得する関数
def conv1(arg):
    arg = [item.getText() for item in arg]
    return arg

# 改行コード『\n\t』を『, 』に書き換えた
# 先頭の改行コード『\n\t』まで『, 』に変換されたためスライスの始点を3文字目にする関数
def conv2(arg):
    arg = [item.getText().replace('\n\t', ', ')[2:] for item in arg]
    return arg

# 要素からURLを取得する関数
def GetLink(arg):
    arg = [item.get('href') for item in arg]
    return arg

# Blogの1〜15ページをスクレイピング（CSSセレクタを用いて情報取得）
for page in range(1, 16):

    # スクレイピングするBlogのURLを外部ファイルから呼び出し（.gitignore済）
    url = SiteUrl()[1] + str(page)

    # fake_useragentを使ったUA設定（今回はブラウザChromeとしてランダム生成）
    ua = UserAgent()
    custom_headers = {'User-Agent': ua.Chrome}

    # UA設定した状態でリクエスト
    fake = get(url, timeout=3, headers=custom_headers)

    # html5libを用いてGETしたHTMLをパース
    soup = BeautifulSoup(fake.content, 'html5lib')

    # 投稿日の取得
    date = soup.select('#main span time')
    date = conv1(date)

    # 投稿者の取得
    name = soup.select('#main span a[class="url fn n"]')
    name = conv1(name)

    # カテゴリの取得
    category = soup.select('footer span ul[class="post-categories"]')
    category = conv2(category)

    # タイトルの取得
    title = soup.select('#main h2 a')
    title = conv1(title)

    # 本文の取得
    body = soup.select('div[class="entry__content"] p')
    body = conv1(body)

    # URLの取得
    link = soup.select('#main h2 a')
    link = GetLink(link)

    # ページ内の記事投稿数（date, name, category, title, body, linkのいずれかを引数とする）
    cnt = len(date)

    # 上記cntをエンドポイントとし取得内容を出力
    for row in range(0, cnt):
        print(date[row])
        print(name[row])
        print(category[row])
        print(title[row])
        print(body[row])
        print(link[row])

    # サーバ負荷減のためページ切り替え時に1〜3秒間ランダム待機
    if page <= 14:
        time = randint(1, 3)
        sleep(time)