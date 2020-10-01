import numpy as np
import os
import sys

from mininet.net import Mininet
import threading
from threading import Thread
import time
from datetime import datetime

h1 = net.get('h1')
h2 = net.get('h2')
h3 = net.get('h3')
h4 = net.get('h4')
h5 = net.get('h5')
h6 = net.get('h6')


stop = False
#latency_log = open("latlog.txt", "a")
h1_log = open("h1.txt", "a")
h2_log = open("h2.txt", "a")
h3_log = open("h3.txt", "a")
h4_log = open("h4.txt", "a")
h5_log = open("h5.txt", "a")
h6_log = open("h6.txt", "a")


def timer():
	global h1_log
	global h2_log
	global h3_log
	global h4_log
	global h5_log
	global h6_log
	global stop
	global threads
	print "TIMER IS DONE"
	stop = True
	h1.cmd("pkill curl | killall curl")
	h2.cmd("pkill curl | killall curl")
	h3.cmd("pkill curl | killall curl")
	h4.cmd("pkill curl | killall curl")
	h5.cmd("pkill curl | killall curl")
	h6.cmd("pkill curl | killall curl")
	os.system("pkill curl")
	h1_log.close()
	h2_log.close()	
	h3_log.close()	
	h4_log.close()	
	h5_log.close()	
	h6_log.close()	
	for pr in threads:
		pr.join()
	sys.exit()
def h1_wget():
	global h1
	global stop 
	global np
	global h1_log
	global time
	
	while not stop:
		rand = int(np.random.normal(14,14))
		if rand <= 0 or rand > 28:
			rand = 14
		t_start = time.time()
		for i in range(rand):
			h1.cmd("curl -so /dev/null -w '%{time_total}\n' >> h1.txt 10.0.0.8:80 &")
			time.sleep(0.2)
		time_to_divide = time.time()
		time_passed_since_batch = time_to_divide - t_start
		if time_passed_since_batch < 1:
			time.sleep(1 - time_passed_since_batch)

		
def h2_wget():
	global h2
	global stop 
	global np
	global h2_log
	global time
	
	while not stop:
		rand = int(np.random.normal(14,14))
		if rand <= 0 or rand > 28:
			rand = 14
		t_start = time.time()
		for i in range(rand):
			h2.cmd("curl -so /dev/null -w '%{time_total}\n' >> h2.txt 10.0.0.8:80 &")
			time.sleep(0.2)
		time_to_divide = time.time()
		time_passed_since_batch = time_to_divide - t_start
		if time_passed_since_batch < 1:
			time.sleep(1 - time_passed_since_batch)

		
			
def h3_wget():
	global h3
	global stop 
	global np
	global h3_log
	global time
	while not stop:
		rand = int(np.random.normal(14,14))
		if rand <= 0 or rand > 28:
			rand = 14
		t_start = time.time()
		for i in range(rand):
			h3.cmd("curl -so /dev/null -w '%{time_total}\n' >> h3.txt 10.0.0.7:80 &")
			time.sleep(0.2)
		time_to_divide = time.time()
		time_passed_since_batch = time_to_divide - t_start
		if time_passed_since_batch < 1:
			time.sleep(1 - time_passed_since_batch)

			
			
def h4_wget():
	global h4
	global stop 
	global np
	global h4_log
	global time

	while not stop:
		rand = int(np.random.normal(14,14))
		if rand <= 0 or rand > 28:
			rand = 14
		t_start = time.time()
		for i in range(rand):
			h4.cmd("curl -so /dev/null -w '%{time_total}\n' >> h4.txt 10.0.0.7:80 &")
			time.sleep(0.2)
		time_to_divide = time.time()
		time_passed_since_batch = time_to_divide - t_start
		if time_passed_since_batch < 1:
			time.sleep(1 - time_passed_since_batch)

######			
def h5_wget():
	global h5
	global stop 
	global np
	global h5_log
	global time
	
	while not stop:
		rand = int(np.random.normal(14,14))
		if rand <= 0 or rand > 28:
			rand = 14
		t_start = time.time()
		for i in range(rand):
			h5.cmd("curl -so /dev/null -w '%{time_total}\n' >> h5.txt 10.0.0.7:80 &")
			time.sleep(0.2)
		time_to_divide = time.time()
		time_passed_since_batch = time_to_divide - t_start
		if time_passed_since_batch < 1:
			time.sleep(1 - time_passed_since_batch)

	
####
def h6_wget():
	global h6
	global stop 
	global np
	global h6_log
	global time

	while not stop:
		rand = int(np.random.normal(14,14))
		if rand <= 0 or rand > 28:
			rand = 14
		t_start = time.time()
		for i in range(rand):
			h6.cmd("curl -so /dev/null -w '%{time_total}\n' >> h6.txt 10.0.0.7:80 &")
			time.sleep(0.2)
		time_to_divide = time.time()
		time_passed_since_batch = time_to_divide - t_start
		if time_passed_since_batch < 1:
			time.sleep(1 - time_passed_since_batch)		



threads = []
t = threading.Timer(60, timer)
t.start()


		
h1_t = Thread(target = h1_wget)
h2_t = Thread(target = h2_wget)
h3_t = Thread(target = h3_wget)
#h4_t = Thread(target = h4_wget)
#h5_t = Thread(target = h5_wget)
#h6_t = Thread(target = h6_wget)

h1_t.start()
threads.append(h1_t)
h2_t.start()
threads.append(h2_t)
h3_t.start()
threads.append(h3_t)
#h4_t.start()
#threads.append(h4_t)
#h5_t.start()
#threads.append(h5_t)
#h6_t.start()
#threads.append(h6_t)


for pr in threads:
	pr.join()

h1_log.close()
h2_log.close()	
h3_log.close()	
h4_log.close()	
h5_log.close()	
h6_log.close()	
	


	

	
