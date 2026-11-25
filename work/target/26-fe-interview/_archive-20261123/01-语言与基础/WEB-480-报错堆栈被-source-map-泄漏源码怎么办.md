---
title: [WEB-480] 报错堆栈被 source map 泄漏源码怎么办
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-480：报错堆栈被 source map 泄漏源码怎么办

**答**：
- 问题：`.map` 文件随站点发布后，任何人 F12 就能还原出你的完整源码（含注释、内部路径、私有逻辑）
- 标准方案：构建时生成 map 但不部署到 CDN，只上传到错误监控平台（Sentry 类），线上 `hidden-source-map` / 删除 map 引用注释
- 权衡：不发布 map 的代价是本地复现调试要靠本地构建同版本；Sentry 的 artifact 缓存可补齐
- 中间态：`nosources-source-map` 只暴露行号映射不含源码内容；或 map 走鉴权路径
- 治理动作：CI 加检查「产物目录不得包含 .map」，上线清单固定一项

```javascript
// vite.config.js
export default defineConfig({
  build: { sourcemap: 'hidden' }, // 生成但不指向；map 单独传监控平台
});
```
