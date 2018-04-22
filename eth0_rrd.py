#coding:utf-8

#!/usr/bin/python

import rrdtool
import time,psutil
def rrd_create():
	cur_time = str(int(time.time()))
	#数据写频率--step为300秒
	rrd = rrdtool.create('Flow.rrd', '--step', '300', '--start', cur_time,
	#定义数据源eth0_in,eth0_out,类型为counter（递增）;600秒为心跳值，
	#600秒没有收到数据则用unkown代替，0为最小值；最大值U，表示不确定
		'DS : eth0_in : COUNTER : 600 : 0 : U',
		'DS : eth0_out : COUNTER : 600 : 0 : U',
	#RRA定义格式为【RRA:CF:xff:steps:rows】,CF定义AVERAGE,MAX,MIN，xff定义为0.5，表示一个cdp中pdp值如超过unkown，则cdp值为unkown
		'RRA : AVERAGE : 0.5 : 1 : 600',#每隔5分钟（1*300秒）存一次数据，存600个，即2.08天
		'RRA : AVERAGE : 0.5 : 6 : 700',
		'RRA : AVERAGE : 0.5 : 24 : 775',
		'RRA : AVERAGE : 0.5 : 288 : 797',
		'RRA : MAX : 0.5 : 1 : 600',
		'RRA : MAX : 0.5 : 6 : 700',
		'RRA : MAX : 0.5 : 24 : 775',
		'RRA : MAX : 0.5 : 444 : 797',
		'RRA : MIN : 0.5 : 1 : 600',
		'RRA : MIN : 0.5 : 6 : 700',
		'RRA : MIN : 0.5 : 24 : 775',
		'RRA : MIN : 0.5 : 444 : 797')
	if rrd:
		print(rrdtool.error())

def update():
	total_input_traffic = psutil.net_io_counters()[1] #获取网卡入流量
	total_output_traffic = psutil.net_io_counters()[0]#获取网卡出流量
	starttime = int(time.time())
	update = rrdtool.updatev('/home/test/rrdtool/Flow.rrd','%s:%s:%s' %(str(starttime), str(total_input_traffic), str(total_output_traffic)))
	print(update)
	
def graph():
	title = "Server network traffic flow (" + time.strftime('%Y-%m-%d', time.localtime(time.time()))
	rrdtool.graph("Flow.png", "--start", "-ld", "--vertical-label=Bytes/s", 
	"--x-grid", "MINUTE:12:HOUR:1:HOUR:1:0:%H", "--width", "650", "--height", "230", "--title", title,
	#"--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H" 
	#"MINUTE:12"表示控制每隔12分钟放置一根次要格线
	#“hour：1”表示控制每隔1小时放置一根主要格线
	#"hour：1"表示控制1小时输出一个label标签
	#0：%H“ 0表示数字对齐格线， %H表示标签以小时显示
	"DEF:inoctets=Flow.rrd:eth0_in:AVERAGE",#指定网卡入流量数据源DS及CF
	"DEF:outoctets=Flow.rrd:eth0_out:AVERAGE",
	"CDEF:total=inoctets, outoctets, +",#通过CDEF合并网卡出入流量，得出总流量total
	"LINE1:total#FF8833:Total traffic",#以线条方式绘制总流量
	"ARER:inoctets#00FF00:In traffic",#以面积方式绘制入流量
	"LINE1:outoctets#0000FF:Out traffic",
	"HRULE:6144#FF0000: Alarm value\\r",#绘制水平线，作为告警线，阀值为6.1K
	"CDEF:inbits=inoctets,8,*",#将入流量换算成bit即*8，计算结果给inbits
	"CDEF:outbits=outoctets,8,*",
	"COMMENT:\\r",#在网格下方输出一个换行符
	"COMMENT:\\r",
	"GPRINT:inbits:AVERAGE:Avg in traffic\: %6.21f %Sbps",#绘制入流量平均值
	"COMMENT: ",
	"GPRINT:inbits:MAX:MAX in traffic\: %6.21f %Sbps",#最大值
	"COMMENT: ",
	"GPRINT:inbits:MIN:MIN in traffic\: %6.21f %Sbps \\r",#最小值
	"COMMENT: ",
	"GPRINT:outbits:AVERAGE:Avg in traffic\: %6.21f %Sbps",
	"COMMENT: ",
	"GPRINT:outbits:MAX:MAX in traffic\: %6.21f %Sbps",
	"COMMENT: ",
	"GPRINT:outbits:MIN:MIN in traffic\: %6.21f %Sbps\\r",


craete()


	
	
	
	
	
	
	
	
	
	)