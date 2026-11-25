---
title: [RBL-815] 场景题：CI 并行度优化——构建/测试/检查任务的依赖图与队列调度
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-815：场景题：CI 并行度优化——构建/测试/检查任务的依赖图与队列调度

**答**:
- CI 流水的总时长 = 关键路径（拓扑最长链）而非任务总和——优化目标是最小化关键路径：1) 依赖图显式化（build → [unit, lint, typecheck] 并行 → e2e 依赖 build+deploy-preview）；2) **独立任务并行**（lint/typecheck/unit 互不依赖就别串行——最常见的 CI 浪费）；3) 任务切分（unit 测试按文件 sharding 到 N 容器——单容器 10 分钟变 1 分钟×10）。
- 队列调度与成本的平衡：并行度拉满 = 关键路径最短但 runner 成本高/排队竞争——组织级「并发预算」（高峰期限制每 PR 的 runner 数，低优先任务延后）；抢占机制（hotfix PR 抢占队列）。
- 缓存与调度的交互：task 缓存命中（RBL-581）让任务秒过但仍占调度槽——「命中即跳过调度」是 turbo/nx 的核心收益；失败重试与缓存失效联动（失败任务的输入标记避免错误缓存）。
- 产物传递：build 的 dist 给 e2e 用——runner 间传产物（artifact 上传下载是隐藏耗时，大 dist 下载 30s+）——「产物直传缓存」（同 job 内共享/对象存储直链）。
- 追问钩子：为什么「加机器」不能线性缩短 CI 时长？——关键路径上的串行任务（build→e2e）无法并行化，加机器只优化并行段；且调度开销（容器启动/产物传输）随并行度上升——优化 CI 的正确顺序是「改依赖图（串行变并行）→ 切分大任务 → 才是加机器」。

```javascript
// CI 任务图与关键路径
const graph = {
  build: { deps: [], est: 300 },
  unit: { deps: ['build'], est: 600, sharding: 6 },
  lint: { deps: ['build'], est: 120 },
  typecheck: { deps: [], est: 180 },                     // 不依赖 build：并行启动
  e2e: { deps: ['unit', 'deploy'], est: 900 },
  deploy: { deps: ['build'], est: 60 },
};
function criticalPath(graph) {
  const memo = {};
  const path = (id) => memo[id] ??= (graph[id].est +
    (graph[id].deps.length
      ? Math.max(...graph[id].deps.map(d => path(d))) : 0));
  return path('e2e');                                    // 关键路径总时长
}
// 优化前：build(300)+unit(600)+e2e(900) = 1800s（unit 未切分时 600）
// unit 切 6 份 -> 100s：关键路径 = 300+100+900 = 1300s（省 500s）
console.log(criticalPath(graph));
```
