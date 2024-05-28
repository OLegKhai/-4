from abc import ABC, abstractmethod
from typing import Any, Iterable


class AbstractCatArray(ABC):
    @abstractmethod
    def __init__(self, initial_data: list = None) -> None:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> Any:
        pass

    @abstractmethod
    def __setitem__(self, index: int, value: Any) -> None:
        pass

    @abstractmethod
    def append(self, value: Any) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, value: Any) -> None:
        pass

    @abstractmethod
    def index(self, value: Any, start: int = 0, stop: int = None) -> int:
        pass

    @abstractmethod
    def remove(self, value: Any) -> None:
        pass

class AbstractStructureExtended(AbstractCatArray):
    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def copy(self) -> list:
        pass

    @abstractmethod
    def __iter__(self) -> Iterable:
        pass

    @abstractmethod
    def __next__(self) -> Any:
        pass

    @abstractmethod
    def __delitem__(self, key) -> None:
        pass

    @abstractmethod
    def extend(self, values: Iterable) -> None:
        pass

    @abstractmethod
    def pop(self, index: int = -1) -> Any:
        pass

    @abstractmethod
    def reverse(self) -> None:
        pass

    @abstractmethod
    def count(self, value: Any) -> int:
        pass
