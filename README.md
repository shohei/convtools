# convtools
2014 March, Shohei Aoki

## 概要
Fab Modulesを日本語に翻訳するためのスクリプトです。

## 実行環境
Pythonの実行環境が必要です。
Python2.7.5, Mac OSX Mavericksで動作を確認しています。

ダウンロードしたフォルダをfab_srcフォルダの直下に置いて下さい。

(フォルダ構成）

```
fab_src --- commands.html 
		 |- Makefile
		 |- src
		 |- convtools (本フォルダ) 
				|- README.md
　　　　        		|- initialize.py
				|- main.py
				|- dictionary.txt
				|- dictionarize.py
```

## 使い方
1. 文字エンコーディングの設定を追加する

```
$ python initialize.py
```

2. 辞書ファイルにしたがって置き換える

```
$ python main.py
```


### 補足：辞書の作成

任意の日本語に直すためのスクリプトが同梱されていますので、自分の好きなように辞書ファイル(dictionary.txt)を作成することも可能です。Fab Modulesのアップデートがあったときなどに活用して下さい。

dictionarize.pyを実行します．

```
$ python dicitionarize.py
```

辞書ファイルのひながた，dictionary_temp.txtが生成されます。

左側が原文です。右側には対応する日本語を記入するため空欄になっています。


dictionary_temp.txt

```
'OK'	''
'from format:'	''
'to process:'	''
...
```

対応する日本語を全て記入して辞書を作って下さい。

ところどころ翻訳が不要な部分（変数名など）がありますが、その行は削除して構いません。

（作成例）
```
'OK'	'OK'
'from format:'	'フォーマット'
'to process:'	'プロセス'
...
```
作成できたらdictionary.txtにリネームして保存して下さい。

後は上の操作2.を実行して下さい。



