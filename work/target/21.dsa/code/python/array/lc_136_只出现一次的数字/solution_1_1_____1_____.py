# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145029963
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def singleNumber(nums):  # 定义函数 singleNumber（参数：数组）
    ret = 0  # 把 0 存入 ret
    for item in nums:  # 逐个取出 数组 的元素（item）
        ret ^= item  # 把 item 写入 ret ^
    return ret  # 返回 ret


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(singleNumber([1, 2, 3]))  # 打印输出
