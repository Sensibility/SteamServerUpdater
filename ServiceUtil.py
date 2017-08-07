import psutil, os, subprocess

class ProcessUtil():
	@staticmethod
	def GetProcessByName(name):
		for n in psutil.pids():
			p = psutil.Process(n)
			if(p.name() == name):
				return p
		
	@staticmethod
	def KillProcess(id):
		try:
			p.terminate()
			return True
		except:
			print("Could not terminate {}".format(str(n)))
			sys.exit(1)

	@staticmethod
	def RunProcess(dir, exe, wait=False):
		try:
			os.chdir(dir)
			if not wait:
				return subprocess.Popen(exe)
			else:
				return subprocess.run(exe, shell=True, stdout=subprocess.PIPE)
		except Exception as e:
			print(str(e))