class MyHashSet:
    my_set = []

    def __init__(self):
        self.my_set = [-1] * 1000001

    def add(self, key: int) -> None:
        self.my_set[key] = 1

    def remove(self, key: int) -> None:
        self.my_set[key] = -1

    def contains(self, key: int) -> bool:
        return self.my_set[key] != -1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)