# 19-企业详情：配置路由构造页面

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day02 SAAS-HRM数据库设计与前端框架
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day02 SAAS-HRM数据库设计与前端框架\19-企业详情：配置路由构造页面_【海量资源尽在 ubkz.com】.mp4
- 时长 8分35秒（音频 515s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 好了那到目前为止呢其实我们已经把企业列表相应的这些内容呢都已经给它展示出来了那其实对于我们这个企业列表展示的过程当中呢你说有难度吗其实难度不多难度也适中其实就是把握好我们刚才画的这张图以及它的一个执行顺序就可以了那对于一个模块来说呢我们先创建好了之后配置它私有的一个路由那配置好路由接着进入到页面在页面部分
[00:33] 通过create调用methodmethod调用我们写的API那API我们写好了跟后台进行交互得到数据绑定到模型接着关注我们的页面所以呢这边做一个简单总结对于我们来说要想去进行我们自己模块的一个开发我们重点关注的点在哪呢其中重点关注的点一共有这么几个首先第一个就是我们要构建一个模块然后呢配置我们的路由规则
[01:06] 好了那接下来第二个点第二个点呢我们就需要需要构建一个我们跳转的页面那在页面当中通过create调用我们的method的方法那还有一个我们要构建叫做API那构建了API接着第四件事我们想办法我们的页面搞得好看一点那所以在页面部分我们可以使用Elem UI的组件来构造好了这个就是我们关注的
[01:36] 这么几个点好了这个呢咱们做了一个总结之后呢在我们的内容呢最后还有一块就是要做一个企业详情的这么一块内容那对于企业详情这块内容来说首先看我们的域名原型那在这边呢我有一个查看按钮操作有一个查看按钮一点你会发现进入到一个页面这个页面上面这部分代表的是链接发生了变化指的是这是一个路由地址那接着这个路由地址指定到一个页面
[02:06] 那我们先把这个页面呢有了之后接下来底下其实展示的是我们这个公司是不是他的一个详细的这么一个详情的一个介绍啊那所以对于我们接下来要完成的工作就是去把这个企业详情给他做出来那要做这个企业详情的话我们刚才已经说过我们重点关注的这四步首先第一个模块我们已经有了
[02:32] 我们要去配置你当前请求的这个路由规则OK各位来看请求地址detail下的后面有我们的一个地址参数那这个玩意儿其实也属于我们刚才这个企业SaaS Client这个模块当中的那所以找到router底下继续去添加一个子路由抽准下去添加好了抽准下这回添加呢pass请求路径好了这个请求路径呢我们叫做
[03:07] 就跟它一致吧detail写杠冒号ID那我需要跟各位解释一下这个冒号ID啥意思是因为在我们这个页面请求的过程当中呢各位来看冒号后面的其实是我们的一个ID的这么一个地址参数那地址参数有可能变的是有可能会变的它其实代表是一个参数那我们这边冒号ID指的是对这个参数起了一个名称叫做IDOK那我们的地址写好了之后呢接着有一个component
[03:38] 我直接从上面直接考过来了component好了接下来呢component呢这边少一逗号那引入我们这回引入的就叫做d e t a l e detaildetail这么一个页面那接下来呢这边给它的名字呢我也做一个简单的修改ok好了这个就叫做sus企业详情ok那这样一来基本的这个路由我们也配置好了那配置好了之后接下来的问题就是说呀我还少一个detail
[04:12] 这么一个界面根据我们刚才分析的这么几个步骤路由构造好了之后构建页面那构造页面我们需要在Clance下边配置私下搞一个叫做Detail这么一个页面出来所以我来个Detail.voe那里面的代码呢大同小异我从这边call一个过来从这边call一个过来把里面所有的内容全部都删掉主要是为了要它这个结构
[04:44] 主要是为了要这个结构我就不用自己再去创建了OK基本上这边改一个名字detail好了那接下来那接下来我们可以一起去构造页面构造页面构造好了之后接下来就是说在我这边在企业详情后边是不是应该有一个按钮叫做查看那查看的时候是不是就可以跳转到我们刚才添加好的这个页面上面
[05:16] 那所以呢我们这个按钮呢也需要给它做一个简单的修改找到我们index页面index页面是我们的列表其中呢把这个button去掉了那我们现在有一个查看有一个查看那我们查看的时候呢可以用A标签比如说叫做查看A标签进行一个页面的跳转当了A标签里面呢我们可以加一个href嘛
[05:45] 你要跳转到什么地方当然了你除了A标签这种方式还有其他的一种方式比如说我们可以借助VUE当中提供的一个叫做router-link标签它跟A标签的效果是一样的那中间呢也是我们的叫做查看那接下来它有一个to属性那这个to属性就是指你要跳转到哪个地址那我们要跳转的地址根据我们刚才
[06:18] 根据刚才我们自己写的这个路由规则来看根据我们自己写的这个路由规则来看要跳转到我们SaaS Client 私下Detail 下好了找到页面做一个修改SaaS Client 私下DETAL那后面呢要加一个参数那这个参数指的是你当前选中这一行它的ID嘛那这个ID在哪呢注意scope我们就可以获取好了前面加冒号
[06:52] 我们要拼接加上scope.row.id后面多一个猫号OK那这样一来我这个地址呢已经构造好了那构造好了之后构造好了之后我们看一下能不能跳转过去好了刷新一把查看哎报了一个错误我们可以打开F12一起来检查一下回退刷新刷新
[07:35] SaaS企业SaaS企业好了接下来呢刷新查看那各位来看左下角其实这个链接地址也已经有了我走左下角链接地址已经有了我们可以检查一下SaaS Clients-Detail-10SaaS Clients-Detail-10找到我们的路由配置我这边地址叫做Details啊抱歉叫做Details
[08:24] OK 刷新页面我们再来看一下效果Details走你发现现在已经进入到SaaS详情页面了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Vue.js 项目中配置路由，实现 SaaS 企业列表页面与详情页面的跳转和数据展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在 Visual Studio Code 中打开 `index.Vue` 文件，展示 Vue 组件模板和脚本部分，其中 `data()` 函数返回空数组 `datalist: []`，用于存储企业列表数据。
画面2：展示一个流程图，说明 Vue 页面的构成：`router/index.js` 路由配置（1）指向 `demo/pages/index.Vue` 视图（2），视图内部包含 `<template>` 和 `<script>` 标签（7），其中 `<script>` 标签内包含 `data()`（7）、`methods`（5）、`created`（3）等生命周期钩子，通过 API 方法（6）与 Java 服务端后台（6）交互，实现双向绑定（8）。
画面3：展示 PPT 页面，标题为“4.3.2 企业详情”，内容为“（1）配置路由”，并提示在 `/src/module-saas-clients/router/index.js` 添加新的子路由配置。
画面4：展示 SaaS 企业详情页面，显示“江苏传智播客教育科技股份有限公司”的企业信息表单，包括公司名称、公司地区、公司地址等字段。
画面5：在浏览器中打开 SaaS 企业详情页面，同时在任务栏中显示 Visual Studio Code 窗口，表明正在编辑相关代码。
画面6：在浏览器中打开 SaaS 企业详情页面，鼠标悬停在“公司地区”输入框上，显示“特级地区”字样。
画面7：在 Visual Studio Code 中，右键点击 `router/index.js` 文件，弹出菜单，显示“Generate from Maven Archetype”选项。
画面8：在浏览器中，鼠标悬停在左侧导航栏的“组织架构”菜单项上。
画面9：在 Visual Studio Code 中打开 `index.Vue` 文件，展示 Vue 组件模板和脚本部分，其中 `data()` 函数返回空数组 `datalist: []`，用于存储企业列表数据。
画面10：在 Visual Studio Code 中，展示 `router/index.js` 文件内容，其中配置了 `children` 数组，包含 `index` 和 `detail` 两个子路由，分别指向 `saas-clients/index` 和 `saas-clients/detail` 组件。
画面11：在浏览器中，访问 `/saas-clients/detail/10` 路径，页面显示 404 错误页面。
画面12：在浏览器中，访问 `/saas-clients/index` 路径，页面显示企业列表，包含序号、企业名称、版本、联系电话、截至时间、状态和操作列。
画面13：在浏览器中，访问 `/saas-clients/index` 路径，页面显示企业列表，包含序号、企业名称、版本、联系电话、截至时间、状态和操作列。
画面14：在浏览器中，访问 `/saas-clients/index` 路径，页面显示企业列表，包含序号、企业名称、版本、联系电话、截至时间、状态和操作列。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面1：
```Vue
<template>
  <el-table-column fixed="right" label="操作" width="150">
    <template slot-scope="scope">
      <el-button type="text" size="small">查看</el-button>
      <el-button type="text" size="small">编辑</el-button>
    </template>
  </el-table-column>
</el-table>
</template>

<script>
import { list } from '@/api/base/saasClient'
export default {
  name: 'saas-clients-index',
  data () {
    return {
      datalist: []
    }
  }
}
</script>
```

画面2：
```html
<template>
  <script>
  data() {
    数据模型（双向绑定）7
  },
  method() {
    当前页面需要的方法 5
  },
  created() { // 页面实例化之前执行 3
    行的方法（Vue子系统） 3
  }
  </script>
  <style>
  </style>
```

画面3：
在 `/src/module-saas-clients/router/index.js` 添加新的子路由配置。

画面7：
```javascript
// router/index.js
{
  path: '/saas_clients',
  redirect: 'noredirect',
  name: 'saas-clients',
  meta: {
    title: 'xxx企业模块管理',
    icon: 'component'
  },
  children: [
    {
      path: 'index',
      component: () => import('@/views/saas-clients/pages/index'),
      name: 'saas-clients-index',
      meta: {
        title: 'SAAS企业列表',
        icon: 'component',
        noCache: true
      }
    },
    {
      path: 'detail/:id',
      component: () => import('@/views/saas-clients/pages/detail'),
      name: 'saas-clients-detail',
      meta: {
        title: 'SAAS企业详情',
        icon: 'component',
        noCache: true
      }
    }
  ]
}
```

画面10：
```javascript
// router/index.js
{
  path: '/saas_clients',
  redirect: 'noredirect',
  name: 'saas-clients',
  meta: {
    title: 'xxx企业模块管理',
    icon: 'component'
  },
  children: [
    {
      path: 'index',
      component: () => import('@/views/saas-clients/pages/index'),
      name: 'saas-clients-index',
      meta: {
        title: 'SAAS企业列表',
        icon: 'component',
        noCache: true
      }
    },
    {
      path: 'detail/:id',
      component: () => import('@/views/saas-clients/pages/detail'),
      name: 'saas-clients-detail',
      meta: {
        title: 'SAAS企业详情',
        icon: 'component',
        noCache: true
      }
    }
  ]
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
- 标题：无明确标题，但内容为“Vue 页面构成”。
- 流程图结构：
  - `router/index.js` 路由配置（1）指向 `demo/pages/index.Vue` 视图（2）。
  - `demo/pages/index.Vue` 视图（2）包含 `<template>` 和 `<script>` 标签（7）。
  - `<script>` 标签（7）内包含 `data()`（7）、`methods`（5）、`created`（3）等生命周期钩子。
  - `methods`（5）通过 API 方法（6）与 Java 服务端后台（6）交互。
  - `data()`（7）与 `methods`（5）之间存在双向绑定（8）。

画面3：
- 标题：4.3.2 企业详情。
- 内容：（1）配置路由。
- 说明：在 `/src/module-saas-clients/router/index.js` 添加新的子路由配置。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

