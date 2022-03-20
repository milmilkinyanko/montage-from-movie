# montage-from-video
- 動画から一定時間ごとにスナップショットをとり、番号をつけた上でタイル状に並べて一枚の画像にするスクリプト群
- ロボットの動きを論文に載せる際などに使えます
- 参考: https://qiita.com/mo256man/items/b6e17b5a66d1ea13b5e3
- 必要パッケージ: ffmpeg, python3, numpy, imagemagick, opencv
    - 大体もとから入ってるはず

## 使い方
- usage: `$ ./mktile.sh sample.mp4`
    - sampleは使用可能な動画が簡単に見つからなかったのでpublic repoには載せていません
- うまくいかないときはimgフォルダの中身を消してください
