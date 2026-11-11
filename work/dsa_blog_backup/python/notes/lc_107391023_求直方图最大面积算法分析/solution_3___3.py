# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def get_result(n, h):  # 定义函数 get_result（参数：元素个数, h）
    # 算法3：卡位计算 O(n^2)
    res = 0  # 把 0 存入 结果
    for a in range(1, n + 1):  # 让 数组 从 1 到 元素个数 加 1 遍历
        cur_h = h[a]  # 把 h[数组] 存入 cur_h
        # 找左卡位点
        lo = a - 1  # 把 数组 减 1 存入 左边界
        while lo >= 1 and h[lo] >= cur_h:  # 循环，直到不满足「左边界 不低于 1 and h[左边界] 不低于 cur_h」
            lo -= 1  # 左边界累减 1
        # 找右卡位点
        hi = a + 1  # 把 数组 加 1 存入 右边界
        while (
            hi <= n and h[hi] >= cur_h
        ):  # 循环，直到不满足「右边界 不超过 元素个数 and h[右边界] 不低于 cur_h」
            hi += 1  # 右边界累加 1
        area = (hi - lo - 1) * cur_h  # 把 (右边界 减 左边界 减 1) 乘 cur_h 存入 area
        if area > res:  # 若 area 超过 结果
            res = area  # 把 area 存入 结果
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    h = [0, 2, 3, 3, 3, 2, 0]  # 把 [0, 2, 3, 3, 3, 2, 0] 存入 h
    print(get_result(5, h))  # 输出: 10
