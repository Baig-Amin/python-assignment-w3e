numbers = [12, 75, 150, 180, 145, 525, 50]


condition1 = [i for i in numbers if i%5==0]
# print(condition1)

for num in condition1:

    if num > 500:
        break
    elif num > 150:
        continue
    else:
        print(num,end = "")

