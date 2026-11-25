---
title: [JS-374] 可暂停 Promise 与生成器调度
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-374：可暂停 Promise 与生成器调度

**答**：
- 可暂停语义的两种实现：① 信号量 gate（await gate()：暂停点等 resume 信号）；② 生成器（yield 交出控制权，外部 .next() 恢复）——前者适合流程级暂停，后者适合步进式（分步向导/算法单步调试）
- 暂停场景：轮播 hover 暂停、下载限速、动画逐帧调试、游戏暂停——「暂停不取消」（恢复后继续）与「取消」（丢弃）要区分 API 面
- deferred 模式：`{ promise, resolve, reject }` 三件套是所有「外部控制异步流」的原子——手动 gate、任务栅栏、测试桩都靠它
- 生成器 + 队列：把生成器当「可恢复任务」，外部调度器控制推进节奏（协程式调度）——React 早期 suspender、游戏脚本引擎都这么实现
- 边界注意：生成器内 await 需要套 async generator（yield 与 await 混用时推进语义变复杂）；暂停期间收到的消息要决定「缓冲还是丢弃」

```javascript
function createGate() {
  let release;
  let gate = new Promise(r => release = r);
  return {
    async wait() { await gate; },                        // 暂停点
    resume() { const r = release; gate = new Promise(res => release = res); r(); },  // 先换新 gate 再释放旧的
    pause() { /* gate 已由 resume 重建，暂停点天然生效 */ },
  };
}
const g = createGate();
async function worker() {
  while (true) {
    await g.wait();                       // 可暂停
    await doStep();
  }
}
```

**追问**：

1. `createGate` 里 resume 之后为什么必须立刻重建 gate？ → 否则恢复后马上再进 `wait()` 会 await 已 resolve 的旧 Promise 直接穿过去，暂停点失效；顺序应是先换新 gate 再 release 旧的那个。
2. 生成器里 yield 出 Promise，谁来负责推进？ → 调度器拿到 yield 值必须 `await` 后把结果 `next(value)` 回传；不 await 直接 next，生成器内部只能拿到一个未决 Promise。
3. 暂停期间到达的事件该缓冲还是丢弃？ → 状态型数据（最新值有效）只留最后一个即可；事件型（不能丢）要入队并在 resume 后按序消费，同时设队列上限防止内存无限增长。
