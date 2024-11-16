HTML_END = ".html" # объявляем константу

input_string = list(input("Введите строки: ").split()) # считываем строку

need_items = [item for item in input_string if item.endswith(HTML_END)]
# оставляем только нужные
print(*need_items) # выводим нужные на экран