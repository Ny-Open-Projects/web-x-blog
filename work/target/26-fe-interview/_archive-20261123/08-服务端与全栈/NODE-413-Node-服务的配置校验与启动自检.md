---
title: [NODE-413] Node 服务的启动自检（配置/依赖/schema 版本）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-413：启动自检设计
**答**:
- fail fast 原则：配置缺失/非法（NODE-362 schema 校验）、依赖不可达（DB/Redis 连通测试）、DB schema 版本不匹配（迁移未跑——代码版本 vs migration 版本比对）——任何一项不过拒绝启动，宁可不起也不要带病上线。
- 自检清单：环境变量 schema 解析、依赖连接 ping、迁移版本检查（migration 表最新版本 = 代码期望版本）、关键文件/目录可写（临时目录/日志目录）、时钟偏移（NTP 偏差 > 5s 告警——token 校验受影响）。
- 预热流程：自检通过 → 缓存预热（热数据回填，NODE-353）→ 连接池预热 → readiness true 接流（NODE-389）；预热期间探针延迟 ready。
- 自检结果可见：启动日志结构化输出自检清单（每项耗时/结果），启动慢可归因到项。
- 防呆：自检通过不代表永远健康——运行期依赖监控独立（NODE-404），自检只保出生质量。
```javascript
async function startup() {
  const checks = [ ['config', () => configReady()], ['db', () => ping(db)],
    ['migration', () => checkMigrVersion()], ['clock', () => ntpOffset() < 5000] ];
  const results = [];
  for (const [name, fn] of checks) {
    const t = Date.now();
    results.push({ name, ok: await fn().then(() => true, () => false), ms: Date.now() - t });
  }
  if (results.some(r => !r.ok)) { log.error({ results }); process.exit(1); } // fail fast
  await warmup(); ready = true;                                   // 预热后接流
}
```
