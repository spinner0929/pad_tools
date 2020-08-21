# pad_tools
<br>
Android SDK ツール内の ADB コマンドで、パズドラのパズル操作を拡張するプログラムです。

## 概要
<br>
### puzzle_copy_to_joseki.py
<br>
ADB でパズドラの画面をスクショし、定石メーカーに反映させます。  
具体的には、スクショした盤面から各ドロップの色を判別し、それを定石メーカーのURLの盤面情報の部分に入れてブラウザで開きます。  
実行の際はパズドラを起動した Android を接続し、パズル操作可能な状態にしてください。

### joseki_to_adb.py
<br>
定石メーカーでシミュレーションしたパズルの軌跡を実機のパズル操作に反映させます。  
プログラム実行後、コマンドラインで定石メーカーのパズル共有のURLを入力する仕様です。  
具体的には、URLのパズル情報を位置情報の羅列（軌跡）に変換し、その軌跡通りにスワイプの命令をします。  
Android SDK ツールにはスワイプのコマンドが用意されていますが、直線以外のスワイプには対応できません。  
```
adb shell input swipe (x1) (y1) (x2) (y2) (半径)
```
<br>
その代わり、(x1, y1) → (x2, y2) → (x3, y3) のスワイプ操作は以下のコードで可能です。  
<br>
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
<br>
実行の際はパズドラを起動した Android を接続し、パズル操作可能な状態にしてください。  

### getevent2sendevent.py
ADB のイベントログを解析するためのプログラムです。  
adb shell getevent で得られるイベントログを、デバイス操作のコマンドに変換できます。  
<br>
(使用例)  
log.txt に「adb shell getevent」の出力結果の一部を入れる  
<br>
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
<br>
<br>
python getevent2sendevent.py の出力結果  
<br>
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
<br>
<br>
この結果をコピペして実行すれば、Android のデバイス操作を再現できます。  
画面スワイプなどの操作であれば、/dev/input/event1 のみ抽出します。

## 環境
<br>
SDK Platform Tools 30.0.4  
ADB 1.0.41  
MacOS Catelina 10.15.6  
Win10 Home 1909  
Python 3.6.4, 3.7.4  
(Win は試してません)  

## 作者
<br>
[@nagagutsu_af](https://twitter.com/nagagutsu_af)
