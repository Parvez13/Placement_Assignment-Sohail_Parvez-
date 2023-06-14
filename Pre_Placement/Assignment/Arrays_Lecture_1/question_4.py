def return_largest(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_length = len(digits)
        
        i = digit_length - 1
        
        while digits[i] == 9 and i >= 0:
            i -= 1
        
        if i == -1:
            results = [0]*(digit_length + 1)
            results[0] = 1
            return results
        
        results = [0]*(digit_length)
        
        results[i] = digits[i] + 1
        
        for j in range(i-1, -1, -1):
            results[j] = digits[j]
        
        return results

if __name__ == '__main__':
    digits = [9,9,9,9,9]
    sol = return_largest(digits)
    print(sol)
