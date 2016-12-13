import urllib2
import json
import random
import base64

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

def get_url(url="https://api.github.com/orgs/openedoo/repos"):
	try:
		response = urllib2.Request(url,headers={'User-Agent' : "Magic Browser"})
		read = urllib2.urlopen(response).read()
		data = json.loads(read)
		return data
	except Exception as e:
		raise e

def check_modul_available(url="https://api.github.com/orgs/openedoo/repos"):
	data = get_url(url)
	number_git = len(data)
	number_awal = 0
	list_all = []
	for number_awal in xrange(number_awal,number_git):
		jumlah = (number_awal+1)-1
		modul = data[jumlah]
		cek_modul = data[jumlah]['name']
		if 'modul_' in cek_modul:
			modul_url = modul['contents_url']
			modul_url_original = modul_url.replace("{+path}", "")
			modul_url_requirement = modul_url.replace("{+path}", "requirement.json")
			modul_name = modul['name']
			modul_list = {'name':modul_name,'url':modul_url_original,'url_requirement':modul_url_requirement}
			list_all.append(modul_list)
		else:
			pass
	return list_all
def check_modul_requirement(url=None):
	if url is None:
		return "your field is null"
	try:
		response = get_url(url)
		content = response['content']
		data = base64.b64decode(content)
		data = json.loads(data)
		return data
	except Exception as e:
		return e

def find_modul(modul_name=None):
	if modul_name is None:
		return "your field is null"
	data = check_modul_available()
	number_akhir = len(data)
	number_awal = 0
	output = {'message':'modul not found'}
	for number_awal in xrange(number_awal,number_akhir):
		jumlah = (number_awal+1)-1
		if modul_name in data[jumlah]['name']:
			output = {'url':data[jumlah]['url'],'url_requirement':data[jumlah]['url_requirement']}
			return output
		else:
			pass
	return output

def install_git(url=None,directory=None,name_modul=None):
	if url == None:
		return "your url is None"
	if name_modul == None:
		return "please input your modul"
	if directory is None:
		directory = ("{base_dir}/openedoo".format(base_dir=BASE))
	Repo.clone_from(url,directory)
	message = {'message':'your modul had installed'}
	return message