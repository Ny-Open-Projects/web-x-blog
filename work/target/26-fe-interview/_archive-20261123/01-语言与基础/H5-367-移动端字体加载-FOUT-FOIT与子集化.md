---
title: [H5-367] 移动端字体加载：FOUT/FOIT 与子集化
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## H5-367：移动端字体加载：FOUT/FOIT 与子集化

**答**：
- 阻塞行为：默认 font-display: auto = 隐形期约 3s（FOIT 白屏文本），swap 立即回退字体（FOUT 抖动），optional 网络差直接用回退不换——按页面性质选：正文 swap + 预加载，品牌标题 optional
- 中文字体子集化是关键：完整中文字体 5~10MB 不可接受——按页面实际用字生成子集（fontmin/pyftsubset）或走云端按需子集服务（按 unicode-range 切片）
- unicode-range 切片方案：字体按使用频率切成几十片 woff2 + @font-face unicode-range 声明，浏览器只下载用到的切片——业界「中文 web font」标准做法
- 预加载与缓存：woff2 加 preload + font-display 配合；字体缓存有效期长（immutable），版本 hash 更新
- 降级体验：字体加载期用 metrics 相近的回退字体（size-adjust/ascent-override 调宽度）减小布局抖动

```css
@font-face {
  font-family: 'PingFangFallback'; src: local('PingFang SC');
  size-adjust: 98%; ascent-override: 92%;           /* 减少切换抖动 */
}
@font-face {
  font-family: 'BrandCN'; src: url('/fonts/brand-cn-0.woff2') format('woff2');
  unicode-range: U+4E00-4FFF;                        /* 切片1: 常用汉字段 */
  font-display: swap;
}
.title { font-family: 'BrandCN', 'PingFangFallback', sans-serif; }
```

```html
<link rel="preload" href="/fonts/brand-cn-0.woff2" as="font" type="font/woff2" crossorigin>
```
