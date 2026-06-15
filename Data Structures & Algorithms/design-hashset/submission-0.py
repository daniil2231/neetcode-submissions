class MyHashSet:

    def __init__(self):
        self.hashSet = [-1] * 1000000

    def add(self, key: int) -> None:
        self.hashSet[key] = key

    def remove(self, key: int) -> None:
        if self.hashSet[key] == key:
            self.hashSet[key] = -1

    def contains(self, key: int) -> bool:
        if self.hashSet[key] == key:
            return True

        return False        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)