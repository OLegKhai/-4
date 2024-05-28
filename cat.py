from typing import List, Union, Iterable
from abstractstructure import AbstractCatArray

class Cat:
    def __init__(self, name: str, breed: str, color: str, age: Union[int, float], weight: Union[int, float], category: str) -> None:
        self.name = name
        self.breed = breed
        self.color = color
        if isinstance(age, (int, float)):
            self.age = round(float(age), 1)
        else:
            raise ValueError("Age must be a number")
        if isinstance(weight, (int, float)):
            self.weight = round(float(weight), 1)
        else:
            raise ValueError("Weight must be a number")
        self.category = category

    def __repr__(self) -> str:
        return f"Cat({self.name}, {self.breed}, {self.color}, {self.age}, {self.weight}, {self.category})"
    
    def __eq__(self, other):
        if isinstance(other, Cat):
            return (
                self.name == other.name and
                self.breed == other.breed and
                self.color == other.color and
                self.age == other.age and
                self.weight == other.weight and
                self.category == other.category
            )
        return False

class CatArray(AbstractCatArray):
    def __init__(self, initial_data: List[Cat] = None) -> None:
        if initial_data is None:
            self.data = []
        else:
            self.data = list(initial_data)

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return repr(self.data)

    def __getitem__(self, index: int) -> Cat:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]

    def __setitem__(self, index: int, value: Cat) -> None:
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        self.data[index] = value

    def append(self, value: Cat) -> None:
        self.data.append(value)

    def insert(self, index: int, value: Cat) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of range")
        self.data.insert(index, value)

    def index(self, value: Cat, start: int = 0, stop: int = None) -> int:
        if stop is None:
            stop = len(self.data)
        for i in range(start, stop):
            if self.data[i] == value:
                return i
        raise ValueError(f"{value} is not in list")

    def remove(self, value: Cat) -> None:
        for i in range(len(self.data)):
            if self.data[i] == value:
                del self.data[i]
                return
        raise ValueError(f"{value} not found in list")
    
    def clear(self) -> None:
        self.data = []

    def copy(self) -> list:
        return self.data.copy()

    def __iter__(self) -> Iterable:
        return iter(self.data)

    def __next__(self) -> Cat:
        raise NotImplementedError("Custom iterator not implemented for CatArray")

    def __delitem__(self, key) -> None:
        del self.data[key]

    def extend(self, values: Iterable[Cat]) -> None:
        self.data.extend(values)

    def pop(self, index: int = -1) -> Cat:
        return self.data.pop(index)

    def reverse(self) -> None:
        self.data.reverse()

    def count(self, value: Cat) -> int:
        return self.data.count(value)

# Пример использования:
if __name__ == "__main__":
    cats = [Cat("Барсик", "Персидська", "білий", 0.3, 1.5, "довгошерстий")]
    cat_array = CatArray(cats)
    print(cat_array)
    cat_array.append(Cat("Мурзик", "Сіамська", "сірий", 2, 4.5, "короткошерстий"))
    print(cat_array)
    print(cat_array.index(cats[0]))
    cat_array.remove(cats[0])
    print(cat_array)
