#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.webdriver import ChromeOptions, Chrome
from os.path import basename

# chrome_getという名前でChrome起動を関数化
def ChromeGet(url):

    # UA設定
    options = ChromeOptions()
    options.add_argument('--user-agent=Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)')

    # URLを指定しChromeを起動
    driver = Chrome(options=options)
    driver.get(url)

    # このモジュール名を取得
    mod = basename(__file__)

    # 戻り値
    return driver, mod

if __name__ == '__main__':
    ChromeGet()