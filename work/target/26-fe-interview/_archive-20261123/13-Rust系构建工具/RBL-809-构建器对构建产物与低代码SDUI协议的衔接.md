---
title: [RBL-809] 场景题：SDUI（服务端驱动 UI）的产物衔接——协议版本与降级渲染的构建配合
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-809：场景题：SDUI（服务端驱动 UI）的产物衔接——协议版本与降级渲染

**答**:
- SDUI（服务端下发 UI 描述 JSON，客户端解释渲染）与构建器的衔接点：1) **组件注册表**（客户端支持的组件类型清单 = 产物的一部分——服务端下发的组件类型必须 ⊆ 客户端注册表，否则静默不渲染）；2) 协议版本协商（server 协议版本 vs client 支持——版本落差时降级渲染）；3) 组件懒注册（低频组件按需动态 import，RBL-612 虚拟模块承载注册表）。
- 构建器的契约校验：SDUI 协议 schema（组件类型/属性集合）与客户端注册表的双向 diff——服务端新版本用了新组件而客户端未更新 → 构建期暴露（协议测试而非线上白屏）；「注册表覆盖度报告」是客户端发版依据。
- 降级渲染的产物层：未知组件类型的 fallback 渲染器（占位/文本摘要）必须内置于核心 chunk（不可懒加载——降级路径不能依赖网络）；fallback 的能力边界（不执行未知行为，防协议注入）。
- 版本策略：客户端注册表版本随产物发布（semver），服务端按客户端版本下发兼容协议（能力协商）——构建器输出「协议兼容矩阵」供服务端路由。
- 追问钩子：为什么 SDUI 的 fallback 渲染器不能懒加载？——fallback 的触发场景是「服务端下发了客户端不认识的组件」，此时客户端的产物版本是旧的/落后的——依赖懒加载等于依赖「网络可达 + 服务端不下发」，降级路径必须零依赖；「降级路径零依赖」是容错设计的通用原则。

```javascript
// SDUI 注册表构建
export const registry = {
  banner: () => import('./components/banner'),          // 懒注册
  button: lazy(() => import('./components/button')),
};
const KNOWN = Object.keys(registry);                     // 构建器抽取 -> 协议兼容矩阵

// 契约校验（构建期）
function auditSDUI(schema, registry) {
  const known = new Set(Object.keys(registry));
  const serverTypes = schema.components.map(c => c.type);
  const unknown = serverTypes.filter(t => !known.has(t));
  if (unknown.length)
    fail(`SDUI 协议使用未注册组件: ${unknown}——客户端升级或服务端降级`);
  const unused = [...known].filter(k => !serverTypes.includes(k));
  return { unused };                                     // 覆盖度报告
}
// 降级渲染（核心 chunk 内置）
export function renderFallback(node) {
  return { type: 'placeholder', text: node.text ?? `[${node.type}]`, safe: true };  // 只取安全字段
}
```
