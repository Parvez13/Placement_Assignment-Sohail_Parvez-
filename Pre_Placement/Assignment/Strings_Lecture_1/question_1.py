# Ismorphic strings should be equal in length
def is_ismorphic(s, t):
    if len(s) != len(t):
        return False 
    
    mapping = {}
    mapped = set()
    for c in range(len(s)):
        if s[c] not in mapping:
            if t[c] in mapped:
                return False 
            mapping[s[c]] = t[c]
            mapped.add(t[c])
        else:
            if mapping[s[c]] != t[c]:
                return False 
    return True 

s = 'egg'
t = 'add'
print(is_ismorphic(s,t))