---
title: [WEB-159] storage 事件在跨页同步时有哪些序列化陷阱？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-159：storage 事件在跨页同步时有哪些序列化陷阱？
**答**：
- localStorage 只能存字符串：对象必须 JSON.stringify，Date/Map/Set/undefined/函数会直接丢或变形（Date 变字符串、Map 变空对象）。
- storage 事件的 oldValue/newValue 也是字符串：比较前先 parse，不能拿字符串直接 !== 判断"是否变化"。
- stringify 大对象有 CPU 开销，跨页高频同步别走 localStorage（用 BroadcastChannel）。
- 循环引用 stringify 会直接抛错，存前要扁平化或改用结构化克隆能力的存储。

```javascript
// 陷阱复现与安全封装
localStorage.setItem('meta', JSON.stringify({ at: new Date(), tags: new Map([['a', 1]]) }));
const back = JSON.parse(localStorage.getItem('meta'));
console.log(back.at instanceof Date); // false，Date 退化成字符串
console.log(back.tags);               // {}，Map 直接丢失

// 封装：统一入口 + 脏数据容错
function setJSON(key, value) {
  localStorage.setItem(key, JSON.stringify({ v: value }));
}
function getJSON(key, fallback = null) {
  try { return JSON.parse(localStorage.getItem(key))?.v ?? fallback; }
  catch { return fallback; }  // 历史脏数据容错
}
// 跨页监听：先 parse 再比较内容
window.addEventListener('storage', (e) => {
  if (e.key === 'meta' && JSON.parse(e.newValue ?? 'null')?.v?.id !== currentState.id) sync();
});
```
