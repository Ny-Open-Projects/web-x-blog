---
title: [RBL-011] webpack 迁移 Rspack 的配置迁移策略是什么？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-011：webpack 迁移 Rspack 的配置迁移策略是什么？
**答**：
- 第一步盘点：列出现有配置里用到的 loader、plugin、自定义钩子，对照 Rspack 兼容清单分成三类——可直接平移 / 换 rspack 替代品 / 需要改造或放弃。
- 第二步配置平移：rspack.config.js 直接复制 webpack.config.js 的高兼容字段（entry/resolve/module.rules 主体/optimization.splitChunks），先让冷启动跑通。
- 第三步收敛 JS 层：babel-loader→builtin:swc-loader，css-loader+MiniCssExtract→内置 css 类型，Terser/Copy/Define/Html→内置或 rspack 官方版。
- 第四步灰度验证：产物 diff（文件清单+hash 对比+体积对比）、跑 E2E、看 sourcemap 与 publicPath 边界，再切 CI 流量。
- 兜底技巧：迁移期保留 webpack 构建命令并行可用，一个环境变量切换，出问题秒回滚。
- 追问钩子：官方提供 webpack 自动迁移工具（把可自动转换的字段生成 rspack.config.js + 报告不兼容项）。

```javascript
// 迁移期双轨构建脚本（package.json）
// "build:wp": "webpack --config webpack.config.js",
// "build:rs": "rspack build -c rspack.config.js",
// 验证脚本：对比两份产物
const fs = require('fs');
const wp = require('./dist-wp/manifest.json');
const rs = require('./dist-rs/manifest.json');
for (const [k, v] of Object.entries(wp)) {
  const rv = rs[k];
  if (!rv) console.log('缺失:', k);
  else console.log(k, 'wp=', wp[k].size, 'rs=', rv.size);
}
```
