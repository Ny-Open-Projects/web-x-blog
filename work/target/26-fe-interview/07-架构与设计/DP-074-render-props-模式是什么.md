---
title: [DP-074] render props 模式是什么？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-074：render props 模式是什么？
**答**：
- render props：组件把"渲染逻辑"作为 props（常叫 `render`/`children` 函数）接收，把内部状态/能力作为参数交给它调用。
- 本质：**渲染权移交** + 逻辑注入——数据提供方不关心 UI，UI 方不关心数据来源（控制反转的组件版）。
- 经典库：react-router 的 `<Route render>`、react-motion、Formik 的 `<Formik render>`。
- 与 HOC 对比：HOC 生成新组件（静态组合），render props 在 JSX 中动态组合、嵌套多层时产生"回调地狱"（hooks 出现后多为替代）。

```jsx
// 数据提供者：只管取数，渲染交给外部
class MouseTracker extends React.Component {
  state = { x: 0, y: 0 };
  handleMove = (e) => this.setState({ x: e.clientX, y: e.clientY });
  render() {
    return (
      <div onMouseMove={this.handleMove} style={{ height: 200 }}>
        {/* 渲染权移交：内部状态作为参数传给 render prop */}
        {this.props.render(this.state)}
      </div>
    );
  }
}
// 消费方1：用同一数据源渲染完全不同的 UI
<MouseTracker render={({ x, y }) => <h1>鼠标位置 {x},{y}</h1>} />
// 消费方2：复用监听逻辑，渲染猫图
// <MouseTracker render={({ x, y }) => <Cat x={x} y={y} />} />

// children 即函数：现代写法（children as function）
const Toggle = ({ children }) => {
  const [on, setOn] = React.useState(false);
  return children({ on, toggle: () => setOn((v) => !v) });
};
// <Toggle>{({ on, toggle }) => <button onClick={toggle}>{on ? '开' : '关'}</button>}</Toggle>

// 与 hooks 的对照：useMouse() 逻辑等价，嵌套更浅 —— hooks 胜出的原因
// function useMouse() { const [pos, setPos] = useState(...); useEffect(...); return pos; }
```
