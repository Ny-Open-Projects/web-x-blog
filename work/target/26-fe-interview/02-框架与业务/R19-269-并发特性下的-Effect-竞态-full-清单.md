---
title: [R19-269] 并发特性下 useEffect 的竞态问题清单与系统性解法？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-269：并发特性下 useEffect 的竞态问题清单与解法？
**答**：
- 问题清单：StrictMode 双执行（副作用跑两次）、组件可被渲染但更新未提交、并发中断后 effect 依赖已变、async effect 旧请求覆盖新请求、卸载后 setState。
- 解法：请求竞态用 seq/AbortController；副作用幂等；卸载清理 cleanup 完整；数据请求迁到 Suspense 数据层（effect-free）；同步 DOM 副作用用 useLayoutEffect 且考虑可中断性。
- StrictMode 是「故意暴露非幂等」的工具：开发期双跑暴露问题，生产单跑。
- 架构级解法：能用 Server 组件/Action 解决的不要进客户端 effect——减少 effect 本身就是解药。
- 检查工具：React Compiler 也能静态识别部分竞态模式。
