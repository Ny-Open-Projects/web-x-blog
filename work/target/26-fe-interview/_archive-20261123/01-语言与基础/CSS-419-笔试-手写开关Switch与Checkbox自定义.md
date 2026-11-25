---
title: [CSS-419] 笔试：手写开关 Switch（纯 CSS + 状态样式）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-419：笔试：手写开关 Switch

**题目**：实现开关组件：① input[type=checkbox] + label 实现（原生键盘可达）；② 滑块位移 + 颜色过渡（transform 动画）；③ 三态支持：checked/indeterminate/禁用；④ 尺寸变体（sm/lg）；⑤ 焦点环（:focus-visible）。写出核心实现。

```html
<label class="switch sw-lg">
  <input type="checkbox" role="switch">
  <i class="knob-track"><i class="knob"></i></i>
  <span>接收推送</span>
</label>
```

```css
.switch { display: inline-flex; align-items: center; gap: 8px; cursor: pointer; }
.switch input { position: absolute; opacity: 0; }   /* 隐藏但保留可聚焦 */
.knob-track {
  position: relative;
  width: 40px; height: 22px; border-radius: 11px;
  background: #ddd; transition: background .2s;
}
.knob {
  position: absolute; top: 2px; left: 2px;
  width: 18px; height: 18px; border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 3px #0003;
  transition: transform .2s var(--ease-out-quart);   /* 合成器动画 */
}
.switch input:checked + .knob-track { background: var(--primary); }
.switch input:checked + .knob-track .knob { transform: translateX(18px); }

/* indeterminate 半选态 */
.switch input:indeterminate + .knob-track .knob { transform: translateX(9px); }
.switch input:indeterminate + .knob-track { background: color-mix(in oklab, var(--primary) 50%, #ddd); }

/* 尺寸变体 */
.sw-sm .knob-track { width: 32px; height: 18px; }
.sw-sm .knob { width: 14px; height: 14px; }
.sw-sm input:checked + .knob-track .knob { transform: translateX(14px); }

/* 禁用与焦点 */
.switch input:disabled + .knob-track { opacity: .5; cursor: not-allowed; }
.switch input:focus-visible + .knob-track { outline: 2px solid var(--primary); outline-offset: 2px; }
```

**评分点**：
- 原生 checkbox 语义（键盘空格切换/读屏可用）
- 滑块 transform 位移（合成器）+ checked 选择器链
- indeterminate 三态处理
- focus-visible 焦点环 + 尺寸变体 token 化
