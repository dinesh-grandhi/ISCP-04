n = int(input())
count = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    if x > 0 and y > 0:
        count += 1
print('{:.6f}'.format(count / n))