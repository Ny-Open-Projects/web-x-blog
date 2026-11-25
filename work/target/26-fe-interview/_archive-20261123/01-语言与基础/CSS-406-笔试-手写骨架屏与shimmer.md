---
title: [CSS-406] 笔试：手写骨架屏（shimmer 动画 + 布局一致性）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-406：笔试：手写骨架屏

**题目**：实现列表骨架屏：① 骨架块 shimmer 扫光动画（渐变位移）；② 骨架布局与真实内容一致（头像圆 + 双行文本 + 图块比例）；③ 骨架与真实内容切换无跳动（尺寸一致）；④ 纯 CSS 扫光（background-position 动画）与合成器替代方案（transform 平移伪元素）；⑤ 支持 dark 模式色板。写出核心实现。

```html
<div class="sk-card">
  <div class="sk-avatar sk"></div>
  <div class="sk-lines"><div class="sk sk-line w80"></div><div class="sk sk-line w50"></div></div>
  <div class="sk sk-img"></div>
</div>
```

```css
.sk {
  position: relative; overflow: hidden;
  background: #eee;
}
.sk::after {                       /* 扫光层: 平移方案(合成器) */
  content: ''; position: absolute; inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(90deg, transparent, rgb(255 255 255 / .6), transparent);
  animation: shimmer 1.4s infinite;
}
@keyframes shimmer { to { transform: translateX(100%); } }
/* dark */
:root[data-theme='dark'] .sk { background: #262626; }
:root[data-theme='dark'] .sk::after {
  background: linear-gradient(90deg, transparent, rgb(255 255 255 / .08), transparent);
}

.sk-avatar { width: 40px; height: 40px; border-radius: 50%; }
.sk-line { height: 14px; border-radius: 4px; margin: 6px 0; }
.w80 { width: 80%; } .w50 { width: 50%; }
.sk-img { width: 100%; aspect-ratio: 16/9; border-radius: 8px; }
/* 真实内容与骨架同尺寸: 切换无 CLS */
.sk-card { display: flex; gap: 12px; padding: 12px; }
```

**评分点**：
- 扫光用伪元素 translateX（合成）优于 background-position（重绘）
- 骨架结构与真实布局一致 + aspect-ratio 防 CLS
- dark 模式双套扫光透明度
- overflow hidden 裁剪扫光层
