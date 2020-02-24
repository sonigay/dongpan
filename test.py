import discord
import asyncio
import random
import os
import datetime
from time import sleep
import arrow
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope1 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #정책시트
scope2 = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #재고시트
creds1 = ServiceAccountCredentials.from_json_keyfile_name('dongpan-699a93059b16.json', scope1) #정책시트
creds2 = ServiceAccountCredentials.from_json_keyfile_name('jumun-8151173be58f.json', scope2) #재고시트
client1 = gspread.authorize(creds1) #정책시트
client2 = gspread.authorize(creds2) #재고시트
doc1 = client1.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI') #정책시트
doc2 = client2.open_by_url('https://docs.google.com/spreadsheets/d/15p6G4jXmHw7Z_iRCYeFwRzkzLxqf-3Pj0c6FeVuFYBM') #재고시트




client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='업무지원', type=1))

@client.event
async def on_member_join(member):
    sleep(1)	
    fmt = '{1.name} 에 오신것을 환영합니다.\n{0.mention} 님!! \n매장이름/직급/성함/연락처 이렇게 남겨주시면 \n확인후 권한을 승인해드리겠습니다. '
    channel = member.server.get_channel("661832869521391646")
    return await client.send_message(channel, fmt.format(member, member.server))


@client.event
async def on_message(message):
    
          
	if message.content.startswith('!동판'):
		SearchID = message.content[len('!동판')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표수정').worksheet('동판출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		embed1 = discord.Embed(
			title = ' :globe_with_meridians:  ' + SearchID + ' 안내 ',
			description= '**```css\n' + SearchID + '  오늘 정책입니다. ' + result + ' ```**',
			color=0x00ffff
			)
		embed2 = discord.Embed(
			title = ' :globe_with_meridians: 동판 ' + SearchID + ' 정책조회!! ',
			description= '```' "출력자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0x00ffff
			)
		await client.send_message(client.get_channel("674653007132229632"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
	if message.content.startswith('!공짜폰'):
		SearchID = message.content[len('!공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표수정').worksheet('무선공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 공짜폰 안내 ',
			description= '**```css\n' + SearchID + '  정책입니다. ' + result + ' ```**',
			color=0x4BAF4B
			)
		embed2 = discord.Embed(
			title = SearchID + ' 공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0x4BAF4B
			)
		await client.send_message(client.get_channel("674652501693300737"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
		
		
	if message.content.startswith('!외국인공짜폰'):
		SearchID = message.content[len('!외국인공짜폰')+1:]
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표수정').worksheet('외국인공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed1 = discord.Embed(
			title = ' 오늘의 ' + SearchID + ' 외국인공짜폰 안내 ',
			description= '**```css\n' + SearchID + '  정책입니다. ' + result + ' ```**',
			color=0xFF848F
			)
		embed2 = discord.Embed(
			title = SearchID + ' 외국인공짜폰 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0xFF848F
			)
		await client.send_message(client.get_channel("674654114592063498"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
		
	if message.content == '!정책표':
		command_list = ''
		command_list += '\n'
		command_list += '📌 공지사항\n'
		command_list += '```diff\n-2020-02-18기준 금일부터\n-방x위 지시사항으로 정책표상에 시간기재가 금지됩니다.\n-정책적용기준은 폰클 상에 작성된 기준시간과\n-"!정책표" 명령시 테이블 상단 적용일시 확인바랍니다.```'
		command_list += '\n'
		command_list += '웹사이트 링크\n'
		command_list += 'https://docs.google.com/spreadsheets/d/1gGOqkMcSau3lXHnP5_UZfEW1rbJOi5czd3w-22QX2j4/pubhtml# \n'     #!링크
		command_list += '\n'
		command_list += '엑셀다운 링크\n'
		command_list += 'https://docs.google.com/spreadsheets/d/1gGOqkMcSau3lXHnP5_UZfEW1rbJOi5czd3w-22QX2j4/pub?output=xlsx \n'     #!링크
		gc1 = gspread.authorize(creds1)
		wks = gc1.open('정책표수정').worksheet('무선구두')
		result = wks.acell('E3').value
		embed1 = discord.Embed(
			title = ':bar_chart: 정책 적용일시: ' + result + '',
			description= command_list,
			color=0xf29886
			)
		embed1.add_field(
			name="❗ 주의사항 ",
			value= '```diff\n-위 엔드정책은 참고용입니다. \n-정산은 폰클 정책표에서 그레이드 합산후 날짜별로 구두추가하시고 \n-맞추셔야하십니다.감사합니다.\n-폰클단가표 보는법은 앞자리 2빼고 뒷두자리 입니다.\n-그레이드확인은 "!그레이드" 로 확인 가능하십니다..```'
			)
		embed2 = discord.Embed(
			title = ':bar_chart: 적용일시: ' + result + ' 출력!',
			description= '```' "출력자:" + message.author.display_name +"\n거래처:" + message.channel.name + '```',
			color=0xf29886
			)
		await client.send_message(client.get_channel("672022974223876096"), embed=embed2)
		await client.send_message(message.channel, embed=embed1)
		
	if message.content.startswith('!그레이드'):
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('오전재고').worksheet('그레이드')
		result = wks.acell('B1').value
		embed1 = discord.Embed(
			title = ' 파트너 그레이드 안내!! ',
			description= '**```css\n' + result + ' ```**',
			color=0x7fffd4
			)
		embed2 = discord.Embed(
			title = ' 파트너 그레이드 조회!! ',
			description= '```' "조회자:" + message.author.display_name +"\n거래처:" + message.channel.name + ' ```',
			color=0x00ffff
			)
		await client.send_message(message.channel, embed=embed1)
		await client.send_message(client.get_channel("674827771817623572"), embed=embed2)
		
	if message.content.startswith('!주문'):
		curruntTime = datetime.datetime.now() + datetime.timedelta(hours = 9)
		krnow = curruntTime.strftime('%Y/%m/%d %H:%M')
		gc2 = gspread.authorize(creds2)
		wks = gc2.open('오전재고').worksheet('재고주문')
		wks.insert_row([krnow, message.channel.name, message.author.display_name, message.content[4:]], 3)
		embed1 = discord.Embed(
			title = message.author.display_name + "님 의 주문 ",
			description= '```fix\n' + message.content[4:] + '```',
			color=0xCBFF75
			)
		embed1.add_field(
			name=" 주문접수 확인... ",
			value= '```diff\n!주문내용이 전달되어 정상적으로\n!접수되었습니다. 부득이한경우\n!개인답변 드리겠습니다.```'
			)
		embed2 = discord.Embed(
			title = message.author.display_name + "님 의 주문내용 ",
			description= '```' + message.content[4:] + '```',
			color=0xCBFF75
			)
		embed2.add_field(
			name=" 주문 접수처... ",
			value= '```' "거래처:"+ message.channel.name +"\n채널아이디:" + message.channel.id + '```'
			)
		await client.send_message(message.channel, embed=embed1)
		await client.send_message(client.get_channel("667343258296254464"), embed=embed2)
		
	if message.content.startswith('!답변'):
		member = discord.utils.get(client.get_all_channels(), id=message.content[4:22])
		neyongdabtotal = message.content[23:]
		neyongdab = neyongdabtotal.split("/")
		neyong = neyongdab[0]
		dab = neyongdab[1]
		
		embed = discord.Embed(
			title = "주문내용",
			description= '```fix\n' + neyong + '```',
			color=0xFF0000
			)
		embed.add_field(
			name = message.author.display_name + "님 답변",
			value= '```Tex\n' + '$' + dab + '```'
			)
		await client.send_message(member, embed=embed)
		

	if message.content.startswith('!공지'):
		if message.author.id == '315237238940106754' :
			embed = discord.Embed(    
				title = "📌 공지사항",
				description= '```' + message.content[4:] + '```',
				color=0xFF0000	
				)
			await client.send_message(client.get_channel("667707237623660569"), embed=embed)
			await client.send_message(client.get_channel("667239441307533312"), embed=embed)
			await client.send_message(client.get_channel("667241204739604490"), embed=embed)
			await client.send_message(client.get_channel("667241430070198273"), embed=embed)
			await client.send_message(client.get_channel("667241481907470336"), embed=embed)
			await client.send_message(client.get_channel("667241531694120970"), embed=embed)
			await client.send_message(client.get_channel("667241582411513856"), embed=embed)
			await client.send_message(client.get_channel("667241378534653983"), embed=embed)
			await client.send_message(client.get_channel("667240616207450122"), embed=embed)
			await client.send_message(client.get_channel("667242915378102293"), embed=embed)
			await client.send_message(client.get_channel("667243361614168088"), embed=embed)
			await client.send_message(client.get_channel("667243407227224064"), embed=embed)
			await client.send_message(client.get_channel("667243524433117218"), embed=embed)
			await client.send_message(client.get_channel("667247020926435344"), embed=embed)
			await client.send_message(client.get_channel("667243630989410304"), embed=embed)
			await client.send_message(client.get_channel("667243696915218432"), embed=embed)
			await client.send_message(client.get_channel("667243782604849155"), embed=embed)
			await client.send_message(client.get_channel("667243837206429696"), embed=embed)
			await client.send_message(client.get_channel("667244790404087808"), embed=embed)
			await client.send_message(client.get_channel("667244947677904898"), embed=embed)
			await client.send_message(client.get_channel("667245023359664142"), embed=embed)
			await client.send_message(client.get_channel("667245114619592765"), embed=embed)
			await client.send_message(client.get_channel("667245155790618625"), embed=embed)
			await client.send_message(client.get_channel("667245231447474176"), embed=embed)
			await client.send_message(client.get_channel("667245522549211138"), embed=embed)
			await client.send_message(client.get_channel("667245576014004256"), embed=embed)
			await client.send_message(client.get_channel("667245650802507777"), embed=embed)
			await client.send_message(client.get_channel("667245748907147275"), embed=embed)
			await client.send_message(client.get_channel("667245819786690560"), embed=embed)
			await client.send_message(client.get_channel("667245916947742760"), embed=embed)
			await client.send_message(client.get_channel("667246076453191690"), embed=embed)
			await client.send_message(client.get_channel("667246146074443807"), embed=embed)
			await client.send_message(client.get_channel("667246234851082240"), embed=embed)
			await client.send_message(client.get_channel("667246316652593163"), embed=embed)
			await client.send_message(client.get_channel("667246366468079626"), embed=embed)
			await client.send_message(client.get_channel("667246430074699777"), embed=embed)
			await client.send_message(client.get_channel("667246487872339968"), embed=embed)
			await client.send_message(client.get_channel("667246552238129153"), embed=embed)
			await client.send_message(client.get_channel("667246600019771472"), embed=embed)
			await client.send_message(client.get_channel("667246718198218772"), embed=embed)
			await client.send_message(client.get_channel("667246834892144640"), embed=embed)
			await client.send_message(client.get_channel("667247069580492820"), embed=embed)
			await client.send_message(client.get_channel("667247107232628736"), embed=embed)
			await client.send_message(client.get_channel("667247142833881108"), embed=embed)
			await client.send_message(client.get_channel("667247180188483584"), embed=embed)
			await client.send_message(client.get_channel("667247225847545866"), embed=embed)
			await client.send_message(client.get_channel("667247261734141962"), embed=embed)
			await client.send_message(client.get_channel("667247287679975446"), embed=embed)
			await client.send_message(client.get_channel("667247313525407755"), embed=embed)
			await client.send_message(client.get_channel("667247368902672404"), embed=embed)
			await client.send_message(client.get_channel("667247397075681299"), embed=embed)
			await client.send_message(client.get_channel("667247433041838100"), embed=embed)
			await client.send_message(client.get_channel("667247472908828676"), embed=embed)
			await client.send_message(client.get_channel("667247519264407552"), embed=embed)
			await client.send_message(client.get_channel("667247545893781524"), embed=embed)
		
		
	if message.content == '!명령어':
		command_list = ''
		command_list += '!명령어\n'     #!명령어
		command_list += '!모델명\n'     #!모델명
		
		embed = discord.Embed(
			title = ":keyboard: 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !그레이드\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 N976 화이트 1대 보내주세요 >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 [구단위]\n---< ex)!재고 남동구 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !동판 동판\n'+'@ !동판 소호신규\n@ !동판 소호기변\n@ !동판 후결합\n@ !동판 재약정\n@ !동판 재약정단독\n@ !동판 단독\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await client.send_message(message.channel, embed=embed)
        
	if message.content == '!영업명령어':
		command_list = ''
		command_list += '!영업명령어\n'     #!명령어        
		command_list += '!모델명\n'     #!모델명
		command_list += '!거래처\n'     #!모델명	
		
		embed = discord.Embed(
			title = "🚗 영업부 기본명령어",
			description= '```fix\n' + command_list + '```',
			color=0xFFD5B4
			)
		embed.add_field(
			name="📈 실적관련 명령어 ",
			value= '```diff\n- !전월실적\n---< 전월 전체실적 >\n+ !전월실적 영업사원이름\n---< ex)!전월실적 홍길동 >\n- !당월실적\n---< 데이터 입력일까지 당월 전체실적 >\n+ !당월실적 영업사원이름\n---< ex)!당월실적 홍길동 >\n\n실적 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="📶 정책관련 명령어 ",
			value= '```diff\n- !정책표\n- !그레이드\n- !비하인드\n---< 비하인드 명령어는 음성지원만 확인가능합니다. >\n+ !단가 모델명 요금제군 유형\n---< ex)!단가 N976 A군 MNP >\n+ !외국인단가 모델명 요금제군 유형\n---< ex)!외국인단가 N976 A군 MNP >\n+ !공짜폰 요금제군 유형\n---< ex)!공짜폰 C군 MNP >\n+ !외국인공짜폰 요금제군 유형\n---< ex)!외국인공짜폰 A군 신규 > ```',
			inline = False
			)
		embed.add_field(
			name="📲 재고관련 명령어 ",
			value= '```diff\n- !주문\n---< ex)!주문 A305 A505 배정부탁드립니다. >\n+ !재고 모델명\n---< ex)!재고 N976 >\n+ !재고 거래처코드\n---< ex)!재고 A34 >\n- !불량\n---< 전체불량현황 >\n+ !불량 거래처코드\n---< ex)!불량 A34 >\n- !유심\n---< 10개 미만 유심현황 >\n+ !유심 전체\n---< 거래처 총 유심현황 >\n+ !퀵비 [동단위/동단위]\n---< ex)!퀵비 논현동/가좌동 >\n\n퀵비 멍령어는 실행은 되지만\n데이터량이 많아 다소 결과가 늦게 나옴 ```',
			inline = False
			)
		embed.add_field(
			name="🌐 동판관련 명령어 ",
			value= '```Cs\n# !동판 동판\n'+'@ !동판 소호신규\n@ !동판 소호기변\n@ !동판 후결합\n@ !동판 재약정\n@ !동판 재약정단독\n@ !동판 단독\n\n\n\n ```',
			inline = True
			)
		embed.add_field(
			name="🎲 기타 명령어 ",
			value= '```diff\n= !영화순위\n= !주사위\n= !복권\n+ !나이 생년-월-일 \n---< ex)!나이 2002-02-01 >\n+ !유지기간 개통일\n---< ex)!유지기간 2020-01-01 >\n+ !사다리 뽑을인원수 인원1 인원2 인원3...\n---< ex)!사다리 2 홍길동 갑돌이 갑순이 >\n+ !타이머 초시간\n---< ex)!타이머 5 >```',
			inline = True
			)
		await client.send_message(message.channel, embed=embed)		
		
		
		
		
		
		
		
		
		


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
