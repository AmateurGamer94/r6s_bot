import discord
import datetime

token = 'NjE5Mzc4NTk0NTE0NDY4ODY0.XYD0bQ.nYdN1P5mD9uRS3-PW8jRpKfPL_Y'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Log in completed')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('!'):
            now = datetime.datetime.now()
            embed = discord.Embed(title="이거슨 제목이라 합니다!", description="sadfasfasdfdasfd\nasdfasfasdfadsf\nasdfafsd", color=0x888888)
            embed.set_thumbnail(url='https://github.com/AmateurGamer94/r6s_bot/blob/master/profiles/amaru.webp')
            embed.set_image(url='https://i.imgur.com/xzPCXp8.jpg')
            embed.set_footer(text = '%s년 %s월 %s일 %s %s:%s'%(now.year, now.month, now.day, '오전' if now.hour < 13 else '오후', now.hour if now.hour < 13 else now.hour - 12, now.minute))
            await message.channel.send(embed=embed)

client = MyClient()
client.run(token)