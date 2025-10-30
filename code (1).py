    print("\n" + "="*50)
    print("ИСХОДНАЯ МАТРИЦА (по строкам):")
    print("="*50)
    for i, row in enumerate(matrix):
        print(f"Строка {i+1}: {row}")

def main():

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


