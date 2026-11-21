---
title: [NODE-014] 流的错误处理与销毁生命周期是怎样的？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-014：流的错误处理与销毁生命周期是怎样的？
**答**：
- 流是 **EventEmitter**，`error` 事件不处理会直接抛到进程级（uncaught crash）。规则：**每条 pipeline 用集中式回调/promise 错误处理**，不要给每个流单独挂 listener。
- 销毁：`stream.destroy(err)` 触发 `close`，释放底层资源；销毁后不可再用。`pipeline`/`compose` 的核心价值就是**一处出错全链 destroy**。
- 关键事件顺序：Readable `end`（数据读完）→ Writable `finish`（数据写完刷盘）→ 两者都会在 destroy 后触发 `close`。`autoDestroy: true`（默认）保证 `end`/`finish` 后自动 close。
- 未消费的 Readable 要显式 destroy，否则 fd 一直占着（服务长跑必然 fd 泄漏告警）。

```javascript
const fs = require('node:fs');
const { pipeline } = require('node:stream/promises');

async function copyWithCleanup(src, dest) {
  const rs = fs.createReadStream(src);
  const ws = fs.createWriteStream(dest);
  try {
    await pipeline(rs, ws);            // 任一环节错误 → 全链自动 destroy + close
  } catch (err) {
    console.error('复制失败，资源已释放:', err.code);
    // 手工兜底：pipeline 已 destroy，此处保险
    rs.destroyed || rs.destroy();
    ws.destroyed || ws.destroy();
    fs.unlink(dest, () => {});         // 清理写一半的脏文件
    throw err;
  }
}

// 事件顺序验证
const demo = fs.createWriteStream('/tmp/demo.txt');
demo.on('finish', () => console.log('1. finish 数据写完'));
demo.on('close', () => console.log('2. close 资源释放'));
demo.end('hello');                      // end 触发 finish → autoDestroy → close

// 服务器退出前统一清理：关闭所有未完成流
process.on('SIGTERM', () => {
  for (const stream of [demo]) stream.destroyed || stream.destroy();
});
```

---

## 三、HTTP 服务
