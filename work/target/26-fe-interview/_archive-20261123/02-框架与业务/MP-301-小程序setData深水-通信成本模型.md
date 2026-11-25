---
title: [MP-301] setData 深水：通信成本模型与优化
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## MP-301：setData 深水：通信成本模型与优化

**答**：
- 成本模型：setData = 逻辑层数据序列化 → 跨线程传输 → 渲染层 diff → DOM 更新——高频/大 payload 是两大成本源；单次 data 建议 <256KB、频率 <1s 一次
- 序列化成本：对象会被 JSON 化（含函数/Symbol 丢失）——大数组整包 set 一次传几十 KB 是典型反模式；改用「路径更新」：`this.setData({ 'list[12].status': 'done' })`
- 高频更新合并：滚动/输入场景（60fps 的 setData）——在逻辑层合帧（rAF 不可用，用 throttle 16ms 窗口）+ 只传变化字段
- 渲染层 diff 语义： setData 是「全量数据 + 精确路径」——路径更新让渲染层只 diff 那个节点；嵌套对象直接换引用会让整棵子树 diff
- 深水点：setData 回调（下一次通信完成）——「连续 setData」的时序感知，避免以未完成的数据做下一步判断

```javascript
// 反模式: 整包更新
this.setData({ list: this.data.list });            // 全量传输
// 正解: 路径更新 + 合帧
let pending = null;
function scheduleUpdate(patch) {
  pending = { ...pending, ...patch };
  if (pending.__t) return;
  pending.__t = setTimeout(() => {
    const { __t, ...patchData } = pending;
    pending = null;
    this.setData(patchData, () => this.measure());
  }, 16);
}
this.setData({ 'list[12].status': 'done', [`list[${i}].price`]: 9.9 });  // 路径语法
```
