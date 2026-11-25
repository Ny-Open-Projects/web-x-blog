---
title: [NODE-637] Node 集群（cluster/PM2）怎么横向扩展？状态怎么管？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-637：集群扩展怎么做？
**答**：
- cluster 模型：master fork N 个 worker（按 CPU 核），master 分发连接（默认 round-robin on POSIX）——worker 各自独立事件循环；PM2 是 cluster 的运维增强（0 秒重载/日志/守护）。
- 状态管理：worker 内存状态不共享（每 worker 独立 heap）——session 缓存/限流计数必须外置（Redis）或 sticky session（会话粘住同 worker，SCN-OPS-244 sticky 同源）。
- 平滑重启：PM2 reload（逐 worker 下线——先 stop accepting 再退出，零停机）；优雅退出先行（SCN-NODE-优雅关闭——排空在途请求）。
- 共享端口：master 统一 listen 后分发 handle（SO_REUSEPORT 是另一方案——内核级负载均衡）。
- 追问钩子：为什么「worker 内存限流计数」在 cluster 下必然失真——限流计数器在每个 worker 各自一份，N 个 worker 各记 1/4 的请求数，总限流阈值被放大 N 倍；解法是计数外置 Redis（原子 INCR）或 master 层聚合——「任何依赖进程内共享状态的机制」在多 worker 下都要重新设计，这是 cluster 迁移的第一审计项。

```javascript
// cluster + 外置状态
if (cluster.isPrimary) {
  for (let i = 0; i < os.cpus().length; i++) cluster.fork();
  cluster.on('exit', (w) => cluster.fork());           // 崩溃自动拉起
} else {
  app.listen(3000);                                    // worker 监听（master 分发）
}
// 限流必须外置
const rate = await redis.incr(`rl:${ip}`);             // Redis 原子计数
```
