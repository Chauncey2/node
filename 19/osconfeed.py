"""
下载数据源的脚本
"""

from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = './data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON,'r') as fp:
        return json.loads(fp.read())


if __name__ == '__main__':
    feed = load()
