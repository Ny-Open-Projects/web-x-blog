---
title: [XP-287] 小程序 setData 的路径更新语法
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-287：小程序 setData 的路径更新语法

**答**：
- 路径更新：setData 的 list[2].status 形式只更新数组项，避免整组传输。
- 坑：路径更新不能增删数组项（需整组）；对象深路径同样支持。
- 度量：setData 数据量监控（> 100KB/次告警）。

```javascript
// 路径 setData
function updateListItem(page, index, patch) {
  const data = {};
  for (const [k, v] of Object.entries(patch))
    data[`list[${index}].${k}`] = v;
  page.setData(data);                                // 只传变化字段
}
// 监控：
function wrapSetData(page) {
  const orig = page.setData.bind(page);
  page.setData = (d) => {
    const size = JSON.stringify(d).length;
    if (size > 100 * 1024) report({ type: 'setdata-huge', size });
    return orig(d);
  };
}
```
