# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241347
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def canJump(nums):  # 定义函数 canJump（参数：数组）
    # 贪心：维护当前能到达的最远下标，若遇到下标已超过最远则失败
    max_reach = 0  # 把 0 存入 max_reach
    for i, step in enumerate(nums):  # 同时取 下标 i 与 步数 遍历
        if i > max_reach:  # 若 下标 i 超过 max_reach
            return False  # 返回 False
        max_reach = max(max_reach, i + step)  # 把 取较大值 max_reach, 下标 i 加 步数) 存入 max_reach
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(canJump([2, 3, 1, 1, 4]))  # 打印输出
    print(canJump([3, 2, 1, 0, 4]))  # 打印输出
