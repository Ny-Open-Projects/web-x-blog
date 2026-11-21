---
title: [RBL-067] Rolldown 处于什么阶段？生产采用策略是什么？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-067：Rolldown 处于什么阶段？生产采用策略是什么？
**答**：
- 阶段：rolldown 独立发布 npm 包可独立用于库打包；Vite 集成路线为 rolldown-vite（实验性替换内核的 vite 包）→ 逐步默认化；核心 API 已稳定但实验特性仍带 experimental 前缀。
- 生产采用策略：新库项目可试 rolldown（产物质量对齐 rollup）；业务应用建议跟随 rolldown-vite 的官方节奏，不要手工魔改内核；已有 rollup 单独项目可在 CI 加"影子构建"（同配置双跑 diff 产物）灰度验证。
- 风险控制：锁定版本、产物 diff 门禁、保留旧构建命令回滚。
- 版本敏感点：experimental.* 命名空间（原生插件、full bundle mode）API 可能变动，不进生产主链路。
- 团队落地路径：先在非关键项目试点 → 收集插件兼容问题清单 → 再全量推广。
- 追问钩子：判断成熟度的方法——看官方 milestones 与 vite 仓库的 rolldown 相关 issue 关闭速度，而不是宣传文案。

```javascript
// 影子构建 CI 灰度方案
// build.sh
// npm run build:rollup && npm run build:rolldown
// diff-dist.js：产物清单与 hash 对比，不一致仅告警不阻塞
const { execSync } = require('child_process');
const report = execSync('node scripts/diff-dist.js dist-rollup dist-rolldown').toString();
if (/diff/.test(report)) console.warn('[shadow] rolldown 产物与 rollup 有差异：\n', report);
```
