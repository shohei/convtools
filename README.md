# convtools
2014 March, Shohei Aoki

Fot those who use this code with your languages, please see a bottom description.

## 概要
Fab Modulesを日本語に翻訳するためのスクリプトです。


## 実行環境
Pythonの実行環境が必要です。
Python2.7.5, Mac OSX Mavericksで動作を確認しています。

またGNU-sedの導入が必要です。Homebrewなどでインストールしておいて下さい。

**GNU sedのインストール**
```
$ brew install gnu-sed
```

## 使い方
ターミナルを開いてfab modulesのソースコードがある場所に移動します。
```
$ cd (fab_srcのある場所) 
```
Gitがインストールされている場合は、本スクリプトを次のコマンドでcloneします。

```
$ git clone git@github.com:shohei/convtools.git
```
あるいは手動でダウンロードしてfab_srcフォルダの直下に置いて下さい。

フォルダ構成は以下のようになります。

```
fab_src --- commands.html 
		 |- Makefile
		 |- src
		 |- convtools (本フォルダ) 
				|- README.md
				|- setup.py
				|- initialize.py
				|- replace.py
				|- dictionary.txt
				|- tools
```

準備ができたら以下のコマンドを実行して下さい。
```
$ python setup.py
```
日本語への変換が終わったら上の階層に上がって、通常のようにビルドして下さい。
```
$ cd ../
$ make fab
```

Have fun!

### 補足：辞書の作成
**以下の項目は書きかけです。**

辞書ファイルdictionary.txtを生成するスクリプトが同梱されていますので、自分の好きなようにカスタマイズすることが可能です。Fab Modulesのアップデートがあったときなどに活用して下さい。

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

後は上の操作を実行して下さい。

# For international users
This code can be used even for your languages with a modification of a dictionary file.

First, you need a Python environment. This code was verified with Python 2.7.5 and Mac OSX Mavericks.

GNU-sed is also required. Install it by homebrew (Mac users) or other means.

>**Installing GNU-sed with homebrew**
>```
>$ brew install gnu-sed
>```

Download a fab modules source code and move to the folder location.
```
$ cd /path/to/fab_src
```

Clone this program (or download it manually). 
```
$ git clone git@github.com:shohei/convtools.git
```

Move to the convtools directory, and you'll find a dictionary file named dictionary.txt. 

(Folder location)
```
fab_src --- commands.html 
	 |- Makefile
	 |- src
	 |- convtools (this program)
		|- README.md
		|- setup.py
		|- initialize.py
		|- replace.py
		|- dictionary.txt
		|- tools
```

Open dictionary.txt with a text editor. Now we modify it. I show you an example for French translation

**Before (Japanese translation)**
```
...
"Exit"	"終了"
"Finished."	"終了しました。"
"Origin:"	"原点:"
"Ready."	"準備完了。"
...
```

**After (French translation)**
```
...
"Exit"	"Sortie"
"Finished."	"Terminé."
"Origin:"	"Origine:"
"Ready."	"Prêt."
...
```

After changing all the words, save the file. Then run a following command.

```
$ python setup.py
```
The command will convert original English words to your language.

After running the command, move to upper directory and build fab modules as usual.

```
$ cd ../
$ make fab

```

Voilà, ça marche! I hope you enjoy it.
