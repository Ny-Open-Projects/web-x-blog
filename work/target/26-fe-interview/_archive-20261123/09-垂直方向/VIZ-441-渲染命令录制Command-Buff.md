---
title: [VIZ-441] 渲染命令录制（Command Buffer）与重排序
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-441：渲染命令录制（Command Buffer）与重排序

**答**：
- 思想：渲染逻辑与执行解耦——收集命令（记录 pass/draw），统一排序再执行。
- 收益：排序优化（按材质/深度）不必侵入渲染逻辑；命令可复用（静态场景预录制）。
- Web：WebGPU 天生 command encoder；WebGL 模拟为 draw 队列。

```javascript
// 命令录制
class RenderList {
  constructor() { this.cmds = []; }
  draw(cmd) { this.cmds.push(cmd); }        // { program, vao, uniforms, sortKey }
  flush(execute) {
    this.cmds.sort((a, b) => a.sortKey - b.sortKey);
    for (const c of this.cmds) execute(c);
    this.cmds.length = 0;                   // 复用数组
  }
  // 静态场景：cmds 不清空，直接 flush 重放（脏标记触发重录）
```
