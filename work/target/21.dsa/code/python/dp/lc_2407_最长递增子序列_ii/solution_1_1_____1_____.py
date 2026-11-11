# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144827578
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def lengthOfLIS(nums, k):  # 定义函数 lengthOfLIS（参数：数组, 下标 k）
    if not nums:  # 若 not 数组
        return 0  # 返回 0
    import bisect  # 引入依赖

    vals = sorted(set(nums))  # 把 sorted(set(数组)) 存入 vals
    comp = {v: i for i, v in enumerate(vals)}  # 把 {值: 下标 i for 下标 i, 值 in enumerate(vals)} 存入 comp
    m = len(vals)  # 把 长度(vals) 存入 映射表
    size = 1  # 把 1 存入 大小
    while size < m:  # 循环，直到不满足「大小 小于 映射表」
        size <<= 1  # 把 1 写入 size <<
    tree = [0] * (2 * size)  # 把 [0] 乘 (2 乘 大小) 存入 tree

    def update(pos, val):  # 定义函数 update（参数：pos, 值）
        pos += size  # pos累加 大小
        if val > tree[pos]:  # 若 值 超过 tree[pos]
            tree[pos] = val  # 把 值 写入 tree[pos]
        pos >>= 1  # 把 1 写入 pos >>
        while pos:  # 循环，直到不满足「pos」
            tree[pos] = max(
                tree[2 * pos], tree[2 * pos + 1]
            )  # 把 取较大值 tree[2 乘 pos], tree[2 乘 pos 加 1]) 写入 tree[pos]
            pos >>= 1  # 把 1 写入 pos >>

    def query(l, r):  # 定义函数 query（参数：左指针, 右指针）
        l += size  # 左指针累加 大小
        r += size  # 右指针累加 大小
        res = 0  # 把 0 存入 结果
        while l <= r:  # 循环，直到不满足「左指针 不超过 右指针」
            if l & 1:  # 若 左指针 按位与 1
                res = max(res, tree[l])  # 把 取较大值 结果, tree[左指针]) 存入 结果
                l += 1  # 左指针累加 1
            if not (r & 1):  # 若 not (右指针 按位与 1
                res = max(res, tree[r])  # 把 取较大值 结果, tree[右指针]) 存入 结果
                r -= 1  # 右指针累减 1
            l >>= 1  # 把 1 写入 l >>
            r >>= 1  # 把 1 写入 r >>
        return res  # 返回 结果

    ans = 0  # 把 0 存入 答案
    for x in nums:  # 逐个取出 数组 的元素（x）
        ci = comp[x]  # 把 comp[x] 存入 ci
        lo = bisect.bisect_left(vals, x - k)  # 把 bisect.bisect_left(vals, x 减 下标 k) 存入 左边界
        best = 0  # 把 0 存入 当前最优
        if lo <= ci - 1:  # 若 左边界 不超过 ci 减 1
            best = query(lo, ci - 1)  # 把 query(左边界, ci 减 1) 存入 当前最优
        cur = best + 1  # 把 当前最优 加 1 存入 当前值
        if cur > ans:  # 若 当前值 超过 答案
            ans = cur  # 把 当前值 存入 答案
        update(ci, cur)  # update(ci, 当前值)
    return ans  # 返回 答案


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(lengthOfLIS([4, 2, 1, 4, 3, 4, 5, 8, 15], 3))  # 打印输出
