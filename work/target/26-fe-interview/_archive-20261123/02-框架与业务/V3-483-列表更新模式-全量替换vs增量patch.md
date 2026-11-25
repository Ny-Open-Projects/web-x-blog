---
title: [V3-483] 列表更新模式：全量替换 vs 增量 patch 的取舍
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## V3-483：列表更新模式：全量替换 vs 增量 patch 的取舍

**答**：
- 全量替换（list.value = newList）：语义简单、vdom diff 处理对齐——大列表 diff 成本 O(n)，key 稳定时 diff 只做移动标记，实际成本可控；但 5000+ 条仍明显
- 增量 patch：数据层 splice/直接改 item 字段——响应式精准触发，diff 范围小；代价是「数据来源多路写入」的心智负担（WebSocket 推送场景天然增量）
- 混合策略：分页列表全量替换（整页换）；实时 feed 用增量（insert/splice + 头部插入用 unshift 且 key 稳定）——按数据到达形态选
- key 的两种成本：稳定 id（diff 按键对齐，只移动必要节点）vs index key（追加尾部等效，但头部插入全列表重新对齐）——头部插入的列表必须稳定 id
- 配合优化：列表项组件化 + v-memo（按 item.updatedAt 跳过）、分页过渡用 CSS 保持位置（scroll anchoring）

```javascript
// 实时 feed 增量
ws.onmessage = ({ data }) => {
  const item = JSON.parse(data);
  const idx = list.value.findIndex(x => x.id === item.id);
  idx >= 0 ? list.value[idx] = item : list.value.unshift(item);  // 增量
};
// 分页全量
async function loadPage(p) { list.value = await api.page(p); }
```
