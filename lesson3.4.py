#Пользователь вводит 3 числа, сказать сколько из них положительных
#и сколько отрицательных
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
a_is_positive = a > 0
b_is_positive = b > 0
c_is_positive = c > 0
positive_count = a_is_positive + b_is_positive + c_is_positive
print(positive_count)
