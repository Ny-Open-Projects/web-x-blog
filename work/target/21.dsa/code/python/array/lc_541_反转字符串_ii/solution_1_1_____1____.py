# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145565975
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def reverseStr(s, k):  # 定义函数 reverseStr（参数：字符串, 下标 k）
    arr = list(s)  # 把 列表(字符串) 存入 数组
    n = len(arr)  # 把 长度(数组) 存入 元素个数
    for i in range(0, n, 2 * k):  # 让 下标 i 从 0 到 元素个数 到 2 乘 下标 k 遍历
        left, right = i, min(
            i + k - 1, n - 1
        )  # 把 下标 i, 取较小值 下标 i 加 下标 k 减 1, 元素个数 减 1) 写入 left, right
        while left < right:  # 循环，直到不满足「左边界 小于 右边界」
            arr[left], arr[right] = (
                arr[right],
                arr[left],
            )  # 把 数组[右边界], 数组[左边界] 写入 arr[left], arr[right]
            left += 1  # 左边界累加 1
            right -= 1  # 右边界累减 1
    return "".join(arr)  # 返回 ''.join(数组)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(reverseStr("abc", 1))  # 打印输出
