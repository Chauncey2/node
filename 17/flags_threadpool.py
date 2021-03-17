from concurrent import futures
from flags import save_flags, get_flags, show, main

MAX_WORKERS = 30


def download_one(cc):
    image = get_flags(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


if __name__ == '__main__':
    '''
    运行结果：
    FRCNBDIDVNINUSPHBREGETNGJPRUDEMXIRTRCDPK
    20 flags downloaded in 22.70s
    '''
    main(download_many)
