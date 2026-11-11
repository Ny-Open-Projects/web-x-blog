# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130456218
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def grayCode(n):  # 定义函数 grayCode（参数：元素个数）
    def recursion_fn(k):  # 定义函数 recursion_fn（参数：下标 k）
        if k == 1:  # 若 下标 k 等于 1
            return ["0", "1"]  # 返回 ['0', '1']
        prev = recursion_fn(k - 1)  # 把 recursion_fn(下标 k 减 1) 存入 前一个
        result = []  # 把 [] 存入 结果
        prefix = "1" + "0" * (k - 1)  # 把 '1' 加 '0' 乘 (下标 k 减 1) 存入 prefix
        for item in prev[::-1]:  # 逐个取出 前一个 的元素（item）
            result.append(prefix[: -len(item)] + item)  # 把 prefix[: 减 长度(item 追加到列表尾部
        return prev + result  # 返回 前一个 加 结果

    if n == 0:  # 若 元素个数 等于 0
        return [0]  # 返回 [0]
    codes = recursion_fn(n)  # 把 recursion_fn(元素个数) 存入 codes
    return [int(x, 2) for x in codes]  # 返回 [int(x, 2) for x in codes]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(grayCode(1))  # 打印输出
