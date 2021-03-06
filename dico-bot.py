import discord
import os

class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("멈춰 대기")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("READY")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        
        if message.content == ('멈멈아'):
            channel = message.channel
            msg = "왜 불렁~"
            await channel.send(msg)
            return None
        if message.content[-3:] == "멈춰!":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = message.content + "\n:raised_hand:"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content.startswith('뭐야') and message.content[-2:] == ('줘요'):
            channel = message.channel
            msg = "이래서 눈치빠른 놈들은 싫다니까"
            await channel.send(msg)
            return None
        if message.content.startswith('미안하다'):
            channel = message.channel
            msg = "이거 보여주려고 어그로 끌었다"
            await channel.send(msg)
            return None
        if message.content == ('엄'):
            channel = message.channel
            msg = "준"
            await channel.send(msg)
            return None
        if message.content == ('알분의 와이'):
            channel = message.channel
            msg = "사인함수 ~\n알분의 엑스  코사인 함수 ~"
            await channel.send(msg)
            return None
        if message.content.startswith('이야..'):
            channel = message.channel
            msg = "그죠..?"
            await channel.send(msg)
            return None
            
# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run(os.environ['token'])
