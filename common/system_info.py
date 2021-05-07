#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from os.path import basename
from platform import mac_ver
from sys import version
from os.path import basename

# システム情報を返す関数（macOS専用）
def SysInfo():

    # macOSのバージョンを取得
    os_ver = mac_ver()[0]

    #Pythonのバージョンを取得
    py_ver = version[0:5]

    # 現在日時を取得
    dt_now = datetime.now()

    # 現在日時（書式設定）
    ym_now = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

    # spam対策用4桁認証文字列（書式設定）
    md_now = dt_now.strftime('%m%d')

    # このモジュール名を取得
    mg = basename(__file__)

    # 戻り値
    return os_ver, py_ver, ym_now, md_now, mg

if __name__ == '__main__':
    SysInfo()