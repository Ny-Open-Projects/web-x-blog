# 05.前端系统搭建之自定义菜单

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day03-项目介绍以及开发后台系统
- 源文件：03.阶段三 好客租房(生活服务)项目\day03-项目介绍以及开发后台系统\05.前端系统搭建之自定义菜单【海量资源尽在 ubkz.com】.mp4
- 时长 4分57秒（音频 297s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢我们来看一下编写左侧的这个菜单那么我们根据需求呢去修改左侧的一个菜单那么我们来先看一下效果啊当然了这个效果呢或者说这个菜单呢我已经都写好了对吧但是呢我们需要给大家讲解的是如果说你现在你的需求啊跟我现在的这个需求是不一样的话那么我们该如何去修改这个菜单修改成我们自己制定的一个这样的菜单呢我们来看一下
[00:28] 那么首先其实你要参考你的需求文档或者说你要看你的一个产品原型是不是根据我们这个产品原型是不是去做一个修改
[00:37] 那我们可以看到在这个位置是不是有一个房源管理下面有看房请求租房管理房源管理新房源等等一些信息那么我们就根据这个信息是不是来修改我们的这块的一个内容对不对那么前面我们讲pro的时候是不是也讲到过那么这块的一个信息是如何修改的呢其实我们是不是要找到什么呢找到它有一个config配置是不是一个路由的配置还记得吗是不是这个路由的
[01:03] Router这个configure那么在这个里面呢我们可以看到是不是只需要我们在这添加一些这个路由的规则然后呢这个pro框架它就会根据我们所添写的这个路由的规则自动来生成左侧这个菜单是不是这样的一个效果啊那么我们可以看到在这个位置是不是有个房源管理下面是不是有一个房东管理你看是不是有个房东管理那么是不是有一个合约管理用户管理等等
[01:30] 那么我们需要给大家讲的是第一个点是说我们在这个位置做修改就可以去修改制定的一个菜单这第一个点第二个点的是当我们去做一个我们项目开发的时候那么我们需要在这个src的配置下面去创建自己的一个目录注意
[01:47] 你要创建自己的目录然后呢要把我们的所有的一些页面呢都丢到我们这个目录下面来不要和他的pro系统的一些目录我们混淆这个大家能够理解吗好那么我们来看一下在这个下面呢我们会有一些什么像房东房源等等一些这个目录比如说我们有一个这个host那么这个里面是不是放了我们一些房源的一些这个文件什么and啊还有一个看房啊啊等等一些这个文件那么所对应的是不是就是我们页面中的这样的一些文件啊
[02:17] OK好那么现在呢我们根据这个需求是不是已经就完成了我们的一个这个左侧菜单的这样的一个编写大家注意一定要根据我们这个需求文档来或者说根据我们的产品原型来OK好那我们来看一下现在我们要做一个小小的一个一件事情就是当我去直接访问到我页面的时候
[02:41] 大家有没有发现他默认是访问的是我们Despot这个页面我觉得这个其实很不爽对吧那么我想让他去比如说进入我这个房源管理进入这个页面那么应该怎么做大家想一想那么我让他去直接访问8000端口的时候那么默认直接进入的就进入我的房源管理的页面那么应该怎么做大家想一想
[03:07] 其实它也是非常简单的对吧好那我们一起来看一下那么在这个路由依然肯定还是在路由这个文件中对不对那我们来看一下在路由这个位置它是不是有一个这样的一个配置叫做pass斜杠是不是就代表的根也就是我们访问的这个8000这个根是不是在这然后呢它的后面有一个redirector做一个重定向重定向有一个叫做
[03:31] 下面有一个Layers那么显然我们可以看到它默认从定向的是不是就是一个分析页面那么我们想让它去跳转到我们的一个房源管理那我们是不是就应该去找到我们的房源是不是就在这儿是不是有一个房源那么我们把这个内容拷过来往这一丢是不是就可以实现这样的效果那我们来看一下对不对然后把它删掉然后回车看效果
[04:00] 你注意它是不是自动就会跳转到我们这个房源管理然后呢我们可以发现它是不是也是选中了就是这个房源管理啊好那么这样的效果是不是就根据我们自己的需求完成了我们首页的这样的一个跳转哎OK好那么我们这样的话呢就基本上完成了啊哎OK
[04:18] 好我建议大家呢你们自己可以手动把这个去修改修改去写一写啊那么这样的话你的理解会更深刻一点哎OK对应的是在这个里面啊要把我们自己的一个自己的一些这个页面啊我们都放到自己的一个目录下面去啊这个大家记得切记要不然的话可能你会搞混哎OK这个是新增房源这个房源管理了这个刚刚我们也说过了然后呢去进入系统去默认打开这个房源管理页面
[04:47] 那么刚刚是不是我们说过了把它往这一丢这样的话效果是不是就实现了好嘞那么关于这个菜单的一个制定义呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

