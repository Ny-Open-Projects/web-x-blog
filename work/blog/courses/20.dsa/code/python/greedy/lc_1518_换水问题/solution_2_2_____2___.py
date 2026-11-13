# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386044
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def numWaterBottles(numBottles, numExchange):  # 定义函数 numWaterBottles（参数：numBottles, numExchange）
    ans = numBottles  # 把 numBottles 存入 答案
    empty = numBottles  # 把 numBottles 存入 empty
    while empty >= numExchange:  # 循环，直到不满足「empty 不低于 numExchange」
        new_bottles = empty // numExchange  # 把 empty 除以 除以 numExchange 存入 new_bottles
        ans += new_bottles  # 答案累加 new_bottles
        empty = new_bottles + empty % numExchange  # 把 new_bottles 加 empty 对…取模 numExchange 存入 empty
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(numWaterBottles(9, 3))  # 打印输出
