import pygame,sys,time,datetime,sqlite3,threading,socket,calendar
from pygame.locals import *
from math import *
pygame.init()

days_font=pygame.font.SysFont('Calibri',15,bold=True,italic=False)
date_font=pygame.font.SysFont('Calibri',15,bold=True,italic=False)
today_date_font=pygame.font.SysFont('Calibri',8,bold=True,italic=False)

def display_calendar_2(surface,pos,w,h,theme_fg):
	#pygame.draw.line(surface,theme_fg,(220,100),(750,100),1)
	hor_ind=pos[1]+40
	pygame.draw.line(surface,theme_fg,(pos[0],hor_ind),(pos[0]+w,hor_ind),1)
	hor_ind+=40
	for i in range(9):
		pygame.draw.line(surface,theme_fg,(pos[0],hor_ind),(pos[0]+175,hor_ind),1)
		hor_ind+=30
	ver_ind=pos[0]+25
	for i in range(7):
		pygame.draw.line(surface,theme_fg,(ver_ind,pos[1]+40),(ver_ind,pos[1]+h),1)
		ver_ind+=25
	st_day_ind=pos[0]+8
	days=["S","M","T","W","T","F","S"]
	for i in days:
		day_text=days_font.render(i,False,theme_fg)
		surface.blit(day_text,(st_day_ind,pos[1]+50))
		st_day_ind+=25
	day_text=days_font.render("14",False,theme_fg)
	st_date_ind=pos[0]+8
	surface.blit(day_text,(st_date_ind,pos[1]+150))

def get_pos_of_day(pos,w,day):
	st_date_ind=1
	if day==0:
		st_date_ind=pos[0]+((w*0.123)*(0.3+0))
	elif day==1:
		st_date_ind=pos[0]+((w*0.123)*(0.3+1))
	elif day==2:
		st_date_ind=pos[0]+((w*0.123)*(0.3+2))
	elif day==3:
		st_date_ind=pos[0]+((w*0.123)*(0.3+3))
	elif day==4:
		st_date_ind=pos[0]+((w*0.123)*(0.3+4))
	elif day==5:
		st_date_ind=pos[0]+((w*0.123)*(0.3+5))
	elif day==6:
		st_date_ind=pos[0]+((w*0.123)*(0.3+6))
	return st_date_ind

def display_calendar(surface,pos,w,h,theme_fg):
	hor_ind=pos[1]+(h*0.1142)
	pygame.draw.line(surface,theme_fg,(pos[0],hor_ind),(pos[0]+w,hor_ind),1)
	hor_ind+=(h*0.1142)
	for i in range(9):
		pygame.draw.line(surface,theme_fg,(pos[0],hor_ind),(pos[0]+(w*0.875),hor_ind),1)
		hor_ind+=(h*0.0857)
	ver_ind=pos[0]+(w*0.125)
	for i in range(7):
		pygame.draw.line(surface,theme_fg,(ver_ind,pos[1]+(h*0.1142)),(ver_ind,pos[1]+h),1)
		ver_ind+=(w*0.125)
	month_num=int(time.strftime("%m"))
	year=int(time.strftime("%Y"))
	cal=calendar.month(year,month_num)
	new_cal=cal.replace(" ","   ")
	new_cal=new_cal.split("\n",)
	result=[]
	for i in new_cal:
		temp_cal=i.split("  ",)
		temp=[]
		for j in temp_cal:
			if j!='':
				temp.append(j)
		result.append(temp)
	if len(result[2])<7:
		for i in range(7-len(result[2])):
			result[2].insert(0,'')
	pos_y=pos[1]+(h*0.134285)
	for j in range(len(result[1])):
		day_text=days_font.render(result[1][j],False,theme_fg)
		st_date_ind=pos[0]+((w*0.125)*(0.1+j))
		surface.blit(day_text,(st_date_ind,pos_y))
	pos_y=pos[1]+(h*0.334285)
	for i in range(2,len(result)):
		for j in range(len(result[i])):
			#print(result[i][j])
			if time.strftime("%d")==result[i][j]:
				day_text=today_date_font.render(result[i][j],False,theme_fg)
				st_date_ind=get_pos_of_day(pos,w,j)
				surface.blit(day_text,(st_date_ind,pos_y+(5)))
			else:
				day_text=date_font.render(result[i][j],False,theme_fg)
				st_date_ind=get_pos_of_day(pos,w,j)
				surface.blit(day_text,(st_date_ind,pos_y))
		pos_y+=(h*0.0857)

def display_calendar_1(surface,pos,w,h,theme_fg):
	#pygame.draw.line(surface,theme_fg,(220,100),(750,100),1)
	hor_ind=pos[1]+(h*0.1142)
	pygame.draw.line(surface,theme_fg,(pos[0],hor_ind),(pos[0]+w,hor_ind),1)
	hor_ind+=(h*0.1142)
	for i in range(9):
		pygame.draw.line(surface,theme_fg,(pos[0],hor_ind),(pos[0]+(w*0.875),hor_ind),1)
		hor_ind+=(h*0.0857)
	ver_ind=pos[0]+(w*0.125)
	for i in range(7):
		pygame.draw.line(surface,theme_fg,(ver_ind,pos[1]+(h*0.1142)),(ver_ind,pos[1]+h),1)
		ver_ind+=(w*0.125)
	st_day_ind=pos[0]+((w*0.125)*0.32)
	days=["S","M","T","W","T","F","S"]
	for i in days:
		day_text=days_font.render(i,False,theme_fg)
		surface.blit(day_text,(st_day_ind,pos[1]+(h*0.14285)))
		st_day_ind+=(w*0.125)
	date=time.strftime("%d")
	month=time.strftime("%b")
	month_num=time.strftime("%m")
	year=time.strftime("%Y")
	we=datetime.datetime(2019,6,17,0,0,0,0).weekday()
	#print(day,month,year)
	cal_text=days_font.render(str(month)+", "+str(year),False,theme_fg)
	surface.blit(cal_text,(pos[0]+(w*0.3),pos[1]+(h*0.0285)))
	month_name_list=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	month_days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
	#print(len(month_days_list),len(month_name_list))
	st_date_ind=0
	#print(day)
	no_of_days=1
	for i in range(12):
		if month_name_list[i]==month:
			no_of_days=month_days_list[i]
	days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
	day_inds=[0,1,2,3,4,5,6]
	day_ind=datetime.datetime(int(year),int(month_num),int(date),0,0,0,0).weekday()
	
	top_remaining=14+day_ind
	bottom_remaining=63-(top_remaining+no_of_days)
	#print(top_remaining,bottom_remaining)
	#print(st_date_ind)
	#print(int(date),rem_dates)
	pos_y=pos[1]+(h*0.34285)
	for i in range(no_of_days):
		if date==str(i+1):
			day_text=days_font.render(str(i+1),False,theme_fg)
			st_date_ind=get_pos_of_day(pos,w,day_ind)
			surface.blit(day_text,(st_date_ind,pos_y))
		else:
			day_text=days_font.render(str(i+1),False,theme_fg)
			st_date_ind=get_pos_of_day(pos,w,day_ind)
			surface.blit(day_text,(st_date_ind,pos_y))
		day_ind+=1
		if day_ind>6:
			day_ind=0
			pos_y+=(h*0.0857)
	
	

def draw_calendar_layout(surface,theme_fg,p,w,h,t):
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0]+w,p[1]),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]+h),(p[0]+w,p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0],p[1]),(p[0],p[1]+h),t)
	pygame.draw.line(surface,theme_fg,(p[0]+w,p[1]),(p[0]+w,p[1]+h),t)

def set_calendar(surface,option,theme_fg):
	pos=(10,150)
	w=200;h=350
	#cal=calendar.month(2019,6)
	draw_calendar_layout(surface,theme_fg,pos,w,h,1)
	display_calendar(surface,pos,w,h,theme_fg)