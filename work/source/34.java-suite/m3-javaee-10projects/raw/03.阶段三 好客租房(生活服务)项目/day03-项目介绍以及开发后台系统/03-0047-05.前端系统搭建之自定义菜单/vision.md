# 画面线理解：05.前端系统搭建之自定义菜单

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\05.前端系统搭建之自定义菜单【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:43, 01:05, 01:15, 01:30, 01:40, 02:21, 02:34, 02:59, 03:11, 03:41, 03:58, 04:26, 04:52
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:28:05

1) 这一组画面整体在讲什么（一句话）：
演示一个房屋租赁管理系统前端路由配置，重点展示如何通过修改路由配置文件使系统默认进入房源管理页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示房屋租赁管理系统前端界面，当前页面为“看房请求”列表页。
画面2：展示系统后台管理界面，当前选中“合约管理”菜单。
画面3：在IntelliJ IDEA中打开路由配置文件router.config.js，显示用户模块的路由配置。
画面4：在router.config.js中，展示房源管理模块的路由配置，包含“/house/resource”、“/house/addResource”、“/house/kanfang”和“/house/zufang”四个子路由。
画面5：在router.config.js中，展示房东管理模块的路由配置，包含“/fangdong/list”子路由。
画面6：在IntelliJ IDEA中展示项目目录结构，选中router.config.js文件。
画面7：在IntelliJ IDEA中，选中router.config.js文件中的“/house”路由块。
画面8：再次展示房屋租赁管理系统前端界面，当前页面为“看房请求”列表页。
画面9：在浏览器地址栏输入“localhost:8000”，并显示自动补全的系统路径。
画面10：在IntelliJ IDEA中，展示router.config.js文件，选中“/house”路由块。
画面11：展示房屋租赁管理系统前端的“分析页”（Dashboard/analysis），包含销售数据、访问量、转化率等统计图表。
画面12：展示房屋租赁管理系统前端的“分析页”（Dashboard/analysis），页面保持不变。
画面13：在Typora中打开Markdown文档，展示“2.2.1. 数据结构”章节，其中包含前端代码目录结构图。
画面14：在Typora中展示“2.2.1. 数据结构”章节，图示说明进入系统后默认打开房源管理页面，并高亮显示路由配置中“/house/resource”路径。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
export default {
  /user
  path: '/user',
  component: '../layouts/UserLayout',
  routes: [
    { path: '/user', redirect: '/user/login' },
    { path: '/user/login', component: './User/Login' },
    { path: '/user/register', component: './User/Register' },
    { path: '/user/register-result', component: './User/RegisterResult' },
  ],
  /app
  path: '/',
  component: '../layouts/BasicLayout',
  Routes: ['src/pages/Authorized'],
  authority: ['admin', 'user'],
  routes: [
    { path: '/', redirect: '/dashboard/analysis' },
    { // 房源管理
      path: '/house',
      name: 'house',
      icon: 'home',
      routes: [
        { path: '/house/resource', name: 'resource', component: './haoke/House/Resource' },
        { path: '/house/addResource', name: 'addResource', component: './haoke/House/AddResource' },
        { path: '/house/kanfang', name: 'kanfang', component: './haoke/House/KanFang' },
        { path: '/house/zufang', name: 'zufang', component: './haoke/House/ZuFang' }
      ]
    },
    { // 房东管理
      path: '/fangdong',
      name: 'fangdong',
      icon: 'key',
      routes: [
        { path: '/fangdong/list', name: 'list', component: './haoke/FangDong/List' }
      ]
    },
    { // 用户管理
      path: '/users',
      name: 'users',
      icon: 'user',
      routes: [
        { path: '/users/list', name: 'list', component: './haoke/Users/List' }
      ]
    },
    { // 合约管理
      path: '/contract',
      name: 'contract',
      icon: 'file',
      routes: [
        { path: '/contract/list', name: 'list', component: './haoke/Contract/List' }
      ]
    }
  ]
}

画面4：
{
  // 房源管理
  path: '/house',
  name: 'house',
  icon: 'home',
  routes: [
    { path: '/house/resource', name: 'resource', component: './haoke/House/Resource' },
    { path: '/house/addResource', name: 'addResource', component: './haoke/House/AddResource' },
    { path: '/house/kanfang', name: 'kanfang', component: './haoke/House/KanFang' },
    { path: '/house/zufang', name: 'zufang', component: './haoke/House/ZuFang' }
  ]
}

画面5：
{
  // 房东管理
  path: '/fangdong',
  name: 'fangdong',
  icon: 'key',
  routes: [
    { path: '/fangdong/list', name: 'list', component: './haoke/FangDong/List' }
  ]
}

画面6：
{
  // 房源管理
  path: '/house',
  name: 'house',
  icon: 'home',
  routes: [
    { path: '/house/resource', name: 'resource', component: './haoke/House/Resource' },
    { path: '/house/addResource', name: 'addResource', component: './haoke/House/AddResource' },
    { path: '/house/kanfang', name: 'kanfang', component: './haoke/House/KanFang' },
    { path: '/house/zufang', name: 'zufang', component: './haoke/House/ZuFang' }
  ]
}

画面7：
{
  // 房源管理
  path: '/house',
  name: 'house',
  icon: 'home',
  routes: [
    { path: '/house/resource', name: 'resource', component: './haoke/House/Resource' },
    { path: '/house/addResource', name: 'addResource', component: './haoke/House/AddResource' },
    { path: '/house/kanfang', name: 'kanfang', component: './haoke/House/KanFang' },
    { path: '/house/zufang', name: 'zufang', component: './haoke/House/ZuFang' }
  ]
}

画面10：
{
  // 房源管理
  path: '/house',
  name: 'house',
  icon: 'home',
  routes: [
    { path: '/house/resource', name: 'resource', component: './haoke/House/Resource' },
    { path: '/house/addResource', name: 'addResource', component: './haoke/House/AddResource' },
    { path: '/house/kanfang', name: 'kanfang', component: './haoke/House/KanFang' },
    { path: '/house/zufang', name: 'zufang', component: './haoke/House/ZuFang' }
  ]
}

画面13：
在src/pages目录下创建haoke文件夹，项目中的页面代码将在此目录中：
```
src
├── assets
├── components
├── e2e
├── layouts
├── locales
├── pages
│   ├── haoke
│   │   ├── AddResource.js
│   │   ├── KanFang.js
│   │   ├── Resource.js
│   │   ├── ZuFang.js
│   │   └── index.js
│   └── index.js
└── utils
```

画面14：
// app
{
  path: '/',
  component: '../layouts/BasicLayout',
  Routes: ['src/pages/Authorized'],
  authority: ['admin', 'user'],
  routes: [
    { path: '/', redirect: '/house/resource' },
    { // 房源管理
      path: '/house',
      name: 'house',
      icon: 'home',
      routes: [
        { path: '/house/resource', name: 'resource', component: './haoke/House/Resource' },
        { path: '/house/addResource', name: 'addResource', component: './haoke/House/AddResource' },
        { path: '/house/kanfang', name: 'kanfang', component: './haoke/House/KanFang' },
        { path: '/house/zufang', name: 'zufang', component: './haoke/House/ZuFang' }
      ]
    }
  ]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面13：PPT标题为“2.2.1. 数据结构”，内容包含前端代码目录结构图。
画面14：PPT标题为“2.2.1. 数据结构”，内容包含前端代码目录结构图，并用红色箭头标注“修改：进入系统后，就打开房源管理页面”，并高亮显示路由配置中“/house/resource”路径。

5) 不要评价画面美观，不要输出与课程无关
