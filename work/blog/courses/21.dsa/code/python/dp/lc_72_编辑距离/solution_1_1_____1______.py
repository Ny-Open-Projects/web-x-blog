# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848060
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def minDistance(word1, word2):  # 定义函数 minDistance（参数：word1, word2）
    n = len(word1)  # 把 长度(word1) 存入 元素个数
    m = len(word2)  # 把 长度(word2) 存入 映射表

    # 有一个字符串为空串
    if n * m == 0:  # 若 元素个数 乘 映射表 等于 0
        return n + m  # 返回 元素个数 加 映射表

    # DP 数组
    D = [
        [0] * (m + 1) for _ in range(n + 1)
    ]  # 把 [[0] 乘 (映射表 加 1) for _ in range(元素个数 加 1)] 存入 D

    # 边界状态初始化
    for i in range(n + 1):  # 让 下标 i 从 元素个数 加 1 遍历
        D[i][0] = i  # 把 下标 i 写入 D[i][0]
    for j in range(m + 1):  # 让 下标 j 从 映射表 加 1 遍历
        D[0][j] = j  # 把 下标 j 写入 D[0][j]

    # 计算所有 DP 值
    for i in range(1, n + 1):  # 让 下标 i 从 1 到 元素个数 加 1 遍历
        for j in range(1, m + 1):  # 让 下标 j 从 1 到 映射表 加 1 遍历
            left = D[i - 1][j] + 1  # 把 D[下标 i 减 1][下标 j] 加 1 存入 左边界
            down = D[i][j - 1] + 1  # 把 D[下标 i][下标 j 减 1] 加 1 存入 down
            left_down = D[i - 1][j - 1]  # 把 D[下标 i 减 1][下标 j 减 1] 存入 left_down
            if word1[i - 1] != word2[j - 1]:  # 若 word1[下标 i 减 1] 不等于 word2[下标 j 减 1]
                left_down += 1  # left_down累加 1
            D[i][j] = min(left, down, left_down)  # 把 取较小值 左边界, down, left_down) 写入 D[i][j]

    return D[n][m]  # 返回 D[元素个数][映射表]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(minDistance("horse", "ros"))  # 打印输出
