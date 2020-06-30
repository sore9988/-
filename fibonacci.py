
fibo=[1,1]
i=2
while True:
	fibo=fibo+[1]
	fibo[i] = int(fibo[i - 1]) + int(fibo[i - 2])
	if int(fibo[i]) > 1000:
		break
	i=i+1
print("費氏數列:\t", fibo)