# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text = "this is a test message for sep"
text2 = text.replace(" ", "-")
print(text2)

text_list = text.split(" ")
print(text_list)
print("-".join(text_list))
