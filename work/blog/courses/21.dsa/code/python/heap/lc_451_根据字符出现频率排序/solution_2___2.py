# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133564001
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级
import heapq  # 引入依赖


class MaxHeap:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.heap = []  # 把 [] 写入 堆

    def push(self, val):  # 定义函数 push（参数：self, 值）
        heapq.heappush(self.heap, -val)  # heapq.heappush(self.堆, 减 值)

    def pop(self):  # 定义函数 pop（参数：self）
        return -heapq.heappop(self.heap)  # 返回 减 heapq.heappop(self.堆)

    def __len__(self):  # 定义函数 __len__（参数：self）
        return len(self.heap)  # 返回 长度(self.堆)


def frequencySort(s):  # 定义函数 frequencySort（参数：字符串）
    map = {}  # 把 {} 存入 映射表
    for item in s:  # 逐个取出 字符串 的元素（item）
        map[item] = map.get(item, 0) + 1  # 把 映射表 查找 item, 0) 加 1 写入 map[item]
    heap = []  # 把 [] 存入 堆
    for char, count in map.items():  # for char, 计数 in 映射表.items():
        heapq.heappush(heap, (-count, char))  # heapq.heappush(堆, ( 减 计数, char))
    result = ""  # 把 '' 存入 结果
    while heap:  # 循环，直到不满足「堆」
        count, char = heapq.heappop(heap)  # 把 heapq.heappop(堆) 写入 count, char
        result += char * (-count)  # 结果累加 char 乘 ( 减 计数)
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(frequencySort("tree"))  # 打印输出
