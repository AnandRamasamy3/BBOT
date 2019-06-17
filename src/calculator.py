import pygame,sys,time,sqlite3,threading,socket
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',12,bold=True,italic=False)

def set_calculator_expression(surface,theme_fg,pos,w,h,calculator_exp):
	exp_text=sys_font.render(calculator_exp,False,theme_fg)
	surface.blit(exp_text,(pos[0]+10,pos[1]+(h*0.85)))

def set_calculator_simplified_answer(surface,theme_fg,pos,w,h,exp,database_location):
	try:
		conn=sqlite3.connect(database_location)
		cursor=conn.cursor()
		result="ooops"
		if "+" in exp:
			numbers=exp.split("+",)
			n1=float(numbers[0])
			n2=float(numbers[1])
			result=n1+n2
		elif "-" in exp:
			numbers=exp.split("-",)
			n1=float(numbers[0])
			n2=float(numbers[1])
			result=n1-n2
		elif "x" in exp:
			numbers=exp.split("x",)
			n1=float(numbers[0])
			n2=float(numbers[1])
			result=n1*n2
		elif "/" in exp:
			numbers=exp.split("/",)
			n1=float(numbers[0])
			n2=float(numbers[1])
			result=n1/n2
		if result!="ooops":
			cursor.execute("INSERT INTO calculator values ('"+str(result)+"');")
			conn.commit()
			return ""
		else:
			return exp
	except:
		return exp

def display_calculator(surface,theme_fg,pos,w,h,last_results):
	#print(last_results)
	if len(last_results)==0:
		last_results=[" "]
	pygame.draw.line(surface,theme_fg,(pos[0],pos[1]+(h*0.7)),(pos[0]+w,pos[1]+(h*0.7)),1)
	ind=h*0.5
	for i in last_results:
		answer_text=sys_font.render("= "+i,False,theme_fg)
		surface.blit(answer_text,(pos[0]+10,pos[1]+ind))
		ind-=(h*0.20)

def draw_calculator_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)
	#pygame.draw.line(surface,theme_fg,(p[0],p[1]+(h*0.75)),(p[0]+w,p[1]+(h*0.75)),t)

def set_calculator(surface,database_location,option,theme_fg):
	pos=(300,10)
	w=180;h=80
	results=[]
	last_results=[]
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from calculator;")
	for row in cursor:
		results.append(row[0])
	results.reverse()
	if len(results)>0:
		last_results.append(results[0])
		if len(results)>1:
			last_results.append(results[1])
			if len(results)>2:
				last_results.append(results[2])
	draw_calculator_layout(surface,theme_fg,pos,w,h,1)
	display_calculator(surface,theme_fg,pos,w,h,last_results)