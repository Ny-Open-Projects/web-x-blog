---
title: [BAS-099] compositionstart 这组中文输入法事件是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-099：compositionstart 这组中文输入法事件是什么？
**答**：
- 输入法组词过程触发 compositionstart → compositionupdate（多次）→ compositionend，期间敲的拼音不是最终输入。
- 搜索框实时联想必须处理：组词期间不触发搜索，等 compositionend 再查，否则拼音字母被当成关键词。
- 通用做法：start 置 isComposing = true，end 置 false；input 回调里先判断再处理。

```javascript
let composing = false;
const input = document.querySelector('#search');
input.addEventListener('compositionstart', () => (composing = true));
input.addEventListener('compositionend', () => {
  composing = false;
  doSearch(input.value);                    // 组词结束才搜索
});
input.addEventListener('input', () => {
  if (!composing) doSearch(input.value);    // 英文数字直接搜
});
```
