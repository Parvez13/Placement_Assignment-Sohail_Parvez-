def maxHarmonicSeries(arr):
    freq = {}
    max_length = 0
    #Count each number frequence
    for i in range(len(arr)):
        freq[i] = freq.get(i, 0)+1
    # Check for harmonious subsequences
    for num in freq:
        if num + 1 in freq:
            print(num+1)
            length = freq[num] + freq[num + 1]
            max_length = max(max_length, length)

    return max_length
# TC: O(N+N)-> O(2N)-> O(N)
# SC: O(N)
arr =  [1,3,2,2,5,2,3,7]
print(maxHarmonicSeries(arr))