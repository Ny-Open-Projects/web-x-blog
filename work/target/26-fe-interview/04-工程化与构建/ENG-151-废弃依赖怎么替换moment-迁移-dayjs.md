---
title: [ENG-151] 废弃依赖怎么替换？moment 迁移 dayjs 全案例怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-151：废弃依赖怎么替换？moment 迁移 dayjs 全案例怎么做？
**答**：
- moment 已停止新特性开发且体积大不可 tree-shake，是废弃替换的教科书案例；迁移走"兼容层先行 逐个清理差异"。
- 第一步用构建 alias 把 moment 指向 dayjs（API 高度兼容），让构建先通过，业务无感切换。
- 差异点逐个清理：locale 文件路径、插件机制（extend）、时区（utc + timezone 插件替代 moment.tz）。
- 验证兜底：日期相关单测全量 + golden 样本比对两种库的格式化输出，历史日期边界重点回归。

```javascript
// vite.config.ts —— alias 兼容层渐进替换 moment
import { defineConfig } from 'vite'

export default defineConfig({
  resolve: {
    alias: [
      // 第一步 API 兼容层 整体替换
      { find: 'moment', replacement: 'dayjs' },
      // 第二步 locale 差异 路径映射
      { find: 'moment/locale/zh-cn', replacement: 'dayjs/locale/zh-cn' },
    ],
  },
  // 第三步 入口注册插件替代 moment.tz
  // import dayjs from 'dayjs'
  // import utc from 'dayjs/plugin/utc'
  // import timezone from 'dayjs/plugin/timezone'
  // dayjs.extend(utc); dayjs.extend(timezone)
  // 第四步 golden 样本回归
  // node scripts/date-golden-test.mjs --from moment --to dayjs
})
```
