#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config.site_url import SiteUrl
from urllib.request import urlopen
from lxml.html import fromstring
from random import randint
from time import sleep

# 余分な改行や文字列を削除し文字列に変換する関数
def conv(arg):
    arg = [item.strip().replace('     |', '') for item in arg]
    arg = ''.join(arg)
    return arg

# Blogの1〜4ページをスクレイピング（xPathを用いて情報取得）
for page in range(1, 5):

    # スクレイピングするBlogのURLを外部ファイルから呼び出し（.gitignore済）
    url = SiteUrl()[4] + str(page) + '/'
    res = urlopen(url)
    dom = fromstring(res.read())

    # ページ構成は1ページ目は22項目それ以降は20項目表示となっているのでエンドポイントを分岐指定
    if page == 1:
        end = 23
    else:
        end = 21

    for row in range(1, end):

        # 日付を取得
        date = dom.xpath('//*[@id="main"]/div[2]/div[' + str(row) + ']/div[2]/div/p/text()[1]')
        date = conv(date)

        # 内容を取得
        info = dom.xpath('//*[@id="main"]/div[2]/div[' + str(row) + ']/div[2]/h3/a/text()')
        info = conv(info)

        # リンクのURLを取得するためにはxPathの後ろに/@hrefを追加
        link = dom.xpath('//*[@id="main"]/div[2]/div[' + str(row) + ']/div[2]/h3/a/@href')
        link = conv(link)

        # コメントのxPathの順番が表示カテゴリ数によって左右されるので変数jでおおよその範囲（おおよそ2〜5の範囲）で条件分岐
        for i in range(2, 6):

            # hrefタグからコメント文字列を取得するためにはxPathの後ろに/text()を追加
            cmnt = dom.xpath('//*[@id="main"]/div[2]/div[' + str(row) +']/div[2]/div/p/a[' + str(i) + ']/text()')
            cmnt = conv(cmnt)

            # infoに『【固定】』の文字が入っていれば広告なので出力せず，また変数rowの範囲に『コメント』の文字が入っていれば出力
            if '【固定】' not in info and 'コメント' in cmnt:
                print(date)
                print(info)
                print(link)
                print(cmnt)

    # サーバ負荷減のためページ切り替え時に1〜3秒間ランダム待機
    if page <= 3:
        time = randint(1, 3)
        sleep(time)
