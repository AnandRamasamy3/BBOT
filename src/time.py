import pygame,sys,time,datetime,sqlite3,threading,socket
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)
time_font=pygame.font.SysFont('Calibri',32,bold=True,italic=False)
sec_font=pygame.font.SysFont('Calibri',17,bold=True,italic=False)

def display_time(surface,theme_fg,p):
	#print(str(time.strftime("%I"))+" : "+str(time.strftime("%M")))
	#print(str(time.strftime("%S")))
	#print(str(time.strftime("%p")))
	#print(str(time.strftime("%d"))+"/ "+str(time.strftime("%b"))+"/ "+str(time.strftime("%Y")))
	time_text=time_font.render((str(time.strftime("%I"))+" : "+str(time.strftime("%M"))),False,theme_fg)
	sec_text=sec_font.render(str(time.strftime("%S")),False,theme_fg)
	sess_text=time_font.render(str(time.strftime("%p")),False,theme_fg)
	surface.blit(time_text,(p[0]+25,p[1]+20))
	surface.blit(sec_text,(p[0]+120,p[1]+30))
	surface.blit(sess_text,(p[0]+160,p[1]+20))
	date_text=sec_font.render((str(time.strftime("%d"))+"/ "+str(time.strftime("%b"))+"/ "+str(time.strftime("%Y"))),False,theme_fg)
	surface.blit(date_text,(p[0]+30,p[1]+80))

def draw_time_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)

def set_time(surface,option,theme_fg):
	pos=(10,10)
	w=220;h=120
	#draw_time_layout(surface,blue,pos,w,h,1)
	display_time(surface,theme_fg,pos)