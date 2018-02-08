#!/usr/bin/env python3

import os
import subprocess
import time
import re

# High level temperature is 55°C, you can change manually *_*
HIGH = 55
print("App is running...")

def main():
	while 1:
		# Terminal commands, finding degree
		command = 'sensors | grep -E  "temp1|Core|Package" | grep "+[1-9]" | cut -d  "+" -f 2 | grep "°C" | cut -d " " -f 1 | grep -v ","  | cut -d "." -f 1'
		# Finding the app that uses the most CPU
		app_name = "ps aux --sort=-pcpu | head -2 | grep -v USER | awk '{print $11}'"
		app_pid = "ps aux --sort=-pcpu | head -2 | grep -v USER | awk '{print $2}'"

		# Command editing.
		ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		output = ps.communicate()[0].decode().splitlines()
		out_len = len(output[0])

		ps_name = subprocess.Popen(app_name,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		appname = ps_name.communicate()[0].decode().splitlines()

		ps_pid = subprocess.Popen(app_pid,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		apppid = ps_pid.communicate()[0].decode().splitlines()
		#print(output, appname, apppid)

		# str to int. degrees
		for i in range(0,out_len):
			output = list(map(int,output))

		# list to str. app information
		str_appname = ''.join(appname)
		str_apppid = ''.join(apppid)
		#print(str_appname,str_apppid)

		# notify-send command
		warning = "\"Warning! High Temperature\""
		message = "\"App Name:   {} \n Pid:   {} \nTry:  sudo kill {} \"".format(str_appname,str_apppid,str_apppid)
		notify = "notify-send "+warning+" "+message+" -i hint"

		for i in range (0,out_len):
			if output[i] > HIGH:
				os.system(notify)
				break
		time.sleep(8)

if __name__ == '__main__':
	main()
# Some of the codes from github.com/0x7000/ph
