---
title: [NODE-185] Serverless 中的 Node 如何实践（冷启动/成本/场景）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-185：Serverless 中的 Node 如何实践（冷启动/成本/场景）？
**答**：
- 冷启动三招：依赖精简（tree-shake + 按需 require）、**初始化放 handler 外**（容器实例复用）、连接池配额按"实例并发 × 池"计算（务必小）。
- 成本模型：费用 = 请求数 + GB·s；**内存调大反而可能更省**（CPU 同比例提升执行更快），要实测找最优配比。
- 适用：低频异步任务、webhook 接收、定时任务、图片处理；不适用：长连接 WS、固定高 QPS（成本劣化）、大内存状态任务。
- 冷启动消除：预留实例（成本换延迟）+ min instances；关键路径服务不建议纯 Serverless。

```javascript
let cachedDb;                                    // 实例级复用，跨请求存活
async function getDb() {
  cachedDb ??= await createPool({                // 初始化放 handler 外
    ...cfg,
    connectionLimit: 2,                          // 实例并发 × 池 = DB 连接，务必小
  });
  return cachedDb;
}

export const handler = async (event) => {
  const db = await getDb();
  const rows = await db.query('SELECT id, title FROM articles WHERE status = ? LIMIT 20', [1]);
  return { statusCode: 200, body: JSON.stringify(rows) };
};
// 成本实测法：改内存配比跑 1000 次请求，比较 费用/请求 与 P99 延迟，找拐点
```
