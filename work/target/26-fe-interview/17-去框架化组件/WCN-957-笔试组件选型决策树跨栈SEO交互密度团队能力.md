---
title: [WCN-957] 手写组件选型决策树：按跨栈 / SEO / 交互密度 / 团队能力输出结论
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-957：手写组件选型决策树：按跨栈 / SEO / 交互密度 / 团队能力输出结论

**题目**：实现 `selectComponentStrategy(input)`，input 形如 `{ crossStack, seoCritical, interactionDensity, teamWCExperience, needIsolation }`（布尔或数值）。要求按以下决策树输出字符串结论：① needIsolation 为真 → 'iframe 沙箱'；② crossStack 为真且 teamWCExperience 为真 → '纯 Web Components'；③ crossStack 为真但团队无 WC 经验 → '框架组件 + 薄适配层（渐进）'；④ seoCritical 且 interactionDensity 低 → '静态 HTML + islands'；⑤ 其余 → '框架原生组件'。要求：所有字段缺省视为 false；返回 `{ strategy, path:[...] }`，path 记录走过的判断节点名便于复盘；不修改输入。请自足实现并给出可运行示例。

**答**：

```javascript
function selectComponentStrategy(input = {}) {
  const { crossStack = false, seoCritical = false,
    interactionDensity = 0.5, teamWCExperience = false,
    needIsolation = false } = input || {};
  const path = [];
  if (needIsolation) { path.push('needIsolation'); return { strategy: 'iframe 沙箱', path }; }
  if (crossStack) {
    path.push('crossStack');
    if (teamWCExperience) { path.push('teamWCExperience'); return { strategy: '纯 Web Components', path }; }
    path.push('noWCExperience');
    return { strategy: '框架组件 + 薄适配层（渐进）', path };
  }
  if (seoCritical && interactionDensity < 0.3) {
    path.push('seoCritical', 'lowInteraction');
    return { strategy: '静态 HTML + islands', path };
  }
  path.push('default');
  return { strategy: '框架原生组件', path };
}
console.log(selectComponentStrategy({ crossStack: true, teamWCExperience: true }));
// { strategy:'纯 Web Components', path:['crossStack','teamWCExperience'] }
console.log(selectComponentStrategy({ needIsolation: true }));
console.log(selectComponentStrategy({ seoCritical: true, interactionDensity: 0.1 }));
```

**评分点**：
- 决策树五条分支逻辑与优先级正确（isolation 最优先）。
- 字段缺省为 false、不修改输入。
- path 记录走过的判断节点，顺序正确可复盘。
- 返回结构 { strategy, path } 正确。
- 示例覆盖多条分支、可运行。
