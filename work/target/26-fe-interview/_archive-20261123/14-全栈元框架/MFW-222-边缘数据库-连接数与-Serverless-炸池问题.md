---
title: [MFW-222] Serverless 直连数据库的连接池爆炸问题
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-222：Serverless 连接池爆炸

**答**:
- 问题本质：每个 serverless 实例（Lambda/Worker）持独立连接池，千级并发实例 = 万级连接打爆数据库 max_connections（传统池化按进程假设失效）
- 解法谱系：①HTTP 驱动数据库（D1/Planetuler serverless driver——无长连接，一查询一 HTTP）②连接代理层（PgBouncer/RDS Proxy/Hyperdrive——代理收敛池）③实例内池上限 = 1（global 单例防实例内泄漏）
- 判定：已有 Postgres 且不能换 → 代理层（Hyperdrive 类）；可换存储 → HTTP 原生数据库
- 附带坑：serverless 冷启动 + 连接建立成本（TLS 握手 50ms+）——HTTP 驱动顺带解决

```javascript
// Node 侧硬防线：全局单例池（防热路径重复建池）
globalThis.__pg ??= new Pool({ max: 1, ...cfg })   // max=1：实例级最多 1 连接
export const GET = () => globalThis.__pg.query(...)  // 千实例 → 千连接（仍需代理层/HTTP 驱动根治）
```
