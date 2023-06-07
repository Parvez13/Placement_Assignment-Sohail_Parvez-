def toString(List):
    return ''.join(List)

def permutationOfString(string, l, r):
    if l == r:
        print(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            print(a[l],a[i])
            permutationOfString(a, l+1, r)
            a[l], a[i] = a[i], a[l]  # backtrack
string="ABC"
n = len(string)
a = list(string)
print(permutationOfString(a,0,n))
