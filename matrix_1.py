a = []
n = int(input())
for i in range(n):
    a.append([0]*n)


# for i in a:
#     print(i)

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 3
        elif i < j:
            a[i][j] = 5
        elif i > j:
            a[i][j] = 2


for i in a:
    print(i)
