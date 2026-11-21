---
title: [RBL-006] Rspack 持久化缓存如何配置与失效？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-006：Rspack 持久化缓存如何配置与失效？
**答**：
- 配置入口：`experiments.cache: true`（或 `cache: true`），缓存写到 node_modules/.cache/rspack；开发与生产都可开，生产首次构建写缓存，后续 CI/本地增量读缓存。
- 失效机制：缓存 key 由配置摘要（resolve/module/插件等影响产物的配置）+ 依赖版本 + 文件内容 hash 共同决定；配置变更或依赖升级自动失效，不需要手动清理。
- 层级：内存缓存兜住 dev watch 的热更新；文件系统缓存兜住"重启进程/换 CI 机器"的冷启动。
- CI 实战：把缓存目录配置成 CI 的缓存 artifact（如 GitHub Actions 的 actions/cache），命中后构建时间可降一个数量级。
- 注意点：JS loader/plugin 内部产生的副作用不在缓存契约内（如 plugin 在 done 钩子写的文件），需要自己保证幂等；变更与产物无关的配置字段尽量不影响缓存 key。
- 追问钩子：对比 webpack 的 filesystem cache——Rspack 缓存以 Rust 数据结构快照存储，恢复时不需要重建 JS 层模块对象，回放更快。

```yaml
# .github/workflows/build.yml：CI 缓存命中 Rspack 持久缓存
- uses: actions/cache@v4
  with:
    path: node_modules/.cache/rspack
    key: rspack-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}-${{ github.sha }}
    restore-keys: |
      rspack-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}-
      rspack-${{ runner.os }}-

# rspack.config.js
module.exports = { experiments: { cache: true } };
```
