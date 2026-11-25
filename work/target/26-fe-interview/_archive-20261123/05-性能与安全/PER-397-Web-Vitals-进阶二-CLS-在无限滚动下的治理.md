---
title: [PER-397] 无限滚动列表的 CLS 治理：加载更多时的位移控制与滚动锚定？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-397：无限滚动列表的 CLS 治理：加载更多时的位移控制与滚动锚定？

**答**：
- 无限滚动的 CLS 来源：① 加载更多时新内容插入底部——正常不位移（追加在下方），但如果出现"顶部插入新内容"（信息流刷新）就会把用户正在看的内容顶下去；② 图片无尺寸占位；③ 骨架屏 → 内容高度不一致；④ 底部加载指示器的高度突变。
- 治理手段：① 追加式更新纪律——新内容永远 append 到当前视口下方，"刷新置顶"类操作改成显式按钮 + 用户确认（用户主动触发不计 CLS 的 500ms 窗口可用，但要防滥用）；② 每条内容固定尺寸契约（卡片高度档位化）；③ 图片 aspect-ratio 必填（组件层强制）；④ 滚动锚定——scroll anchoring（浏览器默认 overflow-anchor）保留，别在容器上设 overflow-anchor: none。
- 度量：无限滚动页面的 CLS 按滚动深度分桶（前 3 屏/3~10 屏/10 屏+）——深层滚动时新增的位移通常来自图片占位缺失，分桶能精确定位。

```css
/* 无限滚动容器的 CLS 纪律 */
.feed { overflow-anchor: auto; }            /* 保留浏览器滚动锚定（默认） */
.feed-item { min-height: 120px; }           /* 卡片高度档位契约 */
.feed-item img { width: 100%; height: auto; aspect-ratio: 16 / 9; }  /* 尺寸必填 */
```
```javascript
// "新内容插入"的纪律：置顶刷新必须用户显式触发
function onRefreshClick() {                          // 用户点击（hadRecentInput 豁免窗口）
  prepend(newItems);                                 // 即便位移也不计 CLS
  scrollToTop();
}
// 反例：轮询自动 prepend —— 用户正在阅读时内容被顶走，CLS + 体验双输
```
