---
title: [V3-445] 笔试：手写图片懒加载指令（IntersectionObserver + WebP 协商 + 失败占位）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-445：笔试：手写图片懒加载指令（IntersectionObserver + WebP 协商 + 失败占位）
**答**：实现 v-lazy 指令：data-src 延迟加载；进入视口（rootMargin 200px 预取）时替换 src；优先请求 .webp（canvas 检测支持）；加载失败显示占位图并允许重试；卸载/元素移除时断开 observer。

```javascript
let webpSupport = null
function supportsWebp() {
  if (webpSupport !== null) return webpSupport
  const canvas = document.createElement('canvas')
  canvas.width = canvas.height = 1
  webpSupport = canvas.toDataURL('image/webp').startsWith('data:image/webp')
  return webpSupport
}
const ob = new IntersectionObserver((entries) => {
  entries.forEach(en => {
    if (!en.isIntersecting) return
    const img = en.target
    let src = img.dataset.src
    if (supportsWebp()) src = src.replace(/\.(png|jpe?g)$/, '.webp')
    img.src = src
    img.onload = () => img.classList.add('loaded')
    img.onerror = () => {
      img.src = '/placeholder.png'    // 占位
      img.dataset.retry = (Number(img.dataset.retry) || 0) + 1
      if (Number(img.dataset.retry) < 2) { img.src = src } // 一次重试
    }
    ob.unobserve(img) // 加载后停止观察
  })
}, { rootMargin: '200px' })
export const vLazy = {
  mounted(el) { ob.observe(el) },
  unmounted(el) { ob.unobserve(el) }
}
// <img v-lazy data-src="/goods/1.jpg" />
```
**评分点**：
- IO rootMargin 预取缓冲 + 加载后 unobserve。
- WebP 能力检测缓存（只测一次）。
- 失败占位 + 重试上限（防死循环）。
- 指令生命周期配对 unobserve。
