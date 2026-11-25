---
title: [BAS-080] font 简写有什么陷阱？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-080：font 简写有什么陷阱？
**答**：
- font 简写必须同时包含 font-size 和 font-family，缺一整条失效；且会把 style/variant/weight/line-height 等重置为默认。
- 行高要写进简写：`font: 14px/1.5 Arial`，size 后用斜杠接 line-height。
- 想保留粗体等设置，要么写进简写（`font: bold 14px/1.5 Arial`），要么放在简写之后。

```css
p {
  font-weight: bold;                          /* 会被下面的简写重置为 normal */
  font: 14px/1.5 "PingFang SC", sans-serif;   /* 合法：size 与 family 必填 */
  font-weight: bold;                          /* 想要粗体就写在简写之后 */
}
```

## 十、JavaScript 语法补充
