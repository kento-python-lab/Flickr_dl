from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys


# APIキーを設定
key = ''
# シークレットキーを設定
secret = ''

# ダウンロード待機時間の設定(あまり短くしない)
wait_time = 3

# 検索ワードの存在チェック
if len(sys.argv) < 3:
    print('キーワードまたは、ダウンロード枚数が指定されていません。')
    sys.exit()

# キーワードを取得
keyword = sys.argv[1]
# 取得枚数を設定
num_sheets = sys.argv[2]

#　保存先ディレクトリ
save_dir = './images/' + keyword

# 保存先ディレクトリが存在しない場合、ディレクトリを作成
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

flickr = FlickrAPI(key, secret, format='parsed-json')

res = flickr.photos.search(
    text=keyword,
    per_page=num_sheets,
    media='photos',
    sort='relevance',
    safe_search=1,
    extras='url_q,license',
)

# 検索結果の表示
photos = res['photos']
pprint(photos)

# 画像取得処理
try:
    for i, photo in enumerate(photos['photo']):
        url_q = photo['url_q']
        file_path = save_dir + '/' + photo['id'] + '.jpg'

        if os.path.exists(file_path):
            continue

        print(str(i + 1) + ':download=' + url_q)
        urlretrieve(url_q, file_path)
        time.sleep(wait_time)

except:
    import traceback
    traceback.print_exc()
