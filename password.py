x = 3
while x > 0 :
	x = x - 1
	password = input('請輸入密碼')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		print('密碼錯誤')
		if x > 0:
			print('還有', x,'次機會')
		else :
			print('帳號已鎖住！請臨櫃辦理')