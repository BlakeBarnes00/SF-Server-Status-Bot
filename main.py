import discord, asyncio
from discord import channel
from discord import client

import requests, json
from commands import *

TOKEN = "" 
with open("token.txt") as f:
	TOKEN = f.readline()


class Client(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create the background task and run it
		self.bg_task = self.loop.create_task(self.print_info())

	# Prints into console on start
	async def on_ready(self):
		print("Logged in as")
		print(self.user.name)
		print(self.user.id)
		print("----------------")
	
	# Prints the info
	async def print_info(self):
		await self.wait_until_ready()
		counter = 0
		channel = self.get_channel(919390138868584489)
		while not self.is_closed():
			counter += 1
			await channel.send(get_server_info(content) + '\n' + get_next_occurences(content))
			await asyncio.sleep(60*5) # runs every 5 minutes

req = requests.get(url="https://stellarflyff.com/server-status")
content = json.loads(req.content) # the json content from the website


client = Client()
client.run(TOKEN)