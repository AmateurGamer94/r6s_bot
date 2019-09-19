import discord
import codecs
import datetime

token = 'NjE5Mzc4NTk0NTE0NDY4ODY0.XYNLZQ.PznhhekhIAX73z3FQMgumZM7os8'
f = codecs.open('database.txt', 'r', 'utf-8').readlines()
color = 0x888888
commands = {}

for i in range(len(f)):
    f[i] = f[i].split()
    f[i][1] = f[i][1].split(';')
    f[i][1].insert(0,f[i][0].capitalize())
    commands[f[i][0]] = f[i][1]
    commands[f[i][1][1]] = f[i][1]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Log in completed')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!') and commands in message.content[1:]:
            embed = discord.Embed(title='%s %s', description='나이\n생일\n방어구', color=color)
            embed.set_thumbnail(url='https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/profiles/amaru.webp')
            embed.set_image(url='https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/portrait/amaru.webp')
            embed = discord.Embed(title='Amaru 아마루', description='나이\n생일\n방어구', color=color)
            embed.set_thumbnail(url='https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/profiles/amaru.webp')
            embed.set_image(url='https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/portrait/amaru.webp')
            embed = discord.Embed(title='Amaru 아마루', description='나이\n생일\n방어구', color=color)
            embed.set_thumbnail(url='https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/profiles/amaru.webp')
            embed.set_image(url='https://raw.githubusercontent.com/AmateurGamer94/r6s_bot/master/portrait/amaru.webp')
            now = datetime.datetime.now()
            embed.set_footer(text = '%s년 %s월 %s일 %s %s:%s'%(now.year, now.month, now.day, '오전' if now.hour < 13 else '오후', now.hour if now.hour < 13 else now.hour - 12, now.minute))
            await message.channel.send(embed=embed)

client = MyClient()
client.run(token)