---
title: [WCN-990] 手写 WC 健康诊断器：按错误率 / 水合耗时 / a11y / 体积输出等级与建议
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-990：手写 WC 健康诊断器：按错误率 / 水合耗时 / a11y / 体积输出等级与建议

**题目**：实现 `diagnose(metrics)`，metrics 形如 `{ errorRate, hydrateMs, a11yViolations, gzipKB }`（分别是错误率%、水合毫秒、a11y 违规数、gzip 体积KB）。要求：① 每项按阈值判定是否超标：errorRate>1、hydrateMs>200、a11yViolations>0、gzipKB>300；② 计算健康分 = 100 - 各超标项扣分（errorRate 每超1%扣20、hydrateMs 每超100ms扣15、a11yViolations 每个扣10、gzipKB 每超100KB扣10），截断 0~100；③ 等级：≥80 '健康'、60~79 '预警'、<60 '危急'；④ 输出 `{ score, level, issues:[{metric,detail}], suggestions:[...] }`，issues 列出超标项，suggestions 针对每项给一条建议；⑤ 字段缺省为 0，非对象输入健壮。请自足实现并给出可运行示例。

**答**：

```javascript
function diagnose(metrics = {}) {
  const m = (metrics && typeof metrics === 'object') ? metrics : {};
  const { errorRate = 0, hydrateMs = 0, a11yViolations = 0, gzipKB = 0 } = m;
  const issues = [], suggestions = [];
  let score = 100;
  if (errorRate > 1) { const d = Math.ceil((errorRate - 1)) * 20; score -= d;
    issues.push({ metric:'errorRate', detail:`${errorRate}%` });
    suggestions.push('排查运行时错误，加错误隔离与回滚'); }
  if (hydrateMs > 200) { const d = Math.ceil((hydrateMs - 200)/100)*15; score -= d;
    issues.push({ metric:'hydrateMs', detail:`${hydrateMs}ms` });
    suggestions.push('减少水合岛、延后非核心水合'); }
  if (a11yViolations > 0) { score -= a11yViolations * 10;
    issues.push({ metric:'a11yViolations', detail:a11yViolations });
    suggestions.push('修复 ARIA/对比度违规，接入 CI 门禁'); }
  if (gzipKB > 300) { score -= Math.ceil((gzipKB-300)/100)*10;
    issues.push({ metric:'gzipKB', detail:`${gzipKB}KB` });
    suggestions.push('代码分割、体积预算门禁'); }
  score = Math.max(0, Math.min(100, score));
  const level = score >= 80 ? '健康' : score >= 60 ? '预警' : '危急';
  return { score, level, issues, suggestions };
}
console.log(diagnose({ errorRate: 2.5, hydrateMs: 350, a11yViolations: 2, gzipKB: 450 }));
console.log(diagnose()); // 全 0，健康
```

**评分点**：
- 四项超标判定与扣分公式正确（含截断）。
- 等级三档划分正确。
- issues 与 suggestions 逐项对应、内容合理。
- 字段缺省与非对象输入健壮。
- 返回结构完整、示例可运行。
