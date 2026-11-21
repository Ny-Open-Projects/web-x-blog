---
title: [BLD-162] CI 缓存安全：缓存投毒风险与隔离设计。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-162：CI 缓存安全：缓存投毒风险与隔离设计。
**答**：
- 攻击面：缓存 key 可被低权限 PR 构造（与目标 run 相同 key），**写入的恶意内容被高权限 workflow 读取**（如被替换的构建产物、node_modules 里的 postinstall 脚本）——GitHub 官方文档明确 cache 是不可信输入。
- 防线一（隔离）：按 `github.ref` 隔离写入面（PR 缓存仅供该 PR），高权限 job（部署/发布）**只读受保护分支产出的缓存**或不读缓存。
- 防线二（校验）：拉取的 node_modules 构建前跑 `pnpm install --frozen-lockfile`（会校验 store 完整性）、产物校验 hash 签名（turborepo signature）、lockfile diff 卡口。
- 通用原则：缓存 = 性能优化层，绝不能影响正确性——"缓存命中等价于真实执行"必须由内容哈希保证（turborepo/webpack 的设计都遵循）。

```yaml
# 危险示例与加固对照（同一文件内演示）
jobs:
  pr-build:                       # 低权限：PR 预览构建
    steps:
      - uses: actions/cache@v4
        with:
          # 加固点 1：key 带上 ref 隔离，PR 的缓存不会污染其他上下文
          key: deps-${{ github.ref_name }}-${{ hashFiles('pnpm-lock.yaml') }}
          path: node_modules
      - run: pnpm install --frozen-lockfile   # 加固点 2：无网安装校验一致性
  release:                        # 高权限：发布（只有 main + tag 触发）
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      # 加固点 3：发布链路不使用任何缓存（或只读 main 前缀缓存）
      - run: pnpm install --frozen-lockfile --ignore-scripts
      - run: pnpm build && pnpm changeset publish
        env: { NPM_TOKEN: '${{ secrets.NPM_TOKEN }}' }
# 结论：缓存永远不进"信任链"，只允许加速"可重建"的输入
```
