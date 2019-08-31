# if_sampple07.py

num = input('正の整数を入力してください:')

num = int(num)

if num > 0:
	if num % 2 == 0:
		print('正の偶数')
	else:
		print('正の奇数')
	print('処理を終了します')
else:
	print('正の数を入力してください')



