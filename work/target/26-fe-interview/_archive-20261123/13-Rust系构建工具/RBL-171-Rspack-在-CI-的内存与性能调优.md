---
title: [RBL-171] Rspack 在 CI 上的资源调优：内存、并发与 runner 选择
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-171：Rspack 在 CI 上的资源调优：内存、并发与 runner 选择

**答**：
- 内存：Rspack 是 Rust 进程，内存占用比 webpack 低但仍随模块数增长；超大仓库 OOM 时排除 node_modules 体积干扰（tree 注入变量减少），并给容器加 memory limit 防止 CI 机器被拖垮。
- 并发调优：Rspack 内部线程池默认用全部核，CI 容器限核（cgroup）时要显式 parallelism 匹配实际配额，否则线程切换反而变慢；同时只跑一个 build job 的机器上 concurrency 不用调小。
- runner 选择：构建型 job 选 4C+（build 时间对核数敏感），lint/test 等轻 job 用 2C 省成本；arm64 runner 通常性价比更高且 Rspack 有官方 arm64 binding。
- 缓存配合：CI 上 Rspack 持久化缓存（cache.buildCache）目录进 CI 缓存，命中后二次构建接近秒级；注意缓存 key 含工具版本。
- 追问钩子：Node 侧还有一层——Rspack 的 JS API 调用与 node 进程内存（grid 环境变量 NODE_OPTIONS=--max-old-space-size）是两回事，OOM 先分清是 Rust 进程还是 Node。

```yaml
# CI 作业资源配置示例
build:
  runs-on: ubuntu-latest-4core   # 构建专用规格
  env:
    NODE_OPTIONS: --max-old-space-size=4096
  steps:
    - uses: actions/cache@v4
      with:
        path: node_modules/.cache/rspack
        key: rspack-${{ hashFiles('pnpm-lock.yaml') }}-rspack-${{ env.RSPACK_VERSION }}
    - run: pnpm --filter @app/web build
```
- 排查内存问题：RSPACK_PROFILE=ALL 出 profile，用 speedscope 分析 alloc 热点；生产实践里多数"Rspack 内存高"最后都定位到个别巨型 loader 插件。
