---
title: [DP-297] 笔试题：手写权限指令 v-perm（隐藏/置灰/提示）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-297：笔试题：手写权限指令 v-perm（隐藏/置灰/提示）？
**答**：实现 Vue 自定义指令 v-perm：1) 值为权限码字符串或数组（任一满足即通过）；2) mode: hide（移除 DOM）/disable（禁用+title 提示）；3) 权限快照热更后已渲染元素同步刷新；4) 提供全局注册与测试辅助。
**评分点**：
- 数组语义（anyOf）正确。
- disable 模式不改变结构（只加属性），hide 模式移除并保存注释占位（热更恢复）。
- 热更刷新：订阅权限 store，变更时重新判定所有已挂载节点。
- 注释占位恢复（hide 后 store 变化可重新插入）。
```javascript
// Vue 3 指令
import { permStore } from './perm';
const mounted = new Map();  // el → { binding }
export const vPerm = {
  mounted(el, binding) {
    mounted.set(el, binding);
    apply(el, binding);
    el.__unsub = permStore.subscribe(() => apply(el, mounted.get(el)));    // 3) 热更刷新
  },
  unmounted(el) { el.__unsub?.(); mounted.delete(el); },
};
function can(perms) {
  const codes = Array.isArray(perms) ? perms : [perms];
  return codes.some(c => permStore.perms.includes(c));     // 1) anyOf
}
function apply(el, { value, modifiers }) {
  const mode = modifiers.disable ? 'disable' : 'hide';     // 2) v-perm.disable
  if (can(value)) {
    if (el.__hidden) { el.__hidden.replaceWith(el); el.__hidden = null; }   // 4) 恢复
    el.disabled = false; el.removeAttribute('title');
  } else if (mode === 'hide') {
    if (!el.__hidden) { const c = document.createComment('v-perm');
      el.replaceWith(c); el.__hidden = c; }
  } else {
    el.disabled = true; el.title = '无权限，点击申请';
  }
}
```
