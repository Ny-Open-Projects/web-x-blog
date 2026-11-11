# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145029963
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def singleNumber(nums):  # 定义函数 singleNumber（参数：数组）
    seen = set()  # 把 set() 存入 已见集合
    for num in nums:  # 逐个取出 数组 的元素（num）
        if num in seen:  # 若 num in 已见集合
            seen.discard(num)  # 已见集合.discard(num)
        else:  # 否则
            seen.add(num)  # 已见集合 追加 num)
    return seen.pop()  # 返回 已见集合 弹出 )


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(singleNumber([1, 2, 3]))  # 打印输出
