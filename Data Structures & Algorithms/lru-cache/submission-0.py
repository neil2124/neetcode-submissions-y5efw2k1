from collections import defaultdict

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapp = {}  # key -> node
        # Sentinel head (MRU side) and tail (LRU side)
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        """Detach a node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node: ListNode) -> None:
        """Insert a node right after head (MRU position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.mapp:
            return -1
        node = self.mapp[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mapp:
            self._remove(self.mapp[key])
        node = ListNode(key, value)
        self.mapp[key] = node
        self._insert_front(node)

        if len(self.mapp) > self.capacity:
            # Evict LRU node (just before tail sentinel)
            lru = self.tail.prev
            self._remove(lru)
            del self.mapp[lru.key]