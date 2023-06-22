def reverse_string(string):
    words = string.split()
    ans = ''
    for i in range(len(words)):
        ans += words[i][::-1]
        if i != len(words)-1:
            ans += ' '
    return ans


string = "Let's take LeetCode contest"
print(reverse_string(string))