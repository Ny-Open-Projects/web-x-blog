---
title: [WCN-969] 性能预算门禁怎么落地到 CI：WC 体积 / 水合耗时 / 内存三项阈值卡点
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-969：性能预算门禁怎么落地到 CI：WC 体积 / 水合耗时 / 内存三项阈值卡点

**答**：
- 结论先行：性能预算要「可量化、卡在合入前」——三项指标（产物体积、水合耗时、运行时内存）各有阈值，CI 跑基准测试超标即失败，避免劣化合入。
- 体积：按 tag 汇总 gzip 体积，设总预算与单元素限额（前文体积分析器），超标需说明或走豁免。
- 水合耗时：用自动化基准（固定数据集 + 无头浏览器）测 hydration 时长，与基线对比超阈值（如 +10%）告警。
- 内存：长跑会话后采样堆快照，检测未释放的 WC 实例/信号订阅（前文内存审计），泄漏超阈值失败。
- 追问钩子：面试官问「基准测试环境抖动导致误报怎么办」——答：多次取中位数、固定机器规格、与基线相对比较而非绝对值，并设噪声容忍带。

```javascript
// CI 门禁：三项指标对比基线
function checkBudget({ gzipKB, hydrateMs, memMB }, baseline) {
  const checks = [
    ['体积', gzipKB, baseline.gzipKB * 1.1, 'KB'],
    ['水合', hydrateMs, baseline.hydrateMs * 1.1, 'ms'],
    ['内存', memMB, baseline.memMB * 1.15, 'MB'],
  ];
  return checks.filter(([, v, limit]) => v > limit)
    .map(([name, v, limit, unit]) => `${name} 超标: ${v}${unit} > ${limit.toFixed(1)}${unit}`);
}
console.log(checkBudget({ gzipKB: 320, hydrateMs: 180, memMB: 60 },
  { gzipKB: 280, hydrateMs: 150, memMB: 50 }));
// ['体积 超标...', '水合 超标...', '内存 超标...']
```
