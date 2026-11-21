---
title: [RBL-313] CSP 与构建的配合（hash/nonce 的构建期生成）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-313：CSP 与构建的配合

**答**:
- 构建期生成 CSP：扫描产物里的行内脚本/eval 使用 → 生成 script-src hash 清单或 nonce 模板——CSP 不是部署方单方面的事，构建必须配合
- 行内脚本治理：html 注入的 runtime script 改外链或加 nonce；产物内禁 eval（csp 不允许 unsafe-eval，某些库要 polyfill 替代）
- 验证闭环：构建产物 + CSP 头 → 本地 CSP 检测器（模拟浏览器执行）跑一遍 → 违规项在构建期暴露而非上线后白屏
- 演进策略：report-only 先行收集违规 → 收敛 → 强制执行；构建期把「CSP 兼容性」纳入门禁

```javascript
// 构建期 CSP hash 清单
const inlineHashes = extractInlineScripts(html).map((s) => `'sha256-${sha256(s)}'`)
const csp = `script-src 'self' ${inlineHashes.join(' ')}`
// 验证：本地模拟执行产物 + CSP → 违规清单
```
