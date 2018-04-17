#coding:utf-8
"""自动化业务流量报表周报"""
import xlsxwriter

workbook = xlsxwriter.Workbook('chart.xlsx') #创建文件名为a的excel文件
worksheet = workbook.add_worksheet()  #建立一个工作表
chart = workbook.add_chart({'type': 'column'}) #创建图标对象
#定义数据表头列表
title = ['业务名称', '星期一', '星期二', '星期三' , '星期四', '星期五', '星期六', '星期日', '平均流量']
buname = ['业务官网', '新闻中心', '购物频道', '体育频道' , '亲子频道']

data = [
	[150, 152, 158, 149, 155, 145, 148],
	[89, 88, 95, 93, 98, 100, 99],
	[201, 200, 198, 175, 170, 198, 195],
	[75, 77, 78, 78, 74, 70, 79],
	[88, 85, 87, 90, 93, 88, 84]
	]
format = workbook.add_format()	#定义format格式对象
format.set_border(1)	#边框加粗1像素
format_title = workbook.add_format() #定义format_title格式对象
format_title.set_border(1)
format_title.set_bg_color("#cccccc") #背景颜色
format_title.set_align("center") #居中对齐
format_title.set_bold() #单元内容加粗

format_ave = workbook.add_format()
format_ave.set_border(1)
format_ave.set_num_format("0.00") #单元格数字类型显示格式

#分别以行或列写入标题，业务名称，流量数据，同时引用不同的格式
worksheet.write_row('A1', title, format_title) 
worksheet.write_column('A2', buname, format)
worksheet.write_row('B2', data[0], format)
worksheet.write_row('B3', data[1], format)
worksheet.write_row('B4', data[2], format)
worksheet.write_row('B5', data[3], format)
worksheet.write_row('B6', data[4], format)

#定义图表数据系列函数
def chart_series(cur_row):
	worksheet.write_formula('I' + cur_row, '=AVERAGE(B' + cur_row + ':H' + cur_row + ')', format_ave) #计算（AVERAGE函数）频道平均流量
	
	chart.add_series({
		'categories': '=Sheet1!$B$1:$H$1',  #将周一至周日作为图表的x轴
		'values':'=Sheet1!$B$' + cur_row + ':$H$' + cur_row,#频道一周所有数据作为数据区域
		'line':	{'color':'black'}, #线条颜色
		'name':	'=Sheet1!$A$' + cur_row,#引用业务名称作为图例项
		})

for row in range(2, 7): #数据域以第2-6行进行图表数据系列函数调用
	chart_series(str(row))
	
#chart.set_table()  #设置X轴表格格式
#chart.set_style(30) #设置图表样式
chart.set_size({'width' : 577, 'height' : 287}) #设置图表大小
chart.set_title({'name' : '业务流量周报图表'})	#设置图表（上方）大标题
chart.set_y_axis({'name' : 'Mb/s'}) #设置y轴（左侧）小标题

worksheet.insert_chart('A8', chart) #在A8单元格插入图表
workbook.close()