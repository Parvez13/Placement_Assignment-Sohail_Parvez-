def reverse_kelements(s, k):
    def swap(text, left, right):
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1


    i = 0
    arr = list(s)

    while i < len(s):
        j = min(i+k-1, len(s)-1)
        swap(arr, i, j)
        i += 2*k
    return "".join(arr)
        

string = "geeksforgeeks"
k = 2
print(reverse_kelements(string, k))