import discord
import asyncio
import random
import os
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('jungsanfile-e5ae2dbc8879.json', scope)
client = gspread.authorize(creds)
doc = client.open_by_url('https://docs.google.com/spreadsheets/d/1hL4uvq2On11zp-_JWoWMG0Gyyuty5Lhvp_gQkfTYsOI/edit#gid=516445068')

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
    
          
	if message.content.startswith('!동판'):
		SearchID = message.content[len('!재고')+1:]
		sheet1.update_acell('A1', SearchID)
		result = sheet1.acell('B1').value
            
		embed = discord.Embed(
			title = ' :globe_with_meridians:  ' + SearchID + ' 안내 ',
			description= '```' + SearchID + '  이번달 정책입니다. ' + result + ' ```',
			color=0x00ffff
			)
		await client.send_message(message.channel, embed=embed)
            

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
