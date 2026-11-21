# 08-部门前端：构造模块

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\08-部门前端：构造模块_【海量资源尽在 ubkz.com】.mp4
- 时长 6分5秒（音频 366s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了至此呢我们微服务这方面的内容就已经都写好了那微服务呢刚才其实使用起来的都比较简单的代码我们基本上完成了一个CIUD操作其实需要各位注意的点呢就是这个企业ID千万别忘了以及我们这个代码抽取的这个工作那我们微服务写好了之后接下来就是关注的前端的一个开发那对于前端的开发呢有必要和各位来提一下
[00:31] 或者我们一起来回顾一下昨天我们讲这个前端咱们如何去做的也就是我们前端的这个开发的一个基本步骤那对于我们前端开发呢首先呢我们去搞这么一个model或者搞这么一个模块出来那在这个模块做好了之后我们接下来去编写APIAPI其实就跟我们后端打交道的那API也编写成功了之后接下来
[01:00] 我们可以在页面让它完成跳转去得到我们的一些数据做一个测试那测试也通过了接下来我们要做的事情其实就是把这个样式页面给它构造的美观一点构造的好看一点把我们的页面样式给它构造出来接着完成增删改查这些操作其实就可以了好了这个就是我们前端开发的基本的这一个步骤
[01:26] 好了其中我们刚才说过了第一件事我们应该要构建一个模块那构建模块的时候呢我们可以自己找一个模块copy过来也没问题但是呢为了节省时间我在这边已经把我要构造的这个模块给各位准备好了来找到我们的前端代码在前端代码有一个model-de-departments在这个departments当中和我们自己构造的这个demo基本上长的是一模一样这个demo我们昨天的案例
[01:57] 其中呢有一个index有一个index好了里面有一个store这store里面没什么内容这我这store更简单什么都没有什么都没有好了那接下来呢还有比如说呢这边有一个routerrouter是我昨天咱们说过的指定你页面跳准的路由我这边也写好了那接下来呢还有一个就是页面page那page叫做index.ve那这个index.ve是我们美工的一些人员做的一个基本的一个静态结构
[02:27] 里面有很多的样式以及它部署的这么一个DIV的一个结构出来所以对于各位来说你想自己去写就自己去写你不想写的话拿我这个前端模块同样可以使用所以我在这边就不客气了Ctrl C找到我的代码注意VS Code当中的我们可以在资源管理器当中显示当前的这个工程那找到SRC把我这个模块Ctrl V拷起来
[02:56] 那靠近来之后注意其中有一个注册模块什么一件事那注册模块很简单找到mnt.js把我们刚才添加的模块拿过来就可以了我们刚才的模块呢叫做model-我为了怕出错怕出错我直接复制了model-departments好了这边呢起一个名字叫做departments接着注册ctrl-cctrl-vok那这样一来我创建模块
[03:31] 就已经创建好那还记着昨天跟各位聊过的这么一件事情啊我们一起来回顾一下昨天我们画过的这么一张简单的图形在图形里面说过了model-某某指的是我们自己要天天的模块里面还有模块的组件等等等等很多内容其中我们有一个路由路由指定的是你当前点击的链接是什么以及这个链接对应的我们的
[04:02] 处理的视图好了接着我们来看一下router代表的是路由路由里面我定义了一个副路径就是departments底下来一个index那我请求的话是不是就变成departments-index那它跳转的页面在哪在我们的departments当然我昨天说过JML会加model-那也就是model-departments找到page找到index那这样一来左侧菜单
[04:32] 就有了并且呢一点菜单是不是进入到这个index.ve啊好了这个代码呢简单的和各位来看了一下那我把这个工程启动起来npm run dvok这边报了一个简单的错误啊这边报了一个错误好了那这个错误是有原因的可能是昨天那个依赖不小心给删除了我在这边呢把这个依赖再添加一下cnpm install
[05:09] 不小心把这个依赖的这个jar 包把这些依赖的这些包不小心给删除了不好意思这边呢再去安装一下好了这个已经安装成功了安装成功了之后我们继续npm run dev启动好了这回就正常了这个启动稍微有一点点慢啊各位我先暂停一下视频等启动成功了之后呢我再继续OK这边呢已经启动成功了那启动成功之后
[05:39] 我们可以打开浏览器访问localhost8080一起来看一下效果走点击登录那左边已经出现了组织架构这个菜单那我们可以点进来来看一下效果好了这个是一个静态的基本的这么一个页面

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 SaaS-HRM 项目中创建并配置“组织机构”模块的前端页面和相关路由。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：使用 Postman 发起 GET 请求，访问本地服务器的部门信息接口，返回 JSON 数据，包含部门 ID、名称、创建时间等字段。
画面2：展示 PPT 页面“1.3 前端实现”下的“1.3.1 创建模块”部分，说明需使用命令行创建 module-departments 模块并引入工程，以及在 src/main.js 中注册模块和在 /module-departments/router/index.js 中配置路由。
画面3：在 Windows 资源管理器中，显示项目目录结构，当前选中“实体类”文件夹，其中包含 DepartmentJava、PermissionJava 等多个 Java 文件。
画面4：在 Visual Studio Code 中打开项目文件夹，显示 index.js 文件内容，其中包含 Vue-router 的导入和安装模块的代码。
画面5：在 Windows 资源管理器中，右键点击“router”文件夹，弹出菜单，显示“打开”、“用 Sublime Text 打开”、“用 Notepad++ 打开”等选项。
画面6：在 Windows 资源管理器中，选中“pages”文件夹下的“index.Vue”文件，准备进行编辑。
画面7：在 Notepad++ 中打开“index.Vue”文件，显示部分 SCSS 样式代码，包含 .el-tree-node、.generalClass、.all 等样式规则。
画面8：在 Windows 资源管理器中，关闭“pages”文件夹窗口。
画面9：在 Windows 资源管理器中，显示项目根目录下的“src”文件夹，其中包含 assets、components、filters、lang、store、router 等子文件夹。
画面10：在 Windows 资源管理器中，显示“hrm”项目根目录，包含 day1、day2、day3 三个子文件夹。
画面11：在 Windows 资源管理器中，打开“day2”文件夹，显示其中包含多个设计图和文档文件，如“05-部门结构.png”、“SaaS-HRM-需求文档.xlsx”。
画面12：在 Visual Studio Code 中打开“index.js”文件，显示路由配置代码，其中包含根路径、重定向、标题、图标和子路由等信息。
画面13：在浏览器中打开 Swagger UI 页面，准备进行 API 测试。
画面14：在浏览器中访问本地服务器的部门页面，显示 HR 系统的“工作日历”和“快速开始”导航等界面。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
(1) 使用命令行创建 module-departments 模块并引入到工程中
  ithema moduleAdd departments
(2) 在 src/main.js 中注册模块
  import departments from '@/module-departments/'
  Vue.use(departments, store)
(3) 在 /module-departments/router/index.js 配置路由
  import Layout from '@/module-dashboard/pages/layout'
  const _import = require('@/router/import' + process.env.NODE_ENV)
  export default [
    {
      root: true,
      path: '/departments',
      component: Layout,
    }
  ]

画面4：
import Layout from '@/module-dashboard/pages/layout'
import routerMaps from '@/router'
import app from './store/app'
export default {
  install(module, store) {
    // 注册路由
    asyncRouterMap.push(routerMaps[0])
    if (store !== undefined) {
      store.registerModule('app', app)
    }
  }
}

画面12：
import Layout from '@/module-dashboard/pages/layout'
const _import = require('@/router/import' + process.env.NODE_ENV)
export default {
  root: true,
  path: '/departments',
  redirect: 'noredirect',
  meta: {
    title: '组织机构',
    icon: 'architecture'
  },
  children: [
    {
      path: 'index',
      component: _import('/departments/pages/index')
    }
  ]
}

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：PPT 标题为“1.3 前端实现”，子标题为“1.3.1 创建模块”，内容包括三个步骤：使用命令行创建模块、在 main.js 中注册模块、在 router/index.js 中配置路由。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

