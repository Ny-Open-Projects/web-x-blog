---
title: [BLD-259] 动态导入分析（context module）怎么运作？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-259：context module 怎么运作？
**答**：
- context module 语义：`import(\`./locales/${lang}\`)` 时打包器生成「目录上下文模块」——把目录下所有匹配文件（按 glob 规则）打成 map（key → chunk），运行时按变量取。
- 体积影响：目录全量打包（SCN-BLD-215 黑洞）——控制手段：更精确的表达式（前缀/后缀缩小 glob 范围）、显式映射替代、ignore 注释排除。
- vite 的 glob import：`import.meta.glob('./locales/*.json')` 显式声明 glob（比隐式 context 可控）——eager/lazy 模式选择。
- 追问钩子：为什么 vite 的 import.meta.glob 是对 context module 的改进——隐式 context（模板字符串 import）的「打包范围」是打包器推断的（黑盒，容易意外打包整个目录）；glob 显式声明模式与转换方式（eager 内联/lazy chunk）——从「打包器猜」变成「开发者说」，可预测性是工具 API 设计的进步。

```javascript
// vite glob：显式声明
const locales = import.meta.glob('./locales/*.json');            // lazy chunk
const eager = import.meta.glob('./locales/*.json', { eager: true });   // 内联进当前 chunk
// 隐式 context 的范围控制
import(`./locales/${lang}.json`)                    // 只匹配 locales/*.json
```
