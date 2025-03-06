def traços():
    print('\033[1;31m-\033[m'*40)

def cabeçalho(msg):
    traços()
    print(f'\033[1;31m{msg:^40}\033[m')
    traços()

