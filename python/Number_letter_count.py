dictionary = {1: 3,
              2: 3,
              3: 5,
              4: 4,
              5: 4,
              6: 3,
              7: 5,
              8: 5,
              9: 4,
              10: 3,
              11: 6,
              12: 6,
              13: 8,
              14: 8,
              15: 7,
              16: 7,
              17: 9,
              18: 8,
              19: 8,
              20: 6,
              30: 6,
              40: 5,
              50: 5,
              60: 5,
              70: 7,
              80: 6,
              90: 6}

numbers = range(1, 1001)


def main():
    total = 0
    for each in numbers:
        num = each
        each = str(each)
        if len(each) < 2:  # for all the ones numbers
            tmp = dictionary[int(each)]
            total += tmp

        elif len(each) == 2:  # meaning the tens numbers
            if num in dictionary:
                tmp = dictionary[num]
                total += tmp
            else:
                tmp = (dictionary[int(each[0]+"0")] +
                       dictionary[int(each[-1])])
                total += tmp
        elif len(each) == 3:
            tmp = dictionary[int(each[0])] + 7
            total += tmp
            if not int(each[1:]) == 0:
                if int(each[1:]) in dictionary:
                    tmp = dictionary[int(each[1:])]
                    total += tmp + 3
                else:
                    total += (dictionary[int(each[-2]+"0")] +
                              dictionary[int(each[-1])]) + 3
        else:
            total += 11
    print total

main()
hundred = 7
andd = 3
thousand = 8
total_and = 9 * 99 * andd
total_hundred = 900 * hundred
tens = 0


# for each in (10, 20, 30, 40, 50, 60, 70, 80, 90):
#     tens += dictionary[each] * 100
# ones = 0
# for each in (1, 2, 3, 4, 5, 6, 7, 8, 9):
#     ones += 91 * dictionary[each]
# total_eleven = 0
# for each in (11, 12, 13, 14, 15, 16, 17, 18, 19):
#     total_eleven += dictionary[11] * 10
#     grandtotal = (total_and + total_eleven + total_hundred
#                   + tens + ones + 11)
# print grandtotal


# def counter(number):
#     length = len(str(number))
#     if length < 3:
#         if number in dictionary and number not in (100, 1000):
#             return dictionary[number]
#         else:
#             return (dictionary[int((str(number)[0] + '0'))] +
#                     dictionary[int(str(number)[-1])])
#     elif number == 1000:
#         return 11
#     else:
#         try:
#             last = counter(int(str(number)[1:]))
#             return last + 10 + dictionary[int(str(number)[0])]
#         except:
#             return 7 + dictionary[int(str(number)[0])]
# sum = 0
# for each in range(1, 1001):
#     print each, counter(each)
#     sum += counter(each)
# print sum
