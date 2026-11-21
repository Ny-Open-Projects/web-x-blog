---
title: [BLD-098] 如何给团队制定构建规范？脚手架内置 vs 各自配置的取舍？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-098：如何给团队制定构建规范？脚手架内置 vs 各自配置的取舍？
**答**：
- 规范的内容分层：统一基线（cache、分包原则、sourcemap 策略、体积预算、CI 卡口）+ 允许差异层（业务专属 loader、自定义 chunk 命名）+ 禁止项（私自关闭 hash、提交 .map 产物）。
- 落地方式对比：脚手架内置（创建即合规，升级靠发版，一致性强）vs 各自配置（灵活但漂移快）；主流是"preset 包 + 最小本地配置"（ CRA/umi/rsbuild 模式），重大配置改动走 RFC 评审。
- 治理机制：定期升级窗口（锁定版本主线）、配置审计脚本（检查禁用项）、构建性能与体积看板。
- 演进策略：规范先在 1~2 个试点项目验证 → 抽成 preset → 全量推行，避免一刀切回归事故。

```javascript
// scripts/audit-config.js：配置审计脚本（禁用项检查）
const fs = require('fs');

const rules = [
  { name: '禁止关闭 contenthash', test: (c) => !/contenthash/.test(JSON.stringify(c.output || {})), level: 'error' },
  { name: '必须开启持久缓存', test: (c) => (c.cache || {}).type !== 'filesystem', level: 'error' },
  { name: '禁止开启 eval devtool 生产', test: (c) => /eval/.test(c.devtool || ''), level: 'error' },
  { name: 'babel-loader 必须 include', test: (c) => !(c.module?.rules || [])
      .some((r) => String(r.loader || '').includes('babel') && r.include), level: 'error' },
];

const config = require(process.argv[2] || './webpack.config.js');
let failed = 0;
for (const r of rules) {
  if (r.test(config)) { console.error(`[FAIL] ${r.name}`); failed++; }
}
process.exit(failed ? 1 : 0);
// CI 里：node scripts/audit-config.js webpack.config.js
```
