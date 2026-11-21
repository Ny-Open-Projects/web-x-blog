---
title: [R19-172] React Compiler 时代，哪些代码能被自动优化？哪些仍要手动？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-172：React Compiler 时代，哪些代码能被自动优化？哪些仍要手动？
**答**：
- 能自动优化：符合"Rules of React"的组件——memo、useMemo、useCallback 基本可以删掉，编译器自动按值依赖做细粒度缓存。
- 会"逃出"优化的写法：渲染期间可变的外部状态（改 ref、改模块变量）、下标/随机数/Date 等不稳定输入进渲染、在渲染中写 props/state。
- 仍需手动：关键渲染路径的**结构性**优化（虚拟化、拆组件、代码分割）、事件与 effect 内的逻辑、依赖不稳定第三方库（未适配编译器的 hook 语义）。
- 落地方法：`eslint-plugin-react-compiler` 先体检存量代码，灰度开启 babel 插件，用 Profiler 对比开启前后耗时，不对全仓一次性打开。

```jsx
// compiler-audit.jsx —— React Compiler 适配性体检示例
import { useMemo, useCallback, useRef, useState } from 'react';

// 1. 可自动优化：纯渲染，编译器自动缓存 -> useMemo/useCallback 可以删
export function OrderRow({ order, onSelect }) {
  // 编译器会自动记住 filteredTotals，依赖不变不重算
  const filteredTotals = order.items
    .filter(i => i.count > 1)
    .reduce((s, i) => s + i.price * i.count, 0);
  return (
    <tr onClick={() => onSelect(order.id)}>
      <td>{order.no}</td>
      <td>{filteredTotals}</td>
    </tr>
  );
}

// 2. 违反规则：渲染期写 ref -> 编译器拒绝优化该组件
function BadMutation({ items }) {
  const cacheRef = useRef(new Map());
  for (const it of items) {
    cacheRef.current.set(it.id, it); // 渲染期间修改可变数据：改到事件或 effect
  }
  return <div>{items.length}</div>;
}

// 3. 违反规则：渲染期读取不稳定输入 -> 每次都变，缓存无效
function BadRandom() {
  const seed = Date.now();            // 放到 effect 或事件里
  return <span>{seed}</span>;
}

// 4. 仍需手动优化的场景：结构性问题编译器救不了
// - 1 万行列表 -> 虚拟化（见 R19-169）
// - 首屏包体 -> 代码分割/预加载
// - 巨型组件 -> 拆分职责
export function ManualWork({ bigList }) {
  const [query, setQuery] = useState('');
  return (
    <>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      {/* 即使 compiler 自动缓存 filter，1 万条全量渲染仍然卡：虚拟化才是解 */}
      {/* <VirtualList items={filtered} ... /> */}
    </>
  );
}

// 接入步骤：
// 1) pnpm add -D eslint-plugin-react-compiler && eslint 加 'react-compiler/react-compiler'
// 2) 修掉所有 lint 报错（violations 即无法优化点）
// 3) babel-plugin-react-compiler 灰度：目录级 enable，Profiler 对比前后 actualDuration
// 4) 全量开启后移除冗余的 useMemo/useCallback（保留少数有副作用语义依赖的）
```

## 第二十六章 React 与其他技术集成（R19-173 ~ R19-177）
