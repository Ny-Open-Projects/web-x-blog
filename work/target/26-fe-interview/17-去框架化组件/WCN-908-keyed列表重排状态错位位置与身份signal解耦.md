---
title: [WCN-908] keyed 列表重排后 item 状态错位：位置 signal 与身份 signal 怎么解耦
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-908：keyed 列表重排后 item 状态错位：位置 signal 与身份 signal 怎么解耦

**答**：
- 结论先行：把「列表位置」与「条目身份」混在一个 signal 里，重排后按位置复用状态必然错位；正确做法是按稳定 key 存状态，位置只决定渲染顺序。
- 数据结构：用 `Map<key, Signal>` 或 `key → state` 的字典存每个条目状态；渲染时遍历 id 数组按 key 取状态，而不是按下标存 state 数组。
- 细粒度更新下尤其重要：Solid 的 `<For>` 按引用 keyed、`<Index>` 按索引，重排时用 `<For>` 才不会让输入框内容串位；虚拟列表复用 DOM 也要按 key reset。
- 身份要稳定：用后端 id 而非数组下标当 key；临时项用持久化的临时 id（创建时生成，删除才回收），避免「插入头部导致全体错位」（大促商品列表常见）。
- 追问钩子：面试官问「key 相同但内容全变了怎么办」——答：key 语义就是「同一实体」，若实体真的替换应换 key；否则在 key 不变时显式 patch 内容字段。

```javascript
// 按 key 存状态，重排不错位
const items = signal([{ id: 'a', name: 'A' }, { id: 'b', name: 'B' }]);
const stateById = new Map(); // 身份 → 状态 signal，与位置无关
function stateFor(id) {
  if (!stateById.has(id)) stateById.set(id, signal('')); // 输入内容
  return stateById.get(id);
}
function render() {
  return items.value.map(it => ({
    key: it.id,
    input: stateFor(it.id).value, // 按 key 取，重排后内容跟着 id 走
  }));
}
items.value = [items.value[1], items.value[0]]; // 重排
console.log(render()); // B 的输入仍是 B 的，不串位
```
