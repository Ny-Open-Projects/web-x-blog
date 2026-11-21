---
title: [MFW-183] ESI（边缘组装）思想是什么？元框架时代的对应物有哪些？
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-183：ESI（边缘组装）思想是什么？元框架时代的对应物有哪些？
**答**：
- ESI（Edge Side Includes）：CDN/代理在响应中解析 `<esi:include>` 标签，为每个片段独立设置 TTL 并分别回源，最终**边缘组装**出整页——主页面 TTL 长、个性化片段 TTL 短，各缓存各的。
- 经典痛点：整页缓存下「导航栏要显示登录名」导致页面无法缓存；ESI 把问题拆成片段级缓存，是微前端/片段缓存的鼻祖。
- 元框架时代的对应物：
  - Next RSC 流式 + PPR：静态壳预渲染，动态段（读 cookies）流式补齐，等同「壳缓存 + 片段动态」。
  - Astro Server Islands：最接近 ESI 的语义——HTML 占位符 + 服务端逐岛渲染注入。
  - CDN 层仍然可用真 ESI（如 Akamai/Fastly 的 Surrogate 处理），配合 `Surrogate-Control` 头。
- 差异：ESI 是纯 HTML 拼接无 JS 运行时；RSC/岛方案带着水合协议，片段能变成可交互组件。
- 面试表达：把「页面级缓存 → 片段级缓存」的演进讲清楚，再点出各框架的落地形态即可。

```html
<!-- 传统 ESI：CDN 在边缘把两个片段分别缓存后拼装 -->
<html>
  <esi:include src="/_fragment/header" onerror="continue"/> <!-- TTL 30s，按 cookie 变体 -->
  <esi:include src="/_fragment/hot-list" ttl="600"/>       <!-- TTL 10min，人人一致 -->
</html>
```