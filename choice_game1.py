import random

while(True):
	
	choice=int(input("[0]剪刀\t[1]布\t[2]石頭\n請出拳:"))
	com=random.randint(0,2)

	dis={ 0:"剪刀", 1:"布", 2:"石頭"}
	print("電腦出:", dis[com])
	print("你出:", dis[choice])
	if choice == com :
		print("平手")
	if choice == (com + 1) % 3:
		print("You lose !!")
	if com == (choice + 1) % 3:
		print("You win !!")
	# elif choice < com & choice + 1 == com :
	# 	print("You win !!")
	# elif choice - 2 == com:
	# 	print("You win !!")

	# elif choice > com & choice - 1 == com :
	# 	print("You lose !!")
	# elif choice + 2 ==com:
	# 	print("You lose !!")
	print()
	continue