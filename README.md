# montage-from-video

![sample_tile-1](https://user-images.githubusercontent.com/23270769/204457838-6a683a72-d251-4a67-bd85-61e8b7710ab3.jpg)

## Feature
- 動画から一定時間ごとにスナップショットをとり、番号をつけた上でタイル状に並べて一枚の画像にするスクリプト群
- ロボットの動きを論文に載せる際などに使えます
- Ubuntu 20.04を標準としています
- 必要パッケージ: ffmpeg, python3, numpy, opencv, svgwrite, inkscape
    - 大体もとから入ってるはず
    - `$python3 -m pip install svgwrite`
    - `$sudo apt install inkscape`

## 使い方
- usage: `$ ./mktile.sh sample.mp4`
    - sampleは https://www.youtube.com/watch?v=FsRjXtt1Sd8 より
