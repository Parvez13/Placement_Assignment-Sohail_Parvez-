def return_largest(digits):
        number = ''.join(str(x) for x in digits)
        number = int(number)+ 1
        number_list = [str(i) for i in str(number)]
        return number_list

if __name__ == '__main__':
    digits = [9,9,9,9,9]
    sol = return_largest(digits)
    print(sol)