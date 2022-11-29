#!/usr/bin/python3
# 参考: https://qiita.com/mo256man/items/b6e17b5a66d1ea13b5e3

import numpy as np
import sys
import base64
import svgwrite
import cv2


def main(body,num,w,mode,col_num,row_num,tile_offset):
    bgcolor = (255,255,255,0) # 透明
    fontPIL = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
    size = 100
    font_size = size * 0.7
    textcolor = (0,0,0,255) # テキストの色、デフォルトは黒
    circle_radius = 90
    offset_w = 20
    offset_h = 20
    circle_stroke_color = "#000000" # 円の外枠の色、デフォルトは黒
    circle_fill_color = "#FFFFFF" # 円の塗りつぶしの色、デフォルトは白
    circle_fill_opacity = 0.7 # 円の塗りつぶしの透過率
    circle_stroke_width = 5

    picture_file = 'img/' + body + '_' + "1".zfill(w) + '.png'
    img_cv = cv2.imread(picture_file)
    height,width,_  = img_cv.shape
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

    col_cnt = 0
    row_cnt = 0

    output_file =  body + '_tile.svg'
    dwg = svgwrite.Drawing(output_file, size=((width+tile_offset)*col_num-tile_offset,(height+tile_offset)*row_num-tile_offset))

    for i in range(num):
        text = str(i+1)
        picture_file = 'img/' + body + '_' + text.zfill(w) + '.png'
        with open(picture_file, "rb") as f:
            img = base64.b64encode(f.read())
        base_offset = (col_cnt*(width+tile_offset), row_cnt*(height+tile_offset))
        print(i, ": ", base_offset)

        img = dwg.image('data:image/jpg;base64,' + img.decode("ascii"), size=(width,height), insert=base_offset)
        shapes = dwg.add(img)
        circle = dwg.ellipse(center=(pos[0]+base_offset[0], pos[1]+base_offset[1]), r=(circle_radius, circle_radius)).fill(circle_fill_color, opacity=circle_fill_opacity).stroke(circle_stroke_color, width=circle_stroke_width)
        shapes = dwg.add(circle)
        text = dwg.text(text, insert=(pos[0]+base_offset[0], pos[1]+base_offset[1]), font_size=font_size, text_anchor="middle", dominant_baseline="central")
        shapes = dwg.add(text)

        col_cnt += 1
        if col_cnt >= col_num:
            row_cnt += 1
            col_cnt = 0

    dwg.save()
    print('saved: ' + output_file)

if __name__ == "__main__":
    body=sys.argv[1]
    num=int(sys.argv[2])
    w=int(sys.argv[3])
    mode=int(sys.argv[4])
    col_num=int(sys.argv[5])
    row_num=int(sys.argv[6])
    tile_offset=int(sys.argv[7])
    main(body,num,w,mode,col_num,row_num,tile_offset)
