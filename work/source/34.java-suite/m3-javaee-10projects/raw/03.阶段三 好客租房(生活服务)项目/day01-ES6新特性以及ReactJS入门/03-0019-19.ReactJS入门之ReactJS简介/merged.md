# 19.ReactJS入门之ReactJS简介

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\19.ReactJS入门之ReactJS简介【海量资源尽在 ubkz.com】.mp4
- 时长 4分20秒（音频 260s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下reactjs的简介啊那么我们首先来看一下它的官网官网呢是这个reactjs.org啊好那我们来看一下打开来看一下这个呢就是它的官网那么在这个官网我们可以看到整个网站的一个风格呢还是比较现代的这样的一种风格啊还是比较看起来比较清爽一点的啊
[00:25] 那么在这个位置呢有一句话其实就说明了React这个框架它是做什么的来看一下它呢其实就是一个java script的一个内库或者说一个框架然后呢去干嘛呢for build your interface就是去用于构建用户这样的一个用户界面这样的一个java script的一个库好
[00:52] 那么它是Facebook所开发的这样一个JS的一个框架那么ReactJS呢它的一个核心思想是什么呢我们一起来看一下它是把复杂的一种页面然后呢拆分成一个一个的组件然后呢将这些组件呢一个一个的拼装起来就会呈现多样的一个页面
[01:16] 那么React-js呢,这可以用于mvc的这种架构也可以用于mvvm的架构或者是一些别的一些架构所以说呢这个React-js呢它的用处还是比较多的啊好,那么下面我们来看一下在React-js中一些圈内的一些这个框架啊大家可能会看到的一些框架我们简单的来做一些这个了解那么首先第一个呢是flux那么这个是什么意思呢这个是
[01:46] Facebook建立这种用户建立客户端web应用程序的前端的一个框架那么它呢其实是一个利用了一个什么呢单向的数据流单向的一个数据流然后呢去补充了React的组件视图的这样的一个组件
[02:06] 那么这更是一种模式非框架大家简单对它有个了解就可以了那么还有一个叫ReduxRedux是叫JavaScript的一个状态的容器这个我们其实会接触到但是我们并不会直接去使用它并不会直接使用它而是我们会通过一些分装之后去使用它一会我们再去介绍这个
[02:33] 那么提供了可预测化的状态的管理那么Redux可以让DX的组件的状态共享注意在这提了一个词是要共享共享变得简单OK好那么第三个就是叫什么的AntDesignOf
[02:52] 那么这个框架是什么呢这个框架是阿里的一个框架它开源的一个基于什么呢React的一个企业级后台的一个产品那么它集成了多种框jar 包括我们上面所提到的这两框架它都包含了那么大家猜的没错它将会作为我们这套课程中所直接去使用的一个React的一个框架
[03:20] 那么我们先学的是reactjs的入门那么在学完之后到后面的课程中我们就会学习这个end design它的一个使用包括还有个叫end design pro那么也是一个这样的产品那么end design它提供了丰富的组件注意在前面我们提到reactjs是不是就把一个复杂的页面拆成一个一个的组件那么end design它也提供了丰富的组件
[03:48] 那么我们通过这个组件的就可以去开发出各种各样的页面那么这些组件的有什么有什么按钮表单表格布局等等等等组件非常非常多那么足以支撑我们去开发一个非常功能丰富的一个我们后台系统的一个页面啊哎OK好那么关于这个reactjs的简介呢我们就学到这里那么下面呢我们就会去搭建它的环境我们就正式的来学习reactjs
[04:18] 好那就先到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
介绍 ReactJS 的核心概念、组件化开发方式以及其在前端开发中的应用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 React 官网首页，介绍其核心特性：声明式、组件化、一次学习多处使用。
画面 2: 同画面 1，鼠标指针移动到“Take the Tutorial”链接。
画面 3: 展示 React 官网的“一个简单组件”示例，包含 JSX 代码和运行结果。
画面 4: 展示 React 官网的“一个有状态的组件”示例，包含计时器代码和运行结果。
画面 5: 展示 Typora 编辑器中的 ReactJS 课程 PPT，标题为“2.2、ReactJS简介”，内容介绍 React 是一个用于构建用户界面的 JavaScript 库。
画面 6: 同画面 5，鼠标指针在“ReactJS简介”段落中。
画面 7: 同画面 5，鼠标指针在“ReactJS简介”段落中。
画面 8: 同画面 5，鼠标指针在“2.3、搭建环境”标题下，显示课程目录结构。
画面 9: 同画面 5，鼠标指针在“React”标题上。
画面 10: 同画面 5，鼠标指针在“ReactJS简介”段落中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```jsx
class HelloMessage extends React.Component {
  render() {
    return (
      <div>
        Hello {this.props.name}
      </div>
    );
  }
}

ReactDOM.render(
  <HelloMessage name="Taylor" />,
  document.getElementById('mountNode')
);
```

画面 4:
```jsx
class Timer extends React.Component {
  constructor(props) {
    super(props);
    this.state = { seconds: 0 };
  }

  tick() {
    this.setState(state => ({
      seconds: state.seconds + 1
    }));
  }

  componentDidMount() {
    this.interval = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  render() {
    return (
      <div>
        Seconds: {this.state.seconds}
      </div>
    );
  }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5:
标题：2.2、ReactJS简介
内容：
- 官方一句话简单的话，道出了什么是ReactJS，就是一个用于构建用户界面的JavaScript框架，是Facebook开发的一款JS框架。
- ReactJS把复杂的页面，拆分成一个个的组件，将这些组件一个个的拼接起来，就会呈现多样化的页面。ReactJS可以用于 MVC 架构，也可以用于 MVVM 架构，或者别的架构。
- ReactJS 内的一些框架简介：
  - Flux
    - Flux是Facebook用户建立客户端Web应用的前端架构，它通过利用一个单向的数据流补充了React的组合视图组件，这更是一种模式而非框架。
  - Redux
    - Redux是JavaScript 状态容器，提供可预测化的状态管理。Redux可以让React组件状态共享变得简单。
  - Ant Design of React
    - 对于开源的基于React的企业级产品，其中集成了很多框架，包含了上面提到的Flux、Redux。
    - Ant Design提供了丰富的组件，包括：按钮、表单、菜单、布局、分页、树形组件、日期等。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

