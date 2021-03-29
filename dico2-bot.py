import discord
import random
import os

#https://discord.com/developers/applications

포브스 = ['가장 집가고 싶은 상태 1위', '졸려죽을것 같은 상황 1위', '이 딸이에요', '가장 듣기싫은 수업 1위' ]

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
        if message.content.startswith("&&"):
            channel = message.channel
            msg = message.content[2:]
            await channel.send(msg)
            return None
        if message.content == ('무야호!'):
            channel = message.channel
            msg = "그만큼 신나시는 거지~!"
            await channel.send(msg)
            return None
        if message.content[-3:] == "멈춰!":
            channel = message.channel
            msg = message.content + "\n:raised_hand:"
            await channel.send(msg)
            return None
        if message.content == ('포브스 선정'):
            channel = message.channel
            msg = random.choice(포브스)
            await channel.send(msg)
            return None
        if message.content[-3:] == ('던가!'):
            channel = message.channel
            msg = "속이 뻥 (울컥울컥)"
            await channel.send(msg)
        if message.content[-5:] == ('뭐냐면..'):
            channel = message.channel
            msg = "네~ 알려드렸습니다~"
            await channel.send(msg)
            return None
        if message.content == ('!도움'):
            channel = message.channel
            msg = "밈밈아\n무야호!\n~멈춰!\n미안하다\n포브스 선정\n알분의 와이\n이야..~\n~던가!\n뭐야~줘요\n미안하다\n엄\n~뭐냐면.."
            await channel.send(msg)
            return None
        # if message.content == ('r 분의 y'):
        #     channel = message.channel
        #     msg = "사인함수~ r 분의 x 코사인 함수~"
        #     await channel.send(msg)
        #     return None
        # if message.content.startswith('이야..'):
        #     channel = message.channel
        #     msg = "그죠..?"
        #     await channel.send(msg)
        #     return None
        #     return None
        # if message.content.startswith('뭐야') and message.content[-3:] == ('줘요'):
        #     channel = message.channel
        #     msg = "이래서 눈치빠른 놈들은 싫다니까"
        #     await channel.send(msg)
        #     return None
        # if message.content.startswith('미안하다'):
        #     channel = message.channel
        #     msg = "이거 보여주려고 어그로 끌었다"
        #     await channel.send(msg)
        #     return None
        # if message.content == ('엄'):
        #     channel = message.channel
        #     msg = "준"
        #     await channel.send(msg)
        #     return None
if __name__ == "__main__":
    client = chatbot()
    client.run(os.environ["token2"])