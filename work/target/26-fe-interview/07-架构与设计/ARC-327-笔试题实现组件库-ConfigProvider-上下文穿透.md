---
title: [ARC-327] 笔试题：实现组件库 ConfigProvider 上下文穿透？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-327：笔试题：实现组件库 ConfigProvider 上下文穿透？
**答**：实现嵌套可合并的 `ConfigProvider`：1) 子 Provider 继承父配置并局部覆盖；2) 支持配置读取 hook（含默认值）；3) Portal 渲染的内容也能拿到配置（Portal 不脱离 React 树，但要求说明 createPortal 上下文特性）；4) 性能：配置变化只重渲染消费组件。
**评分点**：
- 合并逻辑正确（读父 context 再覆盖本次传入字段）。
- useConfig 默认值兜底正确。
- 能说明 createPortal 保留 React 上下文（context 沿 React 树而非 DOM 树传递），DOM 外层不影响。
- value 用 useMemo 稳定引用，防止整树重渲染。
```tsx
const ConfigCtx = createContext({});
function ConfigProvider({ size, locale, theme, children }) {
  const parent = useContext(ConfigCtx);
  const value = useMemo(() => ({                   // 4) 引用稳定
    ...parent,                                     // 1) 继承
    ...(size !== undefined && { size }),
    ...(locale !== undefined && { locale }),
    ...(theme !== undefined && { theme }),
  }), [parent, size, locale, theme]);
  return <ConfigCtx.Provider value={value}>{children}</ConfigCtx.Provider>;
}
function useConfig() {
  return { size: 'md', locale: zhCN, ...useContext(ConfigCtx) };  // 2) 默认兜底
}
// 3) Portal：createPortal 渲染的子树仍在 React 元素树中，context 正常透传（与 DOM 位置无关）
// 场景：<ConfigProvider size="lg"><Modal/></ConfigProvider> —— Modal 内容在 body 下的 portal 里依然拿到 size=lg
```
