# Qiita API + Pythonで記事のアクセス数やいいね数を取得する

## はじめに

`Mac環境の記事ですが、Windows環境も同じ手順になります。環境依存の部分は読み替えてお試しください。`

### 目的

Qiita APIを使って記事のアクセス数やLGTM数を取得します。

この記事を最後まで読むと、次のことができるようになります。

| No.  | 概要      | キーワード |
| :--- | :-------- | :--------- |
| 1    | Qiita API |            |
| 2    | REST API  | requests   |

### 完成イメージ

```command.sh
page_views_count=11130, likes_count=21, title=REST APIを使ってSalesforceのデータを取得する, url=https://qiita.com/nsuhara/items/19cf8ec89b88fb3deb39
page_views_count=04778, likes_count=11, title=AlexaスキルをPython/Lambdaで実装する, url=https://qiita.com/nsuhara/items/5b19cfb5ffb897bd4cfd
page_views_count=04482, likes_count=06, title=Salesforceの添付ファイルに制限をかける, url=https://qiita.com/nsuhara/items/bd41c9ad946b8b832207
page_views_count=04008, likes_count=11, title=Swift向け単体テスト(Unit Test)の作り方, url=https://qiita.com/nsuhara/items/bc06c07ff30a5b78696d
page_views_count=03543, likes_count=03, title=Kony AppPlatformを使ってiOS/Androidアプリを作成する, url=https://qiita.com/nsuhara/items/c28d838492512850520c
page_views_count=02642, likes_count=07, title=Flask-SQLAlchemy + PostgreSQLでWebサービスを作成する, url=https://qiita.com/nsuhara/items/fa5998c0b2f4fcefbed4
page_views_count=02579, likes_count=15, title=Heroku + Selenium + ChromeでWEBプロセスを自動化する, url=https://qiita.com/nsuhara/items/76ae132734b7e2b352dd
page_views_count=02127, likes_count=04, title=Heroku SchedulerでPythonを定期実行する, url=https://qiita.com/nsuhara/items/fac20adb6b0a122a3709
page_views_count=02102, likes_count=07, title=Docker + FlaskでWebサービスを作成する, url=https://qiita.com/nsuhara/items/c7eff7fae3801f85b5cd
page_views_count=01869, likes_count=08, title=Messaging API + LIFF + Heroku + Flask + Framework拡張でLINE BOTを作成する, url=https://qiita.com/nsuhara/items/0c431913165e4af0f8f5
page_views_count=01597, likes_count=04, title=SalesforceのLightningデータサービス(LDS)について学ぶ, url=https://qiita.com/nsuhara/items/ecd77def7aa1f985efcc
page_views_count=01507, likes_count=01, title=Kony AppPlatformで作成したiOS/Androidアプリのコーディングについて学ぶ, url=https://qiita.com/nsuhara/items/bf0e8884a7efc3c55176
page_views_count=01490, likes_count=05, title=FlaskでRESTful Webサービスを作成する, url=https://qiita.com/nsuhara/items/449835bc94f0fb3bbcbd
page_views_count=01477, likes_count=02, title=Pythonを使ってJSONからWord(docx)を作成する, url=https://qiita.com/nsuhara/items/3ba2fa7db38acd04f448
page_views_count=01377, likes_count=02, title=AWS-Lambda + PythonでCSVデータをAWS-S3に書き込む, url=https://qiita.com/nsuhara/items/b2bd1d2623bca0f767f8
page_views_count=01208, likes_count=03, title=AWS-Lambda + PythonでAWS-RDS/PostgreSQLのテーブルを読み込む, url=https://qiita.com/nsuhara/items/dd780c2622258d10f961
page_views_count=01194, likes_count=02, title=Django + SQLAlchemy + SQLite3 / PostgreSQLでWebアプリを作成する, url=https://qiita.com/nsuhara/items/4ab5366273082ee0aa73
page_views_count=01159, likes_count=04, title=AWS-Lambda + Python + CronでWEBスクレイピングを定期的に実行する, url=https://qiita.com/nsuhara/items/0d36600511fc162827f6
page_views_count=01071, likes_count=01, title=Kony AppPlatformで作成したiOS/AndroidアプリとSalesforceをデータ連携する, url=https://qiita.com/nsuhara/items/756120f1bddc6f8fe78b
page_views_count=00887, likes_count=00, title=Kony AppPlatformで作成したiOS/AndroidアプリのAuto Layoutについて学ぶ, url=https://qiita.com/nsuhara/items/a52abd9861c51823ecec
page_views_count=00647, likes_count=02, title=PythonでAWS-S3の署名付き(期限付き)URLを生成する, url=https://qiita.com/nsuhara/items/20160b080c2b30d57729
page_views_count=00597, likes_count=03, title=Kong API GatewayのGUI/Kongaを構築する, url=https://qiita.com/nsuhara/items/a0de75e6767f98cc8fec
page_views_count=00500, likes_count=01, title=Kong API Gatewayを構築する, url=https://qiita.com/nsuhara/items/ad1d8fa1faad7940b5c1
page_views_count=00471, likes_count=00, title=Raspberry PiのセットアップからPython環境のインストールまで, url=https://qiita.com/nsuhara/items/05a2b41d94ced1f54316
page_views_count=00437, likes_count=02, title=Raspberry PiとPythonでリモコンカーを作成する, url=https://qiita.com/nsuhara/items/7970b5dfe95ea76c93d6
page_views_count=00364, likes_count=00, title=Flask-SQLAlchemyでUPSERTを実装する方法, url=https://qiita.com/nsuhara/items/86570f789093222252b1
page_views_count=00307, likes_count=00, title=Raspberry PiとPythonでLCD(16x2)ゲームを作成する, url=https://qiita.com/nsuhara/items/57105fd232feffbcd05c
page_views_count=00140, likes_count=00, title=CSVデータをPostgreSQLに一括挿入する方法, url=https://qiita.com/nsuhara/items/a1b75e0557ed134c5302

items_count=28, total_page_views_count=55690, total_likes_count=125
```

### 実行環境

| 環境           | Ver.    |
| :------------- | :------ |
| macOS Catalina | 10.15.6 |
| Python         | 3.7.3   |
| requests       | 2.24.0  |

### ソースコード

実際に実装内容やソースコードを追いながら読むとより理解が深まるかと思います。是非ご活用ください。

[GitHub](https://github.com/nsuhara/python-qiita-api.git)

### 関連する記事

- [Qiita API v2ドキュメント](https://qiita.com/api/v2/docs)

## 注意事項(苦戦した点)

### 記事のアクセス数(page_views_count)

APIの制約で`記事を一括で取得`、または`他者の記事を取得`した場合は、アクセス数(page_views_count)が`null`になる様です。対策として、Step1:記事のIDを一括で取得する、Step2:IDを使って1件ずつ記事のアクセス数を取得する、の2段階の手順で実現しました。(API利用制限があるため、記事の件数が増える(=リクエスト数が増える)と制限に引っ掛かる可能性があります)

### API利用制限

認証している状態ではユーザごとに1時間に1000回まで、認証していない状態ではIPアドレスごとに1時間に60回までリクエストを受け付けます。

## アクセストークン

### 個人用アクセストークン設定

設定 > アプリケーション > 新しくトークンを発行する > `read_qiita`にチェック > 発行する

`※ 発行した個人用アクセストークンを保存してください。この文字列は再表示できません。`

## コンフィグ

```config.sh
export PYTHONPATH=app/
export QIITA_ACCESS_TOKEN={上記で登録したアクセストークン}
export QIITA_PAGE=1
export QIITA_PER_PAGE=100
export QIITA_URL_ITEM=qiita.com/api/v2/items
export QIITA_URL_LIST=qiita.com/api/v2/authenticated_user/items
```

## メイン

```main.py
"""app/main.py
"""

import os

import requests


def get(url):
    """get
    """
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer {}'.format(os.getenv('QIITA_ACCESS_TOKEN'))
    }
    res = requests.get(url=url, headers=headers)
    print('{}, {}'.format(res.status_code, res.url))
    return res


def get_id_list():
    """get_list
    """
    res = get(url='https://{url}?page={page}&per_page={per_page}'.format(**{
        'url': os.getenv('QIITA_URL_LIST'),
        'page': os.getenv('QIITA_PAGE'),
        'per_page': os.getenv('QIITA_PER_PAGE')
    }))
    return [item.get('id') for item in res.json()]


def get_item(qiita_id):
    """get_item
    """
    res = get(url='https://{url}/{id}'.format(**{
        'url': os.getenv('QIITA_URL_ITEM'),
        'id': qiita_id
    }))
    item = res.json()
    return {
        'page_views_count': item.get('page_views_count'),
        'likes_count': item.get('likes_count'),
        'title': item.get('title'),
        'url': item.get('url')
    }


def output(items):
    """output
    """
    total_page_views_count = 0
    total_likes_count = 0

    print('-'*100)

    for item in items:
        total_page_views_count = total_page_views_count + \
            item.get('page_views_count')
        total_likes_count = total_likes_count+item.get('likes_count')

        print('page_views_count={}, likes_count={}, title={}, url={}'.format(
            str(item.get('page_views_count')).zfill(5),
            str(item.get('likes_count')).zfill(2),
            item.get('title'),
            item.get('url'))
        )

    print('\nitems_count={}, total_page_views_count={}, total_likes_count={}'.format(
        len(items), total_page_views_count, total_likes_count))

    print('-'*100)


def main():
    """main
    """
    items = list()

    for qiita_id in get_id_list():
        items.append(get_item(qiita_id=qiita_id))

    sorted_items = sorted(
        items, key=lambda x: x['page_views_count'], reverse=True)

    output(items=sorted_items)


if __name__ == '__main__':
    main()
```

## 実行例

```sample.sh
~$ git clone https://github.com/nsuhara/python-qiita-api.git -b master
~$ cd python-qiita-api

~$ python -m venv .venv
~$ source .venv/bin/activate
~$ pip install -r requirements.txt
~$ source config

~$ python app/main.py
```
