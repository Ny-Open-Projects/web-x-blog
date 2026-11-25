---
title: [RBL-247] 基准测试的 fixture 仓库怎么设计
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-247：基准测试的 fixture 仓库怎么设计

**答**:
- 形态梯度：小（<100 模块，测启动开销占比）、中（1-5k 模块，典型业务）、大（10k+ 模块，测并行扩展性）——单一规模结论会误导
- 真实性要素：真实框架（React+TS+CSS）、真实依赖树（node_modules 全量）、真实动态 import 与 worker 引用——合成 fixture 的并行性/IO 模式失真
- 增量测试脚本：预定义变更序列（改 1 文件/改 10 文件/切分支），自动化回放
- 数据集版本化：fixture 打 tag，跨期对比用同版本（否则「改进」可能只是 fixture 变了）

```text
fixture 矩阵：
small-100 / mid-3k / large-12k × { cold, warm, watch-edit1, watch-edit10 }
每个格：中位数 + IQR，同 fixture tag
```
