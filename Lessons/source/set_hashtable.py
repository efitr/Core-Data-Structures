from hashtable import HashTable
from linkedlist import LinkedList, Node
# Set basic properties
    # * Size
# Set basic operations
    # * Insert
    # * Contains
    # * Remove
# Set properties operation
    # * Union
    # * Intersection
    # * Subset
    # * Symetric Difference

class SetHashTable(object):

    def __init__(self, init_size=None):
        self.hashtable = HashTable()
        self.hashtable.buckets = [LinkedList() for i in range(init_size)]
        self.hashtable.size = 0
    
    def size(self):
        return self.hashtable.length()
        
    def all_members(self):
        return self.hashtable.items()

    def is_member(self, key):
        return self.hashtable.contains(key)

    def insert(self, key, value):
        if self.is_member(key) is True:
            raise ValueError('Item is already a member: {}'.format(key))
        self.hashtable.set(key, value)
        
    
    def union(self, other_set):
        new_set = SetHashTable()
        for index, member in self.all_members():
            new_set.insert(index, member)
        for index, member in other_set.all_members():
            new_set.insert(index, member)
        return new_set

    def intersection(self, other_set):
        # Must get both elements that intercept here
        new_set = SetHashTable()
        for key, member in self.all_members():
            if other_set.is_member(key, member):
                new_set.insert(key, member)
        return new_set

    def subset(self, other_set):
        pass

    def symmetric_difference(self, other_set):
        pass

    
    