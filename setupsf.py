import os,sys 	
import time
import glob
import platform

def welcoming():
    print "#########################"
    print "#########WELCOME#########"
    print "#####setup flask mpc#####"
    print "#########################"
def detectfile(filename):
    try:
        #if platform.system() =="Windows":
        daftarpro = glob.glob("app\controller\*.py")
        if any(("app\\controller\\%s.py" % filename ) in s for s in daftarpro):
            return "data ada"
        else:
            return "data tidak ada"
    except Exception:
        print "os tidak dikenali"
def pilihmenu():
    time.sleep(0.0125)
    print "menu :"
    print "1) create simple controller"
    input_var = raw_input("enter menu number : ")
    try:
        input_var = int(input_var)
    except Exception:
        print "must be integer"
    if input_var == 1:
        print ("create your controller")
        time.sleep(0.0125)
        input_name = raw_input("enter controller : ")
        if detectfile(input_name) == "data tidak ada":
	    createcontroller(input_name)
        else:
            time.sleep(0.125)
            print "prefix is exist"
            pilihmenu()
    else:
        print "menu tidak tersedia"
        time.sleep(2)
        pilihmenu()
def createcontroller(name):
    print "your controller name is %s.py" % name
    with open('app/controller/%s.py' % name, 'w') as file:
        file.write('''
from flask import Blueprint, render_template
%(s)s = Blueprint('newbot_%(s)s', __name__)
@%(s)s.route('/')
def newbot():
	return "hello world"
''' % {'s': name})
    with open('app/__init__.py', "a") as file:
        file.write('''
from app.controller.%(s)s import %(s)s
app.register_blueprint(%(s)s, url_prefix='/%(s)s')
'''% {'s': name})
    print "finish it"


welcoming()
pilihmenu()
