---
title: [R19-015] React 的合成事件机制 SyntheticEvent？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-015：React 的合成事件机制 SyntheticEvent？
**答**：
- React 把原生事件封装成 SyntheticEvent，抹平浏览器差异，提供 stopPropagation、preventDefault 等统一接口。
- React 17 起事件统一委托绑定到 root 容器上（之前是 document），多个 React 版本共存时不再冲突。
- 想访问原生事件对象用 `e.nativeEvent`；事件处理函数中的 this 不存在，函数组件天然无此问题。
- 合成事件的 stopPropagation 只能阻止 React 合成事件流的传播，极端场景要配合原生监听理解。

```jsx
function EventDemo() {
  const handleClick = (e) => {
    // e 是 SyntheticEvent，跨浏览器行为一致
    e.stopPropagation();
    // 需要原生对象时通过 nativeEvent 获取
    console.log(e.nativeEvent.type, e.target, e.currentTarget);
  };

  // 事件实际委托到 root 容器，不是每个按钮都挂监听
  return <button onClick={handleClick}>点我</button>;
}
```

---

## 第三章 Hooks 全家桶（R19-016 ~ R19-030）
