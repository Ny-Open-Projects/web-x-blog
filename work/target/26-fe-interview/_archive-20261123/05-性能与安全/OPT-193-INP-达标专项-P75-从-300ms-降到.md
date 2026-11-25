---
title: [OPT-193] INP 达标专项（P75 从 300ms 降到 200ms）怎么规划路线？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-193：INP 达标专项（P75 从 300ms 降到 200ms）怎么规划路线？

**答**：
- 第一步拿数据：按 OPT-129 三段归因聚合，输出"交互类型 × 归因段"矩阵，找到 P75 贡献最大的 Top3 交互（通常是：下拉筛选、图表切换、表单提交）。
- 路线按归因分配：inputDelay 主导→治理长任务（切片/Worker，预期 -60~100ms）；processing 主导→回调瘦身（同步逻辑下沉、防抖合并）；presentation 主导→缩小重排范围（内容可见性、transform、分层）。
- 每个交互做 A/B 或前后灰度对比，专项目标是**全站 P75**，所以还要盯"长尾交互"——P75 边缘的那批会话是最后 20ms 的来源。
- 回归防护：INP 进 RUM 告警（劣化 15% 报警）+ Lab 侧关键交互基线测试进 CI。

```javascript
// 一一对应：INP 专项的交互归因矩阵与长任务切片改造
// 1. 归因聚合：输出 交互类型 × 段位 的 P75 矩阵（服务端视角示意）
function buildInpMatrix(reports) {   // reports: OPT-129 上报的 worst 数组
  const cell = new Map();            // "selector|segment" -> []
  for (const r of reports) {
    const seg = r.inputDelay > r.processing && r.inputDelay > r.presentation ? 'inputDelay'
              : r.processing > r.presentation ? 'processing' : 'presentation';
    const key = `${r.target}|${seg}`;
    (cell.get(key) || cell.set(key, []).get(key)).push(
      seg === 'inputDelay' ? r.inputDelay : seg === 'processing' ? r.processing : r.presentation
    );
  }
  return [...cell.entries()]
    .map(([k, arr]) => { const s = arr.sort((a, b) => a - b); return { k, p75: s[Math.floor(s.length * .75)] }; })
    .sort((a, b) => b.p75 - a.p75).slice(0, 5);
}
// 输出决定改造顺序，例如：筛选按钮|inputDelay P75 180ms → 长任务治理

// 2. 主力改造：把 220ms 的同步渲染回调切成多个 <50ms 块
async function onFilterClick(filter) {
  const rows = computeVisibleRows(filter);       // 80ms
  await scheduler?.yield?.();                     // 让出：可响应新输入
  const updates = diffRows(rows);                 // 70ms
  await scheduler?.yield?.();
  commitToDOM(updates);                           // 40ms，且只更新变化行
}
// 3. presentation 段优化：大列表容器 content-visibility 让浏览器跳过屏外渲染
// .row { content-visibility: auto; contain-intrinsic-size: auto 48px; }
```
