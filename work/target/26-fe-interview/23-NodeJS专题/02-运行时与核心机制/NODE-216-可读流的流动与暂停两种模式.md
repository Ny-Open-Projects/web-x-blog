---
title: [NODE-216] 可读流的流动与暂停两种模式？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-216：可读流的流动与暂停两种模式？
**答**：
- 两种模式：paused（默认，read() 手动拉取）与 flowing（data 监听器/rAF 类 pipe 自动推送）。切换开关：`readable.pipe()` / `on('data')` 进入 flowing；`unpipe()` / `pause()` 回 paused。
- 高水位线语义：readable 内部缓冲到 highWaterMark 后停止底层 _read 调用——push 持续超过水位线则 push 返回 false（生产者背压）。
- 混用陷阱：既 on('data') 又 read() 会造成消费竞争；async iterator（for await）内部是 paused 模式的封装——推荐用它写消费逻辑。
- 面试加分：指出 flow 模式下 'readable' 事件与 'data' 事件的互斥关系。

```javascript
// paused 模式（显式拉取）
readable.on('readable', () => {
  let chunk;
  while ((chunk = readable.read()) !== null) process(chunk);
});
// flowing 模式
readable.on('data', chunk => process(chunk));
readable.pause(); readable.resume();
// async iterator（推荐）
for await (const chunk of readable) process(chunk);   // 内部 pause/read/push 封装
// 水位线与 push 背压（自定义可读流）
class Source extends Readable {
  _read() {
    const ok = this.push(nextChunk());               // 返回 false = 缓冲区满
    if (!ok) setTimeout(() => this._read(), 10);     // 等待消费消化，勿暴力继续 push
  }
}
```
