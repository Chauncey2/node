import os
import time
import sys
import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'http://flupy.org/data/flags'

DEST_DIR = 'downloads/'


def save_flags(img, filename):
    """
    以二进制的形式写入图片
    """
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flags(cc):
    # cc 作为参数，调用format函数的时候，
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end='')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flags(cc)
        show(cc)
        save_flags(image, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    """
    运行结果：
    
    BDBRCDCNDEEGETFRIDINIRJPMXNGPHPKRUTRUSVN
    20 flags downloaded in 187.00s
    """
    main(download_many)
