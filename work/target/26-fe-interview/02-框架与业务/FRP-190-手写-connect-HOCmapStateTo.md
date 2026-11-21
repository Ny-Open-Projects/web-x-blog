---
title: [FRP-190] 手写 connect HOC：mapStateToProps 的订阅与浅比较怎么实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-190：手写 connect HOC：mapStateToProps 的订阅与浅比较怎么实现？

**答**：
- connect 是"订阅 + 注入"的高阶组件：内部订阅 store（componentDidMount 时机），mapStateToProps 计算出 props 对象，与已有 props **浅比较**决定要不要 setState 触发子组件重渲。
- 浅比较是性能核心：合并后的 props（own + stateProps + dispatchProps）任一引用变了才重渲——子 reducer 保持引用（FRP-189）是浅比较生效的前提。
- 绑定时机与脏检查：订阅在 mount 建立、unmount 移除；每次 store 变化都跑 mapStateToProps 但只有结果不同才渲染——"多算一次不渲染"换正确性。
- React-Redux 8+ 内核换成 useSyncExternalStore，但"mapState 计算 + 浅比较门控"的策略不变。

```javascript
// 简化实现，帮助理解 connect
function connect(mapStateToProps, mapDispatchToProps) {
  return function wrap(WrappedComponent) {
    return class Connect extends React.Component {
      state = { mergedProps: null };

      static getDerivedStateFromProps(nextProps, prevState) {
        // 计算 stateProps（首次与每次 render 前）
        const stateProps = mapStateToProps
          ? mapStateToProps(store.getState(), nextProps)
          : {};
        const dispatchProps = mapDispatchToProps
          ? bindActionCreators(mapDispatchToProps, store.dispatch)
          : { dispatch: store.dispatch };
        const merged = { ...nextProps, ...stateProps, ...dispatchProps };
        // 浅比较：全等（含引用级）才跳过渲染
        if (shallowEqual(prevState.mergedProps, merged)) return null;
        return { mergedProps: merged };
      }

      componentDidMount() {
        this.unsubscribe = store.subscribe(() => {
          // store 变化：重算并浅比较 —— 相同则不 setState
          const stateProps = mapStateToProps?.(store.getState(), this.props) ?? {};
          const merged = { ...this.props, ...stateProps, ...this.dispatchProps };
          if (!shallowEqual(this.state.mergedProps, merged)) {
            this.setState({ mergedProps: merged });   // 有变化才渲染
          }
        });
      }
      componentWillUnmount() { this.unsubscribe?.(); }

      render() {
        return <WrappedComponent {...this.state.mergedProps} />;
      }
    };
  };
}

function shallowEqual(a, b) {
  if (Object.is(a, b)) return true;
  const keysA = Object.keys(a), keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;
  return keysA.every(k => Object.is(a[k], b[k]));   // 只比较一层引用
}

function bindActionCreators(creators, dispatch) {
  return Object.fromEntries(
    Object.entries(creators).map(([k, c]) => [k, (...args) => dispatch(c(...args))])
  );
}

// 用法：
// const TodoList = connect(
//   (state) => ({ todos: state.todos.items }),   // 选择器：订阅的"依赖面"
//   { toggleTodo }                                // action creator 自动绑定
// )(TodoListComp);
// 性能前提：state.todos.items 在无关 dispatch 时保持同一引用 —— 子 reducer 引用不变（combineReducers）
```
