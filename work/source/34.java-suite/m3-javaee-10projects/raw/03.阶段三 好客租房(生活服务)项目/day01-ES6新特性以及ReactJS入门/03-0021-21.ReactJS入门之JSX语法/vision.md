# 画面线理解：21.ReactJS入门之JSX语法

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\21.ReactJS入门之JSX语法【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:20, 01:27, 01:30, 01:45, 01:47, 01:53, 02:00, 02:04, 02:46, 03:01, 03:12, 03:57, 04:00, 04:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:11:01

1) 这一组画面整体在讲什么（一句话）：
演示在 React 项目中编写 JSX 语法时，因未正确包裹多个相邻元素而导致编译失败，并展示如何修正错误。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 IntelliJ IDEA 中，编辑器显示 `HelloWorld.js` 文件，内容为 `export default () => { return <div>hello world</div>; }`，终端显示 webpack 编译成功。
画面2：浏览器显示 `localhost:8000/HelloWorld` 页面，内容为“hello world”。
画面3：编辑器中光标在 `return <div>hello world</div>;` 行，终端显示编译成功。
画面4：浏览器页面内容仍为“hello world”。
画面5：浏览器显示编译失败，错误信息为：`SyntaxError: ./src/pages/HelloWorld.js: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX Fragment?`。
画面6：编辑器中光标在 `return` 后，显示自动补全建议，包括 `const`, `static`, `class` 等。
画面7：浏览器显示编译失败，错误信息与画面5相同。
画面8：编辑器中修改代码为 `return <div><div>hello</div> <div>world</div></div>;`，终端显示编译成功。
画面9：编辑器中光标在 `return` 后，代码为 `return <div><div>hello</div> <div>world</div></div>;`。
画面10：编辑器中光标在 `return` 后，代码为 `return <div><div>hello</div> <div>world</div></div>;`，终端显示编译成功。
画面11：编辑器中光标在 `return` 后，显示自动补全建议，包括 `extends`, `class`, `constructor` 等。
画面12：编辑器中修改代码为 `const t = () => "黑马程序员"; return <div><div>hello</div> <div>world {!t()}</div></div>;`，终端显示编译成功。
画面13：编辑器中光标在 `return` 后，代码为 `return <div><div>hello</div> <div>world {!t()}</div></div>;`，终端显示编译中。
画面14：显示 Typora 中的 PPT 页面，标题为“2.4. React快速入门”，子标题“2.4.1. JSX语法”，并包含 JSX 语法说明和示例代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```javascript
export default () => {
  return <div>hello world</div>;
}
```

画面5：
```text
./src/pages/HelloWorld.js
Module build failed (from ./node_modules/babel-loader/lib/index.js):
SyntaxError: ./src/itcast-reactjs/src/pages/HelloWorld.js: Adjacent JSX elements must be wrapped in an enclosing tag. Did you want a JSX Fragment
```

画面8：
```javascript
export default () => {
  return <div><div>hello</div> <div>world</div></div>;
}
```

画面12：
```javascript
const t = () => "黑马程序员";
return (
  <div>
    <div>hello</div>
    <div>world {!t()}</div>
  </div>
);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14：
PPT标题：2.4. React快速入门
子标题：2.4.1. JSX语法
内容：
- JSX语法：JSX语法是嵌入HTML片段，是React自创的一种语法。
- 使用JSX语法，需要2点注意：
  1. 所有的HTML标签必须是闭合的，如：`<div>hello world</div>` //正常
  2. 在JSX语法中，只能有一个根标签，不能有多个。
- 代码示例：
  ```javascript
  function getName(user) {
    if (user) {
      return <div>Hello, {formatName(user)}!</div>;
    }
    return <div>Hello, stranger.</div>;
  }
  ```
- 2.4.2. 组件：
  - 组件是React中最重要的概念，一个网页，可以被拆分成一个或多个组件，像这样：
    - 传输数据
    - 北京中心站
    - 传输数据可以是：用户、数据、消息等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
