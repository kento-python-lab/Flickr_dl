# Flickr_dll
Flickr APIを使用した画像取得スクリプト

*****
### 事前準備
・Flickr APIに登録して、APIキーとシークレットキーを取得する。


・APIキーとシークレットキーをスクリプト内に追記する。

　　key = ''　←　APIキー

　　secret = ''　←　シークレットキー


・下記コマンドを実行してPythonライブラリ取得する。

　　pip install -r requirements.txt


*****
### 実行
・下記コマンドを実行すると、画像保存先(./images/{検索ワード})に

　対象の画像が保存される。

　　python image_dll.py {検索ワード} {取得枚数}

