---
title: [WCN-561] Qwik 的「可恢复性」对事件处理器的特殊要求：为什么事件必须序列化成字符串 URL？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-561：Qwik 的「可恢复性」对事件处理器的特殊要求：为什么事件必须序列化成字符串 URL？

**答**：
- 结论：Qwik 目标「零水合」——页面 HTML 里不能有 JS 函数引用，事件处理器必须序列化成可懒加载的 URL 字符串。
- on:click="./chunk#handler" 形式，点击时才按 URL 加载并执行对应函数，闭包状态从 DOM/序列化状态恢复。
- 字符串 URL 可被 SSR 原样输出，浏览器无需提前下载/执行 JS。
- 追问：闭包捕获的变量如何恢复？（答：编译期提取为序列化状态挂到 DOM 属性，执行时重建）

```javascript
// SSR 输出：<button on:click="./chunk-abc.js#onClick" q:obj="{'count':0}">+</button>
function serializeHandler(fn, chunkUrl) {
  const captured = extractCaptured(fn);                 // 提取闭包依赖
  return { qrl: `${chunkUrl}#${fn.name}`, state: JSON.stringify(captured) };
}
// 客户端：点击时按 qrl 懒加载
async function onDemand(el) {
  const { qrl, state } = parseQrl(el.getAttribute('on:click'));
  const mod = await import(qrl.split('#')[0]);
  mod[qrl.split('#')[1]](restoreState(state));
}
```
