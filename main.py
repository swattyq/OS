import hashlib
import datetime
import multiprocessing
import itertools


def f(x):
    x = ''.join(x)
    return (x, hashlib.sha256(x.encode('cp1251')).hexdigest())


if __name__ == '__main__':
    count_treads = int(input('Введите количество потоков:'))
    # Считываем все ключи из файла
    with open('pass.txt') as fl:
        passwords = fl.readlines()
    # Для каждого ключа ищем пароль
    for ps in passwords:
        print(datetime.datetime.now())
        ps = ps.strip().lower()
        if len(ps) == 0:
            continue
        with multiprocessing.Pool(count_treads) as pool:
            for s, _ in filter(lambda x: x[1] == ps, pool.imap_unordered(f, itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=5), chunksize=1000)):
                print(s)
    print(datetime.datetime.now())
