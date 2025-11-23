def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = []
        for line in lines:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
        return matrix

def write_results_to_file(filename, results):
    with open(filename, 'w') as file:
        for result in results:
            file.write(result + '\n')

def find_min_in_even_rows(matrix):
    results = []
    results.append("1. Наименьшие элементы четных строк:")
    for i in range(1, len(matrix), 2):
        min_element = min(matrix[i])
        results.append(f"Строка {i+1}: {min_element}")
    return results

def swap_min_max_elements(matrix):
    results = []
    
    flat_matrix = [element for row in matrix for element in row]
    min_val = min(flat_matrix)
    max_val = max(flat_matrix)
    
    results.append(f"\n2. Исходные значения:")
    results.append(f"Наименьший элемент: {min_val}")
    results.append(f"Наибольший элемент: {max_val}")
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min_val:
                matrix[i][j] = max_val
            elif matrix[i][j] == max_val:
                matrix[i][j] = min_val
    
    results.append(f"\nМатрица после замены:")
    for row in matrix:
        results.append(' '.join(map(str, row)))
    
    return results, matrix

def main():
    filename_input = "Исмонов_Хакимджон_Мукимджонович_УБ-52_vvod.txt"
    filename_output = "Исмонов_Хакимджон_Мукимджонович_УБ-52_vivod.txt"
    
    try:
        matrix = read_matrix_from_file(filename_input)
        
        results = []
        results.append("Исходная матрица:")
        for row in matrix:
            results.append(' '.join(map(str, row)))
        
        results.extend(find_min_in_even_rows(matrix))
        
        swap_results, modified_matrix = swap_min_max_elements(matrix.copy())
        results.extend(swap_results)
        
        write_results_to_file(filename_output, results)
        
        print("Результаты успешно записаны в файл", filename_output)
        
    except FileNotFoundError:
        print("Файл не найден!")
    except Exception as e:
        print("Ошибка:", e)

def create_test_file():
    test_matrix = [
        [3, 7, 2, 8],
        [1, 5, 9, 4],
        [6, 2, 8, 3],
        [7, 1, 4, 6],
        [2, 9, 5, 1]
    ]
    
    with open("Исмонов_Хакимджон_Мукимджонович_УБ-52_vvod.txt", 'w') as file:
        for row in test_matrix:
            file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    create_test_file()
    
    main()