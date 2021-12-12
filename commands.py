def get_server_info(json_data):
	output = ""
	output += "Server Status: " + json_data["data"]["serverStatus"] + '\n'
	output += "Server Time: " + json_data["data"]["serverTime"] + '\n'
	return output

def get_next_occurences(json_data):
	next_occurances = json_data["data"]["nextOccurences"]
	output = ""
	output += "Next Occurences"
	output += "Guild Siege: " + next_occurances["guildSiege"]
	output += "Capture the Flag: " + next_occurances["captureTheFlag"]
	output += "Team Deathmatch: " + next_occurances["teamDeathmatch"]
	output += "Dodge the Attack: " + next_occurances["dodgeTheAttack"]
	output += "Monster Invasion: " + next_occurances["monsterInvasion"]
	output += "Dungeon Energy: " + next_occurances["dungeonEnergy"]
	output += "Daily Mission: " + next_occurances["dailyMission"]
	output += "Weekly Mission: " + next_occurances["weeklyMission"]
	return output