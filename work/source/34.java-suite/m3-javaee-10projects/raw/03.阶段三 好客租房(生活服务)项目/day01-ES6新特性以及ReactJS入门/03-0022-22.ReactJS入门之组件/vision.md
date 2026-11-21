# 画面线理解：22.ReactJS入门之组件

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\22.ReactJS入门之组件【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:59, 02:01, 02:49, 03:06, 03:43, 04:16, 04:52, 05:20, 06:21, 07:10, 08:06, 08:40, 09:41, 10:16
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:11:37

1) 这一组画面整体在讲什么（一句话）：
演示如何在 React 中创建和使用组件，包括定义组件、传递属性（props）和子元素（children）。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 Typora 中打开课程笔记，展示 React 入门章节目录，同时在右侧预览窗口中显示 React 官网的宣传页。
画面2：在 IntelliJ IDEA 中打开项目，展示项目结构，当前编辑的是 HelloWorld.js 文件，顶部显示 import React from 'react';。
画面3：在 HelloWorld.js 中，将光标置于 extends 关键字上，弹出类型提示，显示 React.Component 的类型信息。
画面4：在 HelloWorld.js 中，选中 export default HelloWorld; 这一行代码。
画面5：在 HelloWorld.js 中，将光标置于 render 方法内，输入 return 语句，并在其中添加 <div>我的第一个ReactJS的组件</div>。
画面6：在项目结构中右键点击 Show.js 文件，弹出上下文菜单，显示“Create File”等选项。
画面7：在 IntelliJ IDEA 中，打开 Show.js 文件，光标位于 class Show extends React.Component{ 之后，弹出类型提示，显示 React 的相关类型。
画面8：在浏览器中访问 localhost:8000/show，页面显示编译失败，错误信息为：SyntaxError: Unexpected token (8)。
画面9：在 IntelliJ IDEA 中，打开 HelloWorld.js 文件，光标位于 render 方法内，显示 <div>我的第一个ReactJS的组件</div>。
画面10：在 IntelliJ IDEA 中，打开 HelloWorld.js 文件，光标位于 render 方法内，显示 <div>我的第一个ReactJS的组件</div>。
画面11：在 IntelliJ IDEA 中，打开 Show.js 文件，编辑内容为 import React from 'react'; import HelloWorld from './HelloWorld'; class Show extends React.Component{ render() { return ( <HelloWorld name="张三"/> ); } export default Show;。
画面12：在浏览器中访问 localhost:8000/show，页面显示“我的第一个ReactJS的组件，name = 张三”，下方是一个包含多个截图的图片。
画面13：在 IntelliJ IDEA 中，打开 HelloWorld.js 文件，光标位于 render 方法内，显示 <div>我的第一个ReactJS的组件，name = {this.props.name}，内容 = {this.props.children}</div>。
画面14：在 Typora 中打开课程笔记，展示如何使用 props 传递属性，代码为：import React from 'react'; class HelloWorld extends React.Component { render() { return <div>hello world name={this.props.name} address={this.props.address}</div>; } export default HelloWorld;，并在下方的浏览器预览中显示：hello world name=张三 address=上海。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
import React from 'react';

画面3：
extends
export
exports (index.d.ts, node) any
external (lib.dom.d.ts) External
EXT_frag_depth (lib.dom.d.ts) External
executor(resolve: (value?: (PromiseLike< T> | T) | void) => void) T
expectedClass (... args: any) T
expirationTime
EXT_texture_filter_anisotropic (lib.dom.d.ts) External
ExtendableEvent (lib.webworker.d.ts) External
ExtendableMessageEvent (lib.webworker.d.ts) External

画面4：
export default HelloWorld;

画面5：
return (
<div>我的第一个ReactJS的组件</div>
);

画面6：
class Show extends React.Component{

画面7：
import React from 'react';
class Show extends React.Component{

画面8：
Failed to compile
./src/pages/Show.js
Module build failed (from ./node_modules/babel-loader/lib/index.js):
SyntaxError: F:\code\itcast-reactjs\pages\Show.js: Unexpected token (8)

画面9：
return (
<div>我的第一个ReactJS的组件</div>
);

画面10：
return (
<div>我的第一个ReactJS的组件</div>
);

画面11：
import React from 'react';
import HelloWorld from './HelloWorld';
class Show extends React.Component{
render() {
return (
<HelloWorld name="张三"/>
);
}
export default Show;

画面13：
return (
<div>我的第一个ReactJS的组件，name = {this.props.name}，内容 = {this.props.children}</div>
);

画面14：
import React from 'react'; //第一步，导入React
class HelloWorld extends React.Component { //第二步，编写并继承 React.Component
render() { //第三步，编写render()方法，用于返回页面
return <div>hello world name={this.props.name} address={this.props.address}</div>; //JSX语法
}
export default HelloWorld; //第四步，导出该类

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：PPT 标题为“12. export default Show;”，内容为“其中，name=“zhangsan”就是属性传递，shanghai就是标签内容的传递。那么，在HelloWorld.js组件中如何接收这些参数呢？对应的有两种方法：属性：this.props.name 接收；标签内容：this.props.children 接收；使用如下：”，并附带代码示例和浏览器预览。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
