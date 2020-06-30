import random

start = input('輸入起始值: ')
end = input('輸入最末值: ')

r = random.randint(int(start),int(end))
i = 0
while True:
	num = input('請猜數字: ')
	num = int(num)
	i = i + 1
	if num == r :
		print('這是第 ', i, ' 次猜數字')
		print('恭喜正確!!')
		break
	elif num > r :
		print('正確答案小於 ', num)
	elif num < r :
		print('正確答案大於 ', num)
	print('這是第 ', i, ' 次猜數字')