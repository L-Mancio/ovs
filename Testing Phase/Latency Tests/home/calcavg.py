import os
h1_log = open("h1.txt", "r")
h2_log = open("h2.txt", "r")
h3_log = open("h3.txt", "r")
h4_log = open("h4.txt", "r")
h5_log = open("h5.txt", "r")
h6_log = open("h6.txt", "r")


latencies = [] 
for line in h1_log.readlines():
	if line[0] == 'b':
		continue
	line = line[:-1]
	latencies.append(float(line))
for line in h2_log.readlines():
	if line[0] == 'b':
		continue
	line = line[:-1]
	latencies.append(float(line))
for line in h3_log.readlines():
	if line[0] == 'b':
		continue
	line = line[:-1]
	latencies.append(float(line))
for line in h4_log.readlines():
	if line[0] == 'b':
		continue
	line = line[:-1]
	latencies.append(float(line))
for line in h5_log.readlines():
	if line[0] == 'b':
		continue
	line = line[:-1]
	latencies.append(float(line))
for line in h6_log.readlines():
	if line[0] == 'b':
		continue
	line = line[:-1]
	latencies.append(float(line))



print "average: " + str(sum(latencies) / len(latencies))
#
os.remove("h1.txt")
os.remove("h2.txt")
os.remove("h3.txt")
os.remove("h4.txt")
os.remove("h5.txt")
os.remove("h6.txt")