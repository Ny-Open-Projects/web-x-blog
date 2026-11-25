---
title: [SCN-1139] IoT 设备控制台的设备搜索（模糊多条件）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1139：IoT 设备控制台的设备搜索（模糊多条件）

**答**：
- 搜索：按 SN/名称/位置/状态组合搜索，联想（SN 前缀）+ 筛选器组合。
- 性能：服务端索引检索（设备名倒排），前端防抖 300ms。
- 结果：搜索结果高亮 + 保存为自定义视图（常用筛选）。

```javascript
// 设备搜索
function deviceSearch(query, filters) {
  return debounce(300, () => api('/device/search', {
    q: query, ...filters }));
}
// 自定义视图：
function saveView(name, filters) {
  return api('/device/view/save', { name, filters });   // 常用筛选保存
}
}
```
