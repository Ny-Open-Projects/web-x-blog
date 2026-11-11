# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116938
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def sortedSquares(nums):  # 定义函数 sortedSquares（参数：数组）
    ans = [x * x for x in nums]  # 把 [x 乘 x for x in 数组] 存入 答案
    ans.sort()  # 排序
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(sortedSquares([1, 2, 3]))  # 打印输出
