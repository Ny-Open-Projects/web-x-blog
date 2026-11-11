# 来源（blog）：LeetCode 66. 加一 — 方案1：末位进位
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def plus_one(digits):  # 定义函数 plus_one（参数：digits）
    d = digits[:]  # 把 复制 digits 存入 d
    for i in range(len(d) - 1, -1, -1):  # 让 下标 i 从 长度(d) 减 1 倒数回去（每步减 1）
        if d[i] == 9:  # 若 d[下标 i] 等于 9
            d[i] = 0  # 把 0 写入 d[i]
        else:  # 否则
            d[i] += 1  # d[i]累加 1
            return d  # 返回 d
    res = [0] * (len(digits) + 1)  # 把 [0] 乘 (长度(digits) 加 1) 存入 结果
    res[0] = 1  # 把 1 写入 res[0]
    return res  # 返回 结果


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    cases = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9, 9, 9], [1, 0, 0, 0]),
    ]
    for inp, want in cases:  # for inp, want in cases:
        got = plus_one(inp)  # 把 plus_one(inp) 存入 got
        assert got == want, f"plusOne({inp}) = {got}, want {want}"  # 断言校验
    print("PASS")  # 全部用例通过，输出 PASS
