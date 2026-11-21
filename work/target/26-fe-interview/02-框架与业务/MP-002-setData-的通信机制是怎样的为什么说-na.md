---
title: [MP-002] setData 的通信机制是怎样的？为什么说 native 层是中转站？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-002：setData 的通信机制是怎样的？为什么说 native 层是中转站？
**答**：
- 逻辑层 `setData(data)` → 数据被**序列化**为字符串 → 传给 native 层 → native 转发给对应页面的渲染层 WebView → 渲染层反序列化，与 WXML 编译出的虚拟树做 diff，再应用到真实 DOM。
- 一次 setData 至少经历 **逻辑层→native→渲染层两次跨线程通信 + 两次序列化**，因此数据量与调用频率都直接决定耗时。
- 渲染层到逻辑层的事件（tap、input）同样经 native 中转，方向相反。
- 所以优化方向永远是：**少调、小数据、路径更新**（详见 MP-016）。

```javascript
// setData 的数据会被完整序列化后跨线程传输
this.setData({
  'list[2].status': 'done',        // 推荐：路径更新，只传变化字段
  user: this.data.user,            // 不推荐：大对象全量传输，双倍序列化开销
  _cache: bigComputedObject        // 更不推荐：不参与渲染的数据纯属浪费
})
```
