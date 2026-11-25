---
title: [OPT-178] Speculation Rules API 如何实现浏览器级预取/预渲染？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-178：Speculation Rules API 如何实现浏览器级预取/预渲染？

**答**：
- Speculation Rules 用 JSON 声明让浏览器**自主**执行预取（prefetch）或完整预渲染（prerender），比 JS 预取更底层：预渲染直接在隐藏 tab 渲染页面，点击即瞬间呈现（接近 BFCache 级体验）。
- 规则写法：`eagerness` 四档（conservative/moderate/eager）控制触发时机——moderate 在 hover 时预取，eager 页面加载即预取；`where` 用 CSS 选择器圈定链接范围。
- 成本控制：prerender 是完整渲染（含 JS 执行），要限制候选数量（moderate 默认 2 个），排除登出/删除类链接（`not` 规则），避免副作用请求（预渲染页面执行数据变更操作必须延迟到激活后）。
- 观测：`document.prerendering` 与 `activationstart` 判定预渲染命中；Chrome DevTools 的 Speculation 面板看命中/失败原因。

```html
<!-- 一一对应：Speculation Rules 预取 + 预渲染规则 -->
<script type="speculationrules">
{
  "prefetch": [
    {
      "source": "document",
      "where": { "href_matches": "/*" },
      "eagerness": "moderate",          <!-- hover 触发预取，成本最低 -->
      "not": { "href_matches": ["/logout", "/*/delete*", "/checkout?*confirm=1"] }
    }
  ],
  "prerender": [
    {
      "source": "document",
      "where": {
        "and": [
          { "href_matches": "/p/*" },          <!-- 详情页最可能被点击 -->
          { "selector": ".card-link" }          <!-- 且是列表卡片链接 -->
        ]
      },
      "eagerness": "moderate"           <!-- 浏览器自动限制约 2 个候选，控成本 -->
    }
  ]
}
</script>
<script>
  // 页面内判定：自己是被预渲染的，还是普通加载
  if (document.prerendering) {
    // 预渲染阶段：只做无副作用准备，不发埋点/不做数据变更
    addEventListener('prerenderingchange', () => {
      // 激活瞬间执行：真正的埋点、倒计时、实时数据刷新
      reportPageView();
      refreshRealtimeData();
    });
  } else {
    reportPageView();  // 普通加载
  }
  // 性能指标：预渲染命中时 LCP 从 activation 时刻起算
  // nav.activationStart —— 上报时减去该值才是用户感知耗时
</script>
```
