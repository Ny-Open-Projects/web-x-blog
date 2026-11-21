---
title: [JS-231] console.log 也会导致泄漏吗：DevTools 保留引用
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 内存]
type: 面试题
---

## JS-231：console.log 也会导致泄漏吗

**答**：
- 现象：DevTools 打开时，console 打印过的对象被 Console 面板持有引用，GC 不回收——「打印一次，钉住一生」
- 影响范围：只在 DevTools 打开期间存在；生产用户（不开 DevTools）无此问题
- 为什么重要：开发期内存分析被它污染——「怎么内存一直涨」，其实是自己的 console.log 钉住
- 实践规范：构建期删除 console（terser/esbuild drop console）；调试大对象打印关键字段而非整对象
- 关联知识：Vue/React dev 模式的 inspect 面板同样持有组件实例，分析内存要关掉相关面板

```javascript
// ❌ 大响应对象被 Console 持有
console.log(res.json);
// ✅ 只打印需要的
console.log(res.json.items.length);
// 构建配置（esbuild）
// esbuild --define:process.env.NODE_ENV='"production"' --drop:console
```
