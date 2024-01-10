def filter_strings(arr):
    # Фильтрация строк и создание нового массива
    return [s for s in arr if len(s) <= 3]

# Примеры использования
input_array1 = ["Hello", "2", "world", ":-)"]
input_array2 = ["1234", "1567", "-2", "computer science"]
input_array3 = ["Russia", "Denmark", "Kazan"]

output_array1 = filter_strings(input_array1)
output_array2 = filter_strings(input_array2)
output_array3 = filter_strings(input_array3)

print(output_array1)  # ['2', ':-)']
print(output_array2)  # ['-2']
print(output_array3)  # []
