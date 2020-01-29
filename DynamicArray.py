class DynamicArray:
    def __init__(self, size):
        self.count = 0
        self.size = size

        self.storage = [None] * size

    #[None, None, None, None]
    # value: 1 --> insert into first available slot.
    def append(self, value):
        if self.count == self.size:
            self.resize()

        self.storage[self.count] = value
        self.count += 1

    def insert(self, value, idx):
        # resize if we need
        if self.count == self.size:
            self.resize()
        # move over by one
        for i in range(self.count, idx, -1):
            self.storage[i] = self.storage[i - 1]

        self.storage[idx] = value

        self.count += 1

    def resize(self):
        self.size *= 2
        # make a new array, whish is double the size of the old array
        temp_storage = [None] * self.size
        # copy everything into new array
        for index in range(self.size // 2):  # can also use self.count
            temp_storage[index] = self.storage[index]

        self.storage = temp_storage
   # TODO check if we need to resize
