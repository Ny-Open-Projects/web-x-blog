---
title: [TS-116] 如何用 as const 让映射配置对象反推枚举与映射类型？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-116：如何用 as const 让映射配置对象反推枚举与映射类型？
**答**：
- `as const` 把配置对象冻结成字面量类型，`keyof typeof` 得到状态联合，`typeof` 得到配置类型。
- 配置的值（文案、颜色、图标）有明确的字面量类型，映射使用处天然类型安全。
- 这是"配置即类型"最常用的模式：新增一个状态只需要改配置对象，所有类型自动跟着变。

```typescript
const STATUS_CONFIG = {
  pending:  { text: "待支付",  color: "#999" },
  paid:     { text: "已支付",  color: "#0a0" },
  closed:   { text: "已关闭",  color: "#f00" },
} as const;

type Status = keyof typeof STATUS_CONFIG;            // "pending" | "paid" | "closed"
type StatusText = (typeof STATUS_CONFIG)[Status]["text"]; // "待支付" | "已支付" | "已关闭"
type StatusMeta = typeof STATUS_CONFIG[Status];      // { text: ...; color: ... } 联合

function renderStatus(s: Status) {
  const meta = STATUS_CONFIG[s]; // 自动收敛到对应配置
  return { label: meta.text, style: { color: meta.color } };
}

renderStatus("paid");   // OK
// renderStatus("refunding"); // 报错：不在配置内
```
