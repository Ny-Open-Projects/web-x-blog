---
title: [ENG-286] 笔试题——实现 monorepo 影响面计算器（变更→受影响包闭包）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-286：手写 monorepo 影响面计算器

**需求与边界**：
- 输入：包依赖图 `{ pkg: [deps] }`（A 依赖 B 表示 B 变更影响 A）、变更文件路径到包的映射；输出受影响包集合（反向闭包）。
- 边界：① 反向闭包用 BFS 消费者方向遍历；② 循环依赖防死循环（visited）；③ 变更文件不属任何包时按根配置影响全部（保守策略）；④ 输出按拓扑层级排序供 CI 调度。

**答**：
```javascript
function affectedPackages(graph, changedFiles, fileToPkg) {
  const changed = new Set();
  for (const f of changedFiles) {
    const pkg = fileToPkg(f);
    if (pkg) changed.add(pkg);
    else return { all: true, affected: Object.keys(graph) };   // 根配置变更保守全量
  }
  // 反向图：consumers[pkg] = [谁依赖它]
  const consumers = {};
  for (const [pkg, deps] of Object.entries(graph))
    for (const d of deps) (consumers[d] ??= []).push(pkg);
  const affected = new Set(changed), queue = [...changed];
  while (queue.length) {                                       // BFS 反向闭包
    const cur = queue.shift();
    for (const c of consumers[cur] || [])
      if (!affected.has(c)) { affected.add(c); queue.push(c); }
  }
  // 拓扑层级排序（CI 调度：依赖浅的先建）
  const depth = {};
  const getDepth = (p, seen = new Set()) => {
    if (depth[p] !== undefined) return depth[p];
    if (seen.has(p)) return 0;                                 // 循环防御
    seen.add(p);
    return (depth[p] = 1 + Math.max(0, ...(graph[p] || []).map(d => getDepth(d, seen))));
  };
  return { all: false, affected: [...affected].sort((a, b) => getDepth(a) - getDepth(b)) };
}
```

**评分点**:
- 反向消费者图构建 + BFS 闭包（方向不能搞反）。
- 未归属文件保守全量（根配置影响一切的意识）。
- 循环依赖 visited/depth 记忆化防死循环。
- 拓扑排序输出（供 CI 分层调度）。
