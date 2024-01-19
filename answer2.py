import time
from math import log

class CacheNode:
    def __init__(self, key, value, weight):
        self.key = key
        self.value = value
        self.weight = weight
        self.score = 0
        self.next = None
        self.prev = None
        self.last_accessed_time = time.time()

class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.node_map = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.node_map:
            node = self.node_map[key]
            self.update_score(node)
            return node.value
        return -1

    def put(self, key, value, weight):
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.update_score(node)
        else:
            node = CacheNode(key, value, weight)
            self.node_map[key] = node
            self.insert_node(node)
            self.size += 1

            if self.size > self.capacity:
                self.remove_last_node()

    def update_score(self, node):
        current_time = time.time()
        time_diff = current_time - node.last_accessed_time + 1
        node.score = node.weight / (log(time_diff) + 1)
        node.last_accessed_time = current_time

        # Maintain the order of the nodes based on scores
        self.remove_node(node)
        self.insert_node(node)

    def insert_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            curr = self.head
            while curr and curr.score >= node.score:
                curr = curr.next

            if not curr:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            elif not curr.prev:
                node.next = curr
                curr.prev = node
                self.head = node
            else:
                node.next = curr
                node.prev = curr.prev
                curr.prev.next = node
                curr.prev = node

    def remove_node(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def remove_last_node(self):
        if self.tail:
            del self.node_map[self.tail.key]
            self.remove_node(self.tail)
            self.size -= 1

cache = Cache(capacity=3)
cache.put("first", 1, 5)
cache.put("second", 2, 5)

print(cache.get("first"))
print(cache.get("second"))

"""
Hash table is used

For get():
Best time complexity: O(1)
Average time complexity: O(1)
Worst time complexity: O(n)

For put():
Best time complexity: O(1)
Average time complexity: O(1)
Worst time complexity: O(n)

Explaination:
Both use direct access to the bucket based on the hash value of the key. so they has a constant time complexity of O(1) in the best and average cases
However In the worst case scenario, where all keys collide and hash to the same bucket, the time complexity becomes O(n)

"""