import os

# os.makedirs("C:/1/test",exist_ok=True) #2ой аргумент нужен если допускаем, что создаваемая папка уже есть

my_dir = "D:/"
content = os.listdir(my_dir)
# print(content)

list_txt_files = []

for item in content:
    # item - это либо файл, либо папка
    # 1) Проверяем, что item это файл, а не папка
    # 2) Если элемент - файл, то проверяем расширение файла

    if os.path.isfile(os.path.join(my_dir,item)) and item.endswith(".txt"):
        list_txt_files.append(item)
print(list_txt_files)
