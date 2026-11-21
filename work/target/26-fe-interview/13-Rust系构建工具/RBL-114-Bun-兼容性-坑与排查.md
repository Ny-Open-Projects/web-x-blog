---
title: [RBL-114] Bun 从 Node 迁移的兼容性坑有哪些？如何排查？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-114：Bun 从 Node 迁移的兼容性坑有哪些？如何排查？
**答**：
- native addon 类：依赖 N-API 之外的 C++ 扩展（老版本 node-sass、某些数据库驱动）可能崩——先跑依赖扫描，看有没有已知不兼容的包。
- 行为细节类：process.nextTick 语义、worker_threads 边界、stream backpressure 细节差异；长驻服务要压测验证。
- 生态工具类：依赖 Node 特有运行时行为（如 --inspect 协议、V8 flags）的工具链不可用。
- 排查方法：分层灰度（脚本→测试→dev server→生产）、bun 兼容性 issue 搜索、写冒烟测试覆盖关键路径（启动、DB 连接、关键接口）。
- 回退设计：命令双轨（bun run / npm run），运行时切换用环境变量管理，随时回退。
- 追问钩子：兼容性排查的本质是"隐式契约审计"——Node 特有行为被业务隐性依赖的地方最容易炸。

```bash
# 兼容排查清单脚本
grep -rl "node-sass\|native ." package.json    # native 依赖
bun test                                        # 冒烟
bun run build && diff dist dist.node/           # 产物对比
# 双轨脚本
# "start": "node dist/server.js",
# "start:bun": "bun dist/server.js"
```
