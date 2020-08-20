import numpy as np
from PIL import Image
import subprocess
import webbrowser as wb

def get_rgb(pic, box=""):
    # 画像のRGBを取得する
    if box == "":
        box = (0, 0, pic.width, pic.height)
    rgbimg = pic.crop(box).convert("RGB")
    rgb = np.array(rgbimg.getdata())
    return [__round(rgb[:,0]),  __round(rgb[:,1]), __round(rgb[:,2])]

def color(array):
    # ドロップの色の基準値
    col = {"0" : [219, 95, 83], "2" : [84, 150, 206], "1" : [78, 166, 113], "3" : [201, 191, 92], \
           "4" : [164, 83, 178], "5" : [229, 106, 178], "6" : [140, 124, 149], "7" : [49, 62, 83]}

    max = 0
    result = ""
    # 相関係数が最も大きいものを選ぶ
    for k, c in col.items():
        tmp = np.corrcoef(np.array(array), np.array(c))[0][1]
        if max < tmp:
            result = k
            max = tmp
    return result

def __round(array):
    # 配列の平均値を算出
    return int(round(np.average(array)))
    
def get_url(strs):
    # 定石メーカーのURLを生成
    url = "http://serizawa.web5.jp/puzzdra_theory_maker/index.html?layout=" + str(strs) + "&route=05,&ctwMode=false"
    return url

if __name__ == "__main__":
    # 盤面のマス目の座標を設定する
    xa, xs, xb = 27, 170, 197
    ya, ys, yb =  1267, 170, 1437
    
    # 盤面をスクショして認識する
    a = ("adb", "shell", "screencap", "-p", "/sdcard/screen")
    b = ("adb", "pull", "/sdcard/screen", "screenshot.png")
    c = ("adb", "shell", "rm", "/sdcard/screen")
    subprocess.call(a)
    subprocess.call(b)
    subprocess.call(c)
    pic = Image.open("./screenshot.png", 'r')
    color_list = []

    # すべてのドロップに対して処理をおこなう
    for j in range(5):
        for i in range(6):
            box = (xa + xs*i + 26, ya + ys*j + 26, xb + xs*i - 26, yb + ys*j - 26)
            rgb = get_rgb(pic, box)
            color_list.append(color(rgb))
    
    field = "".join(color_list)
    wb.open(get_url(field))
