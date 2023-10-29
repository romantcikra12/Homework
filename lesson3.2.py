# Пользователь вводит 3 числа, найти среднее арифмитическое с точностью 3

from statistics import mean

m = [3]
n = int(input())
for i in range(n):
    m.append(int(input()))
print(mean(m))
