---
title: [DP-120] HOC、Hook、render props 三种复用方式如何做迁移决策？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-120：HOC、Hook、render props 三种复用方式如何做迁移决策？（高频）
**答**：
- 判定表：复用"无 UI 的行为"（订阅、取数）→ Hook；需要在渲染时暴露内部状态给调用方自由画 UI → render props / children as function；包裹增强已有组件且无法改其内部（第三方组件）→ HOC。
- 新代码优先 Hook；HOC 的嵌套地狱与 props 冲突是主要债务，老 HOC 可改为"返回 Hook 的工厂"渐进迁移。
- 组合而非互斥：Headless 组件内部用 Hook 管状态、用 render props/children 暴露 UI（DP-122）。

```jsx
// 方式1 HOC：增强无法修改的第三方组件（唯一适合的场景）
const withTheme = (Comp) => (props) => {
  const theme = useContext(ThemeCtx);
  return <Comp {...props} theme={theme} />;
};
const ThemedCard = withTheme(ThirdPartyCard);
// 方式2 Hook：行为复用的默认答案
function useOnline() {
  const [online, setOnline] = useState(navigator.onLine);
  useEffect(() => {
    const on = () => setOnline(true), off = () => setOnline(false);
    window.addEventListener('online', on); window.addEventListener('offline', off);
    return () => { window.removeEventListener('online', on); window.removeEventListener('offline', off); };
  }, []);
  return online;
}
function StatusDot() { const online = useOnline(); return <span>{online ? '在线' : '离线'}</span>; }
// 方式3 render props：调用方决定 UI 形态
function Online({ children }) { return children(useOnline()); }
<Online>{(online) => <Banner text={online ? '同步已开启' : '离线中，稍后重试'} />}</Online>
// 迁移决策：行为且 UI 自由 → Hook/render props；只能从外部包第三方 → HOC
```
