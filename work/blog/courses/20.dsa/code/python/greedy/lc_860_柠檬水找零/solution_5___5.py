# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134661209
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lemonadeChange(bills):  # 定义函数 lemonadeChange（参数：bills）
    # 计数贪心：分别记录 5/10/20 面额零钱的数量
    c5 = c10 = 0  # 把 c10 赋值为 0 存入 c5
    for b in bills:  # 逐个取出 bills 的元素（b）
        if b == 5:  # 若 b 等于 5
            c5 += 1  # c5累加 1
        elif b == 10:  # 否则，若 b 等于 10
            if c5 == 0:  # 若 c5 等于 0
                return False  # 返回 False
            c5 -= 1  # c5累减 1
            c10 += 1  # c10累加 1
        else:  # 20
            if c10 > 0 and c5 > 0:  # 若 c10 超过 0 and c5 超过 0
                c10 -= 1  # c10累减 1
                c5 -= 1  # c5累减 1
            elif c5 >= 3:  # 否则，若 c5 不低于 3
                c5 -= 3  # c5累减 3
            else:  # 否则
                return False  # 返回 False
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lemonadeChange([5, 5, 5, 10, 20]))  # 打印输出
    print(lemonadeChange([5, 5, 10, 10, 20]))  # 打印输出
