---
title: [WCN-987] 手写多端组件一致性校验流水线：输入多端产物输出差异报告
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-987：手写多端组件一致性校验流水线：输入多端产物输出差异报告

**题目**：实现 `checkConsistency(products)`，products 形如 `{ web:{ 'ds-button':{ props:['label','size'], events:['click'] } }, mini:{...}, flutter:{...} }`（各端组件 API 描述）。要求：① 以 web 为基准，检查其余端是否有缺失组件；② 对每个共有组件，检查 props/events 是否与 web 一致（集合比较，顺序无关），缺失的记入报告；③ 返回 `{ platforms:['...'], missingComponents:{platform:[...]}, apiDiffs:[{platform,component,missingProps:[],missingEvents:[]}], consistent }`；④ 输入非对象按空处理；⑤ consistent 为无任何缺失时 true。请自足实现并给出可运行示例。

**答**：

```javascript
function checkConsistency(products = {}) {
  const p = (products && typeof products === 'object') ? products : {};
  const platforms = Object.keys(p);
  const base = p.web || {};
  const missingComponents = {}, apiDiffs = [];
  for (const plat of platforms.filter(x => x !== 'web')) {
    const cur = p[plat] || {};
    missingComponents[plat] = Object.keys(base).filter(c => !(c in cur));
    for (const c of Object.keys(base)) {
      if (!cur[c]) continue;
      const missProps = base[c].props.filter(x => !(cur[c].props || []).includes(x));
      const missEvents = base[c].events.filter(x => !(cur[c].events || []).includes(x));
      if (missProps.length || missEvents.length)
        apiDiffs.push({ platform: plat, component: c,
          missingProps: missProps, missingEvents: missEvents });
    }
  }
  const consistent = Object.values(missingComponents).every(a => a.length === 0) && apiDiffs.length === 0;
  return { platforms, missingComponents, apiDiffs, consistent };
}
console.log(checkConsistency({
  web: { 'ds-button': { props: ['label','size'], events: ['click'] } },
  mini: { 'ds-button': { props: ['label'], events: [] } },
}));
```

**评分点**：
- 基准为 web，缺失组件检查正确。
- props/events 集合比较（顺序无关）正确，缺失项记录完整。
- 返回结构 platforms/missingComponents/apiDiffs/consistent 正确。
- 非对象输入健壮、consistent 判定正确。
- 示例可运行、输出正确。
