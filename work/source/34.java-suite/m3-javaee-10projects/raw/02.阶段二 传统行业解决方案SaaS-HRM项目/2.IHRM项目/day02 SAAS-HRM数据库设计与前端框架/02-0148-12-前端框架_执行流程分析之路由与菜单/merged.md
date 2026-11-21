# 12-前端框架：执行流程分析之路由与菜单

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\12-前端框架：执行流程分析之路由与菜单_【海量资源尽在 ubkz.com】.mp4
- 时长 8分0秒（音频 481s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好,我们已经把这个工程跑起来了,并且呢我们刚才简单的说了一下它整个的工程目录结构。
[00:12] 那接下来呢我们就来分析一下它整个这个脚手架工程它是如何执行的。
[00:19] 那这个执行过程呢我准备分成这么两个阶段来看,首先呢第一个就是它的路由以及菜单,还有第二个就是它前端与后台数据进行的一个交互。
[00:32] 那我们一个一个来看首先看的就是这个路由和菜单那对于路由而言我们可以简单的理解成是你敲的这个地址和你展示出页面的这么一个关联关系的一个配置那我们一起来找到它这个路由究竟在什么地方那这个路由呢我们刚才说过两方面一个叫做rotor是在我们SRC原代码目录
[00:59] 那在我们的模块下边呢它也有一个这么一个router这么一个配置那我们首先看的是前边这个源代码里面的router目录router目录好了来找到我们的代码看一下里面的router在里面的这个router呢前两个import这两个内容我们不需要重点关注我们关注的是一个叫做index.js这是路由的总配置在这个index.js里面各位来看各位来看其中
[01:28] 我配置了一个什么-login什么配置了一个-reg配置了一个什么-also redirect那接着我们可以把这个工程呢给它退出那退出之后各位来看我当前请求的就是-login那请求的-login根据我们的路由配置来说它找到的是一个dashboard-login我们一起来找一下一起来找一下好了找到
[02:02] 注意找到这个dashboard那这个dashboard从哪找呢是这边调用的是一个inputimport这么一个函数这个import在最上边import在最上边那这个import在最上边这里面它究竟做的什么事情呢是这样的它就会去找会去找找到哪找到这个把model全前面加上model就这个意思module那这样一来它就会去找到model-dashboard
[02:31] 那以各位来看不就它吗当然了我们前面是一个省略的写法它自己内部会有一个拼接的过程那找到它那接着在这里面找到配置配置司那由配置司那继续来看是不是还有一个叫做login那各位来看配置司找到login那在login当中在login当中这边还没有账号立即注册什么什么等等等等这些内容不就跟我们页面显示的一模一样吗
[02:58] OK那这样一来我们就已经知道了路由其实指的是我们请求链接和它页面跳转这个Vue视图之间的一个匹配关系那接下来呢咱们继续再来看那现在所有的这些路由配置到了一个叫做concentroutermap当中这个rotormap其实是一个数组那这个rotormap指的是公共的一些页面因为我们用的是人家的教授家工程教授家工程已经给我们准备好了公共的页面
[03:27] 它只有登录退出或者错误或者什么404401这些错误的界面等等但是但是对于一些我们自己模块的这些路由还没有所以这些路由它叫做私有的一些路由或者叫做模块路由那模块路由在哪呢在这个里面的最底下配置的一个叫做async router map这个async router map它会动态的
[03:55] 加载它会动态的加载你这个模块当中的所有你这个模块当中所有的模块当中所有的router下的内容那我们一起来看一起来看就目前来说就目前来说这里面的内容比较少内容比较少那各位来看各位来看那底下这边呢还有一个菜单那这个菜单呢我们登录进去能够看到有一个XXX什么E5模块那这个XXXE5模块究竟在哪呢那这边是一个案例
[04:26] 这边是一个例子它告诉我有这么一个模块那这个模块把它放到什么地方呢我们一起来找一下一起来找一下你会发现总的这个录用里没有但是我们打开到模块里面它有一个router这边也有一个index那各位来看这边告诉我XXX有模块配置了一个title配置了一个titleXXX也有模块那其中我们如果要点击访问
[04:53] susclents-index那这个susclentsindex在哪进行的配置我们一起来找一下susclents选取路径susclents好了我们再切回代码这边加一个index前面代表副路径后面不就代表子路径吗那我们一起来找这个代表副路径这边还有个pass抽证代表是子吗所以副路径子路径那它们拼接起来不就是susclents-index吗
[05:23] 那这个susclan-index由于里面配置了一个title那这个title其实指的就是你菜单要显示的模块名称比如说呢我们这边就要做demoOK那各位来看变成了demo菜单已经有了那当前我如果要敲击这个链接的话敲击这个链接的话它会帮我们知道哪个页面呢注意这边有一个叫做component这component指的是你的页面究竟在哪
[05:53] 好了那这个pass我们指的是请求地址好了那components指的就是当前请求地址你要跳转的跳转的Vue试图界面那各位应该还记着我这边写了一个下滑线import demo那前面默认的给我要加一个modo所以我们一起来找一起来找modomodo-demomodo-demo不就在这那从里面找找到配置司
[06:25] 再去找是不是找到index就是点Vue啊那么点开index.Vue这里面就是我们的页面的一些效果当然这个页面效果呢现在看的还不太完整还不太理想因为我们看不出什么内容那么可以这样就是把里面的这些内容呢先给它注视起来先给它注视起来好了那接着里面我们写一句话比如说那种demo页面OK那我们再来刷新一下一刷新你会发现
[07:07] 里面只留了这么一句话好了这个就是我们当前工程它如何去配置你请求地址如何去挂载菜单那咱们就已经说清楚了那我们简单的再来总结一下在我们这个工程当中如果你要想去配置请求地址和我们跳转页面的逻辑关系那么需要找到自己定义的模块找到模块当中的router里面的index.js
[07:35] 那这里面以这种结构的形式去配置你的请求地址那上面是副地址底下是子地址那通过component指定你要跳转的视图或者你要跳转的页面在哪那我们默认找到的是demo page index下那找到demo page index下那这个我们的页面其实就已经跳转过来了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解基于 Vue 的 SaaS HRM 系统的路由配置、菜单结构及前端页面实现。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT 的第 9 页，内容为“3.4 执行流程分析”下的“3.4.1 路由和菜单”，说明路由和菜单绑定，以及 constantRouterMap 和 asyncRouterMap 两种路由类型。
画面 2: 展示课程 PPT 的第 24 页，包含“黑马程序员”Logo和“改变中国IT教育，我们正在行动”的标语，以及一个路由示意图：通用路由指向“登录、404等通用页面”。
画面 3: 展示一个 PPT 页面，用图示说明项目代码目录结构，包括 api、assets、components、filters、lang、mock、module-dashboard、module-demo、router、store、styles、utils、App.Vue、main.js 等目录和文件，并标注了各部分的作用。
画面 4: 在 Visual Studio Code 中展示项目文件结构，同时显示了 index.js 文件的开头部分，包含 import、require、Vue.use(Router) 和 NProgress 配置。
画面 5: 在 Visual Studio Code 中展示 index.js 文件，聚焦于 constantRouterMap 的定义部分，显示了路由配置的注释和部分代码。
画面 6: 在 Visual Studio Code 中展示 login.Vue 文件，显示了登录页面的 HTML 结构和部分 Vue 代码，包括按钮和弹窗组件。
画面 7: 在 Visual Studio Code 中展示 index.js 文件，显示了 constantRouterMap 中的 login、reg 和 authredirect 路由配置。
画面 8: 在 Visual Studio Code 中展示 index.js 文件，显示了路由守卫的代码，用于处理登录验证。
画面 9: 展示 HRM 系统的登录后首页，包含“早安，HR 专员，祝你开心每一天！”的欢迎语、工作日历和快速开始导航。
画面 10: 展示 Windows 桌面，多个窗口打开，包括浏览器、Visual Studio Code、PowerDesigner、SQLyog、Microsoft Excel 等，显示了开发环境的多任务状态。
画面 11: 在 Visual Studio Code 中展示 index.js 文件，显示了 module-demo 模块的路由配置，包含 index 路由。
画面 12: 在 Visual Studio Code 中展示 index.js 文件，显示了 module-demo 模块的路由配置，包含 index 路由，并注释了“// 海外出口”。
画面 13: 在 Visual Studio Code 中展示 index.Vue 文件，显示了页面的 HTML 结构和 Vue 代码，包括表格和数据绑定。
画面 14: 展示 HRM 系统的 demo 页面，页面标题为“demo页面”，内容为空白。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```javascript
// 宝文
const _import = require('./import') // process.env.NODE_ENV // 环境变量
const whitelist = ['login', '/reg', '/authredirect'] // 白名单
Vue.use(Router)
NProgress.configure({ showSpinner: false }) // NProgress 配置
```

画面 5:
```javascript
// 在栏目目录中
if 'hidden' true will not show in the sidebar(default is false)
if set true, will always show the root menu, whatever its child routes length
if not set alwaysShow, only more than one route under the children
it will becomes nested mode, otherwise not show the root menu
if 'redirect' is used by the route, it will not redirect in the breadcrumb
```

画面 6:
```html
<el-button class="loginBtn" type="primary" style="width:180px;margin-bottom:30px;" :loading="loading" @click.native.prevent="handleLogin">
  <div class="tips">
    <span class="companyName">{{companyName}}</span>
    <span>654321</span>
  </div>
</el-form>
<el-dialog :title="$t('login.thirdparty')" :visible.sync="showDialog" append-to-body>
  <div class="login-thirdparty">
    <div class="login-thirdparty-item">
      <img src="..." alt="...">
    </div>
  </div>
</el-dialog>
```

画面 7:
```javascript
export const constantRouterMap = [
  {
    path: '/login',
    component: _import('dashboard/pages/login'),
    hidden: true
  },
  {
    path: '/reg',
    component: _import('dashboard/pages/reg'),
    hidden: true
  },
  {
    path: '/authredirect',
    component: _import('dashboard/pages/authredirect'),
    hidden: true
  }
]
```

画面 8:
```javascript
// 登录验证
store.dispatch('login').then(() => {
  Message.error('登录失败，重新登录！')
  next({ path: '/login' })
}) else {
  next()
} else {
  if (whitelist.indexOf(to.path) !== -1) {
    next()
  } else {
    next('/login') // 若当前页面是 login，不会触发 beforeEach
  }
}
```

画面 11:
```javascript
{
  path: 'index',
  component: _import('demo/pages/index'),
  name: 'demo',
  meta: { title: 'demo', icon: 'component', noCache: true }
}
```

画面 12:
```javascript
{
  path: 'index',
  // 海外出口
  component: _import('demo/pages/index'),
  name: 'demo',
  meta: { title: 'demo', icon: 'component', noCache: true }
}
```

画面 13:
```html
<template slot-scope="scope">
  <span>{{scope.row.forecast}}</span>
</template>
<el-table :data="tableData">
  <el-table-column prop="id" label="ID" width="100"></el-table-column>
  <el-table-column prop="name" label="姓名" width="100"></el-table-column>
  <el-table-column prop="forecast" label="预测值" width="100"></el-table-column>
</el-table>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2: PPT 标题为“黑马程序员”，副标题为“改变中国IT教育，我们正在行动”，下方有一个流程图：通用路由指向“登录、404等通用页面”。
画面 3: PPT 中的架构图用箭头标注了各个目录和文件的作用，例如“api”指向“工具方法（和后端数据交互API方法）”，“assets”指向“公共的组件”，“components”指向“当模块的Vue视图”，“router”指向“当前模块的路由”，“store”指向“状态管理：在多个页面中共享数据”，“utils”指向“工具库”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

