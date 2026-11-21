---
title: [FRP-129] 一次"父更新导致子更新"的完整链路是怎样的（props 如何传递）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-129：一次"父更新导致子更新"的完整链路是怎样的（props 如何传递）？

**答**：
- 父的 render effect 触发 → 父重新 render 出新 vnode 树 → patch 旧子树：遇到**同类型组件 vnode** 走 `updateComponent` 路径而不是 remount。
- `shouldUpdateComponent(n1, n2)` 决定要不要让孩子重渲：有 patchFlag 时按位判断（动态 props 才触发）、否则全量对比 props/children——这是编译优化在组件更新上的落地。
- 真正的职责切分（高频考点）：**父只负责把新 props 写进 `instance.props`（updateProps）**，然后触发子自己的 render effect——子的重渲染是"子的响应式副作用"，父从不替子 render。
- updateProps 里逐 key 比对新旧 props：变化的 key trigger 对应依赖（所以子模板里只依赖 `props.a` 时，改 `props.b` 不触发子更新）。

```javascript
// 简化实现，帮助理解父子更新的完整链路
function updateComponent(n1, n2) {
  const instance = n1.component;
  n2.component = instance;
  const { props: prevProps } = n1;

  // 1. 父的职责：计算 props 差异
  if (shouldUpdateComponent(n1, n2)) {
    const propsChanged = updateProps(instance, prevProps, n2.props);
    if (propsChanged) {
      instance.vnode = n2;
      // 2. 触发子自己的渲染 effect（不是在这里替子 render！）
      queueJob(instance.update);   // 子更新同样进批处理队列
    }
  } else {
    // 不需要子更新：仅同步 vnode 引用（保持 el/props 最新即可）
    instance.vnode = n2;
  }
}

function updateProps(instance, prev, next) {
  let changed = false;
  // 3. 逐 key 比较：只 trigger 真正变化的 key
  for (const key in next) {
    if (next[key] !== prev[key]) {
      instance.props[key] = next[key];   // props 是浅 reactive：set 内部 trigger
      changed = true;
    }
  }
  for (const key in prev) {
    if (!(key in next)) { delete instance.props[key]; changed = true; trigger(key, 'delete'); }
  }
  return changed;
}

// shouldUpdateComponent：有编译信息就走快速路径
function shouldUpdateComponent(n1, n2) {
  const { patchFlag, props } = n2;
  if (patchFlag > 0) {
    if (patchFlag & 8 /* PROPS */) {
      // 只检查动态 props key 是否变化（编译器写入 dynamicProps 列表）
      const dynamicProps = n2.dynamicProps;
      if (dynamicProps) {
        return dynamicProps.some(k => n1.props[k] !== props[k]);
      }
    }
    return true;
  }
  // 无编译信息：全量比较
  return JSON.stringify(n1.props) !== JSON.stringify(n2.props);
}

// 验证"改 props.b 不触发只依赖 props.a 的子组件"：
// instance.props 是 shallowReactive + 模板 effect 只 track 'a' —— props.b 赋值时依赖集为空
```
