#!/usr/bin/env python3

coins = [1, 2, 5, 10, 20, 50, 100, 200]


def ways(sum, ind):
    global coins
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    value = 0
    for each in coins[ind:]:
        value += ways(sum-each, coins.index(each))
    return value

print("number of ways: ", ways(200, 0))






# def proceed(left, next):
#     if left < next:
#         return 0
#     elif left == next:
#         return 1
#     else:
#         return proceed(left-next)


# # def countGroup(sum, index):
# #      b


# # sum = 200
# # while sum != 0:
# #     groups = 1

# dic = { 1: 1, 2:1, 5:1, 10:1, 20:1, 50:1, 100:1, 200:1, }

# group = 0
# for i in range(1, 201):
#     if i % 2 == 0:
#         group += 1
#     if i % 5 == 0:
#         group += 1
#     if i % 10 == 0:
#         group += 1
#     if i % 20 == 0:
#         group += 1
#     if i % 50 == 0:
#         group += 1
#     if i % 100 == 0:
#         group += 1
#     if i % 200 == 0:
#         group += 1


# print("Groups: ", group)


# dic = { 1: 1, 2:1, 5:1, 10:1, 20:1, 50:1, 100:1, 200:1, }

# group = 0
# for i in range(1, 201):
#     if i % 2 == 0:
#         group += 1 * dic[2]
#         dic[2] = group
#     if i % 5 == 0:
#         group += 1 * dic[5]
#         dic[5] = group
#     if i % 10 == 0:
#         group += 1 * dic[10]
#         dic[10] = group
#     if i % 20 == 0:
#         group += 1 * dic[20]
#         dic[20] = group
#     if i % 50 == 0:
#         group += 1 * dic[50]
#         dic[50] = group
#     if i % 100 == 0:
#         group += 1 * dic[100]
#         dic[100] = group
#     if i % 200 == 0:
#         group += 1 * dic[200]
#         dic[200] = group
# print(dic)
# print("Groups: ", group)
