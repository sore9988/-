import random
i = 0
times = 1000000
w = 0
q = 0
while i < times :
	# 準備三個門
	doors = ["羊", "羊"]
	c = random.randint(0,2)
	doors.insert(c, "車")
	###print("實際上:", doors)
	# 參賽者選一個門
	c = random.randint(0,2)
	###print("參賽者選的:", doors[c])
	del doors[c]
	###print("剩下的門:", doors)
	# 開一隻羊
	doors.remove("羊")
	###print("剩下最後的門:", doors)
	# 確定輸贏
	if doors[0] == "車" :
		w = w + 1
	###	print("You Win !!")
	else :
		q = q + 1
	###	print("You Lose !!")
	i=i+1
ww = w / times * 100
qq = q / times * 100
print("經過", times, "次,贏的機率為" , ww, "%")
