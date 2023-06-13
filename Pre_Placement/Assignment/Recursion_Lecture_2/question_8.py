# def countConsonants(string):
# 	consonants = 0
# 	vowels = 0
# 	for i in string:
# 		if i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u':
# 			vowels = vowels+1;
# 		else:
# 			consonants = consonants+1
# 	return consonants
def check_consonant(x):
	x = x.lower()
	return not(x=='a' or x=='e' or x=='i'or 
				x=='o' or x=='u')

def count_consonants(string,n):

	if n == 1:
		return check_consonant(string[0])

	return count_consonants(string, n-1)+check_consonant(string[n-1])


string = "GEEKSFORGEEKS PORTAL"
print(count_consonants(string,20))