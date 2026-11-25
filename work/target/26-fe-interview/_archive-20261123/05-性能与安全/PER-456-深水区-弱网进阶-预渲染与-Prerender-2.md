---
title: [PER-456] Speculation Rules API：预渲染（prerender）的正确使用与滥用风险？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-456：Speculation Rules API：预渲染的正确使用与滥用风险？

**答**:
- 能力：`<script type="speculationrules">` 声明预取（prefetch）与预渲染（prerender）规则——浏览器在空闲时提前加载/渲染"可能去的页面"（命中规则 + 置信度），用户点击时页面已就绪（LCP ≈ 0）。Chrome 121+ 支持 eagerness 分级（conservative/moderate/eager）。
- 正确使用：高置信导航（列表页 → 详情的点击、分页 next）用 moderate prerender；文档类链接（帮助页）prefetch；配合 SRP（document rules）按 CSS 选择器指定哪些链接预渲染。
- 滥用风险：① 资源消耗——每 prerender 一个页面 ≈ 完整渲染成本（内存/CPU），eager 模式全链接预渲染会拖垮低端机；② 副作用触发——prerender 页面的 JS 照常执行（埋点/轮询/动画全部提前跑，统计虚增 + 服务端压力）——埋点需判断 document.prerendering 状态延迟到 activation；③ 缓存失效——prerender 的数据到 activation 时可能已陈旧。
- 度量：prerender 命中率（activation/渲染数）与浪费率——低于 30% 命中就该收窄规则（eagerness 降级）。

```html
<script type="speculationrules">
{
  "prerender": [{ "where": { "href_matches": "/goods/*" },
                  "eagerness": "moderate" }],        <!-- 列表→详情：高置信预渲染 -->
  "prefetch": [{ "where": { "href_matches": "/help/*" },
                 "eagerness": "conservative" }]
}
</script>
```
```javascript
// 副作用防护：prerender 期间 JS 已执行——埋点延迟到 activation
if (document.prerendering) {
  document.addEventListener('prerenderingchange', () => trackPageView(), { once: true });
} else trackPageView();
// 度量：activation 数 / prerender 数 = 命中率；< 30% → eagerness 降级收窄规则
```
