import urllib.request, json, os

class SteamManager():
	STEAM_API_URL = "http://api.steampowered.com/ISteamApps/UpToDateCheck/v1/?key={}&appid={}&version={}"

	def __init__(self, apiKey, appId, versionFile, version=0):
		self.versionFile = versionFile
		self.version = version
		self.apiKey = apiKey
		self.appId = appId

	def CheckVersion(self):
		json = self.GetAPIPage()
		if(json['success']):
			if(json['up_to_date']):
				print("Up to date, exiting")
				self.version = json["required_version"]
				self.WriteServerVersion()
				return self.version
			else:
				return False
		else:
			return None

	def InitAPIUrl(self):
		return self.STEAM_API_URL.format(self.apiKey, self.appId, self.version)

	def GetServerVersion(self):
		if(os.path.isfile(self.versionFile)):
			with open(self.versionFile) as f:
				self.version = str(f.read())
				return self.version

	def WriteServerVersion(self):
		with open(self.versionFile, "w") as f:
			f.write(str(self.version))

	def GetAPIPage(self):
		with urllib.request.urlopen(self.InitAPIUrl()) as resp:
			data = resp.read()
			encoding = resp.info().get_content_charset('utf-8')
			return json.loads(data.decode(encoding))['response']

	def CheckStatus(self):
		json = self.GetAPIPage()
		if(json['success']):
			if(json['up_to_date']):
				return self.version
			else:
				self.version = json["required_version"]
				self.WriteServerVersion()
				return False
		else:
			return None
