class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)
        max_no, min_no = s_num, s_num
        
        ## Attempt 2
        for digit in s_num:
            if digit != '9':
                max_no = s_num.replace(digit, '9')
                break
        
        first_digit = s_num[0]
        if first_digit == '1':
            for digit in s_num:
                if digit != '1' and digit != '0':
                    min_no = s_num.replace(digit, '0')
                    break
        else:
            min_no = s_num.replace(first_digit, '1')

        return int(max_no) - int(min_no)




        ## Attemp 1, 45% test cases passed 
        # count = collections.Counter(s_num)

        # ## case of 555, 111
        # if (len(count)) == 1:
        #     no_digits = len(s_num)
        #     a = int('9' * no_digits) # string multiplication
        #     b = int('1' * no_digits)
        #     return a - b

        # ## Other cases
        # first_digit = s_num[0]
        # max_digit = max(count, key=count.get)
        # print(first_digit, max_digit)

        # if first_digit == max_digit:
        #     j = '1'
        # else:
        #     j = '0'

        # replace_nine = s_num.replace(max_digit, '9')
        # replace_one = s_num.replace(max_digit, j)
        # print(replace_nine, replace_one)

        # return int(replace_nine) - int(replace_one)

#  1432. Max Difference You Can Get From Changing an Integer
