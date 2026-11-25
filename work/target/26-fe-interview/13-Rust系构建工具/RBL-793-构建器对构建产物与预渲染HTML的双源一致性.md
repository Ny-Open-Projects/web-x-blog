---
title: [RBL-793] 预渲染 HTML 与运行时渲染的双源一致性：SSG 验证的抽样策略
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-793：预渲染 HTML 与运行时渲染的双源一致性：SSG 验证的抽样策略

**答**:
- SSG（预渲染）页面与 SPA 运行时渲染可能漂移（数据时效/组件版本/环境差异）——「双源一致性」验证：抽样页面在「预渲染产物」与「运行时渲染」各取 DOM 关键结构（标题/列表项数/主内容 hash），diff 超阈值告警——SSG 内容过时是 SEO 事故的直接来源。
- 抽样策略：1) **分层抽样**（首页/高流量页全量、长尾页按 RUM 流量加权抽样）；2) 漂移敏感页优先（数据时效敏感的列表页 vs 静态文档页）；3) 全量成本约束（运行时渲染一页 = 一次 headless 加载，千页级必须抽样）。
- 比较的语义层次：DOM 结构 hash 过于敏感（无关紧要的 class 顺序变化也触发）——比较「语义指纹」（文本内容+结构角色），允许样式类差异；阈值化（内容 hash 相似度 < 0.9 告警）。
- 构建器的角色：输出「预渲染页面清单 + hash 基线」，验证任务消费（CI 定期跑或发布前跑）；漂移页面的处置是「重预渲染」（SSG 增量重建）或「该页转 SSR/ISR」。
- 追问钩子：为什么 SSG 的漂移监控要用「运行时渲染」做基准而不是「再次预渲染」？——再次预渲染只能发现「预渲染管线内的不确定性」，发现不了「数据/环境漂移」（预渲染时的 API 数据 vs 现在的真实数据）；用真实运行时渲染做基准才能捕捉内容时效问题——基准选择决定能发现哪类漂移。

```javascript
// 双源一致性验证
async function verifySSG({ pages, ssgBase, render }) {
  const results = [];
  const sample = stratify(pages, { full: (p) => p.traffic > 0.05, sampleRate: 0.1 });
  for (const page of sample) {
    const live = semanticFingerprint(await render(page.path));
    const base = ssgBase.get(page.path);
    if (!base) { results.push({ page: page.path, status: 'not-prerendered' }); continue; }
    const sim = similarity(base, live);
    results.push({ page: page.path, status: sim > 0.9 ? 'ok' : 'drift', sim });
  }
  const drifted = results.filter(r => r.status === 'drift' || r.status === 'not-prerendered');
  if (drifted.length > sample.length * 0.05) fail(`SSG 漂移超标: ${drifted.length} 页`);
  return results;
}
const semanticFingerprint = (html) => domTextAndRoles(html);   // 文本+角色哈希，忽略样式类
```
