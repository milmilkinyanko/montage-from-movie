#!/usr/bin/python3
# 参考: https://qiita.com/mo256man/items/b6e17b5a66d1ea13b5e3

import numpy as np
import sys
import cv2
from PIL import Image, ImageDraw, ImageFont

def cv2_putText(img, text, org, fontFace, fontScale, color, mode=0):
# cv2.putText()にないオリジナル引数「mode」 orgで指定した座標の基準
# 0（デフォ）＝cv2.putText()と同じく左下 1＝左上 2＝中央

    # テキスト描写域を取得
    fontPIL = ImageFont.truetype(font = fontFace, size = fontScale)
    dummy_draw = ImageDraw.Draw(Image.new("RGB", (0,0)))
    text_w, text_h = dummy_draw.textsize(text, font=fontPIL)
    text_b = int(0.1 * text_h) # バグにより下にはみ出る分の対策

    # テキスト描写域の左上座標を取得（元画像の左上を原点とする）
    x, y = org
    offset_x = [0, 0, text_w//2]
    offset_y = [text_h, 0, (text_h+text_b)//2]
    x0 = x - offset_x[mode]
    y0 = y - offset_y[mode]
    img_h, img_w = img.shape[:2]

    # 画面外なら何もしない
    if not ((-text_w < x0 < img_w) and (-text_b-text_h < y0 < img_h)) :
        print ("out of bounds")
        return img

    # テキスト描写域の中で元画像がある領域の左上と右下（元画像の左上を原点とする）
    x1, y1 = max(x0, 0), max(y0, 0)
    x2, y2 = min(x0+text_w, img_w), min(y0+text_h+text_b, img_h)

    # テキスト描写域と同サイズの黒画像を作り、それの全部もしくは一部に元画像を貼る
    text_area = np.full((text_h+text_b,text_w,4), (0,0,0,0), dtype=np.uint8)
    text_area[y1-y0:y2-y0, x1-x0:x2-x0] = img[y1:y2, x1:x2]

    # それをPIL化し、フォントを指定してテキストを描写する（色変換なし）
    imgPIL = Image.fromarray(text_area)
    draw = ImageDraw.Draw(imgPIL)
    draw.text(xy = (0, 0), text = text, fill = color, font = fontPIL)

    # PIL画像をOpenCV画像に戻す（色変換なし）
    text_area = np.array(imgPIL, dtype = np.uint8)

    # 元画像の該当エリアを、文字が描写されたものに更新する
    img[y1:y2, x1:x2] = text_area[y1-y0:y2-y0, x1-x0:x2-x0]

    return img

def main(body,num,w,mode):
    bgcolor = (255,255,255,0)
    fontPIL = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
    size = 120
    pen_width = 10
    textcolor = (0,0,0,255)
    circle_radius = 90
    offset_w = 20
    offset_h = 20

    for i in range(num):
        text = str(i+1)
        picture_file = 'img/' + body + '_' + text.zfill(w) + '.png'
        # img = np.full((height,width,4), bgcolor, dtype=np.uint8)
        img_raw = cv2.imread(picture_file)
        img = cv2.cvtColor(img_raw,cv2.COLOR_BGR2BGRA)
        height,width,_  = img.shape
        img.reshape((height,width,4))
        pos = (0,0)
        if (mode == 0):
            # 左上
            pos = (circle_radius+offset_w, circle_radius+offset_h)
        elif (mode == 1):
            # 右上
            pos = (width - (circle_radius+offset_w), circle_radius+offset_h)
        elif (mode == 2):
            # 右下
            pos = (width - (circle_radius+offset_w), height- (circle_radius+offset_h))
        elif (mode == 3):
            # 左下
            pos = (circle_radius+offset_w, height- (circle_radius+offset_h))

        img = cv2.circle(img, pos, circle_radius, (0,0,0,255), pen_width) # 黒で外枠
        img = cv2.circle(img, pos, circle_radius, (255,255,255,255), -1) # 白で塗りつぶし
        img = cv2_putText(img = img,
                text = text,
                org = pos,          # 円の中心と同じ座標を指定
                fontFace = fontPIL,
                fontScale = size,
                color = textcolor,
                mode = 2)           # 今指定した座標は文字描写域の中心
        output_file = 'img/' + body + '_' + text.zfill(w) + '_converted' + '.png'
        cv2.imwrite(output_file, img)
        print('saved: ' + output_file)

if __name__ == "__main__":
    body=sys.argv[1]
    num=int(sys.argv[2])
    w=int(sys.argv[3])
    mode=int(sys.argv[4])
    main(body,num,w,mode)
