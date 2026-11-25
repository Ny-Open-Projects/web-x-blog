---
title: [NODE-530] Node 服务的灰度期指标对账（新旧版本指标可比性）如何保证？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-530：灰度期指标对账
**答**:
- 问题：灰度对比（canary vs stable）要公平——指标口径不可比时结论全错（新旧版本日志格式不同/指标名不同/采样率不同/流量构成不同）。
- 可比性清单：指标 schema 一致（新旧版本同名指标同语义同单位——发布 checklist 项）、采样一致（ARC-468 采样策略两版本相同）、标签一致（灰度标签/版本标签规范统一 NODE-497）、流量构成（canary 用户的特征 vs 全量——用户群偏差校正：同质分桶对比而非全量对比）。
- 对账工具：发布前指标冒烟（新旧版本各发固定测试流量 → 断言指标输出一致——发布流水线步骤）、对比报告自动生成（ARC-446 评估器的数据前提）。
- 常见漂移源：新版本改了错误分类（业务错改计为系统错——错误率"上升"其实是口径变）、新版本新增指标（旧版没有——对比缺失处理规则声明）。
- 治理：指标 schema 变更走评审（NODE-372 指标命名规范——变更影响灰度可比性要评估）。
```javascript
// 灰度可比性校验（发布流水线）
async function metricCompat(oldVer, newVer) {
  const o = await smokeMetrics(oldVer), n = await smokeMetrics(newVer);
  const missing = diffKeys(o, n);                                // 指标集合差异
  return { ok: missing.length === 0, missing,
    note: '同名指标需同语义：新指标声明 baseline 兼容规则' };
}
```
