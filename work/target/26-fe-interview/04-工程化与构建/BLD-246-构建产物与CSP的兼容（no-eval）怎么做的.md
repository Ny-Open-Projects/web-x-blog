---
title: [BLD-246] 产物与 CSP 的兼容（no-eval/no-inline）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-246：产物 CSP 兼容怎么做？
**答**：
- 冲突源：打包器的 HMR runtime（eval 执行更新）、某些 loader（style-loader 注入 style 标签——style-src 需要 unsafe-inline）、动态 import polyfill。
- 治理：生产禁 eval（output.environment/terser 不产生 eval——dev 用 eval 实现 HMR 但 prod 不需要）、style 用 link 提取（SCN-BLD-206）、nonce/hash 替代 unsafe-inline（内联脚本带 nonce）。
- 验证：CSP report-only 先行（观察违规报告）→ 收紧。
- 追问钩子：为什么 style-loader 与 CSP 冲突而 mini-css-extract 不冲突——style-loader 运行时往 DOM 注入 <style> 标签（style-src 需要 unsafe-inline）；extract 模式产出独立 .css 文件由 <link> 加载（受 style-src 外链规则，无需 unsafe-inline）——「构建期提取」同时解决了 CSP 与 FOUC 两个问题。

```javascript
// CSP
Content-Security-Policy: script-src 'self' 'nonce-xxx';
  style-src 'self';      // 无 unsafe-inline（extract 模式）
// dev HMR 用 eval 的降级：Report-Only 先行观察
'Content-Security-Policy-Report-Only': ...
```
