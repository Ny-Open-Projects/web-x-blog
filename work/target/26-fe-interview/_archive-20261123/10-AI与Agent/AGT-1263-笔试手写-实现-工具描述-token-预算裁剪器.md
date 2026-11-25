---
title: [1263] 笔试手写：实现 工具描述 token 预算裁剪器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, 工具]
type: 笔试题
---

## 1263：笔试手写：实现 工具描述 token 预算裁剪器

**需求**：工具上百个时全量描述塞不下。实现 trimToolset(tools, budget)：tools 为 { name, description, tokens }[]，预算 budget。规则：与任务相关的（related: true）优先保留；保留总 tokens 不超 budget；被裁掉的工具在返回的 omitted 里按 tokens 降序给摘要名单；保留集必含每个 related 工具（若单 related 超预算则截断其 description 到能放下的长度）。

```js
function trimToolset(tools, budget) {
  const related = tools.filter(t => t.related).sort((a, b) => b.tokens - a.tokens);
  const rest = tools.filter(t => !t.related).sort((a, b) => b.tokens - a.tokens);
  const kept = [], omitted = [];
  let used = 0;
  for (const t of [...related, ...rest]) { // related 全部尝试放
    if (used + t.tokens <= budget) { kept.push(t); used += t.tokens; }
    else if (t.related) { // related 超预算：截断 description（估 1 字 ≈ 1 token）
      const room = Math.max(0, budget - used - 10); // 留 name 等开销
      if (room > 0) { kept.push({ ...t, description: t.description.slice(0, room), truncated: true }); used = budget; }
      else omitted.push(t);
    }
    else omitted.push(t);
  }
  return { kept: kept.map(t => t.name), used, omitted: omitted.map(t => t.name) };
}
```

**评分点**：
- related 优先 + 非相关按体积降序填充
- related 超预算走截断而非丢弃（能力保底）
- omitted 输出供语义路由层兜底（AGT-067）
- 能讨论：裁剪的代价是模型看不见工具 → 语义路由是根治方案
