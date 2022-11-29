# montage-from-video
<<<<<<< HEAD

![sample](/uploads/57fc427f0fc56b4ec9dd0f13df8a6bec/sample.jpg)
=======
![sample](https://user-images.githubusercontent.com/23270769/159157529-1a71072e-d0a3-456a-bddf-ed187e4d022e.jpg)
>>>>>>> 7cc38ee1b068f47ad50a1943d7548ccb77c3d6eb

- 動画から一定時間ごとにスナップショットをとり、番号をつけた上でタイル状に並べて一枚の画像にするスクリプト群
- ロボットの動きを論文に載せる際などに使えます
- 参考: https://qiita.com/mo256man/items/b6e17b5a66d1ea13b5e3
<<<<<<< HEAD
- 必要パッケージ: ffmpeg, python3, numpy, imagemagick, opencv
    - 大体もとから入ってるはず

## 使い方
- `$ ./mktile.sh sample.mp4`
    - sampleは李林くんの動画をつかわせてもらっています
- うまくいかないときはimgフォルダの中身を消してください
=======
- Ubuntu 20.04を標準としています
- 必要パッケージ: ffmpeg, python3, numpy, imagemagick, opencv, IPAexフォント
    - 大体もとから入ってるはず
    - `$sudo apt install fonts-ipaexfont`

## 使い方
- usage: `$ ./mktile.sh sample.mp4`
    - sampleは https://www.youtube.com/watch?v=FsRjXtt1Sd8 より
>>>>>>> 7cc38ee1b068f47ad50a1943d7548ccb77c3d6eb
