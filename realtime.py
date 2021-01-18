import os

# Program to run in Realtime(Infinite Loop)
while True:
	#Use TCP Dump for program parsing.py
	os.system('sudo tcpdump -G 2 -W 1 -w myfile.pcap')
	#run the program parsing.py on the file name myfile.pcap
	os.system('sudo venv/bin/python3 parsing.py')