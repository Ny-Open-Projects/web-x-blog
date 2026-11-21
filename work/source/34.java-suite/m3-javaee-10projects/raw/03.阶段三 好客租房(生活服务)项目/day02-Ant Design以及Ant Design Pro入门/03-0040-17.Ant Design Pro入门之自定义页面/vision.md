# 画面线理解：17.Ant Design Pro入门之自定义页面

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\17.Ant Design Pro入门之自定义页面【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:32, 00:39, 00:58, 01:03, 01:07, 01:14, 01:22, 01:52, 01:58, 02:09, 02:13, 02:16, 02:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:23:35

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
import React from 'react';

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
