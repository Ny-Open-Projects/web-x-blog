---
title: [WCN-259] 如何防止「effect 写信号」引发的无限循环？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-259：如何防止「effect 写信号」引发的无限循环？
**答**：
- 检测：同一批次内同一 effect 被执行超过 N 次（如 100）→ 判定循环抛错。
- 设计规范：effect 只写「其他信号」（单向流），写自己读取的信号 = 环。
- 合法模式：节流反馈（写不同信号 + 条件退出）——用「稳定不动点」检测（值不再变化即停）。
- 工具：开发模式下循环检测开启 + 打印依赖路径，生产关闭。

```javascript
let runs = 0; let lastEffect: Effect | null = null;
function runEffect(e) {
  if (e === lastEffect && ++runs > 100) throw new Error(`响应式循环：${e.debugName}`);
  if (e !== lastEffect) runs = 0;
  lastEffect = e;
  e.fn();
}
r
```
