---
title: [RBL-194] 笔试：手写 artifact 轮转清理（按分支保留 N 份 + 磁盘水位）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-194：笔试：手写 artifact 轮转清理（按分支保留 N 份 + 磁盘水位）

**答**：写 artifact-gc.mjs：1) 输入 artifact 元数据数组（{name, branch, size, createdAt}）与存储目录；2) 保留策略：每个 branch 保留最近 N 份（默认 5）、最近 7 天内的全部保留（ irrespective 分支数）；3) 另有磁盘水位线：删除后总占用仍超水位（默认 20GB）则继续按"最旧优先"全局删除并告警；4) 输出删除清单与删除后总大小；5) 删除前二次校验（文件存在才删），缺失的记为 stale 同步清理元数据。

```javascript
// artifact-gc.mjs
import { existsSync, statSync, rmSync } from 'node:fs';

const DAY = 86_400_000;
export function gc(artifacts, { keepPerBranch = 5, keepFreshDays = 7, quotaBytes = 20 * 1024 ** 3, now = Date.now() } = {}) {
  const missing = artifacts.filter(a => !existsSync(a.path));
  const alive = artifacts.filter(a => existsSync(a.path) && statSync(a.path).size === a.size); // 二次校验

  const keep = new Set();
  const byBranch = new Map();
  for (const a of alive.sort((x, y) => new Date(y.createdAt) - new Date(x.createdAt))) {
    const list = byBranch.get(a.branch) ?? [];
    list.push(a); byBranch.set(a.branch, list);
    if (now - new Date(a.createdAt).getTime() < keepFreshDays * DAY) keep.add(a.name); // 新鲜全保
  }
  for (const list of byBranch.values())
    list.slice(0, keepPerBranch).forEach(a => keep.add(a.name));     // 每分支最近 N 份

  let deletions = [...alive.filter(a => !keep.has(a.name))];
  const remainBytes = () => alive.filter(a => !deletions.includes(a)).reduce((s, a) => s + a.size, 0);
  // 水位兜底：仍超额则全局最旧优先追加删除
  const rest = [...alive].sort((x, y) => new Date(x.createdAt) - new Date(y.createdAt));
  let i = 0;
  while (remainBytes() > quotaBytes && i < rest.length) {
    const a = rest[i++];
    if (!deletions.includes(a)) deletions.push(a);
  }
  const overQuota = remainBytes() > quotaBytes; // 删光仍超额 → 告警
  for (const a of deletions) { try { rmSync(a.path, { recursive: true }); } catch {} }
  return { deleted: deletions.map(a => a.name), stale: missing.map(a => a.name),
    remainBytes: remainBytes(), overQuota };
}
// 剩余字节数为 0 且 overQuota=true 时，说明只靠清理不解决，需扩容或改产物生命周期策略。
```
**评分点**：
- 双策略叠加：分支保留 N 份 + 新鲜期豁免。
- 水位兜底全局最旧优先，删光仍超则告警。
- 存在性/大小二次校验 + stale 元数据清理。
- 排序稳定（createdAt 升降序使用正确）。
- 能说出真实存储应挂对象存储生命周期规则，脚本只是兜底。
