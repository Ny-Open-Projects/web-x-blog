---
title: [PER-608] 手写一个 DOM clobbering 检测器：扫描净化后的 HTML 是否残留可覆盖全局的 id/name 属性
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-608：手写一个 DOM clobbering 检测器：扫描净化后的 HTML 是否残留可覆盖全局的 id/name 属性

**答**：
- 检测目标：净化输出里残留的 `id=`/`name=` 属性中，与常见全局冲突名（config/data/settings/state/window 已有属性）或表单链模式（form[name]）匹配的元素。
- 要点：把净化输出解析成 DOM，遍历收集 id/name；冲突判定两级——直接命中危险名单（config/settings 等）一定报；与 window 已有属性冲突报 warning（`window` 上 in 检查）。
- 边界：业务合法锚点 id（app/root/modal-xxx）走白名单；name 属性在表单控件里是功能性的（radio 分组），要区分表单内功能性 name"与可 clobber 的游离 name"。
- 评分点：危险名名单与表单功能性 name 的区分。

```javascript

const DANGEROUS_NAMES = new Set(['config', 'settings', 'state', 'data', 'env', 'location',
  'origin', 'postMessage', 'fetch', 'params', 'query']);
const SAFE_IDS = new Set(['app', 'root', 'modal', 'toast', 'loading']);
function detectClobber(html) {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  const hits = [];
  doc.querySelectorAll('[id],[name]').forEach(el => {
    const id = el.getAttribute('id'), name = el.getAttribute('name');
    for (const [kind, val] of [['id', id], ['name', name]]) {
      if (!val || SAFE_IDS.has(val)) continue;
      const inForm = !!el.closest('form');                   // 表单内 name 是功能性的
      if (kind === 'name' && inForm && ['INPUT', 'SELECT', 'TEXTAREA'].includes(el.tagName)) continue;
      if (DANGEROUS_NAMES.has(val)) hits.push({ el: el.tagName, kind, val, level: 'high' });
      else if (val in window) hits.push({ el: el.tagName, kind, val, level: 'warn' }); // 覆盖已有全局
    }
  });
  return { hits, clean: hits.every(h => h.level !== 'high') };
}
// CI 中接在净化器之后跑：high 级阻断合并
```
