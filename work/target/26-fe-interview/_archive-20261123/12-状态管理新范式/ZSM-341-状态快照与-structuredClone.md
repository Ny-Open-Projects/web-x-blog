---
title: [ZSM-341] 什么时候真的需要深拷贝状态（structuredClone 的边界）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-341：什么时候真的需要深拷贝状态（structuredClone 的边界）

**答**:
- 绝大多数场景不需要深拷贝：结构共享（浅展开/immer）才是正确默认；真正需要深拷贝的三类——发给不可信边界（postMessage/WCC）、长存快照（回放/审计，防后续变异污染）、隔离外部可变对象（SDK 持有引用会改）
- structuredClone 能力与限制：支持 Map/Set/Date/循环引用，不支持函数/DOM/原型链（类实例变普通对象）——正好符合「数据快照」语义
- 性能：大对象深拷贝是毫秒级操作，放热路径会卡帧；用「拷贝前裁剪」只拷必要子树
- JSON.stringify 替代方案的差异：丢 undefined/Date/Map、key 顺序敏感、不支持循环——快照场景优先 structuredClone

```javascript
// 快照防污染：回放基线
const baseline = structuredClone(store.getState())
replay(baseline)                 // 后续 store 随便变，baseline 不受影响
// 发给 iframe（不可信边界）
iframe.contentWindow.postMessage(structuredClone(dto), origin)
// 拷贝前裁剪
const slim = structuredClone({ items: state.items.slice(0, 50) })
```
