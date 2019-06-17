import pygame,sys,time,random
import src.security.encoded
from pygame.locals import *
from src.security.encoded import *
pygame.init()
black=(0,0,0)
blue=(0,0,255)
myfont=pygame.font.SysFont('calibri',16,bold=True,italic=False)
def get_points_for_the_message(message):
	points=[]
	initial_x=855
	initial_y=0
	for i in range(len(message)):
		points.append([initial_x,initial_y])
		if initial_x>=155:
			initial_x=initial_x-25
		else:
			initial_x=855
			initial_y=initial_y+20
	return points
def blit_complete_numbers(surface,numbers,pos_x,pos_y,message,points,theme_fg):
	message=list(message)
	for i in range(40):
		n=numbers[i]
		y=pos_y[i]
		greenish=10
		for j in range(n):
			temp_number1=random.randint(0,9)
			temp_number2=random.randint(0,9)
			if greenish<=247:
				greenish=greenish+6
			else:
				greenish=10
			if [pos_x[i],y] in points:
				ind=333333
				for k in range(len(points)):
					if [pos_x[i],y]==points[k]:
						ind=k
				if ind!=333333:
					code=get_encoded_alphabet(message[ind])
					nums=myfont.render(code,False,theme_fg)
			else:
				nums=myfont.render(str(temp_number1)+str(temp_number2),False,theme_fg)
			surface.blit(nums,(pos_x[i],y))
			y=y+20
def set_appended_numbers(numbers):
	for i in range(40):
		numbers[i]=numbers[i]+1
	temp_number=random.randint(0,39)
	temp_1=0
	for i in range(40):
		if numbers[i]>6:
			temp_1=3
	if temp_number>20 and temp_1==3:
		temp_number=random.randint(0,39)
		numbers[temp_number]=random.randint(6,16)
		temp_number=random.randint(0,39)
		numbers[temp_number]=random.randint(8,16)
		temp_number=random.randint(0,39)
		numbers[temp_number]=random.randint(12,16)
	return numbers
def increase_pos_y(pos_y):
	temp_pos_y=[]
	for i in range(40):
		temp_pos_y.append(pos_y[i]+10)
	return temp_pos_y
def start_collision(surface,numbers,pos_x,pos_y,message,theme_fg):
	points=get_points_for_the_message(message)
	numbers=set_appended_numbers(numbers)
	blit_complete_numbers(surface,numbers,pos_x,pos_y,message,points,theme_fg)
#start(numbers,pos_x,pos_y,message)