---
title: [NODE-211] 流背压的本质与 JS 层面的表现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-211：流背压的本质与 JS 层面的表现？
**答**：
- 本质：生产速度 > 消费速度时，数据积压在内存。背压机制 = 消费方向告诉生产方向"先停一下"——TCP 滑动窗口思想在流 API 的投影（NODE-010 基础之上的机制层）。
- JS 表现：可写流 `write()` 返回 false 表示内部缓冲区超过 highWaterMark，应暂停读取并监听 'drain'；`writableNeedDrain` 属性。
- 反模式：忽略 write 返回值连续 write（内存膨胀）——大文件处理 OOM 的头号原因。
- pipeline 是正确姿势：官方 API 自动处理背压传递与错误清理（NODE-212 详述）。
- 面试加分：指出 highWaterMark 是"阈值不是上限"——write 依然会执行，只是提示该停了。

```javascript
// 反模式 vs 正确姿势
const rs = createReadStream(bigFile);
const ws = createWriteStream(gzFile);
// 反模式：rs.on('data', chunk => ws.write(chunk)) —— 忽略返回值，内存暴涨
// 手工正确版：
rs.on('data', chunk => {
  if (!ws.write(chunk)) rs.pause();            // 缓冲超限 → 暂停生产
});
ws.on('drain', () => rs.resume());             // 消化完 → 恢复
// 生产推荐：pipeline 自动背压
import { pipeline } from 'node:stream/promises';
await pipeline(rs, ws);
```
