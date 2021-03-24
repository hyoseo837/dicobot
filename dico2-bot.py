import discord
import random
import os
#https://discord.com/developers/applications

포브스 = ['가장 집가고 싶은 상태 1위', '졸려죽을것 같은 상황 1위', '이 딸이에요', '가장 듣기싫은 수업 1위', '가장 집가고 싶은 상태 1위' ]


class chatbot(discord.Client):

    async def on_ready(self):
        game = discord.Game("새로운 밈 연구")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")


    async def on_message(self, message):

        if message.author.bot:
            return None
        
        if message.content == ('밈밈아'):
            channel = message.channel
            msg = "왜 불렁~"
            await channel.send(msg)
            return None
        if message.content == ('무야호!'):
            channel = message.channel
            msg = "그만큼 신나시는 거지~!"
            await channel.send(msg)
            return None
        if message.content[-3:] == "멈춰!":
            channel = message.channel
            msg = message.content
            await channel.send(msg)
            return None
        if message.content == ('다들 뭐해?'):
            channel = message.channel
            msg = "전 새로운 밈을 찾아 헤메고 있어요"
            await channel.send(msg)
            return None
        if message.content == ('신재원이 누구야?'):
            channel = message.channel
            msg = "저를 만들어준 분이세요 ^^"
            await channel.send(msg)
            return None
        if message.content == ('집가고 싶다'):
            channel = message.channel
            msg = "아~ 집가고 싶다~~"
            await channel.send(msg)
            return None
        if message.content == ('포브스 선정'):
            channel = message.channel
            msg = random.choice(포브스)
            await channel.send(msg)
            return None
        if message.content == ('r 분의 y'):
            channel = message.channel
            msg = "사인함수~ r 분의 x 코사인 함수~"
            await channel.send(msg)
            return None
        if message.content == ('아오'):
            channel = message.channel
            msg = "일하기 싫어.."
            await channel.send(msg)
            return None
        if message.content.startswith('이야..'):
            channel = message.channel
            msg = "그죠..?"
            await channel.send(msg)
        if message.content[-3:]('던가!'):
            channel = message.channel
            msg = "속이 뻥 (울컥울컥)"
            await channel.send(msg)


if __name__ == "__main__":
    client = chatbot()
    client.run(os.environ["token2"])
    #이거 토큰 바뀜