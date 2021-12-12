def get_server_info(json_data):
	print("Server Status: " + json_data["data"]["serverStatus"])
	print("Server Time: " + json_data["data"]["serverTime"])

def get_next_occurences(json_data):
	next_occurances = json_data["data"]["nextOccurences"]
	print("Next Occurences")
	print("Guild Siege: " + next_occurances["guildSiege"])
	print("Capture the Flag: " + next_occurances["captureTheFlag"])
	print("Team Deathmatch: " + next_occurances["teamDeathmatch"])
	print("Dodge the Attack: " + next_occurances["dodgeTheAttack"])
	print("Monster Invasion: " + next_occurances["monsterInvasion"])
	print("Dungeon Energy: " + next_occurances["dungeonEnergy"])
	print("Daily Mission: " + next_occurances["dailyMission"])
	print("Weekly Mission: " + next_occurances["weeklyMission"])
