# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def grayCode(n):  # 定义函数 grayCode（参数：元素个数）
    result = [0, 1]  # 把 [0, 1] 存入 结果
    for i in range(1, n):  # 让 下标 i 从 1 到 元素个数 遍历
        for j in range(len(result) - 1, -1, -1):  # 让 下标 j 从 长度(结果) 减 1 倒数回去（每步减 1）
            result.append((1 << i) + result[j])  # 把 (1 小于 小于 下标 i 追加到列表尾部
    return result  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(grayCode(1))  # 打印输出
