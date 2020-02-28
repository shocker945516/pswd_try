pswd = 'a123456'
count = 3
while count > 0:
	x = input('Enter password: ')
	if x == pswd:
		print('Login successfully!')
		break
	else:
		count = count - 1
		print('Incorrect password. You can try', count, 'more time(s).')
