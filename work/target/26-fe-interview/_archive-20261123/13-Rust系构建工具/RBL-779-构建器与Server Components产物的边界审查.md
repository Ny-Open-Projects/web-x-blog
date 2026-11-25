---
title: [RBL-779] 场景题：RSC 产物的边界审查——server/client 分离的构建期约束
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-779：场景题：RSC 产物的边界审查——server/client 分离的构建期约束

**答**:
- RSC 的 'use client' 边界是构建器的核心约束源：1) **client 边界的导出面审查**（client 组件只能从 server 侧拿到「序列化 props + 组件引用」——client 组件导出函数（非组件）/非可序列化对象给 server 使用是违规）；2) server-only 泄漏检测（server 模块被 client 图 import——数据库 SDK/密钥进入 client bundle，安全 + 体积双重事故）；3) client-only 检测（window/document 在 server 组件中直接使用）。
- 构建期检查的实现：模块图带边界注解（'use client' 声明后的闭包全是 client 图）——server-only 包（server-only npm 包的 guard 模式）或构建器按「import 链 + 注解」判定；违规的处置是构建失败（泄漏是安全事故不是警告）。
- 边界的产物影响：client bundle 只含 client 闭包（server 组件代码不进 client bundle——体积优化的本质）；server bundle 反之。两产物一致性（RBL-699 manifest 对齐）在 RSC 场景扩展为「Flight payload 的引用完整性」。
- 与 SWC 转换的配合：'use client' 指令转换（客户端引用编译成 module reference——react-server-dom 的代理协议）；构建器转换正确性靠「Flight payload 可序列化校验」（props 的类型扫描：函数/map/set 等不可序列化类型直接诊断）。
- 追问钩子：为什么「server-only 泄漏」必须构建失败而不是运行时兜底？——泄漏的代价是密钥/数据库凭据进入公开 JS（安全事件）+ bundle 体积暴涨；运行时检测（server-only 包的 throw）只在代码执行到才触发，构建期静态判定把事故消灭在 PR——安全边界的检查时机越早越好。

```javascript
// RSC 边界审查
function auditRSCBoundary(graph) {
  const problems = [];
  for (const mod of graph.modules()) {
    if (mod.isClient) {
      // client 闭包内引用 server-only 标记模块
      for (const dep of mod.deps) {
        if (graph.get(dep)?.serverOnly)
          problems.push({ code: 'RBL6101', mod: mod.id, detail: `client 模块引用 server-only: ${dep}` });
        if (graph.get(dep)?.hasSecret)
          problems.push({ code: 'RBL6102', mod: mod.id, detail: `疑似密钥依赖进 client bundle: ${dep}` });
      }
      // 不可序列化 props（导出的组件签名扫描）
      for (const prop of mod.serializableCheck?.badProps ?? [])
        problems.push({ code: 'RBL6103', mod: mod.id, detail: `client 组件 props 含不可序列化类型: ${prop}` });
    } else if (mod.usesBrowserGlobal && !mod.hasGuard) {
      problems.push({ code: 'RBL6104', mod: mod.id, detail: 'server 组件直接使用浏览器全局' });
    }
  }
  return problems;   // 非空 = 构建失败（泄漏是安全事故）
}
```
