import pygame,sys,time,sqlite3,threading,socket,os
from pygame.locals import *
from math import *

sys_font=pygame.font.SysFont('Calibri',14,bold=True,italic=False)
try:
    current_directory=os.getcwd().replace(chr(92),chr(47))
    temp_list=current_directory.split(":",2)
    current_directory=temp_list[0]+":/"+temp_list[1]
except:
    current_directory=os.getcwd()
img1=pygame.image.load(current_directory+'/src/music/images/music.jpg')
img1=pygame.transform.scale(img1,(219,73))

def draw_music_options(surface,pos,w,h,music_menu,music_sound,img1,theme_fg):
	pygame.draw.line(surface,theme_fg,(pos[0],pos[1]+(h*0.75)),(pos[0]+w,pos[1]+(h*0.75)),1)
	surface.blit(img1,(pos[0]+1,pos[1]+1))
	if music_menu=="pause":
		pygame.draw.line(surface,theme_fg,(pos[0]+(w*0.45),pos[1]+(h*0.83)),(pos[0]+(w*0.45),pos[1]+(h*0.95)),3)
		pygame.draw.line(surface,theme_fg,(pos[0]+(w*0.45),pos[1]+(h*0.83)),(pos[0]+(w*0.5),pos[1]+(h*0.89)),3)
		pygame.draw.line(surface,theme_fg,(pos[0]+(w*0.45),pos[1]+(h*0.95)),(pos[0]+(w*0.5),pos[1]+(h*0.89)),3)
	if music_menu=="play":
		pygame.draw.line(surface,theme_fg,(pos[0]+(w*0.45),pos[1]+(h*0.83)),(pos[0]+(w*0.45),pos[1]+(h*0.95)),3)
		pygame.draw.line(surface,theme_fg,(pos[0]+(w*0.48),pos[1]+(h*0.83)),(pos[0]+(w*0.48),pos[1]+(h*0.95)),3)
	sound_percentage=int(music_sound*100)
	sound_percentage_text=sys_font.render(str(sound_percentage)+" %",False,theme_fg)
	surface.blit(sound_percentage_text,(pos[0]+(w*0.8),pos[1]+(h*0.8)))

def draw_music_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)

def set_music(surface,music,music_menu,music_sound,option,theme_fg):
	pos=(760,10)
	w=220;h=100
	draw_music_layout(surface,theme_fg,pos,w,h,1)
	if music_menu=="play":
		if(pygame.mixer.music.get_busy()==1):
			pygame.mixer.music.unpause()
		elif(pygame.mixer.music.get_busy()==0):
			pygame.mixer.music.play()
	elif music_menu=="pause":
		if(pygame.mixer.music.get_busy()==1):
			pygame.mixer.music.pause()
	pygame.mixer.music.set_volume(music_sound)
	draw_music_options(surface,pos,w,h,music_menu,music_sound,img1,theme_fg)
