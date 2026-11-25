---
title: [ENG-301] 笔试题——实现 merge queue 调度器（批量合并 + 失败二分定位）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-301：手写 merge queue

**需求与边界**：
- 需求：队列攒批（最多 5 个 PR）→ 整批 CI 验证 → 全绿批量 merge；失败时二分定位坏 PR（半批重验），坏 PR 踢出后好 PR 自动重入队。
- 边界：① 批内 PR 基于前一批的合并结果 rebase；② 二分重验次数上限（避免验证爆炸，超过则逐个验）；③ 踢出 PR 的作者收到通知与失败原因。

**答**：
```javascript
async function mergeQueue({ batchSize = 5, maxBisect = 3 } = {}) {
  while (queue.length) {
    const batch = queue.splice(0, batchSize).map(rebaseOntoMain);
    const ok = await runCI(batch);
    if (ok) { batch.forEach(merge); continue; }
    // 失败：二分定位
    let suspects = batch, rounds = 0;
    while (suspects.length > 1 && rounds < maxBisect) {
      const half = suspects.slice(0, Math.ceil(suspects.length / 2));
      const halfOk = await runCI(rebase(half));
      suspects = halfOk ? suspects.slice(Math.ceil(suspects.length / 2)) : half;
      rounds++;
    }
    if (suspects.length === 1) {
      const bad = suspects[0];
      notifyAuthor(bad, ciFailureReason(bad));         // 通知作者
      queue.push(...batch.filter(b => b !== bad));     // 好 PR 重入队
    } else
      for (const pr of suspects) { notifyAuthor(pr, '批量失败，请单独验证'); }
  }
}
```

**评分点**:
- 批量验证吞吐（5 PR 一次 CI）。
- 二分定位 + 重验上限（验证成本可控）。
- 好 PR 重入队（不因坏 PR 全批报废）。
- rebaseOntoMain 保证批内基于最新 main（并发正确性）。
