# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094527
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class DLinkedNode:  # 定义类
    def __init__(self, key=0, value=0):  # 构造函数：初始化成员
        self.key = key  # 把 key 写入 self.key
        self.value = value  # 把 value 写入 self.value
        self.prev = None  # 把 None 写入 前一个
        self.next = None  # 把 None 写入 下一个


class LRUCache:  # 定义类
    def __init__(self, capacity: int):  # 构造函数：初始化成员
        self.capacity = capacity  # 把 capacity 写入 self.capacity
        self.cache = {}  # 把 {} 写入 self.cache
        self.size = 0  # 把 0 写入 大小
        # Dummy head and tail
        self.head = DLinkedNode()  # 把 DLinkedNode() 写入 头节点
        self.tail = DLinkedNode()  # 把 DLinkedNode() 写入 尾节点
        self.head.next = self.tail  # 把 self.尾节点 写入 下一个
        self.tail.prev = self.head  # 把 self.头节点 写入 前一个

    def _add_to_head(self, node):  # 定义函数 _add_to_head（参数：self, 节点）
        node.prev = self.head  # 把 self.头节点 写入 前一个
        node.next = self.head.next  # 把 self.头节点.下一个 写入 下一个
        self.head.next.prev = node  # 把 节点 写入 前一个
        self.head.next = node  # 把 节点 写入 下一个

    def _remove_node(self, node):  # 定义函数 _remove_node（参数：self, 节点）
        node.prev.next = node.next  # 把 节点.下一个 写入 下一个
        node.next.prev = node.prev  # 把 节点.前一个 写入 前一个

    def _move_to_head(self, node):  # 定义函数 _move_to_head（参数：self, 节点）
        self._remove_node(node)  # self._remove_node(节点)
        self._add_to_head(node)  # self._add_to_head(节点)

    def _remove_tail(self):  # 定义函数 _remove_tail（参数：self）
        node = self.tail.prev  # 把 self.尾节点.前一个 存入 节点
        self._remove_node(node)  # self._remove_node(节点)
        return node  # 返回 节点

    def get(self, key: int) -> int:  # 定义函数 get（参数：self, key: int）
        if key not in self.cache:  # 若 key not in self.cache
            return -1  # 返回 减 1
        node = self.cache[key]  # 把 self.cache[key] 存入 节点
        self._move_to_head(node)  # self._move_to_head(节点)
        return node.value  # 返回 节点.value

    def put(self, key: int, value: int) -> None:  # 定义函数 put（参数：self, key: int, value: int）
        if key not in self.cache:  # 若 key not in self.cache
            new_node = DLinkedNode(key, value)  # 把 DLinkedNode(key, value) 存入 new_node
            self.cache[key] = new_node  # 把 new_node 写入 self.cache[key]
            self._add_to_head(new_node)  # self._add_to_head(new_node)
            self.size += 1  # self.size累加 1
            if self.size > self.capacity:  # 若 self.大小 超过 self.capacity
                removed = self._remove_tail()  # 把 self._remove_tail() 存入 removed
                del self.cache[removed.key]  # del self.cache[removed.key]
                self.size -= 1  # self.size累减 1
        else:  # 否则
            node = self.cache[key]  # 把 self.cache[key] 存入 节点
            node.value = value  # 把 value 写入 node.value
            self._move_to_head(node)  # self._move_to_head(节点)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cache = LRUCache(2)  # 把 LRUCache(2) 存入 cache
    cache.put(1, 1)  # cache.put(1, 1)
    cache.put(2, 2)  # cache.put(2, 2)
    print(cache.get(1))  # 打印输出
    cache.put(3, 3)  # cache.put(3, 3)
    print(cache.get(2))  # 打印输出
    cache.put(4, 4)  # cache.put(4, 4)
    print(cache.get(1))  # 打印输出
    print(cache.get(3))  # 打印输出
    print(cache.get(4))  # 打印输出
