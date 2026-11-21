---
title: [R19-006] use API 读取 Context 与 useContext 的区别？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-006：use API 读取 Context 与 useContext 的区别？
**答**：
- `use(Context)` 同样能读 Context，但不受 Hook 规则限制，可以出现在条件语句和循环之后。
- useContext 必须在函数组件顶层调用；use 是通用消费接口，还能读 Promise 或自定义 thenable。
- 混合使用时注意：读 Context 的分支必须在调用之前判断清楚，保持逻辑可预测。
- 这让"条件性订阅 Context"这类需求第一次有了官方写法。

```jsx
import { use, createContext } from 'react';

const ThemeContext = createContext('light');

function Toolbar({ needsTheme }) {
  // use 可以放在条件分支里，useContext 做不到
  if (needsTheme) {
    const theme = use(ThemeContext);
    return <button className={theme}>主题按钮</button>;
  }
  return <button>普通按钮</button>;
}
```
