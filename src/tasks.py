import pygame,sys,time,sqlite3,threading,socket
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)
add_font=pygame.font.SysFont('Calibri',23,bold=True,italic=False)

def upload_task(surface,theme_fg,database_location,pos,h,w,task_text):
	result=""
	#print(task_text)
	conn=sqlite3.connect(database_location)
	conn.execute("INSERT INTO tasks values('"+task_text+"');")
	conn.commit()
	return result

def set_tasks_new(surface,theme_fg,task_text,pos,w,h):
	new_text=sys_font.render(task_text,False,theme_fg)
	surface.blit(new_text,(pos[0]+(w*0.090909),pos[1]+(h*0.04285)))

def display_tasks(surface,theme_fg,p,w,h,tasks):
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.0454545),p[1]+(h*0.0714)),(p[0]+(w*0.954545),p[1]+(h*0.0714)),1)
	ind=p[1]+(h*0.085714)
	no_of_tasks=1
	for i in tasks:
		if len(i)<=33:
			task_text=sys_font.render(str(no_of_tasks)+".  "+i,False,theme_fg)
		else:
			task_text=sys_font.render(str(no_of_tasks)+".  "+i[:33],False,theme_fg)
		surface.blit(task_text,(p[0]+(w*0.090909),ind))
		ind+=(h*0.0285)
		no_of_tasks+=1
		if no_of_tasks>28:
			break

def draw_tasks_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)


def set_tasks(surface,database_location,option,task_add,task_text,theme_fg):
	pos=(760,130)
	w=220;h=350
	tasks=[]
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from tasks;")
	#print(len("lorem ipsum dolor sit amet anand ramasamy"))
	for row in cursor:
		tasks.append(row[0])
	tasks.reverse()
	if task_add=="":
		add_text = add_font.render("+", False, theme_fg)
		surface.blit(add_text, (pos[0] + (w * 0.863636), pos[1] + (h * 0.00571428)))
	if task_add=="add_new":
		set_tasks_new(surface,theme_fg,task_text,pos,w,h)
	draw_tasks_layout(surface,theme_fg,pos,w,h,1)
	display_tasks(surface,theme_fg,pos,w,h,tasks)