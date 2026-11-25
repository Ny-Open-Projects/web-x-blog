---
title: [SCN-148] SaaS 产品支持客户自定义品牌色与图标皮肤，如何做运行时动态主题注入？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-148：SaaS 产品支持客户自定义品牌色与图标皮肤，如何做运行时动态主题注入？
**答**：
- 主题 = 一组 CSS 变量：运行时生成 `:root { --brand: ... }` 样式注入 `<style id="runtime-theme">`，组件只消费变量，切换零重编译。
- 颜色要有派生计算：主色的 hover/active/浅底色由主色计算（HSL 调整），不能要求客户配十个色值。
- 图标皮肤用 iconfont 多套 CSS 按需切换：替换 `<link>` 的 href 并带 hash 防缓存；SVG symbol 方案则替换 symbol 资源。
- 注入要在首屏渲染前（防闪烁）：把租户主题随 HTML 下发或首字节前同步写入。

```javascript
// 动态主题：CSS 变量注入 + 派生色计算 + iconfont 热切换
function hslShift(hex, { l = 0, s = 0 } = {}) {
  const { h, s: sat, l: lig } = hexToHsl(hex);
  return hslToHex(h, clamp(sat + s, 0, 100), clamp(lig + l, 0, 100));
}

export function applyTheme(theme) {
  const brand = theme.brandColor;
  // 派生色：客户只配主色，hover/active/浅底自动算
  const css = `:root{
    --brand:${brand};
    --brand-hover:${hslShift(brand, { l: -6 })};
    --brand-active:${hslShift(brand, { l: -12 })};
    --brand-bg:${hslShift(brand, { l: 42, s: -20 })};
    --radius:${theme.radius ?? 4}px;
  }`;
  let el = document.getElementById('runtime-theme');
  if (!el) { el = document.createElement('style'); el.id = 'runtime-theme'; document.head.appendChild(el); }
  el.textContent = css;                                // 整体替换，避免多次注入叠加

  // 图标皮肤：换 iconfont link，带 hash 防缓存
  const iconHref = `https://cdn.example.com/skins/${theme.skin}/iconfont.css?v=${theme.skinVersion}`;
  const current = document.getElementById('skin-iconfont');
  if (current?.getAttribute('href') !== iconHref) {
    (current ?? createLink('skin-iconfont')).setAttribute('href', iconHref);
  }
}

// 首屏防闪烁：主题以 JSON 内联在 HTML 里，CSS 加载前同步执行
export function bootTheme() {
  const theme = JSON.parse(document.getElementById('__THEME__')?.textContent ?? '{}');
  if (theme.brandColor) applyTheme(theme);
}
```
