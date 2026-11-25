---
title: [ALG-402] 手写 BIT 实现区间排名查询：榜单实时排名
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-402：手写 BIT 实现区间排名查询：榜单实时排名

**答**：
- 题目：积分榜（分数 0~10000），实时加分，查「某人当前排名」（比他分高的人数 + 1）。值域 BIT：加分在分数桶 +1，排名 = 总人数 - 前缀计数。
- 思路：scoreBIT[score] = 该分数人数；rank(user) = n - sum(score(user)) + 1（含并列时用严格大于人数 + 1）。
- 评分点：值域即 BIT 下标（无需离散化 1 万）；排名公式（严格大于 + 1）；并列排名的语义确认。

```javascript
class LeaderboardBIT {
  constructor(maxScore = 10000) { this.max = maxScore; this.bit = new BIT(maxScore);
    this.userScore = new Map(); this.n = 0; }
  setScore(userId, score) {
    const old = this.userScore.get(userId) ?? 0;
    if (old) this.bit.add(old, -1);                         // 旧分撤桶
    this.bit.add(score, 1); this.userScore.set(userId, score);
    if (!old) this.n++;
  }
  rank(userId) {                                            // 严格大于我的人数 + 1
    const s = this.userScore.get(userId);
    const higher = this.n - this.bit.sum(s);                // > s 的人数
    return higher + 1;
  }
  countAbove(score) { return this.n - this.bit.sum(score); }
}
```
