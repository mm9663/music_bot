# music bot

## 動作確認をした環境

python 3.6.1

discord.py

Mac OS X High Sierra 10.13.6

## bot の動かし方

channel_id, token, voice_id ファイルの設定が必要です。

./key/. に discord の bot 用 token を置きます。
ファイル名は token とし、トークンの文字列のみを持つようにして下さい。

bot が動作するチャンネルを指定する必要があります。
bot がいるサーバーの、動かしたいチャンネルの ID のみを持つファイルを
同様に ./key/. にファイル名を channel_id として置いて下さい。
voice_idも同様にお願いします。

playlistフォルダに入れたい曲を突っ込んでください(mp3限定)。
## 現在対応している機能
~~~
?join
~~~
botをボイスチャンネルに入れます
~~~
?play
~~~
playlistフォルダからプレイリストを作成し、再生します
一応ループするはずです
~~~
?next
~~~
プレイリストの次の曲に移動します
~~~
?shuffle
~~~
プレイリストをシャッフルし、最初から再生します
~~~
?stop
~~~
曲を止めます
~~~?
volume down/up
~~~
ボリュ－ムを0.001下げます/上げます
~~~?
volume ddown/uup
~~~
ボリュームを0.01下げます/上げます
