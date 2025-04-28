from typing import TypeVar, Generic, Dict, Iterator, Tuple

K = TypeVar("K")  # Type for keys
V = TypeVar("V")  # Type for values


class Bijection(Generic[K, V]):
    def __init__(self):
        self._forward: Dict[K, V] = {}
        self._backward: Dict[V, K] = {}

    def __getitem__(self, key: K) -> V:
        return self._forward[key]

    def __setitem__(self, key: K, value: V) -> None:
        if key in self._forward:
            raise KeyError(f"Key {key} already exists")
        if value in self._backward:
            raise ValueError(f"Value {value} already exists")
        self._forward[key] = value
        self._backward[value] = key

    def __delitem__(self, key: K) -> None:
        value = self._forward[key]
        del self._backward[value]
        del self._forward[key]

    def __contains__(self, key: K) -> bool:
        return key in self._forward

    def __len__(self) -> int:
        return len(self._forward)

    def __iter__(self) -> Iterator[K]:
        return iter(self._forward)

    def __repr__(self) -> str:
        return f"Bijection({self._forward})"

    def __str__(self) -> str:
        return f"Bijection({self._forward})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Bijection):
            return self._forward == other._forward and self._backward == other._backward
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def items(self) -> Iterator[Tuple[K, V]]:
        return self._forward.items()

    def keys(self) -> Iterator[K]:
        return self._forward.keys()

    def values(self) -> Iterator[V]:
        return self._forward.values()

    @property
    def inv(self) -> "Bijection[V, K]":
        bi = Bijection[V, K]()
        bi._forward = self._backward
        bi._backward = self._forward
        return bi
