---
title: [WCN-976] prefers-reduced-motion 在 SSR 阶段怎么输出：避免水合后动画突变
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-976：prefers-reduced-motion 在 SSR 阶段怎么输出：避免水合后动画突变

**答**：
- 结论先行：减弱动效偏好是 a11y 要求（前庭障碍用户），若只在客户端读取 media query，SSR 首屏会先播动画、hydration 后才停——突变体验差且违反偏好。
- SSR 读取：服务端拿不到用户系统的 media query，靠「请求头提示」（如 Sec-CH-Prefers-Reduced-Motion client hint）或首屏内联一小段脚本在 CSS 应用前给 html 打 `data-reduced-motion` 类。
- CSS 优先：用 `@media (prefers-reduced-motion: reduce)` 在样式层禁用动画/过渡，不依赖 JS——这是最可靠的 SSR 友好方案。
- JS 动画：读取 matchMedia 并在动画库初始化前决定开关；hydration 时若偏好变化，平滑停止而非瞬间跳变。
- 追问钩子：面试官问「怎么测这个偏好」——答：Playwright 可模拟 reducedMotion: 'reduce'，断言动画被禁用、内容仍完整可达。

```javascript
/* CSS 层直接响应，SSR 首屏即生效 */
<style>
.card { transition: transform .3s; }
@media (prefers-reduced-motion: reduce) {
  .card { transition: none; animation: none; }
}
</style>
<script>
// 首屏内联脚本：在样式应用前打标，供 JS 动画库读取（避免水合后突变）
if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.documentElement.dataset.reducedMotion = 'true';
}
</script>
```
