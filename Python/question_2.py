def isValidString(s):
    # Count the frequency of each character in the string
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Count the frequencies of the character frequencies
    freq_count = {}
    for freq in char_freq.values():
        freq_count[freq] = freq_count.get(freq, 0) + 1

    # If all characters have the same frequency, it is a valid string
    if len(freq_count) == 1:
        return "YES"
    # If there are exactly two frequencies and one occurs only once, removing one character will make it valid
    elif len(freq_count) == 2 and (1 in freq_count.values() and freq_count[1] == 1):
        return "YES"
    else:
        return "NO"

# Test Cases
print(isValidString("abc"))  # Output: YES
print(isValidString("abcc"))  # Output: NO
print(isValidString("aabbc"))  # Output: YES
print(isValidString("aabbccd"))  # Output: YES
