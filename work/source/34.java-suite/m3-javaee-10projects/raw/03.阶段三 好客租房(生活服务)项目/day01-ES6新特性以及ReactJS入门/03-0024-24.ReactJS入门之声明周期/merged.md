# 24.ReactJS入门之声明周期

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\24.ReactJS入门之声明周期【海量资源尽在 ubkz.com】.mp4
- 时长 2分54秒（音频 174s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下生命周期函数啊那么组件呢在运行的过程中啊存在不同的阶段那么每一个阶段呢它都会提供了一个钩子函数其实也叫这种回调函数啊有点像这种回调函数那么云起开发者呢是定义每个阶段的执行的一些函数这些函数统称为叫什么呢生命周期方法或者叫生命周期函数啊
[00:29] 好那么下面我们来看一下整个生命周期包括有什么有开始这个阶段有运行中的这个阶段然后呢有这个卸载或者说结束这个阶段啊那么它在每一个这个阶段呢都会有一些这个对应的一些方法那么比如像这个属性的更新啊就会调用这个方法去做更新那么我们下面给大家演示一下啊就好了那么把这个呢我们拷过来把这个代码拷过来那我们测试一下
[01:00] 那么丢到这个里面来那么这个里面呢显示的都是一些我们的这个生命周期的一些方法包括你看像这个呢是我们的构造方法然后呢这个呢方法呢是在组件挂载之后呢去调用然后这个是组件去进行这个移除之前呢去调用然后呢这个是组件在更新之后呢去调用啊等等那么还有这个方法它呢是
[01:26] 每当这个res.properties和stages有变化的时候在render方法之前呢就会调用这个方法哎呀ok然后呢这个是我们render方法最后呢我们做一个app export去导出好那么下面我们来访问一下来访问一下那么可以看一下嗯没有吗我们来哎啊呃注意啊注意这个位置当我刚刚考过来之后啊
[01:56] 他把它定义成是一个加尔文件了这个是有点问题的我们给他去重命名一下改成一个什么的点什么的解释文件好嘞然后呢我们刷新一下是不是可以看到我们的这个三明治周期的这个页面了当我们在执行的时候可以看到在控制台呢是不是有这样的一个输出那么也就是说这两个方法是不是在我们的执行的run之前是不是就已经做了这个执行
[02:26] 那么这个呢大家呢先对它有一个初步的一个认识就可以了在我们后面在写我们的功能的时候也会涉及到一些相关的一些方法的使用啊那么大家对它有一个基本的认识啊就可以了好那么这个知识点呢我们就先讲到这里后面我们在用的过程中我们再去做一个这个强调啊好嘞好那么关于这个生命周期这个函数呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 React 组件生命周期方法（lifecycle methods）及其在组件挂载、更新和卸载阶段的调用时机，并通过代码示例演示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 React 生命周期流程图，包含“开始”、“getDefaultProps”、“getInitialState”、“componentWillMount”、“render”、“componentDidMount”、“运行中”、“shouldComponentUpdate”、“componentWillReceiveProps”、“componentDidUpdate”、“componentWillUnmount”、“卸载”等节点，以及它们之间的调用关系。
画面 2: 与画面 1 相同，但鼠标悬停在“render”节点上，强调其在生命周期中的位置。
画面 3: 展示了 React 生命周期示例代码，包含 `import React from 'React';`、`class LifeCycle extends React.Component {`、`constructor(props) { super(props); console.log("constructor()"); }`、`componentDidMount() { console.log("componentDidMount ()"); }`、`componentWillUnmount() { console.log("componentWillUnmount()"); }`、`componentDidUpdate() { console.log("componentDidUpdate ()"); }`、`shouldComponentUpdate(nextProps, nextState) { console.log("shouldComponentUpdate ()"); }`、`render() { return <div><h1>React Life Cycle!</h1></div>; }`、`export default LifeCycle;`。
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
import React from 'React'; //第一步，导入React
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

