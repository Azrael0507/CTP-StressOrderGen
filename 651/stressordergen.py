# -*- coding: utf-8 -*-
from MyApi import *
import time
import thosttraderapi as api




#print(oneturnsleep)
#print(EXCHANGEID)

invlist = {}
if (EXCHANGEID in ['SHFE', 'INE']):
	offsetpara = 3
else:
	offsetpara = 1


def main():
	with open ('investorlist.txt', 'r') as investorlist:
		typecount = 0
		for line in investorlist.readlines():
			invid = line.strip()
			if (typecount % 2 == 0):
				invlist[invid] = [None, 0, 0]
			else:
				invlist[invid] = [None, 1, 0]
			typecount += 1


	#print(invlist)

	print("start login")
	for invid in sorted(invlist.keys()):
		invlist[invid][0] = CTradeApi()
		invlist[invid][0].start(invid)
		while(1):
			if(invlist[invid][0].LoginCheck() == False):
				print("please wait for login")
				time.sleep(1)
			else:
				break
    
	print("login end!")

	if(autoprocess == "1"):
		print("auto next")
	else:
		input("press enter to continue")

	print("start settle confirm")
	for invid in sorted(invlist.keys()):
		invlist[invid][0].ReqSettleInfoConfirm()
		while(1):
			if(invlist[invid][0].SettConfirmCheck() == False):
				print("please wait for settle confirm")
				time.sleep(1)
			else:
				break
	print("settle confirm end")

	if(autoprocess == "1"):
		print("auto next")
	else:
		input("press enter to continue")

	#print(invlist)
	while(1):
		for invid in sorted(invlist.keys()):
			dirt = invlist[invid][1]
			offsetflag = invlist[invid][2]
			invlist[invid][0].ReqOrIn(dirt, offsetflag)
			invlist[invid][1] = invlist[invid][1]^1
			invlist[invid][2] = invlist[invid][2]^offsetpara
		time.sleep(oneturnsleep)








if __name__ == '__main__':
	main()