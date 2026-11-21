---
title: [H5-159] MutationObserver 深入：配置项、旧值与批量回调？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-159：MutationObserver 深入：配置项、旧值与批量回调？
**答**：
- 配置项：`childList`（子节点增删）、`attributes` + `attributeFilter`（属性白名单）、`characterData`（文本变更）、`subtree`（扩展到全部后代——不加只观察直接子级！）、`attributeOldValue/characterDataOldValue`（记录旧值，不开恒为 null）。
- 回调是**批**的：一次同步代码引发的 N 个变更合并为一次回调、N 条 MutationRecord；时机是微任务（DOM 变更后、渲染前）。
- 坑：被移除节点的内部后续变更不再产生记录（脱离观察树）；class 连改 3 次产生 3 条 record，做脏标记时要按 target 去重合并。
- `takeRecords()` 可同步取走未回调的记录，`disconnect()` 停止观察；与 ResizeObserver（尺寸）/IntersectionObserver（可见性）各管一维。

```javascript
// 深入 MutationObserver：配置、旧值、批量回调
const target = document.querySelector('.list');

const mo = new MutationObserver((records, observer) => {
  // 回调是"批"的：一次同步代码引发的 N 个变更 → 一次回调 N 条 record
  // 时机：微任务，DOM 变更后、渲染前
  for (const r of records) {
    switch (r.type) {
      case 'childList':
        console.log('节点增删', r.addedNodes, r.removedNodes, '于', r.target);
        break;
      case 'attributes':
        // oldValue 需要 attributeOldValue: true，否则恒为 null
        console.log('属性', r.attributeName, r.oldValue, '->',
                    r.target.getAttribute(r.attributeName));
        break;
      case 'characterData':
        console.log('文本', r.oldValue, '->', r.target.data);
        break;
    }
  }
});

mo.observe(target, {
  childList: true,          // 子节点增删
  subtree: true,            // 扩展到所有后代（不加只看直接子级！）
  attributes: true,         // 属性变更
  attributeFilter: ['class', 'data-state'],   // 白名单降噪
  attributeOldValue: true,  // 记录旧属性值
  characterData: true,      // 文本节点内容变更（同样依赖 subtree 覆盖深层）
  characterDataOldValue: true,
});

// 坑 1：被 remove 的节点其内部后续变更不再产生记录（脱离观察树）
// 坑 2：批处理需要自己合并 —— class 连改 3 次有 3 条 record，做脏标记要按目标去重
function coalesce(records) {
  const touched = new Set();
  for (const r of records) touched.add(r.target);
  return [...touched];      // 去重后再触发重渲染
}

// 坑 3：disconnect 前可用 takeRecords() 同步取走未回调的记录（收尾用）
const pendingRecords = mo.takeRecords();
mo.disconnect();

// 典型场景：虚拟列表检测 DOM 被外部改动、编辑器检测粘贴注入、
// 与 ResizeObserver（尺寸）/IntersectionObserver（可见性）各管一维
```
