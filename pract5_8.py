text = input("Введите строку, заканчивающуюся точкой: ")

text = text.rstrip('.')
words = text.split()

word_count = len(words)

print(f"Количество слов в строке: {word_count}")