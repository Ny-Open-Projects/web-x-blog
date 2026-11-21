# 画面线理解：16.Ant Design Pro入门之自定义菜单和路由

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\16.Ant Design Pro入门之自定义菜单和路由【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:12, 01:44, 02:20, 02:45, 03:14, 03:43, 04:06, 04:43, 05:03, 05:32, 06:23, 06:57, 07:30
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:23:05

1) 这一组画面整体在讲如何通过修改路由配置文件来创建和管理 Ant Design Pro 项目中的新页面，并展示其在前端界面中的效果。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Ant Design Pro 项目中“分析页”的前端界面，包含多个数据图表和统计信息。
画面2：在 IntelliJ IDEA 中打开 `src/router.config.js` 文件，高亮显示 `/user` 路由下的注册相关路由配置。
画面3：浏览器页面空白，显示加载中状态，地址栏为 `localhost:8000/user/login/redirect...`。
画面4：在 IntelliJ IDEA 中，`router.config.js` 文件中高亮显示 `/dashboard` 路由下的 `analysis` 子路由配置。
画面5：在 IntelliJ IDEA 中，`router.config.js` 文件中高亮显示 `/dashboard` 路由下的 `monitor` 和 `workplace` 子路由配置。
画面6：在 IntelliJ IDEA 中，`router.config.js` 文件中高亮显示 `/list` 路由下的 `table-list` 和 `basic-list` 子路由配置。
画面7：在 IntelliJ IDEA 中，`router.config.js` 文件中高亮显示 `/dashboard` 路由下的 `analysis` 子路由配置。
画面8：浏览器页面显示“分析页”的骨架界面，左侧菜单栏高亮显示“menu.new.analysis”。
画面9：在 IntelliJ IDEA 中，`router.config.js` 文件中高亮显示 `/new` 路由下的 `analysis`、`monitor`、`workplace` 子路由配置。
画面10：在 IntelliJ IDEA 中，打开 `src/locales/zh-CN.js` 文件，高亮显示 `form` 对象中的多个字段占位符配置。
画面11：在 IntelliJ IDEA 中，打开 `src/locales/zh-CN.js` 文件，高亮显示 `menu` 对象中的多个菜单项配置。
画面12：浏览器页面空白，地址栏为 `localhost:8000/new/monitor`。
画面13：浏览器页面显示“New T/Work”页面的骨架界面，左侧菜单栏高亮显示“New T/Work”。
画面14：在 Typora 编辑器中打开 `讲义.md` 文件，高亮显示“新增页面”章节内容，其中包含对菜单配置的说明。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面2：
```javascript
export default [
  // user
  {
    path: '/user',
    component: '../layouts/UserLayout',
    routes: [
      { path: '/user', redirect: '/user/login' },
      { path: '/user/login', component: '/User/Login' },
      { path: '/user/register', component: '/User/Register' },
      { path: '/user/register-result', component: '/User/RegisterResult' },
    ],
  },
  // app
  {
    path: '/',
    component: '../layouts/BasicLayout',
    Routes: ['src/pages/Authorized'],
    authority: ['admin', 'user'],
    routes: [
      // dashboard
      {
        path: '/',
        redirect: '/dashboard/analysis',
      },
      {
        path: '/dashboard',
        name: 'dashboard',
        icon: 'dashboard',
        routes: [
          {
            path: '/dashboard/analysis',
            name: 'analysis',
            component: '/Dashboard/Analysis',
          },
        ],
      },
    ],
  },
]
```

画面4：
```javascript
// dashboard
{
  path: '/',
  redirect: '/dashboard/analysis',
},
{
  path: '/dashboard',
  name: 'dashboard',
  icon: 'dashboard',
  routes: [
    {
      path: '/dashboard/analysis',
      name: 'analysis',
      component: '/Dashboard/Analysis',
    },
  ],
},
```

画面5：
```javascript
// dashboard
{
  path: '/',
  redirect: '/dashboard/analysis',
},
{
  path: '/dashboard',
  name: 'dashboard',
  icon: 'dashboard',
  routes: [
    {
      path: '/dashboard/analysis',
      name: 'analysis',
      component: '/Dashboard/Analysis',
    },
    {
      path: '/dashboard/monitor',
      name: 'monitor',
      component: '/Dashboard/Monitor',
    },
    {
      path: '/dashboard/workplace',
      name: 'workplace',
      component: '/Dashboard/Workplace',
    },
  ],
},
```

画面6：
```javascript
{
  path: '/list',
  name: 'list',
  routes: [
    {
      path: '/list/table-list',
      name: 'searchtable',
      component: '/List/TableList',
    },
    {
      path: '/list/basic-list',
      name: 'basiclist',
      component: '/List/BasicList',
    },
  ],
},
```

画面9：
```javascript
// dashboard
{
  path: '/',
  redirect: '/dashboard/analysis',
},
{
  path: '/dashboard',
  name: 'dashboard',
  icon: 'dashboard',
  routes: [
    {
      path: '/dashboard/analysis',
      name: 'analysis',
      component: '/Dashboard/Analysis',
    },
    {
      path: '/dashboard/monitor',
      name: 'monitor',
      component: '/Dashboard/Monitor',
    },
    {
      path: '/dashboard/workplace',
      name: 'workplace',
      component: '/Dashboard/Workplace',
    },
  ],
},
```

画面10：
```javascript
'form.optional': '（选填）',
'form.submit': '提交',
'form.save': '保存',
'form.email.placeholder': '邮箱',
'form.password.placeholder': '至少6位密码，区分大小写',
'form.confirm-password.placeholder': '确认密码',
'form.phone-number.placeholder': '位手机号',
'form.verification-code.placeholder': '验证码',
'form.title.label': '标题',
'form.date.label': '起止日期',
'form.date.placeholder.start': '开始日期',
'form.date.placeholder.end': '结束日期',
'form.goal.label': '目标描述',
'form.standard.label': '衡量标准',
'form.client.label': '客户',
'form.client.placeholder': '请描述你服务的客户，内部客户直接 @姓名 / 工号',
'form.invites.label': '邀评人',
'form.invites.placeholder': '请直接 @姓名 / 工号，最多可邀请 5 人',
'form.weight.label': '权重',
'form.weight.placeholder': '请输入',
'form.public.label': '目标公开',
'form.public.label.help': '客户、邀评人默认被分享',
'form.public.radio.public': '公开',
'form.public.radio.partially-public': '部分公开',
'form.public.radio.private': '不公开',
```

画面11：
```javascript
'menu.home': '首页',
'menu.dashboard': 'Dashboard',
'menu.dashboard.analysis': '分析页',
'menu.dashboard.monitor': '监控页',
'menu.dashboard.workplace': '工作台',
'menu.form': '表单页',
'menu.form.basicform': '基础表单',
'menu.form.stepform': '分步表单',
'menu.form.stepform.info': '分步表单（填写转账信息）',
'menu.form.stepform.confirm': '分步表单（确认转账信息）',
'menu.form.stepform.result': '分步表单（完成）',
'menu.form.advancedform': '高级表单',
'menu.list': '列表页',
'menu.list.searchtable': '查询表格',
'menu.list.basiclist': '标准列表',
'menu.list.cardlist': '卡片列表',
'menu.list.searchlist.articles': '搜索列表（文章）',
'menu.list.searchlist.projects': '搜索列表（项目）',
'menu.list.searchlist.applications': '搜索列表（应用）',
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14：PPT 标题为“3.2.3、新增页面”，内容包含对菜单配置的说明，其中提到“所有的页面依然是保存的 src/pages 目录下，以及前端单元创建目录，如：”并列出菜单配置项。

5) 无。
