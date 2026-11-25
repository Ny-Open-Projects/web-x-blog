---
title: [WCN-876] 设计令牌（Design Token）的语义化版本管理如何做？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-876：设计令牌（Design Token）的语义化版本管理如何做？

**答**：
- 结论先行：Token 也要像代码一样语义化版本（semver）——因为它是被几十个组件、多品牌消费的「公共 API」，随意改值（哪怕是改个色值）都可能引发视觉回归，必须按「破坏性/新增/修复」分级发布。
- 版本分级：MAJOR——删除/重命名 token、改变 token 语义（如 `--color-primary` 从蓝变红的语义调整）；MINOR——新增 token、新增主题/别名；PATCH——修正值的小 bug（如对比度不达标微调）、文档补充。
- 自动化判定：比对新旧 token schema——删除/改名=MAJOR，新增=MINOR，仅值变化按影响判定；用 CI 自动计算建议版本号，避免人为误判。
- 消费侧治理：组件库锁定 token 主版本（peer 依赖），semver 范围控制升级节奏；提供 token 变更日志与迁移说明（旧别名保留一个 deprecation 周期）。
- 与 WCN 结合：token 以 CSS 自定义属性注入 Shadow DOM，token 版本变更要能被组件感知；用 `adoptedStyleSheets` + 版本化样式表管理，确保多版本 token 共存时不串味。
- 追问钩子：面试官会问「只是改了个色值算不算破坏性」——答：看语义——如果 `--color-primary` 语义不变只是微调对比度算 PATCH；如果改变了品牌含义或取值范围导致依赖它的组件布局/可读性变化，就要按 MAJOR 处理并走视觉回归。

```javascript
// Token schema 版本判定（semver 建议）
function suggestVersion(oldT, newT) {
  const oldKeys = new Set(Object.keys(oldT)), newKeys = new Set(Object.keys(newT));
  const removed = [...oldKeys].filter(k => !newKeys.has(k));
  const added = [...newKeys].filter(k => !oldKeys.has(k));
  if (removed.length) return { bump: 'major', reason: `删除/改名: ${removed.join(',')}` };
  if (added.length) return { bump: 'minor', reason: `新增: ${added.join(',')}` };
  const changed = [...oldKeys].filter(k => !Object.is(oldT[k], newT[k]));
  return changed.length ? { bump: 'patch', reason: `值修正: ${changed.join(',')}` } : { bump: 'none', reason: '无变化' };
}
console.log(suggestVersion({ primary: '#06c', gap: '8px' }, { primary: '#06c', gap: '8px', radius: '4px' }));
```
