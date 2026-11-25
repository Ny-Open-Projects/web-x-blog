---
title: [SCN-849] 笔试题——实现 RTL 联想适配（导航镜像 + 截断方向 + 对齐）？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-849：手写 RTL 联想适配

**需求与边界**：
- 需求：RTL 语言下：① ↑↓ 导航不变但分组内视觉顺序镜像；② 长文本截断省略号在左；③ 高亮偏移仍按逻辑顺序（码点）计算；④ 容器 direction 属性与 CSS logical properties。
- 边界：① 不用物理属性（left/right）改用 logical（inset-inline）；② 数字与英文段 LTR 嵌入（bidi 隔离）；③ 键盘 ArrowLeft/Right 在 RTL 下语义反转（若支持水平导航）。

**答**：
```javascript
function rtlAwareRender(container, { rtl }) {
  container.dir = rtl ? 'rtl' : 'ltr';                 // 容器方向
  // CSS: .suggest-row { text-align: start; overflow: hidden;
  //        text-overflow: ellipsis; direction: inherit; }
  // logical properties 自动镜像（inset-inline-start 等）
  return {
    navMap: rtl ? { ArrowLeft: 'next', ArrowRight: 'prev' } : { ArrowLeft: 'prev', ArrowRight: 'next' },
    bidiIsolate: (text) => text.replace(/[\dA-Za-z]+/g, (m) => `\u2066${m}\u2069`),   // LRI..PDI 隔离
    highlight: renderHighlight,                        // 偏移按逻辑序，渲染自动镜像
  };
}
// bidi 隔离：'وجدت 5 نتائج' 中数字 5 用 LRI/PDI 包裹防方向混乱
```

**评分点**:
- direction + logical properties 系统镜像（不用物理 left/right）。
- 键盘导航语义映射反转。
- bidi 隔离字符（LRI/PDI）处理混排。
- 高亮逻辑序与视觉镜像分离（offset 计算不变）。
