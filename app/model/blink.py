from tools import setredis
import time

data1 = {"gpio":{"gpio1":"1"},"tutorial":{"1":"on","0":"off"},"reset_time":"10"}
data2 = {"gpio":{"gpio1":"0"},"tutorial":{"1":"on","0":"off"},"reset_time":"10"}

def blink():
	setredis("blink",data1,11)
	time.sleep(10)
	setredis("blink",data2,11)
	time.sleep(10)
	print "loop"
	blink()
	return True

blink()