---
title: [R19-263] 双缓冲 Fiber 树在中断恢复时如何保证一致性？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-263：双缓冲 Fiber 树在中断恢复时如何保证一致性？
**答**：
- workInProgress 树：渲染中断时保留所有已完成节点的副作用标记；恢复时从「最后一个完成单元」继续，不重头算。
- current 树：始终指向已提交的稳定树，屏幕内容不受中断影响。
- 提交时交换：commit 后 workInProgress 变为 current（alternate 指针对调），双缓冲复用对象省内存。
- 中断丢弃：高优插队时低优渲染整体作废，重新从 current 开始（保证不出现半新半旧）。
- effect 清单：completedWork 向上收集 effectList，commit 阶段按清单执行，中断不重复不遗漏。
