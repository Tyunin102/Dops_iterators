class CycleIterator():
    def __init__(self, storage):
        self.storage = storage
        self.iterator = iter(storage)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.storage)
            return next(self.iterator)

if __name__ == '__main__':
    my_it = CycleIterator([1,2,3])

    for item in my_it:
        print(item)


