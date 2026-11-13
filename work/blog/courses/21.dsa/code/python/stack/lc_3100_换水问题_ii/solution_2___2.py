# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145386116
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def maxBottlesDrunk(numBottles, numExchange):  # 定义函数 maxBottlesDrunk（参数：numBottles, numExchange）
    result = 0  # 把 0 存入 结果
    emptyBottles = 0  # 把 0 存入 emptyBottles
    flag = True  # 把 True 存入 flag

    while flag:  # 循环，直到不满足「flag」
        flag = False  # 把 False 存入 flag

        # Drink water
        if numBottles > 0:  # 若 numBottles 超过 0
            result += numBottles  # 结果累加 numBottles
            emptyBottles += numBottles  # emptyBottles累加 numBottles
            numBottles = 0  # 把 0 存入 numBottles
            flag = True  # 把 True 存入 flag

        # Exchange bottles
        if emptyBottles >= numExchange:  # 若 emptyBottles 不低于 numExchange
            numBottles += 1  # numBottles累加 1
            emptyBottles -= numExchange  # emptyBottles累减 numExchange
            numExchange += 1  # numExchange累加 1
            flag = True  # 把 True 存入 flag

    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(maxBottlesDrunk(10, 3))  # 打印输出
