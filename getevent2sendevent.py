#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

'''
(使い方)

log.txt に「adb shell getevent」の出力結果の一部を入れる

/dev/input/event1: 0003 0035 000002f7
/dev/input/event1: 0003 0036 000002cf
/dev/input/event1: 0001 014a 00000001
/dev/input/event1: 0000 0000 00000000
/dev/input/event1: 0003 0030 00000004
/dev/input/event1: 0000 0000 00000000
/dev/input/event5: 0003 0028 0000002b
/dev/input/event5: 0000 0000 00000005
/dev/input/event5: 0003 0028 0000002f
/dev/input/event5: 0000 0000 00000005


python getevent2sendevent.py の出力結果

adb shell sendevent /dev/input/event1 3 53 759
adb shell sendevent /dev/input/event1 3 54 719
adb shell sendevent /dev/input/event1 1 330 1
adb shell sendevent /dev/input/event1 0 0 0
adb shell sendevent /dev/input/event1 3 48 4
adb shell sendevent /dev/input/event1 0 0 0
adb shell sendevent /dev/input/event5 3 40 43
adb shell sendevent /dev/input/event5 0 0 5
adb shell sendevent /dev/input/event5 3 40 47
adb shell sendevent /dev/input/event5 0 0 5


この結果をコピペして実行すれば、Android のデバイス操作を再現できます。
'''

with open("./log.txt", 'r') as log:
    for line in log:
        log_val = line.split()
        log_device = log_val[0].rstrip(":")
        # イベント抽出 & 10進に変換
        log_type = int(log_val[1], 16)
        log_event = int(log_val[2], 16)
        log_value = int(log_val[3], 16)

        # sendevent のコマンド出力
        cmd_str = "adb shell sendevent {device} {type} {code} {value}"
        cmd = cmd_str.format(device=log_device, type=log_type, code=log_event, value=log_value)
        print(cmd)
