import random
r = random.randint (1, 100)
count = 0
while True:
	count += 1 #count = count +1
	num = input('請猜數字:')
	num = int(num)
	if r == num:
		print ('終於猜對了!')
		print ('這是你猜的第', count, '次')
		break #逃出迴圈
	elif r > num:
		print ('比答案小')
	elif r < num:
		print ('比答案大')
	print ('這是你猜的第', count, '次')