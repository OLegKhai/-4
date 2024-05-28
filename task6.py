import time
from cat import Cat, CatArray

# Генератор об'єктів для створення кішок
def generate_cats(num):
    for i in range(num):
        yield Cat(f"Cat {i}", "Unknown", "Unknown", 0, 0, "Unknown")

if __name__ == "__main__":
    # Швидкість додавання всіх об'єктів на початок структури даних
    cat_array = CatArray()
    start_time = time.time()
    for cat in generate_cats(10000):
        cat_array.insert(0, cat)
    end_time = time.time()
    elapsed_time_start = end_time - start_time
    print(f"Час додавання 10 000 кішок на початок масиву: {elapsed_time_start} секунд")
    

    cat_array = CatArray()
    # Швидкість додавання всіх об'єктів в кінець структури даних
    start_time = time.time()
    for cat in generate_cats(10000):
        cat_array.append(cat)
    end_time = time.time()
    elapsed_time_reset = end_time - start_time

    print(f"Час додавання 10 000 кішок на початок масиву після очищення та перестворення: {elapsed_time_reset} секунд")


    # Швидкість зміни об'єкта з центральним індексом за допомогою присвоєння всім 10 000 елементам по черзі
    cat_array = CatArray()
    start_time = time.time()
    for i, cat in enumerate(generate_cats(10000)):
        if i == 5000 and i < len(cat_array):  # Перевірка діапазону індексу
            cat_array[i] = cat
    end_time = time.time()
    elapsed_time_change = end_time - start_time
    print(f"Час зміни об'єкта з центральним індексом: {elapsed_time_change} секунд")

    # Швидкість пошуку першого, останнього та центрального об'єктів
    start_time = time.time()
    if len(cat_array) > 0:
        idx_first = cat_array.index(cat_array[0])
        idx_last = cat_array.index(cat_array[-1])
        idx_middle = cat_array.index(cat_array[5000])
    end_time = time.time()
    elapsed_time_search = end_time - start_time
    print(f"Час пошуку першого, останнього та центрального об'єктів: {elapsed_time_search} секунд")

    # Швидкість доступу до об'єкта за вказаним індексом
    start_time = time.time()
    if len(cat_array) > 5000:
        cat_array[5000]
    end_time = time.time()
    elapsed_time_access = end_time - start_time
    print(f"Час доступу до об'єкта за вказаним індексом: {elapsed_time_access} секунд")

    # Швидкість видалення елементів з початку та з кінця
    start_time = time.time()
    if len(cat_array) > 0:
        cat_array.pop(0)
        cat_array.pop()
    end_time = time.time()
    elapsed_time_remove = end_time - start_time
    print(f"Час видалення елементів з початку та з кінця: {elapsed_time_remove} секунд")
