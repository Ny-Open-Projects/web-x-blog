---
title: [RBL-573] 构建进度展示工程：增量日志、进度条与 CI 下的降级渲染
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-573：构建进度展示工程：增量日志、进度条与 CI 下的降级渲染

**答**：
- 进度输出看似 UI 小事，实际是并发架构问题：数千模块并行完成时逐条打印会淹没终端——需要**事件流 + 渲染层分离**：构建器只发结构化事件（moduleDone/chunkWritten/diagnostic），渲染层决定 TUI（终端 in-place 刷新）还是 CI 纯文本。
- 进度百分比的现实困难：模块数未知（动态 import 运行时才发现）且成本不均（transform 一个大文件 = 100 个小文件）——用「已完成的加权工作量 / 预估总工作量」：预估 = 首轮构建 profile 缓存 + 当前已知模块数，渐进修正；展示上宁可「阶段 + 计数」（transforming 340/estimated 1200）也别给假百分比。
- 刷新节流：TUI 每 100ms 重绘（高并发下事件合帧），滚动日志区 + 固定状态行分离；CI（非 TTY）自动降级为阶段边界一次性输出——检测 isTTY 与 CI 环境变量。
- 诊断事件拥有最高渲染优先级（错误要立即完整输出且不被进度行覆盖）；构建结束必须输出「结尾快照」（总耗时/产物表）保证 CI 日志可追溯。
- 追问钩子：为什么进度输出不能放构建线程同步做？——stdout 阻塞会拖慢构建热路径；事件走 channel 由独立渲染线程消费，构建器与展示完全解耦（这也是渲染层可替换的前提）。

```javascript
// 事件流与渲染分离
const events = new EventEmitter();            // 构建器只发事件，不打印
builder.on('module:done', e => events.emit('ev', { type: 'moduleDone', ...e }));
builder.on('diagnostic', d => events.emit('ev', { type: 'diag', ...d, prio: 0 }));

// TUI 渲染层：合帧刷新 + 优先级插播
class TuiRenderer {
  constructor(ev, out = process.stdout) { this.buf = []; this.ev = ev; this.out = out; }
  start() {
    this.ev.on('ev', e => {
      if (e.type === 'diag') { this.flushState(); console.error(renderDiag(e)); return; } // 错误立即出
      this.buf.push(e);
    });
    this.timer = setInterval(() => this.renderState(), 100);   // 100ms 合帧
  }
  renderState() {
    const n = this.buf.filter(e => e.type === 'moduleDone').length;
    this.out.cursorTo(0); this.out.write(`transforming ${n}/${builder.estimate()} (weighted)`);
    this.buf.length = 0;
  }
  flushState() { clearInterval(this.timer); this.renderState(); }
}

// CI 降级：非 TTY 只输出阶段边界与结尾快照
if (!process.stdout.isTTY || process.env.CI) builder.setRenderer(new PlainRenderer());
```
