---
title: [NODE-084] Node 错误处理的最佳实践（uncaughtException 之后怎么办）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-084：Node 错误处理的最佳实践（uncaughtException 之后怎么办）？
**答**：
- 分层原则：**操作错误**（Expected：网络超时、DB 拒连、4xx——用 try/catch 或 Promise catch 处理，可恢复）；**程序错误**（Bug：undefined 属性、逻辑漏洞——不该 catch 掩盖，记录后**崩溃重启**让进程管理器拉起）。
- `uncaughtException`/`unhandledRejection`：进程状态已不可信，正确动作是**记录 fatal 日志 → 优雅退出（排空连接）→ 由 PM2/K8s 重启**。吞掉继续跑会进入不可预期状态。
- 防线清单：所有 async 入口有 catch；EventEmitter 注册 `error` 监听；流全部走 pipeline；定时器/回调里的 throw 用 domain 替代方案（隔离 worker 或进程边界）；上线前 `process.on('beforeExit')` 清理检查。

```javascript
// 统一错误处理骨架
const logger = require('./logger');

// 1. 兜底：记录后优雅崩溃，交给 PM2/K8s 重启
let exiting = false;
process.on('uncaughtException', async (err) => {
  if (exiting) return;
  exiting = true;
  logger.fatal({ event: 'uncaughtException', msg: err.message, stack: err.stack });
  await gracefulShutdown({ exitCode: 1, timeout: 10000 });   // NODE-060 的排空逻辑
});
process.on('unhandledRejection', (reason, promise) => {
  // 未处理的 Promise 拒绝：Node 15+ 默认已崩，这里确保日志完整
  logger.fatal({ event: 'unhandledRejection', msg: String(reason), stack: reason?.stack });
  throw reason;   // 统一走 uncaughtException 路径
});

// 2. 操作错误：类型化 + 可重试
class OperationalError extends Error {
  constructor(code, message, { status = 500, retryable = false } = {}) {
    super(message);
    this.code = code; this.status = status; this.retryable = retryable;
  }
}

async function callDownstream(url) {
  try {
    return await fetchWithTimeout(url, 3000);
  } catch (err) {
    if (['ECONNRESET', 'ETIMEDOUT'].includes(err.cause?.code)) {
      throw new OperationalError('UPSTREAM_TIMEOUT', '下游超时', { status: 504, retryable: true });
    }
    throw err;   // 未知错误原样上抛，不吞
  }
}

// 3. 可重试错误：指数退避自动恢复
async function withRetry(fn, times = 3) {
  for (let i = 0; i < times; i++) {
    try { return await fn(); }
    catch (err) {
      if (!err.retryable || i === times - 1) throw err;
      await new Promise((r) => setTimeout(r, 2 ** i * 500 + Math.random() * 300)); // 抖动防惊群
    }
  }
}
```
