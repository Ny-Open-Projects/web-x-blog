---
title: [BLD-273] JSON/配置文件的转换处理怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-273：JSON/配置转换怎么做？
**答**：
- JSON 的构建处理：import JSON（tree-shake 友好——named import 摇除）、JSON 转 JS 模块（命名导出——rollup json 插件）、大 JSON 拆分（按需 chunk）。
- 配置文件处理：yaml/toml → JSON/JS（统一中间表示）、schema 校验进构建（SCN-BLD-248）、配置内嵌 vs 外置的边界（SCN-BLD-226 变更频率准则）。
- i18n 资源：按语言拆 chunk（SCN-BLD-226 按需加载）+ key 重命名（缩短产物体积——混淆 key 省体积）。
- 追问钩子：为什么「大 JSON 转 JS 模块」能获得 tree-shaking——JSON import 默认打包整个对象（无法摇除）；转换为 JS 命名导出（export const a = ...）后，named import 未使用的键可被摇除——转换成「可静态分析的结构」是所有资源获得摇树能力的前提。

```javascript
// json 插件
{ test: /\.json$/, use: [{ loader: 'json-to-esm',
  options: { named: true } }] }                        // named exports → 可摇
// i18n 按语言拆分
import(`./locales/${lang}.json`)                       // 语言 chunk（SCN-BLD-215 显式映射）
```
