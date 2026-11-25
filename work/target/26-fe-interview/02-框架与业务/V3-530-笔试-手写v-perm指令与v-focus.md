---
title: [V3-530] 笔试：手写自定义指令集（v-perm / v-focus / v-lazy）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 语言特性]
type: 笔试题
---

## V3-530：笔试：手写自定义指令集

**答**：实现三个指令：① `v-perm="'x:delete'"`：无权限时移除元素（mounted 时判定），支持动态权限更新（updated 钩子重新判定，移除的元素缓存可恢复）；② `v-focus`：挂载聚焦（input 上）+ 组件内 el.$el 处理；③ `v-lazy`：IntersectionObserver 懒加载图片（进入视口设 src，rootMargin 可配，卸载 disconnect）。写出实现。

```javascript
// v-perm: 支持动态恢复
const removed = new WeakMap();
app.directive('perm', {
  mounted(el, { value }) { check(el, value); },
  updated(el, { value, oldValue }) {
    if (value !== oldValue) check(el, value);
  },
});
function check(el, perm) {
  const ok = authStore.has(perm);
  if (!ok && el.isConnected) {
    const anchor = document.createComment('v-perm');
    removed.set(el, { parent: el.parentElement, next: el.nextSibling, anchor });
    el.parentElement?.replaceChild(anchor, el);     // 注释占位, 可恢复
  } else if (ok && removed.has(el)) {
    const { parent, next, anchor } = removed.get(el);
    parent?.insertBefore(el, anchor);               // 权限恢复
    anchor.remove();
    removed.delete(el);
  }
}

// v-focus
app.directive('focus', {
  mounted(el) { (el.tagName === 'INPUT' ? el : el.querySelector('input'))?.focus(); },
});

// v-lazy
app.directive('lazy', {
  mounted(el, { value, modifiers }) {
    const io = new IntersectionObserver((ents) => {
      if (ents[0].isIntersecting) {
        el.src = value;                             // 进入视口才加载
        io.disconnect();
      }
    }, { rootMargin: modifiers.top ? '800px' : '200px' });
    io.observe(el);
    el.__io = io;
  },
  unmounted(el) { el.__io?.disconnect(); },
});
```

**评分点**：
- v-perm 的可恢复设计（注释占位）与 updated 重判
- v-focus 的组件包裹（el.$el/querySelector）处理
- v-lazy 的 IO 生命周期（卸载 disconnect 防泄漏）
- 修饰符扩展（rootMargin 配置）
