---
title: [ALG-397] 手写 BIT 求第 k 小：中奖名次定位
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-397：手写 BIT 求第 k 小：中奖名次定位

**答**：
- 题目：抽奖池已有 N 个名额（BIT 记占用），求「第 k 个空闲名额编号」。BIT 上按计数二分（树上倍增写法：从高位跳 lowbit）。
- 思路：标准树上倍增——pos 从 0 起，按 2^t 降序尝试跳：若 bit[pos + 2^t] < k 则跳过去（k -= bit），最终 pos+1 即第 k 小（空闲 = 计数为 0，用总数减占用转换）。
- 评分点：倍增跳跃写法（不用递归）；k 的语义转换（空闲第 k 个 = 已占用第 k+1 个的间隙）；O(log n) 单次。

```javascript
class KthFree {
  constructor(capacity) { this.n = capacity; this.bit = new BIT(capacity); }
  acquire(id) { this.bit.add(id, 1); }                      // 占用
  release(id) { this.bit.add(id, -1); }
  kthFree(k) {                                              // 第 k 个空闲名额
    let pos = 0, remaining = k;
    for (let pw = 1 << 20; pw > 0; pw >>= 1) {              // 从高位试跳
      const next = pos + pw;
      if (next <= this.n) {
        const occupied = this.bit.sum(next);                // [1..next] 占用数
        const free = next - occupied;                       // 空闲数
        if (free < remaining) { pos = next; remaining -= free; }   // 跳过这段
      }
    }
    return pos + 1;                                         // 倍增定位 O(log n)
  }
}
```
