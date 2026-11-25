---
title: [BAS-160] writing-mode 怎么实现竖排文字？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-160：writing-mode 怎么实现竖排文字？
**答**：
- `vertical-rl` 从右往左竖排（古文、日文），`vertical-lr` 从左往右；text-orientation: upright 让拉丁字符直立。
- 竖排会改变块的流动方向：block 方向变成水平，行内方向变成垂直，margin/padding 的"上下"感知要换脑。
- 典型场景：书脊文字、侧边标签、诗歌排版；配合 logical properties 不受影响。

```css
.vertical {
  writing-mode: vertical-rl;   /* 从右往左竖排 */
  text-orientation: mixed;     /* 中文字直立，英文旋转 90 度 */
}
.spine {
  writing-mode: vertical-rl;   /* 书脊/侧边标签常用 */
  text-orientation: upright;   /* 拉丁字符也逐字直立 */
}
```
