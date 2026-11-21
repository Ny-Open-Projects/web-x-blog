---
title: [ARC-049] 微前端的性能开销如何评估？iframe 被重新认识的取舍是什么？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-049：微前端的性能开销如何评估？iframe 被重新认识的取舍是什么？
**答**：
- 开销清单：HTML Entry 多一次请求与解析、沙箱代理的性能税、样式隔离的编译开销、公共依赖不共享时的重复体积、多实例内存。
- 评估方法：与单体基线对比 TTI/内存/包体积，量化"架构税"，超过 30% 首屏劣化需优化或重估拆分。
- iframe 的新认知：它隔离最彻底（JS/CSS/DOM/存储全隔离）、实现成本几乎为零；体验差（路由、弹窗、通信、SEO）可以逐步被代理修复。wujie 正是"iframe 隔离 + 代理修复体验"的折中。小而封闭的子场景（如内嵌第三方表单）iframe 可能是最便宜正解。

```typescript
// 微前端性能基线对比脚本（CI 中跑，超阈值报警）
const baseline = { tti: 2500, memoryMB: 180, bundleKB: 900 };   // 单体基线
const metrics = await auditMicroApp('https://portal.corp.com');
const tax = {
  ttiTaxPct: (metrics.tti - baseline.tti) / baseline.tti * 100,       // 交互时间税
  memTaxPct: (metrics.memoryMB - baseline.memoryMB) / baseline.memoryMB * 100,
  bundleTaxKB: metrics.bundleKB - baseline.bundleKB,                 // 重复依赖的体积税
};
if (tax.ttiTaxPct > 30) throw new Error(`微前端架构税超标 ${tax.ttiTaxPct.toFixed(1)}%，需评审`);
console.table(tax);

// iframe 取舍速查
// 选 iframe：强隔离（第三方/广告/遗留系统）、无跨应用交互、子应用自治要求高
// 拒 iframe：需要共享登录态与路由、弹窗跨层、SSR/SEO、频繁双向通信
```
