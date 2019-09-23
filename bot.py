import discord
import codecs
import datetime

token = 'NjE5Mzc4NTk0NTE0NDY4ODY0.XYjJxA.Dpn-9DxEVgycN07Z3UuR6XC8iuw'
f = codecs.open('database.txt', 'r', 'utf-8').readlines()
color = 0x888888
commands = {}
url = 'https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/%s/%s.webp'

for i in range(len(f)):
    f[i] = f[i].split()
    f[i][1] = f[i][1].replace('_', ' ')
    f[i][1] = f[i][1].split(';')
    f[i][1].insert(0, f[i][0].capitalize())
    f[i][1][8] = [int(f[i][1][8]) * '■' + (3 - int(f[i][1][8])) *
                  '□', (4 - int(f[i][1][8])) * '■' + (-1 + int(f[i][1][8])) * '□']
    commands[f[i][0]] = f[i][1]
    commands[f[i][1][1]] = f[i][1]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Log in completed')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!') and message.content[1:] in commands:
            code = commands[message.content[1:]]
            ms1 = discord.Embed(title='%s %s' % (code[0], code[1]), description='%s\n\n이름 : %s\n생일 : %s\n나이 : %s\n출생 : %s\n\n소속: %s팀\n방어 %s\n속도 %s' % (
                code[3], code[2], code[4], code[5], code[6], code[7], code[8][0], code[8][1]), color=color)
            ms1.set_thumbnail(url=url % ('profiles', code[0].lower()))
            ms1.set_image(url=url % ('portrait', code[0].lower()))
            ms2 = discord.Embed(title='특수 능력\n%s %s' % (
                code[9], code[10]), description='추가바람~~', color=color)
            ms2.set_thumbnail(url=url % ('skill_icon', code[0].lower()))
            ms2.set_image(url=url % ('skill', code[0].lower()))
            now = datetime.datetime.now()
            ms2.set_footer(text='%s년 %s월 %s일 %s %s:%s' % (now.year, now.month, now.day, '오전' if now.hour <
                                                          13 else '오후', now.hour if now.hour < 13 else now.hour - 12, now.minute))
            await message.channel.send(embed=ms1)
            await message.channel.send(embed=ms2)


client = MyClient()
client.run(token)
