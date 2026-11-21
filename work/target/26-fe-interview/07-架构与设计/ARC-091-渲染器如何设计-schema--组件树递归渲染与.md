---
title: [ARC-091] 渲染器如何设计（schema → 组件树递归渲染与性能）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-091：渲染器如何设计（schema → 组件树递归渲染与性能）？
**答**：
- 递归渲染 schema 节点：查物料注册表 → 解析 props（含表达式绑定）→ 递归渲染 children。
- 性能要点：大节点树用 memo + 稳定 key；表达式求值结果缓存；虚拟滚动接入容器类物料；避免每次渲染重建组件（物料查表结果缓存）。
- 安全要点：表达式沙箱执行（受限求值器，不用 new Function 直接暴露全局），props 白名单透传。

```tsx
// 运行时渲染器：schema → React 树
const registry = new Map<string, ComponentType<any>>(materials);

function renderNode(node: SchemaNode, scope: Scope): ReactNode {
  const Material = registry.get(node.componentName);
  if (!Material) return dev ? <MissingNode name={node.componentName} /> : null;   // 容错：坏物料不白屏
  const props = evaluateProps(node.props, scope);         // 表达式沙箱求值：state.user.name
  const children = node.children?.map((c, i) =>
    <Fragment key={c.id ?? i}>{renderNode(c, scope)}</Fragment>) ?? node.text;
  return <Material {...props}>{children}</Material>;
}

export function Renderer({ schema, state }: { schema: SchemaNode; state: Record<string, unknown> }) {
  const scope = useMemo(() => createScope(state), [state]);
  return <ErrorBoundary fallback={<RenderCrash />}>{renderNode(schema, scope)}</ErrorBoundary>;
}
// 性能：物料查表结果用 Map 缓存（registry 本身即缓存）；表达式求值按 (expr, scopeVersion) memo
// 编辑态复用：Editor 在 renderNode 外包 DndContext 与 SelectionMask，渲染核心完全一致
```
