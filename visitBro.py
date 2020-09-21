import datetime as dt
import random as rd

def visitBro(zangai_bros):
    print(dt.datetime.now())
    bro = zangai_bros[rd.randrange(len(zangai_bros))]
    print('今天我们一起去给' + bro + '拜年吧！')
    zangai_bros.remove(bro)
    return zangai_bros


zangai_bros = []
while(True):
    ch = input('input v to visit, c to show bros, other to quit.')
    if ch == 'v':
        zangai_bros = visitBro(zangai_bros)
    elif ch == 'c':
        print(zangai_bros)
    else:
        print('拜年结束！')
        break

