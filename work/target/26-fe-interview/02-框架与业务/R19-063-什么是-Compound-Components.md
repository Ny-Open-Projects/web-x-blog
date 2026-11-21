---
title: [R19-063] 什么是 Compound Components 组合组件模式？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-063：什么是 Compound Components 组合组件模式？
**答**：
- 父组件与多个子组件共用一个 Context：父持有状态，子（如 Accordion.Item）通过 useContext 消费，调用方自由编排 JSX 结构。
- 通过 `Accordion.Item = Item` 静态属性挂载，让 API 自文档化。
- 优点：调用方不接触内部状态管理，结构又完全可控；Ant Design 的 Collapse、Radix 的多数组件都是这个模式。
- 关键细节：子组件挂静态属性要在导出前完成，并用 displayName 便于 DevTools 识别。

```jsx
import { createContext, useContext, useState } from 'react';

const AccordionContext = createContext(null);

export function Accordion({ children, defaultIndex = 0 }) {
  const [openIndex, setOpenIndex] = useState(defaultIndex);
  return (
    <AccordionContext.Provider value={{ openIndex, setOpenIndex }}>
      <div className="accordion">{children}</div>
    </AccordionContext.Provider>
  );
}

Accordion.Item = function Item({ index, header, children }) {
  const { openIndex, setOpenIndex } = useContext(AccordionContext);
  const open = openIndex === index;
  return (
    <div className="accordion-item">
      <button aria-expanded={open} onClick={() => setOpenIndex(open ? -1 : index)}>
        {header}
      </button>
      {open && <div className="accordion-panel">{children}</div>}
    </div>
  );
};

// 用法：结构完全由调用方编排，状态由 Accordion 统一管理
// <Accordion>
//   <Accordion.Item index={0} header="标题一">内容一</Accordion.Item>
//   <Accordion.Item index={1} header="标题二">内容二</Accordion.Item>
// </Accordion>
```
