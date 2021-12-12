# Get the token for the bot
def get_token():
	with open("token") as f:
		return f.readline()
