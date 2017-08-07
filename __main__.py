import sys, os, json
import SteamUtil, ServiceUtil

class AutoUpdater():
	def __init__(self, config):
		self.APP_ID = config["app_id"]
		self.VERSION_FILE = config["version_file"]
		self.STEAM_API_KEY = config["steam_api_key"]
		self.STEAM_DIR = config["steamcmd_location"]
		self.STEAMCMD_EXE = config["steamcmd_exe"]

		self.GAME_DIR = config["game_dir"]
		self.GAME_PROCESS_NAME = config["process_name"]
		self.GAME_EXE = config["game_exe"]
		self.GAME_NAME = config["game_name"]

		self.CreateSteamManager()

	def CreateSteamManager(self):
		self.steam = SteamUtil.SteamManager(self.STEAM_API_KEY, self.APP_ID, self.GAME_DIR + self.VERSION_FILE)
		
	def GetGameServerVersion(self):
		v = self.steam.GetServerVersion()
		if(v):
			printStr = "Detected version {}"
		else:
			v = 0
			printStr = "Error detecting version, using {}"
		print(printStr.format(v))

	def CheckGameServerVersion(self):
			print("Getting latest version of {}...".format(self.GAME_NAME))
			v = self.steam.CheckStatus()
			if(v):
				print("Up to date")
				return False
			elif(v == False):
				print("Game not up to date")
				return True
			else:
				print("Error contacting steam api server")
				return None

	def KillGameServer(self):
		print("Checking for instances of {}...".format(self.GAME_PROCESS_NAME))
		p = ServiceUtil.ProcessUtil.GetProcessByName(self.GAME_PROCESS_NAME)
		if(p):
			print("Process found with id {}, killing...".format(str(p.pid)))
			ServiceUtil.ProcessUtil.KillProcess(p.pid)
			print("Done")
		else:
			print("None found")

	def UpdateGameServer(self):
		print("Starting steamcmd to check for updates...")
		p = ServiceUtil.ProcessUtil.RunProcess(self.STEAM_DIR, self.STEAMCMD_EXE, True)
		print("Done")

	def StartGameServer(self):
		print("Starting {}...".format(self.GAME_NAME))
		p = ServiceUtil.ProcessUtil.RunProcess(self.GAME_DIR, self.GAME_EXE)
		print("Done")

	def CheckGame(self):
		print("Checking {}...".format(self.GAME_NAME))
		self.GetGameServerVersion()
		# if(self.CheckGameServerVersion()):
		# 	self.KillGameServer()
		# 	self.UpdateGameServer()
		# 	self.StartGameServer()
		print("Done checking {} for updates\n\n".format(self.GAME_NAME))


def GetConfig():
	print("Reading in config file...")
	dir = os.path.dirname(os.path.realpath(sys.argv[0]))
	with open(dir + "\\config.json") as f:
		print("Done\n")
		return json.load(f)

if __name__ == "__main__":
	config = GetConfig()

	for game in config["Games"]:
		if "stream_api_key" not in game:
			game["steam_api_key"] = config["steam_api_key"]
		if "version_file" not in game:
			game["version_file"] = config["version_file"]
		if "steamcmd_location" not in game:
			game["steamcmd_location"] = config["steamcmd_location"]

		a = AutoUpdater(game)
		a.CheckGame()