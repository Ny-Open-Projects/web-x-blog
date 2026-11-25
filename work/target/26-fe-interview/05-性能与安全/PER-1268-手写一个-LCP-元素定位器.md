---
title: [PER-1268] 手写一个 LCP 元素定位器
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1268：手写一个 LCP 元素定位器

**答**：
- 需求：实现 lcpElement(entries, resources)。entries 为 LCP 候选（{ element, size, url, startTime }）；最终 LCP = 最后一个候选；若为图片：在 resources 中找对应资源加载耗时并给出优化建议（preconnect/preload/格式）；若为文本：检查字体是否阻塞（document.fonts 状态）；输出 { type, tag, url, loadMs, advice }。
- 边界：entries 为空返回 null；图片资源未找到 loadMs = null；advice 最多 2 条。
- 评分点：最后候选；图片/文本分支；资源关联；建议限 2

```javascript
function lcpElement(entries, resources, fontState) {
  if (!entries.length) return null;
  const last = entries[entries.length - 1];
  const isImg = last.url && /\.(png|jpe?g|webp|avif|gif)/.test(last.url);
  const advice = [];
  let loadMs = null;
  if (isImg) {
    const res = resources.find(r => r.name.endsWith(last.url.split('/').pop()));
    loadMs = res ? Math.round(res.duration) : null;
    if (res && res.duration > 500) advice.push('LCP 图加载 >500ms：preload + fetchpriority=high');
    if (last.url.endsWith('.png') || last.url.endsWith('.jpg'))
      advice.push('改用 AVIF/WebP');
  } else if (fontState && fontState.loading) {
    advice.push('文本 LCP 受字体阻塞：font-display:swap + 子集化');
  }
  return { type: isImg ? 'image' : 'text',
    tag: last.element?.tagName?.toLowerCase() ?? 'unknown',
    url: last.url ?? null, loadMs, advice: advice.slice(0, 2) };
}
```

## 补充：评分点与变体

**评分点**：

- 能稳定生成选择器（id、class 路径，兜底 nth-of-type），保证同页多次生成结果一致。
- 处理动态插入与 Shadow DOM 边界，采样时元素可能已卸载，要有判空兜底。
- 输出元素尺寸与资源 URL，便于直接判断是图片过大还是加载过晚。
- 重复元素去重，不因重渲染或多次成为候选而重复上报。

**变体与延伸**：

1. 选择器不稳定怎么办？ → 优先 data-* 锚点，退化时用结构路径加文本双因子。
2. Shadow DOM 里怎么定位？ → 沿 composedPath 逐层拼接宿主选择器。
