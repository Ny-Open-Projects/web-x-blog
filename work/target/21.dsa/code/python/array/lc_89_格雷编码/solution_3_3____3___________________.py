# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def grayCode(n):  # 定义函数 grayCode（参数：元素个数）
    ret = [0]  # 把 [0] 存入 ret
    for i in range(1, n + 1):  # 让 下标 i 从 1 到 元素个数 加 1 遍历
        for j in range(len(ret) - 1, -1, -1):  # 让 下标 j 从 长度(ret) 减 1 倒数回去（每步减 1）
            ret.append(
                ret[j] | (1 << (i - 1))
            )  # 把 ret[下标 j] 按位或 (1 小于 小于 (下标 i 减 1 追加到列表尾部
    return ret  # 返回 ret


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(grayCode(1))  # 打印输出
