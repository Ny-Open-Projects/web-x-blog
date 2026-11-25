---
title: [OPT-088] React 19 编译器（React Compiler）能替代手动优化吗？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-088：React 19 编译器（React Compiler）能替代手动优化吗？

**答**：
- React Compiler 在构建期分析组件，自动插入等价于 useMemo/useCallback/React.memo 的记忆化，官方结论是**绝大多数手写 memo 可以删**。
- 能替代：props/JSX 层面的机械记忆化（写错的 useCallback、漏包的 useMemo 这类"体力优化"）。
- 不能替代：**架构层面的范围控制**——状态下沉、selector 订阅、虚拟列表、切片调度、拆分 Provider 这些"少做事"的设计优化。
- 落地建议：新项目开启编译器 + 保留 eslint-plugin-react-compiler 检查违规写法（如渲染期改可变数据）；存量项目按页面灰度开启，用 Profiler 对比后逐步下线手动 memo。

```jsx
// 一一对应：编译器开启配置与"删得掉/删不掉"的优化清单
// babel.config.js / vite.config.js
// import babel from '@babel/core';
export const plugins = [
  ['babel-plugin-react-compiler', {
    // 灰度开关：按目录启用，出问题可快速回退
    sources: (filename) => filename.includes('src/pages'),
  }],
];
// package.json: "babel-plugin-react-compiler": "^19"（RC 版本随 React 19 发布线）

// 编译器能替代的手动代码（直接删）：
function ProductCard({ item, onSelect }) {
  // 以下全部可删：编译器自动记忆化 props 引用与 JSX
  const priceLabel = useMemo(() => formatPrice(item.price), [item.price]);
  const handleSelect = useCallback(() => onSelect(item.id), [item, onSelect]);
  return <div onClick={handleSelect}>{item.name} {priceLabel}</div>;
}

// 编译器不能替代的优化（保留）：
// 1. 状态下沉/上提——组件范围划分是设计问题
// 2. selector 订阅——store 订阅粒度是数据层设计（见 OPT-083）
// 3. 虚拟列表——减少渲染数量本身
// 4. 防抖/节流/useTransition——控制更新频率与优先级
function OptimizedSearch() {
  const [query, setQuery] = useDeferredValue('');
  return <FilterList query={query} />; // 编译器只保证这里不浪费，不保证这里少算
}

// 检查工具：npx eslint --rule '{"react-compiler/react-compiler": "error"}'
// 违规示例（编译器无法记忆化的写法，必须人工修）：
// function Bad({ list }) { list.sort((a, b) => a - b); return <div>{list.length}</div>; }
// 渲染期修改可变数据 -> 检查器报错 -> 改为 useMemo(() => [...list].sort(), [list])
```

## 十五、框架专项：Vue
