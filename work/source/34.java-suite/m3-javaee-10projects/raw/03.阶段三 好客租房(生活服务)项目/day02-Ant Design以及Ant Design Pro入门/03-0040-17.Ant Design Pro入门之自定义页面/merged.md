# 17.Ant Design Pro入门之自定义页面

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\17.Ant Design Pro入门之自定义页面【海量资源尽在 ubkz.com】.mp4
- 时长 2分33秒（音频 153s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下刚刚呢我们是已经完成了这个自定义这个菜单的一个编写对吧那么下面我们来看一下我们该如何在这个pro这个项目中啊添加我们的一个自定义的一个页面啊就是我们自己的一个页面啊怎么样去添加那么我们来看一下所有的这个页面呢依然还是保存在这个pages下面所以呢我们
[00:25] 还是以功能为单元去创建一个目录比如说我们现在写的是一个new这个功能所以我们需要在这个pages这个下面我们来创建一个new这个目录new注意这个n我们采用大写为什么大写呢你可以看到它之前的是不是都是这个以大写开头的那么所以我们也跟它保持一样的风格然后咱们写这个new这个目录然后接下来我们再
[00:54] 这个new这个文件夹上面呢我们去创建一些相关的一些这个文件比如说有个叫做new一个analysis就是我们的一个分析页面对吧那么我们就写一个它那么其实可以看到这呢就是一个我们普通的一个React的一个组件对吧好然后呢我们来看一下修改一下我们这个路由的一个配置啊那么我们可以看到第一个
[01:22] 这个是不是就是一个new下面的underlayer那么它所对应的我们的component并不是despot下面它而应该是什么new这个目录new这个目录下面的什么是不是这个new underlayer是前面给它加一个什么加一个new好这个大家能够理解吗是不是我们通过这样的一个方式就可以去读取到我们这个新的一个页面了
[01:49] 好来看一下效果其实效果是不是已经刷了出来了那么我们在这点击这个new的监控监控页就是这样的一个效果当我们点击这个new分析页的时候是不是可以看到我们刚刚自定义的一个页面已经显示到这个位置来了那么我们学会了这个添加一个新的页面那么我们后面是不是就可以在这个里面去编写自己的一些业务逻辑了
[02:11] 对不对OK好那么这一个小节呢它的一个目的呢就是要告诉我们如何在这个项目中去新增一个页面对吧然后有了这个知识之后呢我们后面就可以去修改或者说去创建我们自己的这个页面来实现我们自己的一些业务功能了好那么关于这个新增页面呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Ant Design Pro 项目中创建并配置一个新的分析页面（NewAnalysis），包括修改路由配置和创建对应的 React 组件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Ant Design Pro 管理后台的“New 分析页”页面，包含销售趋势图表和门店销售排行等数据。
画面 2: 在 IntelliJ IDEA 中打开 `src/config/router.config.js` 文件，显示路由配置，其中 `/new/analysis` 路由指向 `./Dashboard/Analysis`。
画面 3: 在项目结构中右键点击 `pages` 目录，准备创建新文件。
画面 4: 在项目结构中选中 `New` 文件夹，准备在其中创建新文件。
画面 5: 弹出“New JavaScript file”对话框，文件名设为 `NewAnalysis.js`。
画面 6: 创建并打开 `NewAnalysis.js` 文件，内容为一个简单的 React 组件，返回一个包含组件名的 div。
画面 7: 在 Typora 文档中，显示创建 `NewAnalysis.js` 文件的步骤和修改路由配置的代码片段。
画面 8: 在 `router.config.js` 文件中，高亮显示 `/new/analysis` 路由的配置，其 `component` 属性指向 `./Dashboard/Analysis`。
画面 9: 在浏览器中访问 `localhost:8000/new/analysis`，页面显示空白，但导航菜单中“New 分析页”被选中。
画面 10: 在浏览器中，点击导航菜单中的“New 监控页”，页面内容未更新。
画面 11: 在 IntelliJ IDEA 中，选中 `NewAnalysis.js` 文件，显示其内容。
画面 12: 在 Typora 文档中，显示修改路由配置的代码片段，其中 `component` 属性被修改为 `'/New/NewAnalysis'`。
画面 13: 在 Typora 文档中，显示在浏览器中访问 `localhost:8000/new/analysis` 后，页面标题显示为 “NewAnalysis”，并说明新页面已创建并添加到菜单中。
画面 14: 在 Typora 文档中，显示项目结构，`NewAnalysis.js` 文件位于 `pages/New` 目录下。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```javascript
Routes: ['src/pages/Authorized'],
authority: ['admin', 'user'],
routes: [
  {
    path: '/',
    redirect: '/dashboard/analysis'
  },
  // NEW
  {
    path: '/new',
    name: 'new',
    icon: 'user',
    routes: [
      {
        path: '/new/analysis',
        name: 'analysis',
        component: './Dashboard/Analysis',
      },
      {
        path: '/new/monitor',
        name: 'monitor',
        component: './Dashboard/Monitor',
      },
      {
        path: '/new/workplace',
        name: 'workplace',
        component: './Dashboard/Workplace',
      },
    ],
  },
]
```

画面 6:
```javascript
import React from 'React';

class NewAnalysis extends React.Component {
  render() {
    return (
      <div>NewAnalysis</div>
    );
  }
}

export default NewAnalysis;
```

画面 7:
```javascript
// 修改路由中的路径：
// new
{
  path: '/new',
  name: 'new',
  icon: 'user',
  routes: [
    {
      path: '/new/analysis',
      name: 'analysis',
      component: './New/NewAnalysis',
    },
  ],
}
```

画面 8:
```javascript
{
  path: '/new/analysis',
  name: 'analysis',
  component: './Dashboard/Analysis',
}
```

画面 12:
```javascript
{
  path: '/new/analysis',
  name: 'analysis',
  component: './New/NewAnalysis',
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 7: PPT 标题为“3.2.4. pro中的model执行流程”，内容为“在pro系统中，model是按顺序执行的。下面我们以表格为例，探究下在pro中的执行流程。”
画面 13: PPT 标题为“测试：”，内容为“可以看到，一个新的页面就创建好了，并且已经加入到菜单中。”
画面 14: PPT 标题为“创建文件 NewAnalysis.js：”，内容为“在 `pages/New` 目录下创建 `NewAnalysis.js` 文件。”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

