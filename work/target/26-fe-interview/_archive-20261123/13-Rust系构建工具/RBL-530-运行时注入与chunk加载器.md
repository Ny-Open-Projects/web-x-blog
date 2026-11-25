---
title: [RBL-530] 运行时注入：chunk 加载器、publicPath 与错误恢复
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-530：运行时注入：chunk 加载器、publicPath 与错误恢复

**答**:
- 打包器要注入的运行时（runtime）三件套：
- 1) **chunk 加载器**：动态 import 的运行时实现——JSONP（旧）/script 标签/import() 原生——加载器要处理「chunk 已加载去重 + 加载失败重试 + 并发请求合并」。
- 2) **publicPath 解析**：chunk URL 前缀——静态（配置值）/自动推断（`document.currentScript.src`）/运行时变量（`__webpack_public_path__`）——CDN 场景的错误 publicPath 是「404 白屏」的高发源。
- 3) **错误恢复**：chunk 加载失败（网络抖动）的重试与降级——「chunk 加载失败后标记 + 重试 N 次 + 最终 reload」是 PWA/弱网的必备。
- 多入口共享 runtime：runtime 要么内联进每个入口（体积重复），要么提取 runtime chunk（额外请求但可长缓存）——「runtime chunk 提取」的缓存收益在多入口大应用才显著。
- 追问钩子：加载失败的「重试风暴」防护——多个 chunk 同时失败各自重试 → 与 ZSM-758 熔断同构：共享重试预算 + 退避——运行时也要有熔断思维。

```javascript
// 运行时注入三件套
const RUNTIME_TRIO = {
  chunk加载器: '去重 + 失败重试 + 并发合并（同一 chunk 并发请求只发一次）',
  publicPath: {
    modes: ['静态配置', 'document.currentScript 自动推断', '运行时变量 __webpack_public_path__'],
    pitfall: 'CDN 错误 publicPath = 404 白屏高发',
  },
  错误恢复: '失败标记 + 重试 N 次 + 最终 reload——弱网必备',
  runtime提取: '内联每入口（体积重复）vs runtime chunk（长缓存）——多入口大应用才显著',
  重试风暴: '多 chunk 并发重试 → 共享预算 + 退避（ZSM-758 熔断同构）',
}
```
