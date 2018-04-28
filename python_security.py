#coding：utf-8
#!/usr/bin/env python

import timr, pyclamd
from threading import Thread

class Scan(Thread):
	def __init__(self, IP, scan_type, file):
		"""构造方法，参数初始化"""
		Thread.__init__（self）
		self.IP = IP
		self.scan_type = scan_type
		self.file = file
		self.connstr = ""
		self.scanresult = ""
		
	def run(self):
		"""多进程run方法"""
		try:
			cd = pyclamd.ClamdNetworkSocket(self.IP, 3310) #创建网络套接字连接对象
			if cd.ping():	#探测连通性
				self.connstr = self.IP + " connection {OK] "
				cd.reload()		#重载clamd病毒特征库，建议更新病毒库后reload
				if self.scan_type == "contscan_file":	#选择不同的烧苗模式
					self.scanresult = "{0}\n".format(cd.contscan_file(self.file))
				elif self.scan_type == "multiscan_file":
					self.scanresult = "{0}\n".format(cd.multiscan_file(self.file)
				elif self.scan_type == "scan_file":
					self.scanresult = "{0}\n".format(cd.scan_file(self.file)
				time.sleep(1)
			else:
				self.connstr = self.IP + "ping error, exit"
				return
		except Exception as e:
			self.connstr = self.IP + " " + str(e)
			
IPs = ['192.168.1.21', '192.168.1.22'] 	#扫描主机列表
scan_type = "multiscan_file"		#扫描模式
scanfile = "data/www"
i = 1
threadnum = 2	#指定启动的进程数
scanlist = []	#存储扫描Scan类线程对象列表
for ip in IPs:
	currp = Scan(ip, scan_type, scanfile)
	scanlist.append(currp)
	
	if i%threadnum == 0 or i == len(IPs):
		for task in scanlist:
			task.start()	#启动进程
			
		for task in scanlist:
			task.jion()		#等待所有子进程退出，并输出扫描结果
			print(task.connstr)		#打印服务器连接信息
			print(task.scanresult)	#打印扫描结果
		scanlist = []
	i += 1

				
			