import discord
import codecs
import datetime

token = 'NjE5Mzc4NTk0NTE0NDY4ODY0.XYS8uA.AIojH356O2V0AEmKHGa3co9dU7Y'
f = codecs.open('database.txt', 'r', 'utf-8').readlines()
color = 0x888888
commands = {}
url = 'https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/%s/%s.webp'

for i in range(len(f)):
    f[i] = f[i].split()
    f[i][1] = f[i][1].split(';')
    f[i][1].insert(0,f[i][1][0].capitalize())
    f[i][1][8] = [int(f[i][1][8]) * '■' + (3 - int(f[i][1][8])) * '□', (4 - int(f[i][1][8])) * '■' + (4 - int(f[i][1][8])) * '□']
    print(f[i])
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
            print(code)
            # embed = discord.Embed(title='%s %s'%(code[0], code[1]), description='소속: %s\n생일: %s\n나이: %s\n출생지: %s\n팀: %s\n방어구 %s\n속도 %s'%(code[2], code[3], code[4], code[5], code[6], code[7], code[8])), color=color)
            # embed.set_thumbnail(url=url%('profiles', code[0].lower()))
            # embed.set_image(url=url%('portrait', code[0].lower))
            # now = datetime.datetime.now()
            # embed.set_footer(text = '%s년 %s월 %s일 %s %s:%s'%(now.year, now.month, now.day, '오전' if now.hour < 13 else '오후', now.hour if now.hour < 13 else now.hour - 12, now.minute))
            # await message.channel.send(embed=embed)

client = MyClient()
client.run(token)