arr = [int(input(f"Элемент {i+1}: ")) for i in range(8)]

print("Исходный массив:", arr)

arr = [x * 2 if x < 15 else x for x in arr]

print("Преобразованный массив:", arr)