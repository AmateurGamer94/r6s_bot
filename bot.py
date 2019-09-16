import discord
import datetime

token = 'NjE5Mzc4NTk0NTE0NDY4ODY0.XXJqHw.ar9RgG5r59SgxrsUr9-YSiWFsic'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!'):
            now = datetime.datetime.now()
            for i in range(3):
                embed = discord.Embed(title="이거슨 제목이라 합니다!", description="sadfasfasdfdasfd\nasdfasfasdfadsf\nasdfafsd", color=0x888888)
                embed.set_thumbnail(url='D:/Discord/profiles/dokkaebi.webp')
                embed.set_image(url='https://i.imgur.com/xzPCXp8.jpg')
                embed.set_author(name='hehe')
                if i == 2: embed.set_footer(text = '%s년 %s월 %s일 %s %s:%s'%(now.year, now.month, now.day, '오전' if now.hour < 13 else '오후', now.hour if now.hour < 13 else now.hour - 12, now.minute))
                await message.channel.send(embed=embed)

client = MyClient()
client.run(token)