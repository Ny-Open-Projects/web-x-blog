---
title: [NODE-039] 如何用 mysql2/promise 封装一个生产级连接池？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-039：如何用 mysql2/promise 封装一个生产级连接池？
**答**：
- 连接池解决 TCP 建连 + 认证的重复开销与并发上限：`createPool` 按需复用连接。关键参数：`connectionLimit`（单实例上限，按 `maxPoolSize` 全局预算分配）、`queueLimit`（排队上限防内存膨胀）、`connectTimeout`、`enableKeepAlive`。
- 生产要点：查询参数**必须用占位符 `?`**（防 SQL 注入）；捕获 `PROTOCOL_CONNECTION_LOST`/`ETIMEDOUT` 自动重试；慢查询埋点（执行耗时打日志/上报）；读多写少可用主从 + `connection.config` 区分。
- 高频追问：连接数公式 `connectionLimit ≈ DB max_connections / 服务实例数`，不能拍脑袋写 100。

```javascript
const mysql = require('mysql2/promise');

const pool = mysql.createPool({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,   // 凭证走环境变量
  database: 'shop',
  connectionLimit: 20,                 // ≈ DB max_connections / 实例数
  queueLimit: 100,                     // 排队超过直接报错，不无限堆积
  connectTimeout: 5000,
  enableKeepAlive: true,
  waitForConnections: true,
  namedPlaceholders: true,             // 支持 :name 占位符
});

// 统一封装：慢查询日志 + 错误归一
async function query(sql, params) {
  const start = Date.now();
  try {
    const [rows] = await pool.execute(sql, params); // execute 走预处理，防注入
    const cost = Date.now() - start;
    if (cost > 200) console.warn(JSON.stringify({ level: 'warn', event: 'slow_query', sql, cost, params }));
    return rows;
  } catch (err) {
    if (['PROTOCOL_CONNECTION_LOST', 'ECONNRESET'].includes(err.code)) {
      console.error('DB 连接中断，池会自动重连:', err.code);
    }
    throw err;
  }
}

// 使用：占位符 + 命名参数
const users = await query('SELECT id, name FROM users WHERE status = :status LIMIT 10', { status: 'active' });
```
