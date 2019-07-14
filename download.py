from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import os, time, sys

# API key information
key = "d9900a838d982d9be31417d401c2e785"
secret = "3ee5a44175f24e81"
wait_time = 1

# to designate save folder
keyword = sys.argv[1]  # 引数
savedir = "./" + keyword

# 接続クライアントの作成とサーチの実行
flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = keyword,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, license'
)

# 結果の取り出しと格納
photos = result['photos']

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue  # if there is data, continue next roop
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)