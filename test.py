from bijection import Bijection

bi = Bijection[str, int]()
bi["a"] = 1
bi["b"] = 2
bi["c"] = 3

for key, value in bi.items():
    print(f"{key}: {value}")

for key, value in bi.inv.items():
    print(f"{key}: {value}")
