#!/usr/bin/env python

import paramiko	 
'''
远程登录，并循环执行shell命令
'''
def sshclient_execmd(hostname, port, username, password,execmd):  
	paramiko.util.log_to_file("paramiko.log")  
	  
	s = paramiko.SSHClient()  
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())	 
	  
	s.connect(hostname=hostname, port=port, username=username, password=password) 
	stdin, stdout, stderr = s.exec_command (execmd)	
	stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  	 
	print(stdout.read().decode())
	print(stderr.read().decode())
	s.close()  
	
def main():	 
	 
	hostname = '10.24.78.133'
	port = 22  
	username = 'root'  
	password = 'redhat' 
	execmd = ''
	while execmd != 'exit': 
		str=("[%s@%s]#" % (username, hostname))
		execmd = input("%s" %str)
		sshclient_execmd(hostname, port, username, password,execmd) 		 
if __name__ == "__main__":	
	main()	
