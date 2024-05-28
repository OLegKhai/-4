# test_extended_methods.py
import pytest
from cat import Cat, CatArray

# Тести для розширених методів класу CatArray

# Тест для методу clear
def test_clear():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")]
    cat_array = CatArray(cats)
    cat_array.clear()
    assert len(cat_array) == 0



# Тест для методів __iter__ та __next__
def test_iteration():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий"),
            Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")]
    cat_array = CatArray(cats)
    iterator = iter(cat_array)
    assert next(iterator) == cats[0]
    assert next(iterator) == cats[1]

# Тест для методу __delitem__
def test_delitem():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий"),
            Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")]
    cat_array = CatArray(cats)
    del cat_array[0]
    assert len(cat_array) == 1
    assert cat_array[0] == cats[1]

def test_copy():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")]
    cat_array = CatArray(cats)
    cat_array_copy = cat_array.copy()
    assert cat_array.data == cat_array_copy


def test_extend():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")]
    cat_array = CatArray(cats)
    new_cats = [Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")]
    cat_array.extend(new_cats)
    assert len(cat_array) == 2
    assert cat_array.data[-1] == new_cats[0]

if __name__ == "__main__":
    pytest.main([__file__])



# Тест для методу pop
def test_pop():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий"),
            Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")]
    cat_array = CatArray(cats)
    popped_cat = cat_array.pop()
    assert len(cat_array) == 1
    assert popped_cat == cats[-1]

def test_reverse():
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий"),
            Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий")]
    cat_array = CatArray(cats)
    cat_array.reverse()
    assert cat_array[0] == cats[-1]
    assert cat_array[1] == cats[0]

# Тест для методу count
def test_count():
    cat_to_count = Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")
    cats = [cat_to_count,
            Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий"),
            cat_to_count]
    cat_array = CatArray(cats)
    assert cat_array.count(cat_to_count) == 2
