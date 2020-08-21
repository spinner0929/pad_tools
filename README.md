# pad_tools

Android 端末を操作できる ADB というツールで、パズドラのパズル操作を拡張するプログラムです。

## 概要

### puzzle_copy_to_joseki.py

ADB でパズドラの画面をスクショし、定石メーカーに反映させます。  
具体的には、スクショした盤面から各ドロップの色を判別し、それを定石メーカーのURLの盤面情報の部分に入れてブラウザで開きます。  
実行の際はパズドラを起動した Android を接続し、パズル操作可能な状態にしてください。

### joseki_to_adb.py

定石メーカーでシミュレーションしたパズルの軌跡を実機のパズル操作に反映させます。  
プログラム実行後、コマンドラインで定石メーカーのパズル共有のURLを入力する仕様です。  
具体的には、URLのパズル操作の情報を位置情報の羅列（軌跡）に変換し、その軌跡通りにスワイプの命令をします。  
ADBでは、(x1, y1) → (x2, y2) → (x3, y3) のスワイプ操作が以下のように表されます。  

```
# スワイプ開始
adb shell sendevent /dev/input/event1 3 57 (端末ポート番号)
adb shell sendevent /dev/input/event1 3 48 (タッチ領域半径)
adb shell sendevent /dev/input/event1 1 330 1

adb shell sendevent /dev/input/event1 3 53 (x1)
adb shell sendevent /dev/input/event1 3 54 (y1)
adb shell sendevent /dev/input/event1 0 0 0

adb shell sendevent /dev/input/event1 3 53 (x2)
adb shell sendevent /dev/input/event1 3 54 (y2)
adb shell sendevent /dev/input/event1 0 0 0

adb shell sendevent /dev/input/event1 3 53 (x3)
adb shell sendevent /dev/input/event1 3 54 (y3)
adb shell sendevent /dev/input/event1 0 0 0

# スワイプ終了
adb shell sendevent /dev/input/event1 3 57 4294967295
adb shell sendevent /dev/input/event1 1 330 0
adb shell sendevent /dev/input/event1 0 0 0
```

実行の際はパズドラを起動した Android を接続し、パズル操作可能な状態にしてください。  

## 環境

ADB：インストール必須  
MacOS Catelina 10.15.6  
Win10 Home 1909  
Python 3.6.4, 3.7.4  
(Win は試してません)  

## 作者

[@nagagutsu_af](https://twitter.com/nagagutsu_af)
