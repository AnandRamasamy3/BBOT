def get_encoded_alphabet(alpha):
	code=""
	#print(alpha)
	if alpha=='a' or alpha=='A':
		code="03"
	elif alpha=="b" or alpha=="B":
		code="60"
	elif alpha=="c" or alpha=="C":
		code="21"
	elif alpha=="d" or alpha=="D":
		code="06"
	elif alpha=="e" or alpha=="E":
		code="22"
	elif alpha=="f" or alpha=="F":
		code="80"
	elif alpha=="g" or alpha=="G":
		code="91"
	elif alpha=="h" or alpha=="H":
		code="47"
	elif alpha=="i" or alpha=="I":
		code="11"
	elif alpha=="j" or alpha=="J":
		code="02"
	elif alpha=="k" or alpha=="K":
		code="12"
	elif alpha=="l" or alpha=="L":
		code="10"
	elif alpha=="m" or alpha=="M":
		code="07"
	elif alpha=="n" or alpha=="N":
		code="70"
	elif alpha=="o" or alpha=="O":
		code="01"
	elif alpha=="p" or alpha=="P":
		code="09"
	elif alpha=="q" or alpha=="Q":
		code="90"
	elif alpha=="r" or alpha=="R":
		code="37"
	elif alpha=="s" or alpha=="S":
		code="50"
	elif alpha=="t" or alpha=="T":
		code="16"
	elif alpha=="u" or alpha=="U":
		code="41"
	elif alpha=="v" or alpha=="V":
		code="42"
	elif alpha=="w" or alpha=="W":
		code="44"
	elif alpha=="x" or alpha=="X":
		code="08"
	elif alpha=="y" or alpha=="Y":
		code="40"
	elif alpha=="z" or alpha=="Z":
		code="20"
	elif alpha==" ":
		code="00"
	else:
		code="88"
	return code