# 21.ReactJS入门之JSX语法

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\21.ReactJS入门之JSX语法【海量资源尽在 ubkz.com】.mp4
- 时长 4分31秒（音频 271s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下React的快速入门的第一个内容啊就是叫GSX语法那么这个语法呢在前面呢我们也简单的提了一嘴啊就是我们可以在JS文件中呢去插入html片段这个呢是React自创的一种语法那么这种语法呢会被我们的一些转码工具啊进行转码得到正常的一个节制代码再做一个执行
[00:27] 那么使用这个JSX这种语法需要注意两点第一个就是所有的HTML标签必须有闭合那么如果是没有闭合它会报错比如说你这种情况是OK的但是你不可以写成这样只有开头这个标签没有结束这个标签是不可以的
[00:49] 那么第一种第二的是在JSX语法中只能有一个根标签不能有多个比如说你可以这样去写是OK的但是你要写多个这个标签这是不可以的那么你外面可以再加一个DIV把它包裹起来就是说只能有一个根标签OK那么如果在JSX语法中想要插入我们的JS脚本那么就需要通过一个大括号
[01:16] 来做一个插入啊那么接下来我们来做一个演示啊做一个演示就是说我们可以看到啊当你呢如果在这个位置去呃写我们这个hello world他是没有任何问题对不对没有任何问题那么如果呢你要这么样去写我们来看一下那么hello然后呢再来一个什么呢div然后再来一个divdiv然后呢写一个word好来看一下
[01:46] 显然是会报错的这是不可以的那么如果我们在外面再给它去更一个什么的标签再更一个标签什么的DIV然后往大走那么可以看到它是可以的这个大家明白了吗好那么接着我们继续往下面看那么但是大家可以看到在我们编写代码的时候我们编译器是不是一直会报错对不对
[02:14] 大家的这个idea他是比较聪明的他呢会看到说哎你这种写法他是不是使用的是React的JSX呢如果说是的话我们点一个space做一个切换走一切换呢哎他就认为哎你这种写法他是OK的啊他是对的好那么这样的话我们就减少了这个编译啊这样的一个报错啊好那么这个时候我们讲这个语法啊
[02:41] 当然了那么我们这种写法他只是说你只能有一行这个代码当我们有多行的时候你要怎么做呢在这个里面注意添加的不是大括号是小括号累腾什么呢把内容写到这个里面来OK这个大家能够理解吗来刷新看一下效果依然是没有任何问题的是OK的那么前面我们说过如果在这个html代码中我们想要插入节制代码怎么办呢你得通过什么呢
[03:10] 通过一个大括号大括号来去拿一个插入一个解释的一个代码那么这个怎么插入呢我们做这样的一个演示假设呢我在上面这个位置呢我去定义了有一个函数定了函数这个函数的名字呢就叫t等于什么呢没有参数那么然后呢去返回一个什么呢我随便写啊返回一个比如说就叫itcast或者叫什么呢
[03:40] 黑马程序员黑马程序员好那么我这样的话我是不是就我在这个位置是定义了一个函数对不对这个函数我是不是可以在下面的这个我们的JSX这个中的去插入我这个函数怎么样插入呢有一个大括号一对大括号突然作为一个T小括号是不是就去执行我这个函数
[04:01] 好来看一下效果可以看到已经看到效果了是不是Hello World的黑马程序员OK这个大家能够理解了吗就是我们讲的就是说在htm这个标签中要想插入JS脚本你要通过一个大括号是不是来做一个脚本的一个插入OK好那么我们这个呢就是所讲的JSX这种语法这种语法的用起来还是也是比较简单的OK那么关于这个JSX语法呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

