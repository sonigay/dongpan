import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('dongpan-699a93059b16.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI')

sheet1 = doc.worksheet('동판출력')


client = discord.Client()


@client.event
async def on_ready():
	print("login")
	print(client.user.name)
	print(client.user.id)
	print("----------------")
	await client.change_presence(game=discord.Game(name='동판정책 안내', type=1))




@client.event
async def on_message(message):
	global gc #정산
	global creds	#정산
    
          
	if message.content.startswith('!동판'):
		SearchID = message.content[len('!동판')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('정책표').worksheet('동판출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
            
		embed = discord.Embed(
			title = ' :globe_with_meridians:  ' + SearchID + ' 안내 ',
			description= '```' + SearchID + '  오늘 정책입니다. ' + result + ' ```',
			color=0x00ffff
			)
		await client.send_message(message.channel, embed=embed)
		
		
		
	if message.content.startswith('!공짜폰'):
		SearchID = message.content[len('!공짜폰')+1:]
		gc = gspread.authorize(creds)
		wks = gc.open('정책표').worksheet('무선공짜출력')
		wks.update_acell('A1', SearchID)
		result = wks.acell('B1').value
		
		embed = discord.Embed(
			title = ' 오늘의  ' + SearchID + ' 공짜폰 안내 ',
			description= '```' + SearchID + '  정책입니다. ' + result + ' ```',
			color=0x4BAF4B
			)
		await client.send_message(message.channel, embed=embed)
		
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
