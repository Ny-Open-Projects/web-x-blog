---
title: [RBL-663] webpack→Rspack 迁移决策框架：哪些项目适合迁移、哪些不值得
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-663：webpack→Rspack 迁移决策框架：哪些项目适合迁移、哪些不值得

**答**:
- 迁移收益模型：构建时间收益 =（旧构建时间 − 新构建时间）× 触发频率（dev 编辑次数/CI 次数）− 迁移成本 − 维护差异成本。大仓库（webpack 构建 >2min）收益显著；小仓库（<30s）迁移纯增加风险。
- 适配性检查单（迁移前评估）：1) webpack 特有插件依赖（heavy loader 自研/plugin 生态）——Rspack 兼容大部分 loader 但 plugin API 是重写层，自研 webpack 插件要移植；2) 魔法配置依赖（module parser 特殊化/hack 过的 resolve）；3) 微前端打包策略（externals 语义差异）；4) 构建期自定义 runtime（webpack runtime 定制）。
- 不迁移清单：依赖 webpack 内部 API 的深度定制（如 chunk graph 手术）、依赖冷门 loader 无 Rust 等价物、构建时间本来就不是痛点——「迁移是为了快」这个目标不成立时全部成本都白付。
- 迁移路径分级：1) **平替优先**（配置直接翻译：entry/output/alias/loader 一一对应）；2) **插件替换**（webpack 插件 → rspack 内置或社区等价物，列出映射表）；3) **逐仓灰度**（内部仓库按收益排序分批迁，首批选「最标准」仓库建立模板）。
- 迁移验收：产物语义 diff（RBL-649 思路）+ 行为测试 + 构建时间前后对比（同机同任务）——「跑起来没报错」不是验收标准。
- 追问钩子：为什么「首批选最标准仓库」？——迁移过程本身要沉淀「通用翻译规则」，标准仓库验证规则库，之后复杂仓库的迁移成本可预估；反过来先用最难的仓库会消耗团队信心且规则库不成熟。

```javascript
// 迁移评估评分卡
function migrationScore(repo) {
  const factors = {
    buildMinutes: repo.buildSeconds / 60,                // 收益主体
    customPlugins: repo.plugins.filter(isWebpackOnly).length,  // 成本项
    customLoaders: repo.loaders.filter(isCustom).length,
    configHack: countConfigHacks(repo.config),           // parser/resolve hack
    teamFamiliarity: 0.8,                                // 团队对 rspack 熟悉度
  };
  const benefit = factors.buildMinutes * 10;             // 每 10 分钟构建折 10 分收益
  const cost = factors.customPlugins * 3 + factors.customLoaders * 2 + factors.configHack * 4;
  return { benefit, cost, net: benefit - cost,
    verdict: benefit - cost > 5 ? 'migrate-first'
           : benefit - cost > 0 ? 'migrate-later' : 'stay' };
}
// 迁移映射表（部分）
const PLUGIN_MAP = {
  'webpack.DefinePlugin': 'rspack.builtin.DefinePlugin',
  'HtmlWebpackPlugin': 'rspack.HtmlRspackPlugin',
  'MiniCssExtractPlugin': 'rspack.CssExtractRspackPlugin',
  'custom-babel-loader': 'builtin:swc-loader',
};
```
