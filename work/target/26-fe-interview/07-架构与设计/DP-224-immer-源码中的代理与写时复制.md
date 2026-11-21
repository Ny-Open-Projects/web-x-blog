---
title: [DP-224] 源码识别：immer 源码中的代理与写时复制？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-224：源码识别：immer 源码中的代理与写时复制？
**答**：
- 代理模式（核心）：draft 是原对象的 Proxy，get 返回子 draft（懒代理），set 记录修改（marked）——用户以为在改，实际在记录。
- 写时复制（COW）：produce 结束时只对"被修改路径"新建对象，未动分支引用复用（structural sharing）——不可变数据的高效实现。
- 命令记录：修改操作收集为 patches（forward/backward），天然支持撤销重做/增量同步。
- 识别要点：能解释 finalize 的递归逻辑——draft.modified 才 clone，否则原引用返回；以及 scope 内 finishDraft 的批量处理。

```javascript
// immer 源码级简化
function produce(base, recipe) {
  const scope = { patches: [] };
  const draft = createProxy(base, scope);
  recipe(draft);                                   // 用户"直接改"，实际是代理记录
  return finalize(draft, scope);
}
function createProxy(target, scope) {
  const state = { base: target, modified: false, copy: null };
  return new Proxy(target, {
    get(t, k) { return state.modified ? state.copy[k] : t[k]; },
    set(t, k, v) {
      if (!state.modified) { state.copy = { ...t }; state.modified = true; }  // 首次写：COW
      state.copy[k] = v;
      scope.patches.push({ op: 'replace', path: [k], value: v });   // 命令记录
      return true;
    },
  });
}
function finalize(s) { return s.modified ? s.copy : s.base; }       // 未改：引用复用（structural sharing）
// produce(state, d => { d.user.name = 'x' }) → 只有 user 节点是新的，其余引用不变
```
