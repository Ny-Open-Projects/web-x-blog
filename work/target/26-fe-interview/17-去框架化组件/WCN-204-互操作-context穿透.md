---
title: [WCN-204] React Context/Vue provide 无法穿透 Shadow DOM，跨边界共享状态的正确姿势？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-204：React Context/Vue provide 无法穿透 Shadow DOM，跨边界共享状态的正确姿势？
**答**：
- 正确姿势：通过 property 传「状态句柄/store 引用」进元素，元素内部订阅更新。
- 不要用 DOM 全局事件总线做状态传播（时序不可控、难调试）。
- CSS 变量可以穿透（继承），设计 token 走这条通道；逻辑状态不走。
- 复杂场景提供「宿主适配包」：React 组件封装 property 传递 + 订阅同步。

```javascript
// 适配包模式：Context → property 订阅
function GoodsCardR({ store, sku }: any) {
  const ref = useRef<any>(null);
  useEffect(() => { ref.current.store = store; }, [store]);   // 传句柄，元素内部订阅
  return <goods-card ref={ref} sku={sku} />;
}
// 元素内：this.store.subscribe(() => this._render())
r
```
