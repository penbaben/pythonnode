#!/usr/bin/python

import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email import encoders

class SendMail(object):
	def __init__(self, username, passwd, recv, title, content, file=None, email_host="smtp.qq.com", port=25):
		self.username = username
		self.passwd = passwd
		self.recv = recv
		self.title = title
		self.content = content
		self.file = file
		self.email_host = email_host
		self.port = port
	def send_mail(self):
		msg = MIMEMultipart()
		#发送内容对象
		if self.file:#处理附件
			#'octet-stream': binary data   创建附件对象
			att = MIMEBase('application', 'octet-stream') 
			#给附件添加头文件
			att.add_header('Content-Disposition','attachment',filename="%s" %self.file)
			att.add_header('Content-ID','0')  
			att.add_header('X-Attachment-Id', '0') 
			#将附件源文件加载到附件对象
			att.set_payload(open(self.file, 'rb').read())
			encoders.encode_base64(att)                       			                   msg.attach(att)			
		msg.attach(MIMEText(self.content))#邮件正文
		msg['Subject'] = self.title #邮件主题
		msg['From'] = self.username #发送者帐号
		msg['To'] = self.recv #接受者帐号		
		
		try:
			self.smtp = smtplib.SMTP()#发送邮件服务器的对象
			self.smtp.connect(self.email_host, self.port)
			self.smtp.login(self.username, self.passwd)
			self.smtp.starttls()
			self.smtp.sendmail(self.username, self.recv, msg.as_string())
			
			print('发送成功！')
		except Exception as e:
			print('发送失败。。。',e)
	def __def__(self):
		self.smtp.quit()
	
	
if __name__ == '__main__':
	m = SendMail(username='285267803@qq.com', passwd='urikjpgxgboxcafd', recv='penbaben_2010@163.com',title='业务数据', content='weekly', file='doc/week_repo.xlsx')
	m.send_mail()
				
			
				
		