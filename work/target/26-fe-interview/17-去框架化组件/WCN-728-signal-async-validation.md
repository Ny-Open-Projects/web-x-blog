---
title: [WCN-728] signal 表单的异步校验（debounce + 服务端查重）如何避免竞态与闪烁？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-728：signal 表单的异步校验（debounce + 服务端查重）如何避免竞态与闪烁？

**答**：
- 结论：每次输入Generate 一个递增 epoch，只有「最新 epoch」的校验结果才允许写入错误 signal；旧请求返回直接丢弃，避免旧结果覆盖新结果。
- 配合 AbortController 取消过期请求；校验中状态用 pending signal 控制 loading；debounce 用 setTimeout + 清理。
- 追问钩子：用户快速输入后又删回原值，是否该跳过校验？考察「值未变化」的短路优化。

```javascript
const value = signal(''), error = signal(''), pending = signal(false);
let epoch = 0, timer = null;
value.subscribe?.(() => {}); // 假设 value 可订阅
function onInput(v) {
  value.value = v;
  clearTimeout(timer);
  const my = ++epoch;                       // 每次输入 epoch+1
  timer = setTimeout(async () => {
    pending.value = true;
    const ctrl = new AbortController();
    try {
      const res = await check(v, ctrl.signal);
      if (my !== epoch) return;             // 过期结果丢弃
      error.value = res.exists ? '已存在' : '';
    } finally { if (my === epoch) pending.value = false; }
  }, 300);
}
async function check() { return { exists: false }; }
console.log('epoch 机制保证只接受最新校验结果');
```
