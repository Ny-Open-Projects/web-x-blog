# 画面线理解：24.ReactJS入门之声明周期

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\24.ReactJS入门之声明周期【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 00:42, 00:52, 00:59, 01:10, 01:23, 01:36, 01:48, 02:02, 02:20, 02:29, 02:36, 02:41, 02:45
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:13:06

1) 这一组画面整体在讲什么（一句话）：
讲解 React 组件生命周期方法（lifecycle methods）及其在组件挂载、更新和卸载阶段的调用时机，并通过代码示例演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 React 生命周期流程图，包含“开始”、“getDefaultProps”、“getInitialState”、“componentWillMount”、“render”、“componentDidMount”、“运行中”、“shouldComponentUpdate”、“componentWillReceiveProps”、“componentDidUpdate”、“componentWillUnmount”、“卸载”等节点，以及它们之间的调用关系。
画面 2: 与画面 1 相同，但鼠标悬停在“render”节点上，强调其在生命周期中的位置。
画面 3: 展示了 React 生命周期示例代码，包含 `import React from 'react';`、`class LifeCycle extends React.Component {`、`constructor(props) { super(props); console.log("constructor()"); }`、`componentDidMount() { console.log("componentDidMount ()"); }`、`componentWillUnmount() { console.log("componentWillUnmount()"); }`、`componentDidUpdate() { console.log("componentDidUpdate ()"); }`、`shouldComponentUpdate(nextProps, nextState) { console.log("shouldComponentUpdate ()"); }`、`render() { return <div><h1>React Life Cycle!</h1></div>; }`、`export default LifeCycle;`。
画面 4: 展示了浏览器控制台，显示了 `window` 对象和 `this.state` 的信息，但未显示任何 React 生命周期方法的调用日志。
画面 5: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，与画面 3 的代码相同。
画面 6: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，高亮了 `componentDidUpdate` 方法的注释和日志语句。
画面 7: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，高亮了 `render` 方法的返回值。
画面 8: 展示了浏览器中的 404 页面，提示创建 React 组件，但未显示任何 React 生命周期方法的调用日志。
画面 9: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，高亮了 `componentDidMount` 方法的注释和日志语句。
画面 10: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，高亮了 `componentWillMount` 方法的注释和日志语句。
画面 11: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，高亮了 `constructor` 方法的注释和日志语句。
画面 12: 展示了 IntelliJ IDEA 中的 React 生命周期示例代码，高亮了 `componentWillUnmount` 方法的注释和日志语句。
画面 13: 展示了浏览器中显示“React Life Cycle!”的页面，控制台中显示了 `constructor()` 和 `componentDidMount()` 的日志。
画面 14: 展示了 React 生命周期流程图，与画面 1 相同，但鼠标悬停在“开始”节点上。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```javascript
import React from 'react'; //第一步，导入React
class LifeCycle extends React.Component {
    constructor(props) {
        super(props);
        //构造方法
        console.log("constructor()");
    }
    componentDidMount() {
        //组件挂载后调用
        console.log("componentDidMount ()");
    }
    componentWillUnmount() {
        //在组件从 DOM 中移除之前立刻被调用。
        console.log("componentWillUnmount()");
    }
    componentDidUpdate() {
        //在组件完成更新后立即调用。在初始化时不会被调用。
        console.log("componentDidUpdate ()");
    }
    shouldComponentUpdate(nextProps, nextState) {
        //每当this.props或this.state有变化，在render方法执行之前，就会调用这个方法。
        //该方法返回一个布尔值，表示是否应该继续执行render方法。即如果返回false，UI 就不会
        //组件挂载时，render方法的第一次执行，不会调用这个方法。
        console.log("shouldComponentUpdate ()");
    }
    render() {
        return (
            <div>
                <h1>React Life Cycle!</h1>
            </div>
        );
    }
}
export default LifeCycle;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1 和 14: 流程图结构如下：
- “开始” → “getDefaultProps”
- “getDefaultProps” → “getInitialState”
- “getInitialState” → “componentWillMount”
- “componentWillMount” → “render”
- “render” → “componentDidMount”
- “componentDidMount” → “运行中”
- “运行中” → “shouldComponentUpdate”
- “shouldComponentUpdate” → “true” → “componentWillReceiveProps”
- “componentWillReceiveProps” → “componentDidUpdate”
- “componentDidUpdate” → “componentWillUnmount”
- “componentWillUnmount” → “卸载”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
