---
title: [BLD-186] 构建工具从 webpack5 迁到 Rspack 的完整评估报告（含决策矩阵）。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-186：构建工具从 webpack5 迁到 Rspack 的完整评估报告（含决策矩阵）。
**答**：
- **评估维度**（决策矩阵）：构建性能（冷/热/增量）、配置兼容度（本仓插件/loader 盘点）、生态功能（MF/CSS/HMR/sourcemap/宏任务）、团队迁移成本（学习+配置改造+CI 改造）、风险与回滚、长期维护（社区活跃度/版本节奏）。
- 本仓实测数据（示例结论）：冷构建 96s→21s、watch 增量 6.2s→0.9s、HMR 3.1s→0.4s；插件兼容 38 个中 31 直接可用、5 个有等价物、2 个需自研迁移（自定义 TS 转译 plugin）。
- 决策矩阵打分（1-5）：性能 5/5、兼容 4/5、生态 3.5/5、迁移成本 3/5、风险 4/5、加权总分 4.1 —— **建议迁移**，分三阶段（工具站→内部应用→核心交易）。
- 报告结构模板：背景与痛点 → 实测方法论（同机同源码同口径）→ 矩阵打分 → 风险清单与缓解 → 排期与回滚方案。

```text
# 迁移决策矩阵（评估报告核心页，可直接复用）
| 维度(权重)      | webpack5 | Rspack | 说明                      |
|-----------------|----------|--------|---------------------------|
| 冷构建(25%)     | 96s      | 21s    | 同机同源码 3 次中位数     |
| 增量构建(20%)   | 6.2s     | 0.9s   | 修改 1 个业务文件 rebuild |
| 配置兼容(20%)   | -        | 4.1/5  | 38 插件盘点：31/5/2       |
| 生态功能(15%)   | 5/5      | 3.5/5  | MF 可用；css module 新语义|
| 迁移成本(10%)   | -        | 3/5    | 2 人周，CI 双轨期 2 周    |
| 长期维护(10%)   | 4/5      | 4/5    | webpack 稳定；rspack 高频 |
| 加权总分        | 3.6      | 4.1    | 迁移                      |
| 风险清单        |          |        | ①自定义 plugin 迁移 ②产物 diff 校验 ③HMR 时序回归 |
| 回滚方案        |          |        | BUILD_ENGINE=webpack env 开关，CI 双配置并存 |
```

```javascript
// 双引擎并行的构建入口（灰度期使用）：build.js
const engine = process.env.BUILD_ENGINE ?? 'rspack';
const config =
  engine === 'rspack' ? require('./rspack.config.js')
                      : require('./webpack.config.js');
require(engine === 'rspack' ? '@rspack/core' : 'webpack')(config, (err, stats) => {
  console.log(stats.toString({ colors: true, modules: false, assets: true }));
  process.exit(stats?.hasErrors?.() ? 1 : 0);
});
// CI 双轨 job：两个引擎各跑一次 + 产物 diff（BLD-177 脚本）→ 灰度通过后下线 webpack
```
