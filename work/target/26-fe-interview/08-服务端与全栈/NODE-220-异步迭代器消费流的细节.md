---
title: [NODE-220] 异步迭代器消费流的细节？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-220：异步迭代器消费流的细节？
**答**：
- for await (chunk of stream)：paused 模式的语法糖；async 迭代器在循环体抛错时自动 destroy 流（cleanup 集成）。
- 提前退出：break 后调用 stream.destroy()（for await 会自动 destroy，但错误路径建议 try/finally 显式）。
- 与 pipeline 的选择：复杂多级管道用 pipeline；单读多分支处理逻辑用 for await 更直观。
- 并发消费陷阱：循环体内 await 慢操作会让上游背压（这是特性不是 bug——天然流控）；真正需要并发时把 chunk 推进有界队列。

```javascript
// 基本消费
try {
  for await (const chunk of createReadStream(file)) {
    await process(chunk);          // 慢消费 → 上游自动背压（天然流控）
  }
} finally {
  source.destroy();                // 显式兜底（异常路径清理）
}
// 并发消费（有界队列 + 流控）
const queue = new AsyncQueue(4);   // 自建有界队列（NODE-45x 笔试题）
for await (const chunk of source) {
  await queue.push(() => process(chunk));   // 队列满时等待 —— 等价于背压
}
// async iterator 生成（Readable.from）
const words = Readable.from(['a\n', 'b\n']).compose(lineSplitter());   // stream.compose 组合
```
