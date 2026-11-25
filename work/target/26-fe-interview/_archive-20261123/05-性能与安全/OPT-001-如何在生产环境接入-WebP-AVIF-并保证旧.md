---
title: [OPT-001] 如何在生产环境接入 WebP/AVIF 并保证旧浏览器优雅降级？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-001：如何在生产环境接入 WebP/AVIF 并保证旧浏览器优雅降级？

**答**：
- 用 `<picture>` 的多个 `<source>` 声明候选格式：AVIF 优先、WebP 次之、JPEG 兜底，浏览器按顺序选择第一个支持的格式。
- AVIF 相比 JPEG 平均省 50% 体积、WebP 省 25%~35%，LCP 图片收益最明显。
- 服务端/CDN 也可根据请求头 `Accept: image/avif` 做内容协商，直接返回对应格式。
- 注意 AVIF 编码耗时高于 WebP，一般构建期或 CDN 边缘生成，不实时转码。

```html
<!-- 一一对应：picture 多 source 接入 AVIF/WebP 并兜底 JPEG -->
<picture>
  <!-- 浏览器从上到下匹配，支持 AVIF 就用 AVIF -->
  <source type="image/avif" srcset="hero.avif" />
  <!-- 不支持 AVIF 但支持 WebP 时走这里 -->
  <source type="image/webp" srcset="hero.webp" />
  <!-- 最终兜底：所有浏览器都支持 -->
  <img src="hero.jpg" alt="首页主图" width="1200" height="630" fetchpriority="high" />
</picture>
```
