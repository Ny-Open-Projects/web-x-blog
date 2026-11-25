---
title: [BLD-227] 图片资源的构建处理怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-227：图片构建处理怎么做？
**答**：
- 管线：导入声明 → 格式转换（webp/avif 自动生成多格式）→ 尺寸变体（srcset 多分辨率）→ 压缩（质量分级）→ hash 命名 → manifest 生成（引用替换）。
- 内联阈值：小图（<4KB）base64 内联（省请求）——阈值权衡（内联进 JS 使 chunk 变大）。
- 响应式：构建时生成多尺寸 + srcset/sizes 自动生成（设计师上传一张原图）。
- SVG 特殊处理：sprite 合并（svg-sprite）或按需加载（大 SVG 独立文件）；SVG 内容哈希 + 安全清理（去掉注释/元数据）。
- 追问钩子：为什么小图内联的阈值要考虑「chunk 体积」而不只是请求数——内联进 JS 后图片随 chunk 下载，不命中浏览器图片缓存（每 chunk 变化重新下载）；且 JS 中 base64 比 binary 大 33%——阈值不是越小越好，重复使用的小图标才值得内联，一次性大图宁可独立请求（可缓存）。

```javascript
// vite: 资源管线
import logo from './logo.png?url';                   // 产物 URL
// vite-plugin-image: 自动 avif/webp + srcset
<img srcSet={`${logo.avif} 1x, ${logo@2x.avif} 2x`} type="image/avif">
// 内联阈值
assetsInlineLimit: 4096
```
