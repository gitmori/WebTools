#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from config.site_url import SiteUrl
from common.chrome_get import ChromeGet
from selenium.webdriver.common.by import By
from config.my_info import MyInfo
from my_module.get_info import GetInfo
from os.path import basename
from common.system_info import SysInfo
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep

# スクレイピングあるいは自動制御するサイトのURLを外部ファイルから呼び出し（.gitignore済）
url1 = SiteUrl()[2]
url2 = SiteUrl()[3]

# 自作モジュールchrome_getから関数ChromeGetを呼び出し
chrome = ChromeGet(url1)

# Chromeを起動
driver = chrome[0]

# お問い合わせ種別のドロップダウン値の文字列をXPathで取得
category = driver.find_element(By.XPATH, '//*[@id="ctgry_box"]/div[2]/select/option[4]').text

# 外部ファイルmy_infoから個人情報を返す関数MyInfoを呼び出し（.gitignore済）
my_info = MyInfo()

name = my_info[0]
kana = my_info[1]
mail = my_info[2]
zip = my_info[3]
city = my_info[4]
num_bld = my_info[5]
tel = my_info[6]

# 自作モジュールget_infoから関数GetInfoを呼び出し
com_info = GetInfo(url2)

company = com_info[0]
co_name = com_info[1]
ce_name = com_info[2]

# このモジュール名を取得
md = basename(__file__)

# 自作モジュールsystem_infoから関数SysInfoを呼び出し
system = SysInfo()

os_ver = system[0]
py_ver = system[1]
ym_now = system[2]
md_now = system[3]

# 共通・専用モジュール名一覧を配列に格納
sub_module = [SiteUrl()[0], chrome[1], my_info[7], com_info[3], system[4]]

# お問い合わせ・ご注文内容欄に検証結果・システム詳細を出力
body  = company + ': ' + co_name + '\r\n'
body += '代表: ' + ce_name + '　様'+ '\r\n'
body += '' + '\r\n'
body += 'Pythonスクリプトによる自動入力システムにて動作検証テスト' + '\r\n'
body += 'テスト環境: ' + 'macOS ' + os_ver + ', ' + 'Python ' + py_ver + '\r\n'
body += 'テストプログラム: ' + md + '\r\n'
body += '共通モジュール: ' + sub_module[1] + ', ' + sub_module[4] + '\r\n'
body += '専用モジュール: ' + sub_module[0] + ', ' + sub_module[2] + ', ' + sub_module[3] + '\r\n'
body += '' + '\r\n'
body += '検証結果: 正常に動作することを確認しました．' + '\r\n'
body += '' + '\r\n'
body += 'テスト実行日時: ' + ym_now + '\r\n'
body += 'テスト実行者: ' + name

# XPathで指定した各フォームへ各パラメータを入力
driver.find_element(By.XPATH, '//*[@id="ctgry_box"]/div[2]/select').send_keys(category)
driver.find_element(By.XPATH, '//*[@id="name_box"]/div[2]/input').send_keys(name)
driver.find_element(By.XPATH, '//*[@id="name_box2"]/div[2]/input').send_keys(kana)
driver.find_element(By.XPATH, '//*[@id="mail_box"]/div[2]/input').send_keys(mail)
driver.find_element(By.XPATH, '//*[@id="adrs_box1"]/div[2]/input').send_keys(zip)
driver.find_element(By.XPATH, '//*[@id="adrs_box2"]/div[2]/input').send_keys(city)
driver.find_element(By.XPATH, '//*[@id="adrs_box3"]/div[2]/input').send_keys(num_bld)
driver.find_element(By.XPATH, '//*[@id="tel_box"]/div[2]/input').send_keys(tel)
driver.find_element(By.XPATH, '//*[@id="inquiry_box"]/div[2]/textarea').send_keys(body)

driver.find_element(By.XPATH, '//*[@id="verify_box"]/div[2]/input').send_keys(md_now)
#driver.find_element(By.XPATH, '//*[@id="btn_box_right"]/input').click()

# 上記2行の代わりに下記1行でも代用化
#driver.find_element(By.XPATH, '//*[@id="verify_box"]/div[2]/input').send_keys(md_now, Keys.RETURN)

# サーバ負荷減のためページ切り替え時に1〜3秒間ランダム待機
time = randint(1, 3)
sleep(time)

# 確認画面が表示されてから2秒待機後「送信」ボタン押下（本番実行時はコメント解除）
#driver.find_element(By.XPATH, '//*[@id="submit"]').click()

# サーバ負荷減のためページ切り替え時に1〜3秒間ランダム待機
sleep(time)

# 送信完了画面が表示されてから2秒待機してChrome終了
driver.quit()