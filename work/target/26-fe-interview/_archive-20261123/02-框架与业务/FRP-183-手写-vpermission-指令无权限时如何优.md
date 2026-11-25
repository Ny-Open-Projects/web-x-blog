---
title: [FRP-183] 手写 v-permission 指令：无权限时如何优雅地移除节点？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-183：手写 v-permission 指令：无权限时如何优雅地移除节点？

**答**：
- mounted/updated 时检查权限集（store/prop 传入），无权限时**移除元素**——直接 `el.remove()`。
- 需要恢复的场景（权限动态变化）：移除前把 el 与锚点存进 binding，恢复时 `insertBefore` 放回原位置——用**注释占位符**记录原位。
- 对比 v-if 方案：指令不做编译期分支，适合"权限表运行时才确定"的场景；但指令移除的节点在父组件 patch 时可能被重建，所以 updated 里要重复判断。
- 更完备的做法是配合函数式组件/无权限时渲染注释节点，保持 diff 稳定。

```javascript
// 简化实现，帮助理解 v-permission
// 注册：app.directive('permission', vPermission)
const vPermission = {
  // mounted：首次检查并按需移除
  mounted(el, binding) {
    const { value } = binding;                 // v-permission="'admin'" 或数组
    const perms = usePermissionStore();        // 响应式权限集

    if (!hasPerm(perms, value)) {
      removeEl(el, binding);
    }
    // 订阅权限变化：动态恢复/移除
    binding._unwatch = watchEffect(() => {
      hasPerm(perms, value) ? restoreEl(el, binding) : removeEl(el, binding);
    });
  },
  updated(el, binding) {
    // 组件更新可能重建/移动节点：重新校验
    const { value } = binding;
    hasPerm(usePermissionStore(), value) ? restoreEl(el, binding) : removeEl(el, binding);
  },
  unmounted(el, binding) {
    binding._unwatch?.();                      // 清理订阅（避免泄漏）
  }
};

function hasPerm(perms, required) {
  if (!required) return true;
  const need = Array.isArray(required) ? required : [required];
  return need.some(p => perms.includes(p));    // 任一命中即可（or 语义）
}

function removeEl(el, binding) {
  if (!el.parentNode) return;
  // 用注释占位记录原位置，便于恢复
  const placeholder = document.createComment('v-permission');
  el.parentNode.insertBefore(placeholder, el);
  el.parentNode.removeChild(el);
  binding._placeholder = placeholder;
}

function restoreEl(el, binding) {
  const ph = binding._placeholder;
  if (ph && ph.parentNode) {
    ph.parentNode.insertBefore(el, ph);
    ph.parentNode.removeChild(ph);
    binding._placeholder = null;
  }
}

// 用法：
// <button v-permission="'user:delete'">删除</button>
// <button v-permission="['admin', 'editor']">编辑</button>
// 注意边界：权限控制的"移除"只是 UI 层，接口层必须二次校验——前端权限只管体验
```
