---
title: [WCN-044] 笔试：手写按视口可见性懒 define 的调度器（IntersectionObserver + 队列去重）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Web Components]
type: 笔试题
---

## WCN-044：笔试：手写按视口可见性懒 define 的调度器

**题目**：实现 `lazyDefine(tag, loader)` 全局注册表：① 扫描文档中所有未 defined 的带 `data-lazy` 元素，可见时才调用 loader 并 define；② 同一 tag 的 loader 只触发一次（并发去重）；③ loader 失败最多重试 2 次；④ 已 define 的 tag 从观察列表移除；⑤ 提供 `flushAll()` 立即全部加载（用于预加载）。

**答**：

```javascript
const inflight = new Map();   // tag -> Promise（并发去重）
const pending = new Set();    // 待观察元素
const io = new IntersectionObserver((entries) => {
  for (const en of entries) {
    if (!en.isIntersecting) continue;
    io.unobserve(en.target);
    pending.delete(en.target);
    const tag = en.target.tagName.toLowerCase();
    ensureDefine(tag, en.target.dataset.loader ?? tag);
  }
}, { rootMargin: '200px' });

function ensureDefine(tag, loaderPath, attempt = 0) {
  if (customElements.get(tag)) return Promise.resolve();
  if (!inflight.has(tag)) {
    const p = import(/* @vite-ignore */ loaderPath)
      .then((m) => {
        const Ctor = m.default ?? m[tag.replace(/-(\w)/g, (_, c) => c.toUpperCase())];
        if (!Ctor) throw new Error(`no export for ${tag}`);
        customElements.define(tag, Ctor);
      })
      .catch((err) => {
        inflight.delete(tag);                       // 失败允许重试
        if (attempt < 2) return ensureDefine(tag, loaderPath, attempt + 1);
        throw err;
      });
    inflight.set(tag, p);
  }
  return inflight.get(tag);
}

export function observeLazy(root = document) {
  for (const el of root.querySelectorAll('[data-lazy]:not(:defined)')) {
    pending.add(el); io.observe(el);
  }
}
export function flushAll() {
  for (const el of pending) {
    io.unobserve(el);
    ensureDefine(el.tagName.toLowerCase(), el.dataset.loader ?? el.tagName.toLowerCase());
  }
  pending.clear();
}
```

**评分点**：
- inflight Map 去重：同 tag 并发只发一次请求（关键考点）。
- IntersectionObserver 提前量 rootMargin + 回调里 unobserve（一次性触发）。
- 失败重试带次数上限，且 inflight.delete 让重试成为可能。
- `:not(:defined)` 过滤 + flushAll 全量预热接口（工程完整性）。
- loader 路径可被 dataset 覆盖（可配置性）。
