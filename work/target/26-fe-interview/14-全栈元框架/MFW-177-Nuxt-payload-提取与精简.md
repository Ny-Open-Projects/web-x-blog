---
title: [MFW-177] Nuxt 的 payload 提取与精简是怎么回事？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-177：Nuxt 的 payload 提取与精简是怎么回事？
**答**：
- Nuxt SSR 会把服务端取到的数据序列化成 payload 注入 HTML（或内联到 RSC 类似的 `window.__NUXT__` / script 标签），复水时客户端直接用，不发重复请求——这就是 payload 提取。
- payload 会把页面体积撑大：列表页塞 500 条全量对象、组件里的 Date/Map、组件定义引用都会进 payload。**payload 过大是 Nuxt SSR 页面 TTFB 后传输慢的第一大原因**。
- 精简手段：`useAsyncData` 只取需要的字段（服务端投影 select），不要把整个 DB row 塞进去；列表只传页内数据不含冗余；大对象改传 id，客户端按需再取。
- 序列化层面用 devalue（支持 Map/Set/循环引用）；注意函数、类实例不能序列化，会被剔除或报错——别把「带方法的 class 实例」放进 `useState`。
- 诊断工具：Nuxt DevTools 的 payload 面板直接看每页 payload 大小；`payloadExtraction: false` 可关掉提取用于全静态场景。

```javascript
// 精简前：整行塞进 payload（差）
const { data } = await useFetch('/api/products?page=1'); // row 含富文本、埋点字段…

// 精简后：服务端投影，只留视图字段
const { data } = await useFetch('/api/products', {
  query: { page: 1, fields: 'id,title,price,cover' }, // SQL/API 层 select
});
// data 进 payload 的体积从 ~400KB 降到 ~40KB
```
