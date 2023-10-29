# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
name = "Alex"
age = 26
city = "Minsk"
text1 = "Hello my name %s, my age %d, l live city %s" % (name, age, city)
text2 = "Hello my name {}, my age {}, l live city {}".format(name, age, city)
text3 = f"Hello my name {name}, my age {age}, l live city {city}"
print(text1)
print(text2)
print(text3)
