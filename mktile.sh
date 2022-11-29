#!/bin/bash

if [ $# -lt 1 ]; then
    echo "please specify target video"
    exit 1
fi

fname=$1
fname_body=${fname%.mp4}

if [ $fname == $fname_body ]; then
    echo "this script is assuming handle with mp4 file."
    echo "please change \"mp4\" to the correct strings when defining \$fname_body"
    exit 1
fi

rm -rf img/*

w=2 # 連番にする際の桁数
startsec=5
period=17
fps=0.8 # 1fps
# トリミングする際に、全体の幅・高さから引くpixel数 (切り取る幅)
minus_w=500
minus_h=0
# 番号の描画を始める座標
# 左上が0,0
start_w=450
start_h=0
ffmpeg -ss $startsec -t $period -i $fname -r $fps -vf crop=in_w-$minus_w:in_h-$minus_h:$start_w:$start_h -vcodec png img/${fname_body}_%${w}d.png


img_num=$(ls img/ | grep $fname_body | grep -v _converted.png | wc -l)
mode=0
# 左上に番号を振りたい時: 0
# 右上に番号を振りたい時: 1
# 右下に番号を振りたい時: 2
# 左下に番号を振りたい時: 3
echo "./mkwatermark.py $fname_body $img_num $w $mode"
./mkwatermark.py $fname_body $img_num $w $mode

num_columns=5
num_rows=3
tile_offset=30
output="tile_${fname_body}.png"
echo "start making montage"
montage -background none -tile ${num_columns}x${num_rows} -geometry +${tile_offset}+${tile_offset} img/${fname_body}*_converted.png $output
echo "saved tile: $output"
