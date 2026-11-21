---
title: [R19-181] 如何用 React 实现一个低代码渲染器？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-181：如何用 React 实现一个低代码渲染器？
**答**：
- 数据结构：页面 = 组件树 JSON（`{ type, id, props, children }`），渲染器只做一件事：**递归地把 JSON 映射为 React 元素**（`React.createElement(registry[type], props, ...children)`）。
- 双向能力：渲染（schema -> UI）+ 反解（画布选中 -> 定位 schema 节点），每个节点带稳定 id，用 id 索引做选中/拖拽/属性回填。
- 数据域设计：`$state`（页面状态）、`$item`（循环保留字）等上下文，表达式字段在渲染期求值，事件字段声明成 action 链（setState/request/navigate）。
- 安全与性能：schema 白名单组件（注册表机制天然限制）、表达式求值不用 eval（自写安全求值器），大页面按区块 memo。

```tsx
// lowcode-renderer.tsx —— 低代码渲染器核心
import { createContext, useContext, useMemo, useState } from 'react';

// ---- 1. schema 与注册表 ----
type Node = { id: string; type: string; props?: Record<string, any>; children?: Node[] };

const registry: Record<string, React.ComponentType<any>> = {
  Page: ({ children }) => <div>{children}</div>,
  Text: ({ value }) => <span>{value}</span>,
  Input: ({ value, onChange, placeholder }) => (
    <input value={value ?? ''} placeholder={placeholder} onChange={e => onChange?.(e.target.value)} />
  ),
  Button: ({ text, onClick }) => <button onClick={onClick}>{text}</button>,
  List: ({ source, children }) => (
    <ul>{(source ?? []).map((item: any, i: number) => <li key={i}>{children(item)}</li>)}</ul>
  ),
};

// ---- 2. 渲染上下文：状态域 + 事件动作解释器 ----
const RenderCtx = createContext<{
  state: Record<string, any>;
  setState: (patch: Record<string, any>) => void;
  selectedId: string | null;
  select: (id: string) => void;         // 画布选中
}>(null as any);

// 表达式求值：支持 {{ $state.x }} 语法（白名单取值，绝不用 eval）
function evalExpr(expr: string, state: Record<string, any>) {
  if (!expr.startsWith('{{')) return expr;
  const path = expr.slice(2, -2).trim().replace(/^\$state\./, '');
  return path.split('.').reduce((o, k) => o?.[k], state);
}

// ---- 3. 递归渲染器 ----
function RenderNode({ node }: { node: Node }) {
  const { state, setState, selectedId, select } = useContext(RenderCtx);
  const Comp = registry[node.type];
  if (!Comp) return <div style={{ color: 'red' }}>未知组件 {node.type}</div>;

  // props 求值：字符串表达式转实际值，事件名转动作
  const props: Record<string, any> = {};
  for (const [k, v] of Object.entries(node.props ?? {})) {
    if (k.startsWith('on') && typeof v === 'object') {
      // 动作链：[{ type: 'setState', patch: {...} }, { type: 'request', api: '...' }]
      props[k] = (event: any) => {
        for (const action of v) {
          if (action.type === 'setState') setState(evalExprProps(action.patch, state));
          if (action.type === 'navigate') location.hash = action.to;
        }
      };
    } else {
      props[k] = typeof v === 'string' ? evalExpr(v, state) : v;
    }
  }

  const isEditor = selectedId !== undefined; // 画布模式才响应选中
  return (
    <div
      onClick={isEditor ? (e) => { e.stopPropagation(); select(node.id); } : undefined}
      style={selectedId === node.id ? { outline: '2px solid #3b82f6' } : undefined}
    >
      <Comp {...props}>
        {node.children?.map(child =>
          // List 类组件通过函数 children 实现循环保留字 $item
          node.type === 'List'
            ? (item: any) => (
                <RenderCtx.Provider value={{ state: { ...state, $item: item }, setState, selectedId, select }}>
                  <RenderNode key={child.id} node={child} />
                </RenderCtx.Provider>
              )
            : <RenderNode key={child.id} node={child} />,
        )}
      </Comp>
    </div>
  );
}

function evalExprProps(patch: Record<string, any>, state: Record<string, any>) {
  return Object.fromEntries(Object.entries(patch).map(([k, v]) => [k, typeof v === 'string' ? evalExpr(v, state) : v]));
}

// ---- 4. 画布入口 ----
export function LowCodeEditor({ schema }: { schema: Node }) {
  const [state, setStateRaw] = useState<Record<string, any>>({ title: 'Hello' });
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const setState = (patch: Record<string, any>) => setStateRaw(s => ({ ...s, ...patch }));

  return (
    <RenderCtx.Provider value={{ state, setState, selectedId, select: setSelectedId }}>
      <RenderNode node={schema} />
      {/* 属性面板：按 selectedId 从 schema 反查节点，编辑 props 后回写 schema */}
    </RenderCtx.Provider>
  );
}

// 页面 schema 示例：
// { id: 'n1', type: 'Page', children: [
//   { id: 'n2', type: 'Text', props: { value: '{{$state.title}}' } },
//   { id: 'n3', type: 'Input', props: { value: '{{$state.title}}', onChange: { type: 'setState', patch: { title: '{{$event}}' } } } },
// ]}
```
