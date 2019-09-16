import codecs

profileText = '**%s**\n[아이콘 사진]\n```[프로필 사진]\n이름:%s\n소속:%s\n생일:%s\n나이:%s\n출생지:%s\n\n역할:%s\n방어구_%s\n속도_%s```'
f = codecs.open('database.txt', 'r', 'utf-8').readlines()
lines = []
data = {}

def a(i):
    return '■' * i + '□' * (3 - i)

def b(i):
    return '■' * (4 - i) + '□' * (i - 1)

for i in range(len(f)):
    f[i] = f[i].replace('\n', '')
    f[i] = f[i].split()
    if(f[i][1] == '^'):
        f[i][1] = f[i-1][1]
    else:
        array = f[i][1].split(';')
        f[i][1] = profileText%(array[0],array[1],array[2],array[3],array[4],array[5],array[6],array[7],array[8])
    data[f[i][0]] = f[i][1]