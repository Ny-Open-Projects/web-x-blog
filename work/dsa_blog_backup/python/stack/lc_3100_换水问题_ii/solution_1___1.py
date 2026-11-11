# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxBottlesDrunk(numBottles, numExchange):  # 定义函数 maxBottlesDrunk（参数：numBottles, numExchange）
    total = numBottles  # 把 numBottles 存入 总和
    while numBottles >= numExchange:  # 循环，直到不满足「numBottles 不低于 numExchange」
        numBottles += 1 - numExchange  # numBottles累加 1 减 numExchange
        numExchange += 1  # numExchange累加 1
        total += 1  # 总和累加 1
    return total  # 返回 总和


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxBottlesDrunk(10, 3))  # 打印输出
