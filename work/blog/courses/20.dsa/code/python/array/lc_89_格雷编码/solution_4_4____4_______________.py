# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def grayCode(n):  # 定义函数 grayCode（参数：元素个数）
    ret = []  # 把 [] 存入 ret
    for i in range(1 << n):  # 让 下标 i 从 1 小于 小于 元素个数 遍历
        ret.append((i >> 1) ^ i)  # 把 (下标 i 超过 超过 1 追加到列表尾部
    return ret  # 返回 ret


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(grayCode(1))  # 打印输出
