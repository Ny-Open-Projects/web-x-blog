# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133270489
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def instanceOf(A, B):  # 定义函数 instanceOf（参数：A, B）
    p = A  # 把 A 存入 节点
    while p:  # 循环，直到不满足「节点」
        if p == B.prototype:  # 若 节点 等于 B.prototype
            return True  # 返回 True
        p = p.__proto__  # 把 节点.__proto__ 存入 节点
    return False  # 返回 False


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(instanceOf(None, None))  # 打印输出
