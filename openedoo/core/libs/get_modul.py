import urllib2
import json
import random
import base64
import os
from git import Repo
import git

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'moduls')

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
		if 'module_' in cek_modul:
			modul_url = modul['contents_url']
			modul_url_original = modul_url.replace("{+path}", "")
			modul_url_requirement = modul_url.replace("{+path}", "requirement.json")
			modul_name = modul['name']
			modul_git = modul['clone_url']
			modul_list = {'name':modul_name,'url':modul_url_original,\
			'url_requirement':modul_url_requirement,\
			'url_git':modul_git}
			list_all.append(modul_list)
		else:
			pass
	return list_all
def check_modul_requirement(url=None):
	if url is None:
		return "your field is null"
	response = get_url(url)
	content = response['content']
	data = base64.b64decode(content)
	data = json.loads(data)
	return data


def find_modul(modul_name=None):
	if modul_name is None:
		return "your field is null"
	data = check_modul_available()
	number_akhir = len(data)
	number_awal = 0
	output = None

	for number_awal in xrange(number_awal,number_akhir):
		jumlah = (number_awal+1)-1
		if modul_name == data[jumlah]['name']:
			try:
				get_url_requirement = check_modul_requirement(data[jumlah]['url_requirement'])
			except Exception as e:
				return e
			output = {'url':data[jumlah]['url'],'url_requirement':data[jumlah]['url_requirement'],\
			'url_git':data[jumlah]['url_git'],'name':data[jumlah]['name'],'requirement':get_url_requirement,\
			'requirement':get_url_requirement}
			return output
		else:
			pass
	return output

def install_git_(url=None):
	os.chdir('modules/')
	if url == None:
		return "your url is None"
	try:
		git.Git().clone(url)
		message = {'message':'your modul had installed'}
		os.chdir('..')
	except Exception:
		message = {"message":"install failed"}
		os.chdir('..')
	return message
def install_git(url=None,directory=None,name_modul=None):
	directory = 'modules/{}'.format(name_modul)
	if url == None:
		return "your url is None"
	if name_modul == None:
		return "please input your modul"
	try:
		Repo.clone_from(url,directory)
		message = {'message':'your modul had installed'}
	except Exception:
		message = {"message":"install failed"}
	return message
def add_manifest(name_module=None,version_modul=None,url=None):
	if name_module == None :
		return "please insert your name_module"
	if version_modul == None :
		version = "0.1.0"
	if url == None:
		url = ""
	try:
		filename = 'manifest.json'
		with open(filename,'r') as data_file:
			data_json = json.loads(data_file.read())
		os.remove(filename)
		new_data={'name_module':name_module,'version_module':version_modul,'url_module':url}
		data_json['installed_module'].append(new_data)
		with open(filename,'w') as data_file:
			json.dump(data_json, data_file)
	except Exception as e:
		return e
def del_manifest(name_module=None):
	filename = 'manifest.json'
	if name_module == None:
		return "please insert your modul name"
	with open(filename,'r') as data_file:
		data_json = json.loads(data_file.read())
	number_akhir = len(data_json['installed_module'])
	number_awal = 0
	for number_awal in xrange(number_awal,number_akhir):
		jumlah = (number_awal+1)-1
		if name_module == data_json['installed_module'][jumlah]['name_module']:
			os.remove(filename)
			del data_json['installed_module'][jumlah]
			with open(filename,'w') as data_file:
				json.dump(data_json, data_file)
		else:
			pass
	return "modul has deleted"

def create_requirement(name_module=None,version_module=None,url_endpoint=None,requirement=None,comment=None,url=None):
	if comment is None:
		comment = "my module name is {name}".format(name=name_module)
	if requirement is None:
		requirement = "openedoo_core"
	if name_module==None:
		return "please insert name module"
	if version_module is None:
		version_module = "0.1.0"
	if url_endpoint is None:
		url_endpoint = {'url_endpoint':''.format(url=name_module),'type':'function'}
	else:
		url_endpoint = {'url_endpoint':url_endpoint,'type':'end_point'}
	data_json = {"name":name_module,
	"version": version_module,
	"requirement":requirement,
	"pip_library":[],
	"comment":comment,
	"type":url_endpoint['type'],
	"url":url,
	"url_endpoint":url_endpoint['url_endpoint']}
	filename = 'requirement.json'
	with open('modules/{folder}/{filename}'.format(folder=name_module,filename=filename),'w') as data_file:
		json.dump(data_json, data_file)
	return "module has created"

def check_update_official():
	filename = 'manifest.json'
	with open(filename,'r') as data_file:
		data_json = json.loads(data_file.read())
	#return data_json
	number_akhir = len(data_json['installed_module'])
	number_awal = 0
	for number_awal in xrange(number_awal,number_akhir):
		jumlah = (number_awal+1)-1
		name_installed = data_json['installed_module'][jumlah]
		data_git = find_modul(name_installed['name'])
		if StrictVersion(name_installed['version']) < StrictVersion(data_git['requirement']['version']):
			print "{name} update available {version}".format(name=name_installed['name'],version=data_git['requirement']['version'])
