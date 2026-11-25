---
title: [H5-056] wbr 是什么？长单词/长 URL 在窄容器里如何优雅换行？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-056：wbr 是什么？长单词/长 URL 在窄容器里如何优雅换行？
**答**：
- `<wbr>`（word break opportunity）标记"**允许在此处断行**"的位置，正常放得下时不产生任何效果，放不下才在标记处折行。
- 适用场景：超长 URL、SKU 编号、哈希值、驼峰长标识符——这类连续字符串浏览器默认不拆。
- 兄弟方案：`overflow-wrap: break-word` 任意位置硬拆（可能拆出难看的半截），`hyphens: auto` 按连字符规则拆（依赖 lang 且中文场景无关）。
- 组合拳：URL 在 `/`、`?`、`&` 后插 wbr，既保住可读分段又允许折行；CSS 兜底防溢出。
- 复制文本时 wbr 不产生字符，是它优于手动插 `-` 或 `<br>` 的关键。

```html
<style>
  .path {
    width: 220px; border: 1px solid #ccc;
    overflow-wrap: break-word;  /* CSS 兜底：wbr 之外再防溢出 */
  }
</style>

<!-- 在 URL 的分隔符后手工标记可断点 -->
<p class="path">
  https://example.com/<wbr>very/long/<wbr>path/<wbr>to/<wbr>article?id=123<wbr>&amp;from=rss
</p>

<!-- 驼峰长标识符：在词界断行 -->
<p class="path">parse<wbr>SVG<wbr>Path<wbr>Data<wbr>Into<wbr>Matrix</p>

<!-- 表格里的哈希值：每 4 位允许断行 -->
<td>ab12<wbr>cd34<wbr>ef56<wbr>7890</td>
```
