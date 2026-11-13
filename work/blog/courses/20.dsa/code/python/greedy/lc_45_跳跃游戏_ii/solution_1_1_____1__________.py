# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145241433
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def jump(nums):  # 定义函数 jump（参数：数组）
    # 反向贪心：从终点出发，每次找最靠左能跳到当前位置的点，步数 +1
    position = len(nums) - 1  # 把 长度(数组) 减 1 存入 position
    steps = 0  # 把 0 存入 steps
    while position > 0:  # 循环，直到不满足「position 超过 0」
        for i in range(position):  # 让 下标 i 从 position 遍历
            if i + nums[i] >= position:  # 若 下标 i 加 数组[下标 i] 不低于 position
                position = i  # 把 下标 i 存入 position
                steps += 1  # steps累加 1
                break  # 跳出循环
    return steps  # 返回 steps


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(jump([2, 3, 1, 1, 4]))  # 打印输出
