def find_armstrong_numbers(k):
    print(f"Числа Армстронга от 1 до {k}:")
    for num in range(1, k + 1):
        digits = [int(d) for d in str(num)]
        n = len(digits)
        sum_of_powers = sum(d ** n for d in digits)
        
        if sum_of_powers == num:
            print(num)

# Ввод данных и вызов функции
k = int(input("Введите k: "))
find_armstrong_numbers(k)