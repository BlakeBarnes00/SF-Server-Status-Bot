def get_server_info(json_data):
	output = ""
	output += "Server Status: " + json_data["data"]["serverStatus"] + '\n'
	output += "Server Time: " + json_data["data"]["serverTime"] + '\n'
	return output

def get_next_occurences(json_data):
	next_occurances = json_data["data"]["nextOccurences"]
	output = ""
	output += "Next Occurences" + '\n'
	output += "Guild Siege: " + next_occurances["guildSiege"] + '\n'
	output += "Capture the Flag: " + next_occurances["captureTheFlag"] + '\n'
	output += "Team Deathmatch: " + next_occurances["teamDeathmatch"] + '\n'
	output += "Dodge the Attack: " + next_occurances["dodgeTheAttack"] + '\n'
	output += "Monster Invasion: " + next_occurances["monsterInvasion"] + '\n'
	output += "Dungeon Energy: " + next_occurances["dungeonEnergy"] + '\n'
	output += "Daily Mission: " + next_occurances["dailyMission"] + '\n'
	output += "Weekly Mission: " + next_occurances["weeklyMission"] + '\n'
	return output