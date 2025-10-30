def input_matrix_dimensions():
    """
    Ввод размерности матрицы с проверкой корректности
    """
    while True:
        try:
            n = int(input("Введите количество строк матрицы (n): "))
            m = int(input("Введите количество столбцов матрицы (m): "))
            
            if n <= 0 or m <= 0:
                print("Ошибка: размерности должны быть положительными числами!")
                continue
                
            return n, m
            
        except ValueError:
            print("Ошибка: введите целые числа для размерности матрицы!")

def input_matrix_elements(n, m):
    """
    Ввод элементов матрицы построчно
    """
    matrix = []
    print(f"\nВведите элементы матрицы {n}×{m} построчно:")
    
    for i in range(n):
        while True:
            try:
                row_input = input(f"Строка {i+1}: ")
                row_elements = list(map(float, row_input.split()))
                
                if len(row_elements) != m:
                    print(f"Ошибка: необходимо ввести ровно {m} элементов!")
                    continue
                    
                matrix.append(row_elements)
                break
                
            except ValueError:
                print("Ошибка: введите вещественные числа, разделенные пробелами!")
    
    return matrix

def print_matrix_by_columns(matrix, n, m):
    """
    Вывод матрицы по столбцам
    """
    print("\n" + "="*50)
    print("МАТРИЦА ПО СТОЛБЦАМ:")
    print("="*50)
    
    for j in range(m):
        column = []
        for i in range(n):
            column.append(matrix[i][j])
        print(f"Столбец {j+1}: {column}")

def print_original_matrix(matrix):
    """
    Вывод исходной матрицы для сравнения
    """
    print("\n" + "="*50)
    print("ИСХОДНАЯ МАТРИЦА (по строкам):")
    print("="*50)
    for i, row in enumerate(matrix):
        print(f"Строка {i+1}: {row}")

def main():
    """
    Основная функция программы
    """
    print("ПРОГРАММА 'MATRIX INPUT-OUTPUT'")
    print("=" * 40)
    print("Назначение: ввод матрицы построчно, вывод по столбцам")
    print("=" * 40)
    
    # Ввод размерности матрицы
    n, m = input_matrix_dimensions()
    
    # Ввод элементов матрицы
    matrix = input_matrix_elements(n, m)
    
    # Вывод исходной матрицы
    print_original_matrix(matrix)
    
    # Вывод матрицы по столбцам
    print_matrix_by_columns(matrix, n, m)
    
    print("\n" + "="*50)
    print("Программа завершена успешно!")
    print("="*50)

if __name__ == "__main__":
    main()
