# discord 라이브러리 사용 선언
import discord
import random
#https://discord.com/developers/applications

포브스 = ['가장 집가고 싶은 상태 1위', '졸려죽을것 같은 상황 1위', '이 딸이에요', '가장 듣기싫은 수업 1위', '가장 집가고 싶은 상태 1위' ]
class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("새로운 밈 연구")

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
        
        # message.content = message의 내용
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
        if message.content == ('멈춰!'):
            channel = message.channel
            msg = "멈춰!"
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
        if message.content == ('속이 뻥'):
            channel = message.channel
            msg = "울컥울컥"
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


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("ODI0MDExNjkxNDc3MDQxMTUz.YFpKsA.Ezg8ZpVUNVAuHFhsL7FqoynEZ08")