---
title: [RBL-153] CI 构建为什么慢？瓶颈定位的方法论
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-153：CI 构建为什么慢？瓶颈定位的方法论

**答**：
- 先拆阶段：CI 总耗时 ≈ 环境准备（拉镜像/装依赖）+ 构建（编译/打包）+ 测试 + 上传产物 + 排队。构建工具再快，也可能 70% 时间耗在 npm install 或排队上。
- 量化工具：每阶段打点计时（CI 日志 timestamp / 自定义计时脚本）；npm install 用 --timing、构建用 Rsdoctor/timings 输出，拿到数据再谈优化。
- 常见真凶：1) 无缓存每次全量 install；2) 单 job 串行跑 lint+build+test；3) Docker 镜像 COPY 整个 repo 破坏层缓存；4) 测试未分片；5) 构建缓存 key 设计不当导致永远 miss。
- 优化顺序原则：先砍最大头（收益/成本比），而不是先上炫技方案——先缓存与并行，再考虑换 Rspack/Turbopack 这类内核升级。
- 追问钩子：换 Rspack 前先测 install 和测试耗时——如果构建只占 20%，换编译器收益有限，面试时能算这笔账很加分。

```bash
# 在 CI 各阶段打点（GitHub Actions 示例思路）
- name: install
  run: |
    echo "::debug::start $(date +%s%3N)"
    npm ci --timing
    echo "::debug::end $(date +%s%3N)"
- name: build
  run: node scripts/timed.js npm run build   # 包装器记录 start/end

# scripts/timed.js：包装任意命令输出耗时
const { spawnSync } = require('node:child_process');
const [, , cmd, ...args] = process.argv;
const t0 = performance.now();
const r = spawnSync(cmd, args, { stdio: 'inherit', shell: true });
console.log(`[${cmd}] ${(performance.now() - t0) / 1000}s`);
process.exit(r.status);
```
