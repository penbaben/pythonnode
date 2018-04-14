#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

HOST = "smtp.qq.com"  #邮件服务器
SUBJECT = u" 官网业务服务质量周报" #主题
TO = "penbaben_2010@163.com" 
FROM = "285267803@qq.com"
'''
text = "python rules the all!"  #邮件内容
BODY = "\r\n".join((  #组装sendmail方法的邮件主体内容，各段以“\r\n”进行分隔
		"From: %s" % FROM,
		"To: %s" % TO,
		"Subject: %s " % SUBJECT,
		"",
		text))
'''
def addimg(src, imgid): #添加图片函数，参数1：图片路径， 参数2：图片
	fp = open(src, 'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID', imgid)
	return msgImage

msg = MIMEMultipart('related') #创建MIMEImage对象，读取图片内容并作为参数的邮件体

msgtext = MIMEText("""
	<table width="600" border="0" cellspacing="0" cellpadding="4">
		<tr bgcolor="#CECFAD" height="20" style="font-size:14px"> 
			<td colspan=2>*官网数据 <a herf="monitor.domain.com">更多>></a></td>
		</tr>
		<tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
			<td>
				<img src="cid:io"></td><td>
				<img src="cid:key_hit"></td>
		</tr>
		<tr gcolor="#EFEBDE" height="100" style="font-size:13px">
			<td>
				<img src="cid:men"></td><td>
				<img src="cid:swap"></td>
		</tr>
			1)日访问量:<font color=red>152433</font> 访问次数：23651 页面浏览量：45123
	点击数：545122 数据流量：504MB<br>
			2)状态码信息<br>
			&nbsp;&nbsp;500:105  404:326  503:214<br>
			3)访客浏览器信息<br>
			&nbsp;&nbsp;IE:50%  firefox:10% chrome:30% other:10%<br>
			4)页面信息<br>
			&nbsp;&nbsp;/index.php 42153<br>
			&nbsp;&nbsp;/view.php 42153<br>
			&nbsp;&nbsp;/login.php 42153<br>
			</td>
		</tr>
	</table>""","html","utf-8")	
msg.attach(msgtext)
msg.attach(addimg("img/bytes_io.png","io"))
msg.attach(addimg("img/myisam_key_hit.png", "key_hit"))
msg.attach(addimg("img/os_mem.png", "men"))
msg.attach(addimg("img/os_swap.png", "swap"))
msg['Subject'] = SUBJECT
msg['From'] = 'FROM'
msg['To'] = 'TO'
try:
	server = smtplib.SMTP() #创建smtp对象
	server.connect(HOST, "25")  #通过connect方法连接主机
	server.starttls()  #启动安全传输模式
	server.login("285267803@qq.com", "urikjpgxgboxcafd")
	server.sendmail(FROM, TO, msg.as_string()) # 邮件发送
	server.quit()
	print("邮件发送成功！")
except Exception as e:
	print("失败:" + str(e))