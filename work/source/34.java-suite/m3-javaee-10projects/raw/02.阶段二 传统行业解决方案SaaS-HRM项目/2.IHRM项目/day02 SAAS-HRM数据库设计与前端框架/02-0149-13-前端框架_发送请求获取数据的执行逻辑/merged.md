# 13-前端框架：发送请求获取数据的执行逻辑

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\13-前端框架：发送请求获取数据的执行逻辑_【海量资源尽在 ubkz.com】.mp4
- 时长 9分20秒（音频 560s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了我们现在通过一个请求的地址以张图形的形式咱们来看一下我们可以通过一个请求的地址定位到我们要执行的页面这个就是我们的请求地址通过这个页面路由的一个配置通过路由的配置那这个路由在哪呢是在模块目录下的router index点结当中
[00:41] 好了我们现在请求的是susclient-index那我们一起找到susclient-index-router路由配置那我们知道倒入到demo-page-indexok进入到我们的页面注意这个页面呢是一个voe视图voe视图那需要跟各位简单的来聊一下这个voe视图里面究竟有什么咱们一起来做一个分析内容
[01:28] 那VOE视图内容究竟有什么呢来打开它我们简单来看VOEindex.voe在这个VOE视图当中它其实包含这么三个方面这么三个方面那我这边呢直接就手写了好了这三个方面呢首先第一个呢我们叫做template叫template那这个template当中全部都是我们的一些HTML元素页面标签吧
[02:13] 全部都是一些HTML的一些页面标圈这是第一部分好了那除了第一部分之外还有第二部分第二部分呢叫做script就是我们要写的一些GS的一些代码那除了第二部分之外还有第三部分叫做stylestyle呢也比较好理解它是我们的一些样式表那我们重点关注的其实就是这个script的部分那这个script部分里面它又包含了这么一些内容
[02:51] 这些内容呢首先呢我就只讲重点了重要的Data那Data当中定义的都是什么呢你看我这里面也有Data这个Data当中定义的全部都是数据模型是用来做双向数据绑定其实这个双向绑定很好理解很好理解我GS数据部分如果发生变化HTML里面的内容就会跟着改如果我HTML内容发生了变化我这个数据模型它也就发生了变化
[03:32] 它们是属于一个数据双样绑定的如果在这里面你可以给一个参数比如说ABC等于1那你在页面标签里面你就可以引用一下它的一个语法两个大括号ABC那引用ABC那这回是显示的数据就变成1那如果我这个里面想方设法的把ABC变成2那页面这边就变成了2那这个就是这么一个效果那如果说页面你对这个ABC复制比如说ABC等于1 2 3
[03:58] 那我们这个模型ABC它也变成123这个就叫做数据双向绑定好了我把这些没用的都换回来好了Data部分我们做过了一个介绍那除了Data部分还有METHOD那这个METHOD里面定义的全部都是当前页面所需要用到的JS方法用的JS方法那比如说比如说看人家这个例子我也点demo是不是给我返回了一些数据啊
[04:34] 那这些数据列表它从哪来的呢就可以执行Math的方法通过Math的方法去得到我们的结果当然我们除了Math的呢还有一些比如说有一个Created那这个Created呢它也是第三部分第三部分它指的是VUE的勾子函数我这个写不下了抱歉VUE勾子函数OK拿过来VUE勾子函数
[05:10] 那解释一下这个勾子函数究竟代表的什么含义它其实指的是我们页面元素加载加载之前执行的方法这样写吧勾子函数其实指的就是我们VUE页面初始化之前执行的方法那比如说咱们可以举一个例子可以举一个例子那比如说呢当我执行到这个页面的时候
[05:49] 我里面有一个勾子函数那这个勾子函数我可以打印句话比如说console打印点点日志点log那console.log里面呢我就开始写了creative的方法执行了那接着我们可以刷新一下页面我这边打开F12刷新一些页面你发现它自动的是不是把这个creative的方法执行给我打印出来了所以这个里面指的是你页面一加载它就会帮你调用的一些内容好了
[06:27] 这个我们看过了之后那接下来我们可以试想一下试想一下那如果说我想要构造成刚才那种效果一点击这个链接跳转是不是能够跳转到我们刚才指定的这个页面呀那跳转到这个页面我是不是可以通过Credit的帮我调用Method里面的方法这个没画好通过Credit的帮我调用Method里面的方法
[07:02] 那调用Math的方法它主要作用是干什么呢我们可以通过Math的方法是不是发送一些查询当然了说的更加严谨一点我们可以通过Math的方法调用我们刚才说过的一个叫做APIAPI方法那接着在API方法之中我们刚才说过了API方法里面封装的全部都是和后台交互的一些代码好了这是我们的Java服务端后台那这样一来那这样一来
[07:41] 当我页面敲链接它会执行跳转到页面跳转到页面执行credit的方法那credit方法感测到method里面它要调用API通过API调用服务端那服务端有数据有数据是不是拿到这边了那在method当中我们接下来要做的事情怎么让它动态的把标签的内容给它改了那么可以这样是不是可以通过在method当中修改数据模型里面的值
[08:19] 那数据模型的值一旦发生了变化那是不是我们这个HTML元素里面的值它也紧接着发生变化OK这才是一个完整的我们页面动态展示的这么一个效果首先第一件事首先第一件事当我们跳转链接它根据路由的配置进入页面那进入页面执行我们的勾残数那勾残数调用method
[08:56] 那Message里面要用API请求那API请求发API方法发送请求得到数据返回那返回之后绑定到我们的数据模型上那接着我们的HBO标签里面的内容随之发生更改好了这个就是我们整个框架整个框架它的一个执行逻辑OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Vue.js 前端页面（index.Vue）如何通过 API 方法与 Java 服务端后台交互，以及其内部 data、method、created 等生命周期方法的作用和数据流向。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 HRM 系统的前端页面，URL 为 http://localhost:8080/#/saas-clients/index，页面正在加载中。
画面 2: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index。
画面 3: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”。
画面 4: 展示了 Visual Studio Code 编辑器，打开的是项目 saas-hrm-Vue-master，显示了多个窗口，包括浏览器、数据库、PowerDesigner 等工具，以及项目目录结构。
画面 5: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构：`<template>`, `<script>`, `data()`, `method()`, `created()`, `<style>`。
画面 6: 在 Visual Studio Code 中，显示了 index.Vue 文件的代码，包含 data、methods、created 等部分，其中 methods 中的 getlist 方法调用 API 获取数据，created 中调用 getlist 方法。
画面 7: 展示了多个窗口，包括浏览器、数据库、PowerDesigner 等工具，以及项目目录结构。
画面 8: 在 Visual Studio Code 中，显示了 index.Vue 文件的代码，与画面 6 类似，但光标在 created 方法中。
画面 9: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构，同时添加了“API方法”节点，并用箭头指向“Vue组件的结构”框。
画面 10: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构，同时添加了“API方法”节点和“java服务端后台”节点，并用箭头连接“API方法”指向“java服务端后台”。
画面 11: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构，同时添加了“API方法”节点和“java服务端后台”节点，并用箭头连接“API方法”指向“java服务端后台”。
画面 12: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构，同时添加了“API方法”节点和“java服务端后台”节点，并用箭头连接“API方法”指向“java服务端后台”，并添加了“双向绑定”和“修改数据模型”等注释。
画面 13: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构，同时添加了“API方法”节点和“java服务端后台”节点，并用箭头连接“API方法”指向“java服务端后台”，并添加了“双向绑定”和“修改数据模型”等注释，并在 Vue 组件结构中添加了数字标注 1、2、3、4、5、6、7、8。
画面 14: 在绘图工具中，标注了 URL http://localhost:8080/#/saas-clients/index，并添加了注释“路由的配置（模块目录下的 router/index.js）”和“demo/pages/index.Vue 视图”，并框选了 Vue 组件的结构，同时添加了“API方法”节点和“java服务端后台”节点，并用箭头连接“API方法”指向“java服务端后台”，并添加了“双向绑定”和“修改数据模型”等注释，并在 Vue 组件结构中添加了数字标注 1、2、3、4、5、6、7、8。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 6 和 8 的代码：
```javascript
dataList: [],
methods: {
  // 获取列表数据
  getList(res) {
    this.dataList = res.data.items
    console.log(this.dataList)
  },
},
// 计算属性
created() {
  //console.log('created方法执行')
  this.getList()
},
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9-14 的架构图：
- 节点1：Vue组件的结构（包含 `<template>`, `<script>`, `data()`, `method()`, `created()`, `<style>`）
- 节点2：API方法
- 节点3：java服务端后台
- 连接关系：
  - 从“API方法”指向“java服务端后台”（表示 API 方法调用 Java 服务端后台）
  - 从“Vue组件的结构”指向“API方法”（表示 Vue 组件通过 API 方法与后台交互）
  - 从“Vue组件的结构”指向“双向绑定”（表示 Vue 组件内部使用双向绑定）
  - 从“Vue组件的结构”指向“修改数据模型”（表示 Vue 组件内部可以修改数据模型）

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

