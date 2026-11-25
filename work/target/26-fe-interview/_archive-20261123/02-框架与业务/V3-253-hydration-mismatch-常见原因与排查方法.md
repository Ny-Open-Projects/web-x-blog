---
title: [V3-253] Vue hydration mismatch 的常见原因与排查方法有哪些？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-253：Vue hydration mismatch 的常见原因与排查方法有哪些？
**答**：
- 原因 1 时间类：渲染结果依赖 `Date.now()`/随机数/`Math.random` id，服务端与客户端取值不同。
- 原因 2 环境类：`window`/`localStorage` 在客户端 setup 直接读取（服务端报错或值不同），条件渲染分支不一致。
- 原因 3 数据类：客户端组件重新请求接口返回与 SSR payload 不一致（列表顺序变化）。
- 原因 4 结构类：`v-if` 条件两端不一致、非法 HTML 嵌套（浏览器解析后 DOM 与模板不符，如 `<p>` 内嵌 `<div>`）。
- 排查方法：开发模式 Vue 会输出完整 mismatch diff（3.5+ 信息更完整）；先定位首处 mismatch，向上找"两端取值不同的表达式"，统一用 useId、客户端 onMounted 后再读环境值。

```javascript
// 典型修复：环境值延迟到客户端
const count = ref(0);
onMounted(() => { count.value = Number(localStorage.getItem('pv') ?? 0); }); // ✅ 水合后再读
// ❌ 直接 const count = ref(Number(localStorage.getItem('pv')))
// 随机 id 修复：useId() 保证两端一致
const uid = useId();
// 条件渲染统一：isClient 分支造成结构差异时改用 CSS 或 <ClientOnly> 包裹（Nuxt）
```
