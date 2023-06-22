def is_strabogrammatic(num):
    if type(num) != str:
        return False 
    d = {'0': '0', '1': '1', '8' : '8', '9' : '6', '6': '9'}
    left, right = 0, len(num)-1
    while left <= right:
        if(num[left] not in d) or (d[num[left]] != num[right]):
            return False
        left += 1
        right -= 1
    return True

num = 1906
print(is_strabogrammatic(num))
    