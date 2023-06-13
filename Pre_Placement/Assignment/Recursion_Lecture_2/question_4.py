def stringLength(str):
	if str == '':
		return 0
	return 1+stringLength(str[1:])

str = "SohailParvez"
print(stringLength(str))