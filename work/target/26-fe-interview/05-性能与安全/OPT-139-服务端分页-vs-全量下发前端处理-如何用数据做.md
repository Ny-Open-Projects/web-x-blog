---
title: [OPT-139] 服务端分页 vs 全量下发前端处理，如何用数据做取舍？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-139：服务端分页 vs 全量下发前端处理，如何用数据做取舍？

**答**：
- 两个都要量：**传输成本**（全量 JSON 字节数、弱网加载时长）和**交互成本**（前端排序/筛选/搜索是否需要全量数据在本地）。
- 度量方法：取真实数据集测三组——全量（含 gzip 后体积与解析耗时）、标准分页（20 条/页）、游标分页；再叠加"用户实际翻页深度"数据（如果 90% 用户只看前 3 页，全量的尾页数据是纯浪费）。
- 经验边界：≤ 500 条且需要本地实时筛选排序 → 全量（或虚拟列表全量渲染）；500~5000 条 → 分页 + 服务端筛选；> 5000 或无限流场景 → 游标分页。
- 混合策略：首屏服务端分页保证 LCP，用户触发"查看全部"时再懒加载全量进虚拟列表。

```javascript
// 一一对应：全量 vs 分页的实测对比脚本（体积 + 解析 + 渲染）
async function benchmark(table, pageSize = 20) {
  const t0 = performance.now();
  const allRes = await fetch(`/api/records?mode=all&table=${table}`);
  const allText = await allRes.text();
  const t1 = performance.now();
  const all = JSON.parse(allText);                       // 全量解析成本
  const t2 = performance.now();
  const pageRes = await fetch(`/api/records?table=${table}&page=1&size=${pageSize}&fields=id,title,status`);
  const pageText = await pageRes.text();
  const t3 = performance.now();

  return {
    table,
    all_bytes: allText.length,
    all_parse_ms: +(t2 - t1).toFixed(1),                 // JSON.parse 是主线程同步阻塞点
    page_bytes: pageText.length,
    page_payload_ratio: +(pageText.length / allText.length).toFixed(3),
    fields_note: '分页侧同时做了字段裁剪，体积比通常 < 5%',
  };
}

// 决策：结合埋点的翻页深度做加权
function decide(rows, p90PageDepth) {
  if (rows.length <= 500) return '全量下发 + 虚拟列表';
  if (p90PageDepth <= 3)  return '标准分页（首屏快，尾页无人看）';
  return '游标分页 + 搜索走服务端'; // 深翻页/大数据集
}
```
