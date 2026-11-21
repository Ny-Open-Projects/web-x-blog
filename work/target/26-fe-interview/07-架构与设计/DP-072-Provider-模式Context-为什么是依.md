---
title: [DP-072] Provider 模式：Context 为什么是"依赖注入 + 中介"？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-072：Provider 模式：Context 为什么是"依赖注入 + 中介"？
**答**：
- Provider 在组件树顶层"注入"依赖（主题、store、locale），深层组件直接消费——避免逐层透传 props（prop drilling）。
- 依赖注入视角：组件不自己创建依赖，由祖先注入（对照构造器注入）；可测试（测试时换 Provider 的 value）。
- 中介/观察者视角：value 变化由 React 调度系统通知所有 consumer——Provider 是变更的广播源。
- 注意：value 引用不稳定会导致全体 consumer 重渲染——需 useMemo 或拆分 Context。

```jsx
// 依赖注入 + 中介：Context 的双面
const ThemeContext = React.createContext(null); // 注入容器

function ThemeProvider({ children }) {
  const [theme, setTheme] = React.useState('light');
  // value 必须稳定引用，否则消费方全量重渲染
  const value = React.useMemo(() => ({ theme, toggle: () => setTheme((t) => (t === 'light' ? 'dark' : 'light')) }), [theme]);
  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}
// 深层组件：不关心依赖从哪来（DI），只声明"我要什么"
function ThemedButton() {
  const { theme, toggle } = React.useContext(ThemeContext);
  return <button className={`btn-${theme}`} onClick={toggle}>{theme} 主题</button>;
}
// 测试时替换依赖：换一个 Provider value 即可（DI 的可测性）
function App() {
  return (
    <ThemeProvider>
      <header><ThemedButton /></header>
      <main><ThemedButton /></main>  {/* 无需逐层传 props */}
    </ThemeProvider>
  );
}
// 对照 NestJS 风格的 DI：@Injectable() + 构造器注入，本质同样是"容器创建依赖、消费方声明需求"
// React Context 是运行时注入；NestJS 容器是启动时解析注入
```
