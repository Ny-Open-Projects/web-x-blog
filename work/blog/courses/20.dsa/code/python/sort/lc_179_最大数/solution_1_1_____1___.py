# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145369843
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def largestNumber(nums):  # 定义函数 largestNumber（参数：数组）
    from functools import cmp_to_key  # from functools import cmp_to_key

    def compare(x, y):  # 定义函数 compare（参数：x, y）
        xy = str(x) + str(y)  # 把 str(x) 加 str(y) 存入 xy
        yx = str(y) + str(x)  # 把 str(y) 加 str(x) 存入 yx
        if xy > yx:  # 若 xy 超过 yx
            return -1  # 返回 减 1
        elif xy < yx:  # 否则，若 xy 小于 yx
            return 1  # 返回 1
        else:  # 否则
            return 0  # 返回 0

    strs = sorted(
        map(str, nums), key=cmp_to_key(compare)
    )  # 把 sorted(映射表(str, 数组), key 赋值为 cmp_to_key(compare)) 存入 strs
    if strs[0] == "0":  # 若 strs[0] 等于 '0'
        return "0"  # 返回 '0'
    return "".join(strs)  # 返回 ''.join(strs)


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(largestNumber([1, 2, 3]))  # 打印输出
