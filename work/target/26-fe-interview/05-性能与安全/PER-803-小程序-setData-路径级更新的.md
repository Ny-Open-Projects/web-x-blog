---
title: [PER-803] 小程序 setData 路径级更新的写法规范：数据路径语法、数组索引更新与常见误用
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-803：小程序 setData 路径级更新的写法规范：数据路径语法、数组索引更新与常见误用

**答**：
- 路径语法基础：this.setData({ "list[2].status": "done" }) 只更新该字段，等价整对象写法会把整个 list 重新序列化传输。
- 高频误用：① 循环里多次 setData 同一字段（应合并一次）；② 直接改 this.data 再 setData 相同值（不会触发视图但污染数据）；③ 用 JSON.parse(JSON.stringify) 大对象做整量 setData；④ key 含变量拼接时拼错路径（静默失败）。
- 数组操作规范：删除用索引路径 + splice 后只传变化段；追加传 list[length] 或切片，避免全量数组传输。
- 规范落地：lint 规则（禁止循环内 setData、禁止 > 64KB 整对象）+ code review checklist。

```javascript
// 正确 vs 错误对照
const item = this.data.list[2];
// BAD：整对象传输（list 全量过桥）
// this.setData({ list: this.data.list });
// GOOD：路径更新
this.setData({ [`list[${2}].status`]: 'done' });
// GOOD：批量合并（一次调用，多次修改）
const patch = {};
this.data.list.forEach((it, i) => { if (it.dirty) patch[`list[${i}].checked`] = true; });
this.setData(patch);
// BAD：循环内多次 setData（N 次跨线程通信）
// for (const [i, it] of list.entries()) this.setData({ [`list[${i}].x`]: it.x });
// 数组追加：只传新增段
this.setData({ [`list[${this.data.list.length}]`]: newItem });
```
