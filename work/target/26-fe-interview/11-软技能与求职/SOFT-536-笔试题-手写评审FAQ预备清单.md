---
title: [SOFT-536] 手写 genFAQ：从方案文档自动提取高频质疑点生成预备问题清单与应答要点？
date: 2026-11-21
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-536：手写 genFAQ：从方案文档自动提取高频质疑点生成预备问题清单与应答要点

**需求与边界**：
- 实现 genFAQ(doc)。
- 边界要求：① 从文档提取五类质疑点：数字无出处/决策点无备选/风险无触发条件/依赖无确认/性能无数据；② 每条生成问题+应答要点模板（缺什么补什么）；③ 按出现频次排序；④ 无问题的类别不输出；⑤ 输出供预演用（评审人替身脚本）。

**答**：
```javascript
function genFAQ(doc) {
  const faq = [];
  for (const num of doc.metrics.filter(m => !m.source))
    faq.push({ q: `指标「${num.name}」${num.value} 怎么算的？`,
      a: '补：数据出处（监控/财务口径）+ 计算过程' });
  for (const d of doc.decisions.filter(x => !x.alternatives?.length))
    faq.push({ q: `决策点「${d.name}」为什么不用其他方案？`,
      a: '补：至少1个备选+被否理由（可验证）' });
  for (const r of doc.risks.filter(x => !x.trigger))
    faq.push({ q: `风险「${r.name}」的触发条件是什么？`,
      a: '补：预警指标+量化触发线' });
  for (const dep of doc.deps.filter(x => !x.confirmed))
    faq.push({ q: `依赖【${dep.team}】的排期确认了吗？`,
      a: '补：书面确认+联调窗口+备选路径' });
  const perf = doc.claims.filter(c => /性能|P95|QPS/.test(c.text)
    && !c.data);
  for (const c of perf)
    faq.push({ q: `性能声明「${c.text.slice(0, 30)}」有数据吗？`,
      a: '补：压测口径+环境声明' });
  return faq.sort((a, b) => b.freq - a.freq);      // 频次排序
}
```

**评分点**:
- 五类质疑点覆盖（数字/备选/风险/依赖/性能）且判定规则可计算。
- 应答要点是"补什么"模板（可直接行动）。
- 频次排序（预演优先级）。

