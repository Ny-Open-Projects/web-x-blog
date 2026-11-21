---
title: [WCN-269] 两个事件源并发写同一信号（网络回调 + 用户输入）的合并语义？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-269：两个事件源并发写同一信号（网络回调 + 用户输入）的合并语义？
**答**：
- 默认：后写覆盖（LWW）——多数 UI 语义正确。
- 需要合并语义时：update(updater) 基于当前值合并（如列表 append 不覆盖）。
- 跨事件源排序：时间戳/序列号显式仲裁（防乱序回调覆盖新数据）。
- 案例：搜索结果回包乱序——epoch 校验丢弃旧包。

```javascript
// 网络回调晚到覆盖用户输入 → 用 epoch
let epoch = 0;
input.oninput = e => { const ep = ++epoch; query.value = e.target.value; };
fetchCb = (res) => { if (epoch === myEpoch) results.value = res; };  // 旧包丢弃
r
```
