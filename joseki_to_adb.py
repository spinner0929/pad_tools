import subprocess

'''
 *** adb イベントの命令の詳細 ***
3 57 (追跡ID) ... タッチスタート
3 48 (半径) ... タッチ半径
1 330 1 ... ホールド開始
3 53 (x) ... X座標
3 54 (y) ... Y座標
0 0 0 ... 情報送信
...
3 57 4294967295 ... タッチ終了
1 330 0 ... ホールド終了
0 0 0 ... 情報送信
'''

def hold(point_list):  #  定石メーカーのシミュレーションURLを adb の命令形式に変換する
    cmd_str = "adb shell sendevent {event} {types} {axes} {value}"
    subprocess.call(cmd_str.format(event="/dev/input/event1", types="3", axes="57", value="1"), shell=True)
    subprocess.call(cmd_str.format(event="/dev/input/event1", types="3", axes="48", value="1"), shell=True)
    subprocess.call(cmd_str.format(event="/dev/input/event1", types="1", axes="330", value="1"), shell=True)
    for point in point_list:
        subprocess.call(cmd_str.format(event="/dev/input/event1", types="3", axes="53", value=str(point[0])), shell=True)
        subprocess.call(cmd_str.format(event="/dev/input/event1", types="3", axes="54", value=str(point[1])), shell=True)
        subprocess.call(cmd_str.format(event="/dev/input/event1", types="0", axes="0", value="0"), shell=True)
    subprocess.call(cmd_str.format(event="/dev/input/event1", types="3", axes="57", value="4294967295"), shell=True)
    subprocess.call(cmd_str.format(event="/dev/input/event1", types="1", axes="330", value="0"), shell=True)
    subprocess.call(cmd_str.format(event="/dev/input/event1", types="0", axes="0", value="0"), shell=True)


def exe(strs):  # 定石メーカーの軌跡通りに実機でパズルさせる
    # 盤面のマス目とスマホの座標の対応を定義しておく
    default = {"05": [110,1365], "15": [280,1365], "25": [450,1365], "35": [620,1365], "45": [790,1365], "55": [960,1365], \
               "06": [110,1530], "16": [280,1530], "26": [450,1530], "36": [620,1530], "46": [790,1530], "56": [960,1530], \
               "07": [110,1695], "17": [280,1695], "27": [450,1695], "37": [620,1695], "47": [790,1695], "57": [960,1695], \
               "08": [110,1860], "18": [280,1860], "28": [450,1860], "38": [620,1860], "48": [790,1860], "58": [960,1860], \
               "09": [110,2025], "19": [280,2025], "29": [450,2025], "39": [620,2025], "49": [790,2025], "59": [960,2025]} 
    
    # 定石メーカー上の軌跡と盤面の対応
    move = {"0":-9, "1":1, "2":11, "3":-10, "4":10, "5":-11, "6":-1, "7":9}
    list1 = [default[strs[:2]]]

    if(strs[:1] == "0"):  # 0 から始まると Python では十進数として認識しないその変換処理
    	loc = int(strs[1:2])
    else:
    	loc = int(strs[:2])
    
    # 軌跡を表す数字に応じて現在地を変更する
    for i in strs[3:]:
        if(10 <= loc + move[i]):
            list1.append(default[str(loc + move[i])])
        elif(loc + move[i] < 10):
            list1.append(default["0" + str(loc + move[i])])
        loc = loc + move[i]
    
    return list1


if __name__ =='__main__':
    while True:
        url = input("定石メーカーのURL: ")
        if(url == "exit"):  # exit が入力されたら終了
            break
        elif(url[100:][:-14].replace(",","").isdecimal() == True):
            try:
                route = url[100:][:-14]
                hold(exe(route))
            except KeyError:  # 変なURLはエラーが出る
                print("URL が正しくありません！")
        else:  # 定石メーカーのURL 以外もエラー
            print("URL が正しくありません！")
        

    
