array = [[8, 02, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7,
         78, 52, 12, 50, 77, 91, 8]]
array.append([49, 49, 99, 40, 17, 81, 18,
              57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00])
array.append([81, 49, 31, 73, 55, 79, 14,
              29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65])
array.append([52, 70, 95, 23, 04, 60, 11,
             42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91])
array.append([22, 31, 16, 71, 51, 67, 63,
             89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80])
array.append([24, 47, 32, 60, 99, 03, 45,
             02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50])
array.append([32, 98, 81, 28, 64, 23, 67,
             10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70])
array.append([67, 26, 20, 68, 02, 62, 12,
             20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21])
array.append([24, 55, 58, 05, 66, 73, 99,
             26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72])
array.append([21, 36, 23, 9, 75, 0, 76,
             44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95])
array.append([78, 17, 53, 28, 22, 75, 31,
             67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92])
array.append([16, 39, 5, 42, 96, 35, 31,
             47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57])
array.append([86, 56, 0, 48, 35, 71, 89,
             7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58])
array.append([19, 80, 81, 68, 5, 94, 47,
             69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40])
array.append([04, 52, 8, 83, 97, 35, 99,
             16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66])
array.append([88, 36, 68, 87, 57, 62, 20,
             72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69])
array.append([04, 42, 16, 73, 38, 25, 39,
             11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36])
array.append([20, 69, 36, 41, 72, 30, 23,
             88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16])
array.append([20, 73, 35, 29, 78, 31, 90,
             01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54])
array.append([01, 70, 54, 71, 83, 51, 54,
             69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48])


def finder(n):
    found = 0
    for i in range(len(n)):
        for each in range(len(n[i])):

            # for the down product
            product = 1
            for index in range(4):
                try:
                    product *= n[index+i][each]
                except:
                    pass
            if product > found:
                found = product
            # for forward product
            if (each + 4) < len(n[i]):
                product = 1
                for index in range(4):
                    product *= n[i][each + index]
                if product > found:
                    found = product

                # for diagonal product

            product = 1
            for index in range(4):
                try:
                    product *= n[i-index][each+index]
                except:
                    pass
            if product > found:
                found = product

            product = 1
            if each-2:
                for index in range(4):
                    try:
                        product *= n[i+index][each-index]
                    except:
                        pass
            if product > found:
                found = product
    return found
print finder(array)
