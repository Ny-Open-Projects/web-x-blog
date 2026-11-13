# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145346697
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class Node:  # 定义类
    def __init__(self, key=0, value=0, freq=1):  # 构造函数：初始化成员
        self.key = key  # 把 key 写入 self.key
        self.value = value  # 把 value 写入 self.value
        self.freq = freq  # 把 频次表 写入 频次表
        self.prev = None  # 把 None 写入 前一个
        self.next = None  # 把 None 写入 下一个


class DoublyLinkedList:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.head = Node()  # 把 Node() 写入 头节点
        self.tail = Node()  # 把 Node() 写入 尾节点
        self.head.next = self.tail  # 把 self.尾节点 写入 下一个
        self.tail.prev = self.head  # 把 self.头节点 写入 前一个
        self.size = 0  # 把 0 写入 大小

    def add(self, node):  # 定义函数 add（参数：self, 节点）
        node.prev = self.head  # 把 self.头节点 写入 前一个
        node.next = self.head.next  # 把 self.头节点.下一个 写入 下一个
        self.head.next.prev = node  # 把 节点 写入 前一个
        self.head.next = node  # 把 节点 写入 下一个
        self.size += 1  # self.size累加 1

    def remove(self, node):  # 定义函数 remove（参数：self, 节点）
        node.prev.next = node.next  # 把 节点.下一个 写入 下一个
        node.next.prev = node.prev  # 把 节点.前一个 写入 前一个
        self.size -= 1  # self.size累减 1

    def remove_last(self):  # 定义函数 remove_last（参数：self）
        if self.size == 0:  # 若 self.大小 等于 0
            return None  # 返回 None
        node = self.tail.prev  # 把 self.尾节点.前一个 存入 节点
        self.remove(node)  # self 弹出 节点)
        return node  # 返回 节点

    def is_empty(self):  # 定义函数 is_empty（参数：self）
        return self.size == 0  # 返回 self.大小 等于 0


class LFUCache:  # 定义类
    def __init__(self, capacity: int):  # 构造函数：初始化成员
        self.capacity = capacity  # 把 capacity 写入 self.capacity
        self.size = 0  # 把 0 写入 大小
        self.key_to_node = {}  # 把 {} 写入 self.key_to_node
        self.freq_to_list = {}  # 把 {} 写入 self.freq_to_list
        self.min_freq = 0  # 把 0 写入 self.min_freq

    def _update_freq(self, node):  # 定义函数 _update_freq（参数：self, 节点）
        freq = node.freq  # 把 节点.频次表 存入 频次表
        self.freq_to_list[freq].remove(node)  # self.freq_to_list[频次表] 弹出 节点)
        if self.freq_to_list[freq].is_empty():  # 若 self.freq_to_list[频次表].is_empty(
            del self.freq_to_list[freq]  # del self.freq_to_list[频次表]
            if self.min_freq == freq:  # 若 self.min_freq 等于 频次表
                self.min_freq += 1  # self.min_freq累加 1
        node.freq += 1  # node.freq累加 1
        if node.freq not in self.freq_to_list:  # 若 节点.频次表 not in self.freq_to_list
            self.freq_to_list[node.freq] = (
                DoublyLinkedList()
            )  # 把 DoublyLinkedList() 写入 self.freq_to_list[node.freq]
        self.freq_to_list[node.freq].add(node)  # self.freq_to_list[节点.频次表] 追加 节点)

    def get(self, key: int) -> int:  # 定义函数 get（参数：self, key: int）
        if key not in self.key_to_node:  # 若 key not in self.key_to_node
            return -1  # 返回 减 1
        node = self.key_to_node[key]  # 把 self.key_to_node[key] 存入 节点
        self._update_freq(node)  # self._update_freq(节点)
        return node.value  # 返回 节点.value

    def put(self, key: int, value: int) -> None:  # 定义函数 put（参数：self, key: int, value: int）
        if self.capacity <= 0:  # 若 self.capacity 不超过 0
            return  # return
        if key in self.key_to_node:  # 若 key in self.key_to_node
            node = self.key_to_node[key]  # 把 self.key_to_node[key] 存入 节点
            node.value = value  # 把 value 写入 node.value
            self._update_freq(node)  # self._update_freq(节点)
        else:  # 否则
            if self.size >= self.capacity:  # 若 self.大小 不低于 self.capacity
                min_list = self.freq_to_list[
                    self.min_freq
                ]  # 把 self.freq_to_list[self.min_freq] 存入 min_list
                removed = min_list.remove_last()  # 把 min_list.remove_last() 存入 removed
                if removed:  # 若 removed
                    del self.key_to_node[removed.key]  # del self.key_to_node[removed.key]
                    self.size -= 1  # self.size累减 1
            node = Node(key, value, 1)  # 把 Node(key, value, 1) 存入 节点
            self.key_to_node[key] = node  # 把 节点 写入 self.key_to_node[key]
            if 1 not in self.freq_to_list:  # 若 1 not in self.freq_to_list
                self.freq_to_list[1] = DoublyLinkedList()  # 把 DoublyLinkedList() 写入 self.freq_to_list[1]
            self.freq_to_list[1].add(node)  # self.freq_to_list[1] 追加 节点)
            self.min_freq = 1  # 把 1 写入 self.min_freq
            self.size += 1  # self.size累加 1


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    lfu = LFUCache(2)  # 把 LFUCache(2) 存入 lfu
    lfu.put(1, 1)  # lfu.put(1, 1)
    lfu.put(2, 2)  # lfu.put(2, 2)
    print(lfu.get(1))  # 打印输出
    lfu.put(3, 3)  # lfu.put(3, 3)
    print(lfu.get(2))  # 打印输出
    print(lfu.get(3))  # 打印输出
    lfu.put(4, 4)  # lfu.put(4, 4)
    print(lfu.get(1))  # 打印输出
    print(lfu.get(3))  # 打印输出
    print(lfu.get(4))  # 打印输出
