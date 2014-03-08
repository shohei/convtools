FAB MODULES 日本語化スクリプト
2014/3/9 青木翔平 Shohei Aoki

FAB MODULESを日本語に翻訳するためのPythonスクリプトです．
使用する場合はPythonの実行環境が必要になります．

0. 実行環境
このコードはpython2.7.5, Mac OSX Mavericksで動作を確認しています． 
このREADMEがあるフォルダ（convtools: 名前は何でも良い）をfab_srcフォルダの直下において下さい.
（フォルダ構成）
fab_src --- commands.html 
		 |- Makefile
		 |- src
		 |- convtools (本フォルダ) 
				|- README
　　　　        |- putencoding.py
				|- main.py
				|- dictionary.txt
				|- dictionarize.py

1. 文字エンコーディングの設定を追加する．
MIT版のFAB MODULESにはエンコーディングの記述が無いので，一括挿入します．

$ python putencoding.py

2. 辞書ファイルにしたがって置き換える．

$ python main.py



（おまけ．上級者用）
任意の日本語に直すためのスクリプトが同梱されていますので，
自分の好きなように辞書ファイル(dictionary.txt)を作成することも可能です．
Fab Modulesのアップデートがあったときなどに活用して下さい．

1. 日本語化辞書の作成
dictionarize.pyを実行します．
$ python dicitionarize.py

辞書ファイルのひながた，dictionary_temp.txtが生成されます．
左側が原文です．右側には対応する日本語を記入するため空欄になっています．

dictionary_temp.txt
------------------
'OK'	''
'from format:'	''
'to process:'	''
...
------------------

対応する日本語を全て記入して下さい．
ところどころ翻訳が不要な部分（変数名など）があるので
その行は削除して構いません．
（作成例）
------------------
'OK'	'OK'
'from format:'	'フォーマット'
'to process:'	'プロセス'
...
------------------
作成できたらdictionary.txtにリネームして保存して下さい．

後は上の操作と同じです．



