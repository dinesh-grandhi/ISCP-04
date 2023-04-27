# Chappu is addicted to Paneer! She just wants all the dishes to be prepared with Paneer.

# Nikau wants to keep her happy for n days. In order to be happy in i-th day, she needs to eat exactly a[i] kilograms of Paneer.

# There is a big shop uptown and Nikau wants to buy Paneer for her from there. In i-th day, they sell Paneer for pi dollars per kilogram.

# Nikau knows all numbers a1,...,an and p1,...,pn. In each day, he can buy arbitrary amount of Paneer, also he can keep some Paneer he has for the future.

# Nikau is a little tired from cooking Paneer, so he asked for your help. Help him to minimize the total money he spends to keep Chappu happy for n days.
n = int(input())
a = []
p = []
for i in range(n):
    a_i, p_i = map(int, input().split())
    a.append(a_i)
    p.append(p_i)

for i in range(n-1):
    if p[i] < p[i+1]:
        p[i+1] = p[i]

min_cost = sum([a[i] * p[i] for i in range(n)])
print(min_cost)
