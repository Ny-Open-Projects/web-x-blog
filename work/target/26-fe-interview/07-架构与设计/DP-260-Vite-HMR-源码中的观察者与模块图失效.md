---
title: [DP-260] 源码识别：Vite HMR 源码中的观察者与模块失效链？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-260：源码识别：Vite HMR 源码中的观察者与模块失效链？
**答**:
- 观察者链：chokidar（文件系统观察者）→ server 触发 handleHotUpdate → 模块图查询受影响模块 → ws 广播更新消息（三级观察者转发）。
- 策略：模块边界传播策略——顺着 importer 链向上找"可接受更新的边界"（accepting module），找不到则整页刷新。
- 命令：客户端收到 update → 执行 HMR 命令（module.invalidate → 重新 import → accept 回调）。
- 识别要点：能解释 import.meta.hot.accept 的"接受"语义（声明自己是边界）与 CSS/React 的内置 accept 实现。

```javascript
// Vite HMR 链路（源码级简化）
chokidar.watch(root).on('change', async (file) => {
  const mods = moduleGraph.getModulesByFile(file);        // 模块图：失效起点
  const updates = [];
  for (const mod of mods) {
    mod.isSelfAccept ? updates.push({ type: 'js-update', path: mod.url })
                     : propagate(mod, updates);           // 策略：向上传播找边界
  }
  updates.length ? ws.send({ type: 'update', updates })  // 观察者广播
                 : ws.send({ type: 'full-reload' });     // 无边界 → 刷新
});
// 客户端：
import.meta.hot.accept(mod => { mod.default?.(); rerender(); });   // 边界声明 + 命令执行
// import.meta.hot.dispose(data => { data.style = el.textContent })  // 旧模块清理命令
```
