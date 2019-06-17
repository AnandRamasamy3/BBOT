import pygame,sys,time,sqlite3,threading,socket
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)

def display_contacts(surface,theme_fg,contacts,p):
	ind=p[1]+5
	no_of_contacts=1
	for i in contacts:
		name_text=sys_font.render(i[0],False,theme_fg)
		phone_text=sys_font.render(i[1],False,theme_fg)
		surface.blit(name_text,(p[0]+20,ind))
		surface.blit(phone_text,(p[0]+120,ind))
		ind+=10
		no_of_contacts+=1
		if no_of_contacts>6:
			break

def draw_contacts_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)

def set_contacts(surface,database_location,option,theme_fg):
	pos=(10,510)
	w=200;h=80
	draw_contacts_layout(surface,theme_fg,pos,w,h,1)
	contacts=[]
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from contacts;")
	for row in cursor:
		contacts.append([row[0],row[1]])
	display_contacts(surface,theme_fg,contacts,pos)