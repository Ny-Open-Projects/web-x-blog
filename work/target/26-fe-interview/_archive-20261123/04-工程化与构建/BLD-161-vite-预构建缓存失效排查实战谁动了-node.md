---
title: [BLD-161] vite 预构建缓存失效排查实战：谁动了 node_modules/.vite？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-161：vite 预构建缓存失效排查实战：谁动了 node_modules/.vite？
**答**：
- 预构建缓存 key 是 **lockfile 内容 + optimizeDeps 相关配置的哈希**（`getDepHash`）：lockfile 任何字节变化、`optimizeDeps.include/exclude/esbuildOptions`、`resolve.alias`、`define`、`plugins` 数量? 部分配置都会使哈希变化 → 目录重建。
- 排查流程：`--debug optimizeDeps` 看 "hash changed" 日志 → 二分回退配置（git stash 配置变更）→ 常见元凶：动态插件根据 env 返回不同配置、CI 里 `npm install` 修改了 lockfile、时区/locale 影响扫描顺序。
- 症状清单：启动慢（每次都重建）、首屏出现两次 full-reload（新依赖被运行时发现）、`deps` 目录时间戳总是当前时间。
- 缓解：CI 用 `vite optimize` 预热 + 缓存 `node_modules/.vite`；本地 `server.warmup.clientFiles` 预热源码转换。

```bash
# vite 预构建缓存失效的排查序列
npx vite --debug optimizeDeps 2>&1 | grep -E 'hash|scan|optimized' | head -20
# 日志解读：
#   [vite] optimized dependencies changed. reloading   ← 运行时发现新依赖（include 缺失）
#   hash changed: xxxx -> yyyy                          ← 缓存判定失效，即将重建

# 1. 确认 lockfile 是否被改：
git diff --stat pnpm-lock.yaml
# 2. 确认配置指纹是否漂移（常见：插件按 env 生成不同 options）
vite --mode production optimize 2>&1 | grep 'hash:'   # 打印两次 mode 的 hash 对比
# 3. CI 预热 + 缓存目录：
npx vite optimize    # 单独跑预构建，产物进 node_modules/.vite/deps
```

```yaml
# CI 中缓存 vite 预构建产物（key 与失效逻辑对齐）
- uses: actions/cache@v4
  with:
    path: node_modules/.vite
    key: vite-deps-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}-${{ hashFiles('vite.config.*') }}
# 配合：pnpm exec vite optimize 在 build 前跑，把"扫描+打包依赖"提前到缓存恢复之后
```
