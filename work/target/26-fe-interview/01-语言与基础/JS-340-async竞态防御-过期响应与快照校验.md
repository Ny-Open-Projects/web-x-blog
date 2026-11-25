---
title: [JS-340] async 竞态防御：过期响应与快照校验
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-340：async 竞态防御：过期响应与快照校验

**答**：
- 竞态根因：async 函数在 await 之间「状态可被并发修改」——搜索框快速输入时旧请求后到覆盖新结果，是最常见案例
- 三种防御：① AbortController 取消旧请求（治本）；② 请求序号/令牌校验（seq: 响应时检查自己是否仍是最新）；③ 快照 + 条件提交（捕获 await 前的状态，恢复后比对不一致则丢弃）
- 取消的完整性：不只是 fetch abort——业务后续逻辑（setState）也要检查 cancelled 标记，否则「请求取消了但 UI 更新了」
- 通用封装：useLatest-style hook 或 requestManager（按 key 取消旧请求 + 合并去重）——把竞态防御从业务代码下沉到请求层
- 与防抖的区别：防抖减少请求频率但不解决「在途竞态」；两者组合（防抖 + 取消旧）才是完整方案

```javascript
let seq = 0;
async function search(q) {
  const mySeq = ++seq;
  const ctrl = new AbortController();
  currentCtrl?.abort();           // 取消上一个
  currentCtrl = ctrl;
  try {
    const res = await fetch(`/api/search?q=${q}`, { signal: ctrl.signal });
    const data = await res.json();
    if (mySeq !== seq) return;    // 双保险: 已有更新的搜索
    render(data);
  } catch (e) {
    if (e.name !== 'AbortError') throw e;   // 取消不算错误
  }
}
```
