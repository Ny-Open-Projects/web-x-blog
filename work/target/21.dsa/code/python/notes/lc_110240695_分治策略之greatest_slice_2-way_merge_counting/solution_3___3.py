# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/110240695
# Greatest Slice - 方案3: Divide and Conquer (O(n log n))
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


def max_sub_array_dc(arr):  # 定义函数 max_sub_array_dc（参数：数组）
    def helper(lo, hi):  # 定义函数 helper（参数：左边界, 右边界）
        # 返回 (best, prefix, suffix, total)
        if hi - lo == 1:  # 若 右边界 减 左边界 等于 1
            v = arr[lo]  # 把 数组[左边界] 存入 值
            return v, v, v, v  # 返回 值, 值, 值, 值
        mi = (lo + hi) // 2  # 把 (左边界 加 右边界) 除以 除以 2 存入 mi
        l_best, l_pre, l_suf, l_sum = helper(lo, mi)  # 把 helper(左边界, mi) 写入 l_best, l_pre, l_suf, l_sum
        r_best, r_pre, r_suf, r_sum = helper(mi, hi)  # 把 helper(mi, 右边界) 写入 r_best, r_pre, r_suf, r_sum
        crossing = l_suf + r_pre  # 把 l_suf 加 r_pre 存入 crossing
        best = max(l_best, r_best, crossing)  # 把 取较大值 l_best, r_best, crossing) 存入 当前最优
        prefix = max(l_pre, l_sum + r_pre)  # 把 取较大值 l_pre, l_sum 加 r_pre) 存入 prefix
        suffix = max(r_suf, r_sum + l_suf)  # 把 取较大值 r_suf, r_sum 加 l_suf) 存入 suffix
        total = l_sum + r_sum  # 把 l_sum 加 r_sum 存入 总和
        return best, prefix, suffix, total  # 返回 当前最优, prefix, suffix, 总和

    if not arr:  # 若 not 数组
        return 0  # 返回 0
    return helper(0, len(arr))[0]  # 返回 helper(0, 长度(数组))[0]


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    print(max_sub_array_dc([-2, 1, -3, 4, -1, 2, 1]))  # 6
