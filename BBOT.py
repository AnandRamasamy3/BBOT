import pygame,sys,time,sqlite3,threading,socket,os,random
from pygame.locals import *
from math import *
from src.calculator import *
from src.time import *
from src.calendar import *
from src.music import *
from src.gallery import *
from src.contacts import *
from src.tasks import *
from src.themes import *
from src.security.ooops import *
#from src.security.encoded import *

pygame.init()
fps=20
ft=pygame.time.Clock()
surface=pygame.display.set_mode((1000,600),0,32)
pygame.display.set_caption('BBOT')

sys_font=pygame.font.SysFont('Calibri',10,bold=True,italic=False)
try:
    current_directory=os.getcwd().replace(chr(92),chr(47))
    temp_list=current_directory.split(":",2)
    current_directory=temp_list[0]+":/"+temp_list[1]
except:
    current_directory=os.getcwd()
database_location=current_directory+'/src/database/BBOT.db'
music=pygame.mixer.music.load(current_directory+"/src/music/music_list/thalaiva.mp3")
colors=[(255,255,255),(170,0,0),(0,0,255),(0,255,170),(100,50,105),(255,255,0),(0,0,0),(100,100,50),(255,0,0),(0,255,0),(255,0,255),(255,175,100)]

def get_theme_color():
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		theme_bg=row[0]
		theme_fg=row[1]
	#print(theme_bg,theme_fg)
	return theme_bg,theme_fg

def get_image_pos():
	conn=sqlite3.connect(database_location)
	cur=conn.cursor()
	cursor=conn.execute("SELECT * from settings;")
	for row in cursor:
		image_pos=row[3]
	return image_pos

option=""
calculator_exp=""
music_menu="pause"
music_sound=0.2
task_add=""
task_text=""
image_pos=get_image_pos()

def set_theme(mx,my,colors,theme_bg,theme_fg):
	#print(database_location)
	new_bg=str(theme_bg)
	new_fg=str(theme_fg)
	if 760<=mx<=787.5 and 530<=my<=550:
		new_bg="0"
	elif 787.5<=mx<=815 and 530<=my<=550:
		new_bg="1"
	elif 815<=mx<=842.5 and 530<=my<=550:
		new_bg="2"
	elif 842.5<=mx<=869 and 530<=my<=550:
		new_bg="3"
	elif 760<=mx<=787.5 and 550<=my<=570:
		new_bg="4"
	elif 787.5<=mx<=815 and 550<=my<=570:
		new_bg="5"
	elif 815<=mx<=842.5 and 550<=my<=570:
		new_bg="6"
	elif 842.5<=mx<=869 and 550<=my<=570:
		new_bg="7"
	elif 760<=mx<=787.5 and 570<=my<=590:
		new_bg="8"
	elif 787.5<=mx<=815 and 570<=my<=590:
		new_bg="9"
	elif 815<=mx<=842.5 and 570<=my<=590:
		new_bg="10"
	elif 842.5<=mx<=869 and 570<=my<=590:
		new_bg="11"

	elif 869.5<=mx<=897 and 530<=my<=550:
		new_fg="0"
	elif 897<=mx<=924.5 and 530<=my<=550:
		new_fg="1"
	elif 924.5<=mx<=952 and 530<=my<=550:
		new_fg="2"
	elif 952<=mx<=979.5 and 530<=my<=550:
		new_fg="3"
	elif 869.5<=mx<=897 and 550<=my<=570:
		new_fg="4"
	elif 897<=mx<=924.5 and 550<=my<=570:
		new_fg="5"
	elif 924.5<=mx<=952 and 550<=my<=570:
		new_fg="6"
	elif 952<=mx<=979.5 and 550<=my<=570:
		new_fg="7"
	elif 869.5<=mx<=897 and 570<=my<=590:
		new_fg="8"
	elif 897<=mx<=924.5 and 570<=my<=590:
		new_fg="9"
	elif 924.5<=mx<=952 and 570<=my<=590:
		new_fg="10"
	elif 952<=mx<=979.5 and 570<=my<=590:
		new_fg="11"
	
	conn=sqlite3.connect(database_location)
	conn.execute("UPDATE settings SET theme_color_bg=("+new_bg+") WHERE garbage=1;")
	conn.execute("UPDATE settings SET theme_color_fg=("+new_fg+") WHERE garbage=1;")
	conn.commit()

def set_option_for_tasks(mx,my,pos,task_add):
	result=task_add
	if pos[0]+10<=mx<=pos[0]+210 and pos[1]+5<=my<=pos[1]+23:
		result="add_new"
	return result

def draw_options_bar(option,theme_fg):
	if option=="tasks":
		draw_tasks_layout(surface,theme_fg,(760,130),220,350,3)
	if option=="calculator":
		draw_calculator_layout(surface,theme_fg,(300,10),180,80,3)
	if option=="calendar":
		draw_calendar_layout(surface,theme_fg,(10,150),200,350,3)
	if option=="contacts":
		draw_contacts_layout(surface,theme_fg,(10,510),200,80,3)
	if option=="music":
		draw_music_layout(surface,theme_fg,(760,10),220,100,3)
	if option=="gallery":
		draw_gallery_layout(surface,theme_fg,(500,10),200,80,3)
	if option=="themes":
		draw_themes_layout(surface,theme_fg,(760,510),220,80,3)

def set_option_for_music(mx,my,music_menu):
	result=music_menu
	if 855<=mx<=875 and 90<=my<=110:
		if music_menu=="pause":
			result="play"
		elif music_menu=="play":
			result="pause"
	return result

def garbage():
	pass

def set_option(mx,my):
	option=""
	if 300<=mx<=480 and 10<=my<=90:
		option="calculator"
	elif 10<=mx<=210 and 150<=my<=500:
		option="calendar"
	elif 10<=mx<=210 and 510<=my<=590:
		option="contacts"
	elif 500<=mx<=700 and 10<=my<=90:
		option="gallery"
	elif 760<=mx<=980 and 10<=my<=110:
		option="music"
	elif 760<=mx<=980 and 130<=my<=480:
		option="tasks"
	elif 760<=mx<=980 and 510<=my<=590:
		option="themes"
	elif 300<=mx<=480 and 10<=my<=90:
		option="calculator"
	return option

def home(option,calculator_exp,music_menu,music_sound,task_add,task_text,colors,image_pos):
	while True:
		theme_bg,theme_fg=get_theme_color()
		surface.fill(colors[theme_bg])
		mx,my=pygame.mouse.get_pos()
		mcl=(0,0,0)
		mcl=pygame.mouse.get_pressed()
		#print(mx,my)
		#print(theme_bg)
		if mcl[0]==1:
			option=set_option(mx,my)
			if option=="music":
				music_menu=set_option_for_music(mx,my,music_menu)
			elif option=="tasks":
				task_add=set_option_for_tasks(mx,my,(760,130),task_add)
			elif option=="themes":
				set_theme(mx,my,colors,theme_bg,theme_fg)
		#print(mx,my,theme_bg)
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_F10:
					pygame.quit()
					sys.exit()
				if event.key==pygame.K_RIGHT:
					if option=="gallery":
						image_pos+=1
						if image_pos>11:image_pos=11
				if event.key==pygame.K_LEFT:
					if option=="gallery":
						image_pos-=1
						if image_pos<0:image_pos=0
				if event.key==pygame.K_BACKSPACE:
					if option=="calculator":
						exp_list=list(calculator_exp)
						if len(exp_list)>0:
							exp_list.pop(-1)
							calculator_exp=""
							for i in exp_list:
								calculator_exp+=i
					elif option=="tasks":
						exp_list=list(task_text)
						if len(exp_list)>0:
							exp_list.pop(-1)
							task_text=""
							for i in exp_list:
								task_text+=i
				if event.key==pygame.K_SPACE:
					if option=="music":
						if music_menu=="play":
							music_menu="pause"
						elif music_menu=="pause":
							music_menu="play"
				if event.key==pygame.K_UP:
					if option=="music":
						music_sound+=0.1
						if music_sound>1.0:
							music_sound=1.0
				if event.key==pygame.K_DOWN:
					if option=="music":
						music_sound-=0.1
						if music_sound<0.0:
							music_sound=0.0
				if event.key==pygame.K_F1:
					option="calculator"
				if event.key==pygame.K_F2:
					option="gallery"
				if event.key==pygame.K_F3:
					option="music"
				if event.key==pygame.K_F4:
					option="tasks"
				if event.key==pygame.K_F5:
					option="themes"
				if event.key==pygame.K_F6:
					option="contacts"
				if event.key==pygame.K_F7:
					option="calendar"
				if event.key==pygame.K_F8:
					option=""
				if event.key==pygame.K_0:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="0"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="0"
				if event.key==pygame.K_1:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="1"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="1"
				if event.key==pygame.K_2:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="2"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="2"
				if event.key==pygame.K_3:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="3"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="3"
				if event.key==pygame.K_4:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="4"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="4"
				if event.key==pygame.K_5:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="5"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="5"
				if event.key==pygame.K_6:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="6"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="6"
				if event.key==pygame.K_7:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="7"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="7"
				if event.key==pygame.K_8:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="8"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="8"
				if event.key==pygame.K_9:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="9"
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="9"
				if event.key==pygame.K_x:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="x"
				if event.key==pygame.K_PERIOD:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="."
				if event.key==pygame.K_EQUALS:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="+"
				if event.key==pygame.K_MINUS:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="-"
				if event.key==pygame.K_SLASH:
					if len(calculator_exp)<26 and option=="calculator":
						calculator_exp+="/"
				if event.key==pygame.K_a:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="a"
				if event.key==pygame.K_b:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="b"
				if event.key==pygame.K_c:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="c"
				if event.key==pygame.K_d:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="d"
				if event.key==pygame.K_e:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="e"
				if event.key==pygame.K_f:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="f"
				if event.key==pygame.K_g:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="g"
				if event.key==pygame.K_h:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="h"
				if event.key==pygame.K_i:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="i"
				if event.key==pygame.K_j:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="j"
				if event.key==pygame.K_k:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="k"
				if event.key==pygame.K_l:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="l"
				if event.key==pygame.K_m:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="m"
				if event.key==pygame.K_n:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="n"
				if event.key==pygame.K_o:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="o"
				if event.key==pygame.K_p:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="p"
				if event.key==pygame.K_q:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="q"
				if event.key==pygame.K_r:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="r"
				if event.key==pygame.K_s:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="s"
				if event.key==pygame.K_t:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="t"
				if event.key==pygame.K_u:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="u"
				if event.key==pygame.K_v:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="v"
				if event.key==pygame.K_w:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="w"
				if event.key==pygame.K_x:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="x"
				if event.key==pygame.K_y:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="y"
				if event.key==pygame.K_z:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+="z"
				if event.key==pygame.K_SPACE:
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_text+=" "
				if event.key==pygame.K_RETURN:
					main=option
					if option=="calculator":
						calculator_exp=set_calculator_simplified_answer(surface,blue,(300,10),180,80,calculator_exp,database_location)
					if len(task_text)<36 and option=="tasks" and task_add=="add_new":
						task_add=upload_task(surface,blue,database_location,(760,130),220,350,task_text)
						task_text=""
		draw_options_bar(option,colors[theme_fg])
		#print(task_text)
		set_calculator_expression(surface,blue,(300,10),180,80,calculator_exp)
		t1=threading.Thread(target=set_time,args=(surface,option,colors[theme_fg]))
		t2=threading.Thread(target=set_calculator,args=(surface,database_location,option,colors[theme_fg]))
		t3=threading.Thread(target=set_calendar,args=(surface,option,colors[theme_fg]))
		t4=threading.Thread(target=set_tasks,args=(surface,database_location,option,task_add,task_text,colors[theme_fg]))
		t5=threading.Thread(target=set_music,args=(surface,music,music_menu,music_sound,option,colors[theme_fg]))
		t6=threading.Thread(target=set_gallery,args=(surface,option,colors[theme_fg],image_pos))
		t7=threading.Thread(target=set_themes,args=(surface,option,colors,colors[theme_fg]))
		t8=threading.Thread(target=set_contacts,args=(surface,database_location,option,colors[theme_fg]))
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		t7.start()
		t8.start()
		t1.join()
		t2.join()
		t3.join()
		t4.join()
		t5.join()
		t6.join()
		t7.join()
		t8.join()
		pygame.display.update()
		ft.tick(fps)

def unlock(option,calculator_exp,music_menu,music_sound,task_add,task_text,colors,image_pos):
	numbers=[]
	for i in range(40):
		numbers.append(0)
	pos_x=[5]
	temp_number=5
	while (pos_x[len(pos_x)-1]<1000):
		temp_number=temp_number+25
		pos_x.append(temp_number)
	pos_y=[]
	message=""
	limit=random.randint(2,10)
	for i in range(limit):
		message+=chr(random.randint(97,122))
	print(message)
	user_message=""
	for i in range(40):
		temp_1=0
		while temp_1==0:
			temp_number=random.randint(20,180)
			if temp_number%20==0:
				temp_1=3
		pos_y.append(-temp_number)
	state=True
	while state:
		theme_bg,theme_fg=get_theme_color()
		#print(theme_bg,colors[theme_bg])
		surface.fill(colors[theme_bg])
		for event in pygame.event.get():
			if event.type==QUIT:
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==pygame.K_F10:
					pygame.quit()
					sys.exit()
				if event.key==pygame.K_BACKSPACE:
					if len(user_message)>0:
						temp=list(user_message)
						user_message=""
						for i in range(0,len(temp)-1):
							user_message+=temp[i]
				if event.key==pygame.K_a:
					user_message+="a"
				if event.key==pygame.K_b:
					user_message+="b"
				if event.key==pygame.K_c:
					user_message+="c"
				if event.key==pygame.K_d:
					user_message+="d"
				if event.key==pygame.K_e:
					user_message+="e"
				if event.key==pygame.K_f:
					user_message+="f"
				if event.key==pygame.K_g:
					user_message+="g"
				if event.key==pygame.K_h:
					user_message+="h"
				if event.key==pygame.K_i:
					user_message+="i"
				if event.key==pygame.K_j:
					user_message+="j"
				if event.key==pygame.K_k:
					user_message+="k"
				if event.key==pygame.K_l:
					user_message+="l"
				if event.key==pygame.K_m:
					user_message+="m"
				if event.key==pygame.K_n:
					user_message+="n"
				if event.key==pygame.K_o:
					user_message+="o"
				if event.key==pygame.K_p:
					user_message+="p"
				if event.key==pygame.K_q:
					user_message+="q"
				if event.key==pygame.K_r:
					user_message+="r"
				if event.key==pygame.K_s:
					user_message+="s"
				if event.key==pygame.K_t:
					user_message+="t"
				if event.key==pygame.K_u:
					user_message+="u"
				if event.key==pygame.K_v:
					user_message+="v"
				if event.key==pygame.K_w:
					user_message+="w"
				if event.key==pygame.K_x:
					user_message+="x"
				if event.key==pygame.K_y:
					user_message+="y"
				if event.key==pygame.K_z:
					user_message+="z"
				if event.key==pygame.K_RETURN:
					if user_message==message:
						state=False
		print(message,user_message)
		t1=threading.Thread(target=start_collision,args=(surface,numbers,pos_x,pos_y,message,colors[theme_fg]))
		t2=threading.Thread(target=garbage,args=())
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		pygame.display.update()
		ft.tick(fps)
	home(option,calculator_exp,music_menu,music_sound,task_add,task_text,colors,image_pos)
#home(option,calculator_exp,music_menu,music_sound,task_add,task_text)
unlock(option,calculator_exp,music_menu,music_sound,task_add,task_text,colors,image_pos)
