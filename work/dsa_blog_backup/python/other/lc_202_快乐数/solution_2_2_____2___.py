# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355335
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def getNum(n):  # 定义函数 getNum（参数：元素个数）
    seen = set()  # 把 set() 存入 已见集合
    while n != 1:  # 循环，直到不满足「元素个数 不等于 1」
        if n in seen:  # 若 元素个数 in 已见集合
            return False  # 返回 False
        seen.add(n)  # 已见集合 追加 元素个数)
        n = sum(int(d) ** 2 for d in str(n))  # 把 累计和(int(d) 乘 乘 2 for d in str(元素个数)) 存入 元素个数
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(getNum(1))  # 打印输出
