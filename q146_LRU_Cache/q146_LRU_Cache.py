class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):

        if key in self.dic:
            n = self.dic[key]
            self.__remove(n)
            self.__add(n)
            return n.val

        return -1

        # remove item from list and dict
        # add to tail
        # add to dict

    def put(self, key, val):
        if key in self.dic:
            self.__remove(self.dic[key])
        n = Node(key, val)
        self.__add(n)
        self.dic[key] = n

        if len(self.dic) > self.capacity:
            n = self.head.next
            self.__remove(n)
            del self.dic[n.key]

    def __remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

    def __add(self, node):
        p = self.tail.pre
        p.next = node
        self.tail.pre = node
        node.pre = p
        node.next = self.tail
