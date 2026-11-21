---
title: [A007] 最大子数组和(Kadane)
date: 2026-11-17
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A007 · 最大子数组和(Kadane)

> 难度:★★☆ | 标签:动态规划, 数组

**问**:求连续子数组的最大和(至少含一个元素)。

**答**:Kadane:`cur` 表示「以 i 结尾的最大子数组和」,转移 `cur = max(x, cur + x)`(要么续上前面的,要么从自己重新开始),答案取全局 max。O(n) 时间 O(1) 空间。本质是 DP,只是滚动变量压缩到 O(1)。

```python
# 示例:code/07_算法专题/(docs 内嵌,复制可运行) a007_max_subarray.py
def max_subarray(nums: list[int]) -> int:
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)   # 前缀为负就抛弃,从 x 重开
        best = max(best, cur)
    return best

if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6   # [4,-1,2,1]
    assert max_subarray([-3, -1, -2]) == -1                     # 全负取最大单元素
    assert max_subarray([5]) == 5
    print("A007 ok")
```

**追问**:
- 全负数组的正确答案?——最大单元素(子数组至少一个元素);把初始化设成 `nums[0]` 而不是 0,是本题最常见的错。
- 要返回子数组本身怎么改?——记录 cur 的起点,更新 best 时同时记区间;DP 状态多存一个起点。
- 分治解法 O(n log n) 还有意义吗?——线段树/分治版支持「任意区间更新后查询最大子段和」的动态场景;单次静态查询 Kadane 已最优。
