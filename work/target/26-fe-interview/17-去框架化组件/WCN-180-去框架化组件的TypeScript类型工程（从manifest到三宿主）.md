---
title: [WCN-180] 去框架化组件的 TypeScript 类型工程：一套实现如何生成三宿主的完整类型？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-180：去框架化组件的 TypeScript 类型工程：一套实现如何生成三宿主的完整类型？

**答**：
- 源头：组件实现用 TS 严格类型（attribute 解析器 + property getter/setter 类型化），构建时生成 custom-elements.json（lit-analyzer / cem 插件从 JSDoc/TS 提取）。
- 生成器消费 manifest：React → JSX.IntrinsicElements 扩展（attribute + 事件 props `onXxx: (e: CustomEvent<Detail>) => void`）；Vue → GlobalComponents；原生 → HTMLElement 派生接口声明（供 bind:this 类型）。
- 事件 detail 类型治理：`@fires { CustomEvent<{value:number}> } acme-change` 注释驱动生成；detail 类型单独导出（宿主可 import）。
- 类型测试：tsd/expect-type 断言生成类型的形状（防止生成器回归）；双宿主 demo 项目的 tsc 全量编译进 CI。
- 版本联动：类型包与 core 同步发版（同 monorepo changeset），避免类型漂移。

```ts
// 生成的类型（React 侧示意，来自 manifest）
declare module 'react' {
  namespace JSX {
    interface IntrinsicElements {
      'acme-search': React.DetailedHTMLProps<React.HTMLAttributes<HTMLElement> & {
        placeholder?: string; debounce?: number;
        onSearchInput?: (e: CustomEvent<{ value: string; seq: number }>) => void;
      }, HTMLElement>;
    }
  }
}
// 宿主：<acme-search placeholder="搜索" onSearchInput={(e) => e.detail.value} />  // 全类型安全
```
