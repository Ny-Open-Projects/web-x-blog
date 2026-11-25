---
title: [RBL-118] bun build --compile 发布独立二进制的机制与适用场景？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-118：bun build --compile 发布独立二进制的机制与适用场景？
**答**：
- 机制：把 JS/TS 产物嵌进 Bun 运行时二进制（tail 资源附加），目标机无需安装 Bun/Node；跨平台交叉编译（--target=bun-linux-x64 等）。
- 产物：单个可执行文件，启动即原生速度；支持内嵌资源文件（assets）。
- 适用：CLI 工具分发（用户免装环境）、内部运维工具、边缘 agent；不适用大 Web 应用（产物体积与更新成本）。
- 体积与更新：二进制含整个运行时（约数十 MB 起），版本升级要全量重发；对比 Docker 镜像分发与 npm 分发的取舍。
- 注意：native addon 是否被正确打入、平台特有依赖（sharp 等）交叉编译受限。
- 追问钩子：与 deno compile、Node SEA（single executable application）同类能力对比——趋势是运行时原生化交付。

```bash
bun build --compile ./cli.ts \
  --target=bun-linux-x64 \
  --outfile dist/mytool-linux
# CI 矩阵：linux/mac/windows 各出一个二进制
# 用户侧：curl -fsSL https://cdn.example.com/mytool-linux -o mytool && chmod +x mytool
```
