---
title: [PER-1012] 手写一个字体切换 CLS 守卫：度量回退字体并生成 size-adjust
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1012：手写一个字体切换 CLS 守卫：度量回退字体并生成 size-adjust

**答**：
- 需求：实现 fontGuard(targetMetrics, fallbackName)。targetMetrics 为 { ascent, descent, unitsPerEm, advance }；输出 @font-face 覆盖所需的比例值：ascent-override = ascent/unitsPerEm*100%，descent 同理，size-adjust = targetAdvance/fallbackAdvance*100（fallbackAdvance 需实测：用隐藏 span 渲染同文本对比宽度）。
- 边界：参数缺失时抛错；size-adjust 计算 clamp 到 [80,200]；提供 measureFallback(text) 辅助函数用 canvas 实测宽度。

```javascript
function measureFallback(fallbackName, text, size = 100) {
  const c = document.createElement('canvas').getContext('2d');
  c.font = `${size}px ${fallbackName}`;
  return c.measureText(text).width / size;      // 平均字宽
}
function fontGuard(target, fallbackName) {
  const { ascent, descent, unitsPerEm, advance } = target;
  if (!unitsPerEm || !advance) throw new Error('缺少度量参数');
  const fw = measureFallback(fallbackName, '测试Test');
  const sizeAdjust = Math.min(200, Math.max(80, +(advance / fw).toFixed(3) * 100));
  return {
    'ascent-override': +(ascent / unitsPerEm).toFixed(4),
    'descent-override': +(descent / unitsPerEm).toFixed(4),
    'size-adjust': sizeAdjust,
  };
}
// 产出可直接拼进 @font-face 规则，消除 FOUT 宽度跳变
```
