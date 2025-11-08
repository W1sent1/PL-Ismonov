arr = list(map(int, input("Введите числа: ").split()))

duplicates = {}
for i, num in enumerate(arr):
    duplicates[num] = duplicates.get(num, []) + [i]

for num, indices in duplicates.items():
    if len(indices) > 1:
        print(f"Число {num}: индексы {indices}")