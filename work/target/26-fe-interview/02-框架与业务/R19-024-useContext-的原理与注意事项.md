---
title: [R19-024] useContext 的原理与注意事项？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-024：useContext 的原理与注意事项？
**答**：
- 原理：Provider 把 value 放进对应 Context 的 Fiber 节点，useContext 沿 Fiber 树向上查找最近的 Provider 读取。
- value 引用变化时，所有消费该 Context 的组件全部重渲染，不管是否用到变化的字段。
- value 直接写对象字面量会导致每次渲染都是新引用，触发全量消费者更新，需 useMemo 包裹。
- 适合低频更新的全局数据：主题、语言、当前登录用户；高频状态选专门的状态库。

```jsx
import { createContext, useContext, useMemo, useState } from 'react';

const LangContext = createContext(null);

function Child() {
  const { lang, setLang } = useContext(LangContext);
  return (
    <>
      <p>当前语言 {lang}</p>
      <button onClick={() => setLang(lang === 'zh' ? 'en' : 'zh')}>切换</button>
    </>
  );
}

export default function App() {
  const [lang, setLang] = useState('zh');
  // value 用 useMemo 稳定引用，避免无意义的全量更新
  const value = useMemo(() => ({ lang, setLang }), [lang]);

  return (
    <LangContext.Provider value={value}>
      <Child />
    </LangContext.Provider>
  );
}
```
