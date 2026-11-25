---
title: [AIC-914] 三个 Agent 分别改商品列表的 UI、接口层、埋点，如何提前规避合并冲突而不是事后解决？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-914：三个 Agent 分别改商品列表的 UI、接口层、埋点，如何提前规避合并冲突而不是事后解决？
**答**：
- 核心是「写集隔离」：任务分派时明确每个 Agent 的可写文件/目录边界，UI 只碰 components、接口只碰 api、埋点只碰 track 模块，从源头避免同时写同一文件。
- 对必须共享的文件（如同一个页面入口）建立「单一所有者」：该文件只由一个 Agent 改，其他 Agent 通过约定接口/占位符间接依赖。
- 先定义「契约」（接口签名、埋点事件 schema、组件 props）再并行——契约先行让各 Agent 面向稳定边界编码，即使并行也不会语义打架。
- CI 阶段做「跨 Agent 集成检查」：合并后跑契约一致性与类型检查，抓出写集隔离无法覆盖的语义冲突。
- 追问钩子：能说出「最优的冲突解决是不产生冲突——靠写集划分与契约先行」的候选人，从设计层面而非工具层面思考。

```typescript
// 写集隔离：分派时锁定每个 Agent 的可写范围
const assignments = [
  { agent:'ui',   write:['src/components/ProductList/**'] },
  { agent:'api',  write:['src/api/product/**'] },
  { agent:'track',write:['src/track/**'] },
];
function detectWriteOverlap(tasks) {
  const owner = new Map(); const conflicts = [];
  for (const t of tasks) for (const f of t.write) {
    if (owner.has(f)) conflicts.push({ file:f, a:owner.get(f), b:t.agent });
    else owner.set(f, t.agent);
  }
  return { ok: conflicts.length === 0, conflicts };
}
console.log(detectWriteOverlap(assignments)); // ok=true 从源头无文件级冲突
// 共享文件须指定单一所有者，其余通过契约间接依赖
```
