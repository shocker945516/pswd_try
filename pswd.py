pswd = 'a123456'
count = 3
while True:
	x = input('Please enter the password: ')
	if x == pswd:
		print('Login successfully!')
		break
	else:
		count = count - 1
		print('Incorrect password. You can try ', count, ' more time(s).')
		if count == 0:
			print('You can try up to 3 times!')
			break
