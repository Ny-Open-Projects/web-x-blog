---
title: [MFW-502] Flight 序列化的类型边界：能过线的类型与不可序列化的替代方案
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-502：Flight 序列化的类型边界：能过线的类型与不可序列化的替代

**答**:
- 可序列化白名单：原始值、数组、普通对象、Date、Map/Set（$Q/$W 标记）、BigInt、TypedArray/ArrayBuffer（$K）、Promise（$@——流式 resolve）、React 元素（$L）、客户端组件引用（I）；**不可序列化黑名单**：函数（class 方法/任意 fn——server action 除外）、class 实例（无自定义序列化）、Symbol、循环引用中的 DOM 节点、Node 流。
- 黑名单的替代方案：函数 → Server Action（'use server' 标记生成 action id 引用）；class 实例 → 序列化为 plain object（toJSON 或手动映射）；DOM/流 → 不该出现在 props（架构问题不是序列化问题）。
- 错误的诊断体验：不可序列化类型的报错要「定位到具体属性路径」（`objects are not valid... at props.user.friends[0].greet`）——框架序列化器的错误信息质量决定开发体验（RBL-568 哲学的框架版）。
- 边界的架构意义：序列化边界 = server/client 的「通信契约」——props 类型在边界处的约束是 RSC 架构的核心纪律（类型层用 ServerComponents 类型包标注可传类型）。
- 追问钩子：为什么「函数不可序列化」反而塑造了 RSC 的架构？——函数跨不了边界 → 事件处理必须在 client 组件 → 「数据在 server、交互在 client」的组件拆分不是风格偏好而是协议约束；Server Action 是唯一的「函数跨界」通道（且是 id 引用不是真实函数）——理解序列化边界就理解了 RSC 的组件划分规则。

```javascript
// 序列化器的能力探测（自检 props 是否能过线）
function assertSerializable(value, path = 'props', seen = new Set()) {
  if (value == null || typeof value !== 'object') {
    if (typeof value === 'function' && !value.__serverAction)
      throw new Error(`${path}: 函数不可序列化——改用 Server Action 或 client 组件`);
    return;
  }
  if (seen.has(value)) return;                           // 循环引用由协议处理
  seen.add(value);
  if (value instanceof Date || value instanceof Map || value instanceof Set) return;
  if (Array.isArray(value)) return value.forEach((v, i) => assertSerializable(v, `${path}[${i}]`, seen));
  for (const [k, v] of Object.entries(value))
    assertSerializable(v, `${path}.${k}`, seen);
}
// Server Action 的跨界形态
// server: 'use server'; export async function pay(orderId) {...}
// payload: {"$$id": "action_123", ...}  —— id 引用，client 调用走 POST 端点
```
