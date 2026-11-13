# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145355902
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def stoneGame(piles):  # 定义函数 stoneGame（参数：piles）
    # 石子游戏：偶数堆且为先手者对称策略保证必胜，Alice 始终能赢
    return True  # 返回 True


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(stoneGame([5, 3, 4, 5]))  # 打印输出
