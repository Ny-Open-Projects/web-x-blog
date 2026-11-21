---
title: [WCN-081] 笔试：手写 Signals 版秒杀倒计时与库存联动组件
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-081：笔试：手写 Signals 版秒杀倒计时与库存联动

**题目**：秒杀组件：① `endTime` signal 为时间戳，`remain` computed 输出剩余秒数（由 1Hz tick 驱动）；② `stock` signal 服务端推送；③ `canBuy` computed：remain > 0 且 stock > 0；④ 倒计时归零自动派发 `ended` 事件（只派一次）；⑤ 组件销毁停止 tick；⑥ 展示层直接绑定 remain 与 canSubmit（无重渲染）。

**答**：

```javascript
import { createSignal, computed, effect } from './mini.js';

export function setupSeckill(host, { endTime, stock }) {
  const [now, setNow] = createSignal(Date.now());
  const timer = setInterval(() => setNow(Date.now()), 1000);   // 1Hz tick

  const remain = computed(() => Math.max(0, Math.floor((endTime() - now()) / 1000)));
  const canBuy = computed(() => remain() > 0 && stock() > 0);

  let fired = false;
  const stopWatch = effect(() => {
    const r = remain();
    document.querySelector('.cd').textContent = `${Math.floor(r / 60)}:${String(r % 60).padStart(2, '0')}`;
    document.querySelector('.buy').disabled = !canBuy();
    if (r === 0 && !fired) {
      fired = true;   // 只派发一次
      host.dispatchEvent(new CustomEvent('seckill-ended', { bubbles: true, composed: true }));
    }
  });

  return {
    destroy() { clearInterval(timer); stopWatch(); },   // 生命周期配对
  };
}
// 服务端推送：socket.on('stock', (n) => stock(n));
```

**评分点**：
- tick 与 remain 分层：tick 是"时间源"，remain 是纯 computed（可测试性）。
- canBuy 汇聚两个独立 signal；disabled 直绑无重渲染。
- ended 事件用 fired 标志防重复派发（remain 保持 0 时每秒都可能触发）。
- destroy 清理 interval 与 effect（生命周期配对）。
