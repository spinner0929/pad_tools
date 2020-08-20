# pad_tools

Android 端末を操作できる ADB というツールで、パズドラのパズル操作を拡張するプログラムです。

## 概要

### puzzle_copy_to_joseki.py

ADB でパズドラの画面をスクショし、定石メーカーに反映させます。  
具体的には、スクショした盤面から各ドロップの色を判別し、それを定石メーカーのURLの盤面情報の部分に入れてブラウザで開きます。  
実行の際はパズドラを起動した Android を接続し、パズル操作可能な状態にしてください。

### joseki_to_adb.py

定石メーカーでシミュレーションした軌跡を実機の操作に反映させます。  
コマンドラインで定石メーカーのシミュレーションURLを入力する仕様です。
具体的には、URLのパズル操作の情報を位置情報の羅列（軌跡）に変換し、その軌跡通りにスワイプの命令をします。  
実行の際はパズドラを起動した Android を接続し、パズル操作可能な状態にしてください。  

## 環境

ADB：インストール必須  
MacOS Catelina 10.15.6  
Python 3.6.4  
(Win は試してません)  

## 作者

[@nagagutsu_af](https://twitter.com/nagagutsu_af)
