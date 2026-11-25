---
title: [PER-1114] 如何应对 CSP 的误报与体验冲突（CSP 落地深水）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1114：如何应对 CSP 的误报与体验冲突（CSP 落地深水）

**答**：
- 常见冲突：内联样式（组件库）、eval 类依赖（老库）、图片协议（data: blob:）、WebSocket 域遗漏。
- 处理：Report-Only 数据驱动——聚合 top 违规来源，逐个判定（修代码/加白名单/放弃）。
- 渐进：先 report-only 3 个月 → 混合模式（危险指令 enforce + 兼容指令 report）→ 全量 enforce。
- 例外管理：豁免必须带理由与有效期（注释标注），定期清零豁免清单。

```javascript
// CSP 违规聚合分析
const violations = collectReports();   // report-uri 收集
function analyzeCSP(violations) {
  const grouped = {};
  for (const v of violations) {
    const key = `${v.directive}|${new URL(v.blockedURL, location.href).host}`;
    (grouped[key] ??= { count: 0, samples: [] }).count++;
    if (grouped[key].samples.length < 3) grouped[key].samples.push(v.sourceFile);
  }
  return Object.entries(grouped)
    .sort((a, b) => b[1].count - a[1].count).slice(0, 10)
    .map(([k, v]) => ({ key: k, count: v.count,
      action: k.includes('style') ? '样式白名单或重构内联' :
              k.includes('eval') ? '替换依赖或 sandbox' : '补充指令' }));
}
```
