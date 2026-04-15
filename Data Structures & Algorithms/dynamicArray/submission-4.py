class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None for _ in range(self.capacity)]
        self.last_free_idx = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if len(self.arr) == self.last_free_idx:
            self.resize()

        self.arr[self.last_free_idx] = n
        self.last_free_idx += 1

    def popback(self) -> int:
        self.last_free_idx -= 1
        temp = self.arr[self.last_free_idx]
        self.arr[self.last_free_idx] = None
        return temp
        

    def resize(self) -> None:
        self.arr.extend([None for _ in range(len(self.arr))])
        self.capacity *= 2

    def getSize(self) -> int:
        return self.last_free_idx 
    
    def getCapacity(self) -> int:
        return self.capacity


# problems:
# - when you set, you might leave some Nones: [1, 2, None, 4]
# self.last_index never gets updated