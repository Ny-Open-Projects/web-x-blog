---
title: [DP-207] 源码识别：Vue 指令系统与 React HOC 中的装饰器模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-207：源码识别：Vue 指令系统与 React HOC 中的装饰器模式？
**答**：
- Vue 指令（v-loading/v-perm）：对元素能力的**动态附加**——mounted 添加遮罩/监听，unmounted 清理，不改变组件本体，是装饰器（withAssign 的生命周期版）。
- React HOC：`withAuth(Component)` 返回包装组件，props 透传 + 能力附加，纯组件树装饰器；强调"HOC 是组合不是继承"。
- 装饰 vs 继承：指令/HOC/组件包裹（ErrorBoundary）都是"功能叠加但不侵入"，识别标志是**原组件代码零改动**。
- 组合链问题：多个 HOC 叠加（compose(withTheme, withAuth, withData)(Comp)）的执行顺序要能推理——外层先执行生命周期。

```tsx
// Vue 指令：元素级装饰器
const vLoading = {
  mounted(el, { value }) {
    if (value) el.appendChild(createMask(el));   // 附加能力
  },
  updated(el, { value }) { toggleMask(el, value); },
  unmounted(el) { removeMask(el); },             // 卸载清理 = 装饰可逆
};
// React HOC：组件级装饰器
function withAuth(Comp) {
  return function Wrapped(props) {
    const { perms, loading } = useAuth();
    if (loading) return <Skeleton/>;
    return <Comp {...props} perms={perms}/>;     // props 透传 + 能力注入
  };
}
const Enhanced = compose(withTheme, withAuth)(Table);   // 装饰链，外层（withTheme）先 mount
```
