---
title: [NODE-246] PM2 模块与扩展生态？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-246：PM2 模块与扩展生态？
**答**:
- 模块机制：pm2 install <module>（运行在 pm2 daemon 内的常驻进程）——pm2-logrotate（日志切割）/ pm2-server-monit / pm2-prometheus。
- 自研模块：pm2 install <path> 可装内部工具（如采集各 worker 指标聚合上报）——daemon 侧能力扩展。
- CLI 编程接口：pm2 命令有 programmatic API（pm2.connect/list/reload）——自研发布平台直接调用（NODE-241 脚本化）。
- 取舍：重运维场景上 pm2.io 或换 K8s Operator；轻量单机 PM2 模块够用。

```javascript
// PM2 编程接口（发布平台调用）
const pm2 = require('pm2');
pm2.connect(async (err) => {
  await pm2.promise.reload('api');                    // 编程化 reload
  const list = await pm2.promise.list();
  const bad = list.filter(p => p.pm2_env.restart_time > 10);
  if (bad.length) await pm2.promise.rollback?.() ?? report(bad);
  pm2.disconnect();
});
```
