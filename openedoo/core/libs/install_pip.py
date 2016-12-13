import pip

def install(package):
	try:
		print "this is need superuser access"
		pip.main(['install', package])
	except Exception as e:
		raise "please install pip"

# Example
#if __name__ == '__main__':
#	install('nltk')