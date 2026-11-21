---
title: [RBL-028] Rspack 内置压缩器如何工作？如何定制压缩？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-028：Rspack 内置压缩器如何工作？如何定制压缩？
**答**：
- 默认实现：production 模式下 JS 用内置 swc（基于 Rust 的 SWC 压缩器）压缩，CSS 用内置 lightningcss 或 swc CSS 压缩，全在 Rayon 并行执行，替代 Terser（JS）与 cssnano（CSS）。
- 压缩开关：optimization.minimize 控制；定向定制走 optimization.minimizer 数组，可继续用 JsMinimizerRspackPlugin 包 TerserPlugin（但回到 JS 慢路径）。
- 选项透传：通过 `tools.swc`（Rsbuild）或 Rspack 的 optimization.minimizer 配置 swc 压缩选项（compress/drop_console/mangle 阈值）。
- 与 Terser 的差异点：个别压缩启发式（死代码判定、注释保留）不同，迁移后需 diff 产物；保留版权注释用 swc 的注释策略或 optimization 相关配置。
- 体积收益参考：Rspack + swc 压缩产物通常与 Terser 同量级（±5%），构建时间低一个数量级。
- 追问钩子：压缩并行化是"每个 chunk 独立任务"，chunk 越细并行度越高但产物碎片越多——分割策略影响压缩速度。

```javascript
// rspack.config.js：自定义压缩行为（去 console）
module.exports = {
  mode: 'production',
  optimization: {
    minimize: true,
    minimizer: [
      new (require('@rspack/core').SwcJsMinimizerRspackPlugin)({
        compress: { drop_console: true, passes: 1 },
        mangle: true,
        format: { comments: false },
      }),
    ],
  },
};
```
