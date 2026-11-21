---
title: [RBL-116] Bun 的配置体系（bunfig.toml / tsconfig / package.json）？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-116：Bun 的配置体系（bunfig.toml / tsconfig / package.json）？
**答**：
- bunfig.toml：Bun 自己的配置文件，管 install（registry/缓存）、test（覆盖率/预载）、serve 等运行行为；npm 的 .npmrc 语义映射进来。
- tsconfig.json：路径映射（paths）、target/jsx 由 bun 运行时与打包器尊重，无需编译步骤。
- package.json：scripts/dependencies/workspaces 与 npm 同语义，bun 直接消费。
- 三层关系：bunfig 管工具行为、tsconfig 管模块解析与编译目标、package.json 管依赖与脚本——职责清晰不重叠。
- 环境变量：.env 文件自动加载（.env.development 等按 NODE_ENV 选择），Bun.env / process.env 双访问。
- 追问钩子：bun 的 .env 自动加载与 Node 需要 dotenv 显式加载不同，迁移时注意"静默注入"可能改变脚本行为。

```toml
# bunfig.toml
[install]
registry = "https://registry.npmmirror.com"
exact = true

[test]
coverage = true
preload = ["./test-setup.ts"]

[serve.port]
default = 3000
```
```json
// tsconfig.json（bun 尊重 paths）
{ "compilerOptions": { "paths": { "@/*": ["./src/*"] }, "jsx": "react-jsx" } }
```
