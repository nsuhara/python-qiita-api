"""app/main.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/8/28
python version  : 3.7.3
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
