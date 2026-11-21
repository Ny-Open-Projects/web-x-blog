---
title: [HW-114] 手写 RBAC 权限控制——v-permission 指令、按钮级权限点与指令失效防呆
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：按钮级权限两条路线：v-if（组件不渲染，安全但失去状态）与指令（隐藏但 DOM 还在——**必须配合路由级校验**，隐藏 ≠ 安全）。指令实现：权限码集合比对，无权限移除节点或置灰；防呆点：权限更新后已移除的节点无法恢复（移除前记住引用可恢复），推荐默认置灰 + disabled，关键操作再 v-if。

```javascript
// Vue 指令实现
const userPerms = new Set(['goods:edit', 'order:view']);    // 登录时注入

function hasPerm(code) {
  if (code.includes('||')) return code.split('||').some((c) => userPerms.has(c.trim()));
  return userPerms.has(code);                               // 支持 "a||b" 任一满足
}
export const permission = {
  mounted(el, binding) {
    if (hasPerm(binding.value)) return;
    if (binding.modifiers.hide) {
      el.style.display = 'none';                            // 仅隐藏（DOM 仍在——不安全）
    } else {
      el.setAttribute('disabled', '');                      // 默认置灰禁用
      el.setAttribute('aria-disabled', 'true');
      el.title = '无权限';                                   // 可见性反馈
    }
  },
  updated(el, binding) { /* 权限变更后重新评估 */ },
};
// <button v-permission="'goods:edit'">编辑</button>
// <button v-permission.hide="'admin'">危险操作</button>
```
```jsx
// React 版本 + 安全防线：权限点组件
function RequirePerm({ perm, children }) {
  return hasPerm(perm) ? children : null;                    // 不渲染 = 真正不可触发
}
// 服务端防线（必说）：前端权限只是 UX——接口必须独立鉴权，
// 隐藏按钮挡不住直接调 API；无权限调用返回 403 才是安全边界
```

**评分点**：
- 前端权限是 UX 不是安全的边界认知（必须说接口鉴权）——本题最高权重评分点。
- 指令的 hide 与 disabled 两种模式及其差异（DOM 存在性）。
- 权限码表达式（|| 任一）扩展。
- 无障碍（aria-disabled + 可见提示）与权限变更更新语义。
