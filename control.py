import codecs

profileText = '**%s %s**\n[아이콘 사진]\n```[프로필 사진]\n이름:%s\n소속:%s\n생일:%s\n나이:%s\n출생지:%s\n\n역할:%s\n방어구_%s\n속도_%s```'
f = codecs.open('database.txt', 'r', 'utf-8').readlines()
lines = []
data = {}

for i in range(len(f)):
    f[i] = f[i].replace('\n', '')
    f[i] = f[i].split()
    if(f[i][1] == '^'):
        f[i][1] = f[i-1][1]
    else:
        f[i][1] = f[i][1].split(';')
        print(f[i][1])
        j = int(f[i][1][7])
        x = '■' * j + '□' * (3 - j)
        y = '■' * (4 - j) + '□' * (i - j)
        f[i][1] = profileText%(f[i][0].capitalize(), f[i][1][0], f[i][1][1], f[i][1][2], f[i][1][3], f[i][1][4], f[i][1][5], f[i][1][6], x, y)
    data[f[i][0]] = f[i][1]
    data[f[i][1][0]] = f[i][1]