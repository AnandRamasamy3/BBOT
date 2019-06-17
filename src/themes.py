import pygame,sys,time,sqlite3,threading,socket
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)

def display_theme_colors(surface,theme_fg,pos,w,h,colors):
	bg_text=sys_font.render("BG color",False,theme_fg)
	fg_text=sys_font.render("FG color",False,theme_fg)
	surface.blit(bg_text,(pos[0]+(w*0.2),pos[1]+(h*0.075)))
	surface.blit(fg_text,(pos[0]+(w*0.6),pos[1]+(h*0.075)))
	#  --------BG COLOR------
	ind=0
	x=0
	for i in range(4):
		pygame.draw.rect(surface,colors[ind],(pos[0]+(w*x)+2,pos[1]+(h*0.25)+1,(w*0.125)-1,(h*0.25)-1))
		x+=0.125
		ind+=1
	x=0
	for i in range(4):
		pygame.draw.rect(surface,colors[ind],(pos[0]+(w*x)+2,pos[1]+(h*0.5)+1,(w*0.125)-1,(h*0.25)-1))
		x+=0.125
		ind+=1
	x=0
	for i in range(4):
		pygame.draw.rect(surface,colors[ind],(pos[0]+(w*x)+2,pos[1]+(h*0.75)+1,(w*0.125)-1,(h*0.25)-1))
		x+=0.125
		ind+=1
	
	#  --------FG COLOR------
	ind=0
	x=0.5
	for i in range(4):
		pygame.draw.rect(surface,colors[ind],(pos[0]+(w*x)+2,pos[1]+(h*0.25)+1,(w*0.125)-1,(h*0.25)-1))
		x+=0.125
		ind+=1
	x=0.5
	for i in range(4):
		pygame.draw.rect(surface,colors[ind],(pos[0]+(w*x)+2,pos[1]+(h*0.5)+1,(w*0.125)-1,(h*0.25)-1))
		x+=0.125
		ind+=1
	x=0.5
	for i in range(4):
		pygame.draw.rect(surface,colors[ind],(pos[0]+(w*x)+2,pos[1]+(h*0.75)+1,(w*0.125)-1,(h*0.25)-1))
		x+=0.125
		ind+=1
	
def draw_themes_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)
	
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.5),p[1]),(p[0]+(w*0.5),p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+(h*0.25)),(p[0]+w,p[1]+(h*0.25)),t)
	
	
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.125),p[1]+(h*0.25)),(p[0]+(w*0.125),p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.250),p[1]+(h*0.25)),(p[0]+(w*0.250),p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.375),p[1]+(h*0.25)),(p[0]+(w*0.375),p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.625),p[1]+(h*0.25)),(p[0]+(w*0.625),p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.750),p[1]+(h*0.25)),(p[0]+(w*0.750),p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+(w*0.875),p[1]+(h*0.25)),(p[0]+(w*0.875),p[1]+h),t)
	
	
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+(h*0.5)),(p[0]+w,p[1]+(h*0.5)),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+(h*0.75)),(p[0]+w,p[1]+(h*0.75)),t)

def set_themes(surface,option,colors,theme_fg):
	pos=(760,510)
	w=220;h=80
	draw_themes_layout(surface,theme_fg,pos,w,h,1)
	display_theme_colors(surface,theme_fg,pos,w,h,colors)