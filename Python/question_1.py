def frequence_count(string):
    words = string.split()
    word_freq = {}
    for item in words:
        if item in word_freq:
            word_freq[item] += 1
        else:
            word_freq[item] = 1
    longest_key = max(word_freq, key=word_freq.get)
    return len(longest_key)

frequence_count("My name is bob bob and my best fiend name is alex alex alex")
    