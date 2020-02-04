# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


​
# You will need to import or create a Linked List to use here!
​


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


​
​


def _hash(self, key):
    '''
        Hash an arbitrary key and return an integer.
​
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
    return hash(key)


​
​


def _hash_djb2(self, key):
    '''
        Hash an arbitrary key using DJB2 hash
​
        OPTIONAL STRETCH: Research and implement DJB2
        '''
    pass


​
​


def _hash_mod(self, key):
    '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
    return self._hash(key) % self.capacity


​
​


def insert(self, key, value):
    '''
        Store the value with the given key.
​
        Hash collisions should be handled with Linked List Chaining.
​
        Fill this in.
        '''
    # Hash the key --> index
    # If no linked list at that hash/index
    # make one and put it there
    # Add our original key/value pair to the linked list
    pass


​
​
​


def remove(self, key):
    '''
        Remove the value stored with the given key.
​
        Print a warning if the key is not found.
​
        Fill this in.
        '''
    # hash the key, get the index
    # the Linked List holding the node with this key/value pair lives at that index
    # use the original key with Linked List remove to delete the node
    pass


​
​


def retrieve(self, key):
    '''
        Retrieve the value stored with the given key.
​
        Returns None if the key is not found.
​
        Fill this in.
        '''
    pass


​
​


def resize(self):
    '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
​
        Fill this in.
        '''
    pass


​
​
​
if __name__ == "__main__":
    ht = HashTable(2)
​
ht.insert("line_1", "Tiny hash table")
ht.insert("line_2", "Filled beyond capacity")
ht.insert("line_3", "Linked list saves the day!")
​
print("")
​
# Test storing beyond capacity
print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))
​
# Test resizing
old_capacity = len(ht.storage)
ht.resize()
new_capacity = len(ht.storage)
​
print(f"\nResized from {old_capacity} to {new_capacity}.\n")
​
# Test if data intact after resizing
print(ht.retrieve("line_1"))
print(ht.retrieve("line_2"))
print(ht.retrieve("line_3"))
​
print("")
