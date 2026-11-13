# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lemonadeChange(bills):  # 定义函数 lemonadeChange（参数：bills）
    # 计数贪心（另一种写法）：20 优先用 10+5，否则三张 5，否则失败
    five = ten = 0  # 把 ten 赋值为 0 存入 five
    for bill in bills:  # 逐个取出 bills 的元素（bill）
        if bill == 5:  # 若 bill 等于 5
            five += 1  # five累加 1
        elif bill == 10:  # 否则，若 bill 等于 10
            if five <= 0:  # 若 five 不超过 0
                return False  # 返回 False
            five -= 1  # five累减 1
            ten += 1  # ten累加 1
        else:  # 否则
            if ten > 0 and five > 0:  # 若 ten 超过 0 and five 超过 0
                ten -= 1  # ten累减 1
                five -= 1  # five累减 1
            elif five >= 3:  # 否则，若 five 不低于 3
                five -= 3  # five累减 3
            else:  # 否则
                return False  # 返回 False
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lemonadeChange([5, 5, 5, 10, 20]))  # 打印输出
    print(lemonadeChange([5, 5, 10, 10, 20]))  # 打印输出
