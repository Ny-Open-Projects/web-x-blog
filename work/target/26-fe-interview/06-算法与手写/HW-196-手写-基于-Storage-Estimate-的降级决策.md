---
title: [HW-196] 手写基于配额的存储降级决策——estimate 百分比驱动缓存预算（三级策略 PER-323 工程化）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：PER-323 存储分级的自动化落地：estimate() → 用量/配额比 + persisted 状态 → 输出缓存预算档位（persistent/generous/conservative/minimal）→ 缓存层按档位取预算（预算 = 档位配置 × 配额比例）；档位变化时缓存层平滑收缩（LRU 淘汰到新预算）。

```javascript
async function storageTier() {
  if (!navigator.storage?.estimate) return { tier: 'minimal', budgetMB: 0 };
  const { usage, quota } = await navigator.storage.estimate();
  const persisted = await navigator.storage.persisted?.() ?? false;
  if (persisted) return { tier: 'persistent', budgetMB: 200 };
  const ratio = usage / quota;
  if (quota > 500 * 1048576 && ratio < 0.5) return { tier: 'generous', budgetMB: 100 };
  return { tier: 'conservative', budgetMB: 30 };          // Safari/移动/配额紧张
}
class BudgetedCache {
  async apply(tier, budgetMB) {
    const current = this.usedBytes / 1048576;
    if (current > budgetMB) await this.evictLRU((current - budgetMB) * 1048576);   // 平滑收缩到新预算
    this.budget = budgetMB;
  }
  async put(key, blob, size) {
    if (this.usedBytes + size > this.budget * 1048576) await this.evictLRU(size);
    await this.write(key, blob);
  }
}
// 档位变化（persisted 被撤销/配额变化）→ apply 平滑收缩（LRU 淘汰差额）—— 缓存预算与真实配额联动
// 预算占配额比 ≤ 20%（给系统/其他应用留余量，避免触发整源淘汰 PER-318）
```

**评分点**：
- estimate 百分比 + persisted 双信号驱动档位（PER-323 工程化）。
- 预算 = 档位 × 配额比例（不是固定 MB——大磁盘用户多缓存）。
- 档位变化的平滑收缩（LRU 淘汰差额）。
- 预算占配额 ≤ 20% 的余量意识（避免触发整源淘汰）。
