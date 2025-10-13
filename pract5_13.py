text = input("Введите строку: ")
start = text.find('(')
end = text.find(')')

if start != -1 and end != -1 and start < end:
    print(text[start + 1:end])