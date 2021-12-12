import requests, json

url = "https://stellarflyff.com/server-status"

req = requests.get(url)
if req.status_code == 200:
	c = json.loads(req.content)
	print("Server Status: " + c["data"]["serverStatus"])
	print("Server Time: " + c["data"]["serverTime"])

	#print(c["data"]["nextOccurences"])
	
	next_occurances = c["data"]["nextOccurences"]
	print("\nNext Occurences")
	print("Guild Siege: " + next_occurances["guildSiege"])
	print("Capture the Flag: " + next_occurances["captureTheFlag"])
	print("Team Deathmatch: " + next_occurances["teamDeathmatch"])
	print("Dodge the Attack: " + next_occurances["dodgeTheAttack"])
	print("Monster Invasion: " + next_occurances["monsterInvasion"])
	print("Dungeon Energy: " + next_occurances["dungeonEnergy"])
	print("Daily Mission: " + next_occurances["dailyMission"])
	print("Weekly Mission: " + next_occurances["weeklyMission"])

