import pygame,sys,time,sqlite3,threading,socket,os
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)

try:
    current_directory=os.getcwd().replace(chr(92),chr(47))
    temp_list=current_directory.split(":",2)
    current_directory=temp_list[0]+":/"+temp_list[1]
except:
    current_directory=os.getcwd()
img1=pygame.image.load(current_directory+'/src/gallery/img2.jpg')
img2=pygame.image.load(current_directory+'/src/gallery/img9.jpg')
img3=pygame.image.load(current_directory+'/src/gallery/img4.jpg')
img4=pygame.image.load(current_directory+'/src/gallery/img10.jpg')
img5=pygame.image.load(current_directory+'/src/gallery/img6.jpg')

def resize_image_to_width(img,w):
	img=pygame.transform.scale(img,(100,100))

def display_images(surface,p,img1,img2,img3,img4,img5):
	img1=pygame.transform.scale(img1,(40,50))
	img2=pygame.transform.scale(img2,(30,30))
	img3=pygame.transform.scale(img3,(20,30))
	img4=pygame.transform.scale(img4,(60,70))
	img5=pygame.transform.scale(img5,(40,50))
	surface.blit(img1,(p[0]+30,p[1]+15))
	surface.blit(img2,(p[0]+170,p[1]+25))
	surface.blit(img3,(p[0]+10,p[1]+25))
	surface.blit(img4,(p[0]+70,p[1]+5))
	surface.blit(img5,(p[0]+130,p[1]+15))

def draw_gallery_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)

def set_gallery(surface,option,theme_fg,image_pos):
	pos=(500,10)
	w=200;h=80
	draw_gallery_layout(surface,theme_fg,pos,w,h,1)
	display_images(surface,pos,img1,img2,img3,img4,img5)


'''
import pygame,sys,time,sqlite3,threading,socket,os
from pygame.locals import *
from math import *
pygame.init()

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)

current_directory=os.getcwd().replace(chr(92),chr(47))
temp_list=current_directory.split(":",2)
current_directory=temp_list[0]+":/"+temp_list[1]
images=[]
images.append(pygame.image.load(current_directory+'/src/gallery/img1.jpeg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img2.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img3.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img4.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img5.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img6.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img7.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img8.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img9.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img10.jpg'))
images.append(pygame.image.load(current_directory+'/src/gallery/img11.jpg'))

def display_images(surface,pos,images,image_pos):
	

def draw_gallery_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)

def set_gallery(surface,option,theme_fg,image_pos):
	pos=(500,10)
	w=200;h=80
	draw_gallery_layout(surface,theme_fg,pos,w,h,1)
	display_images(surface,pos,images,image_pos)
'''
