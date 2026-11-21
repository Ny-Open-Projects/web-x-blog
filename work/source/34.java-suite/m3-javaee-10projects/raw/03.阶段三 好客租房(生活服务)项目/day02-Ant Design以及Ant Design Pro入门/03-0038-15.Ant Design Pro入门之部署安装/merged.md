# 15.Ant Design Pro入门之部署安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\15.Ant Design Pro入门之部署安装【海量资源尽在 ubkz.com】.mp4
- 时长 6分5秒（音频 366s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来部署安装一下pro那么首先来看它的下载下载呢你可以去它的kithub上面去做一个下载啊也可以使用我们的一个安装包去做一个这样的一个安装啊那么这个包呢我已经给大家下载好了就在我们的资料中呢在这有一个这个按着design pro master这样的一个zip压缩包
[00:26] 那我们先把它解压到我们的任意的一个目录这个目录其实无所谓大家呢你们自己找个目录就可以了我是在F盘这个下面有个code的这个目录我把它解压过来解压到这好那么显然可以看到在这是不是已经是有了这样的一个目录哎呀OK好那么解压完成了就可以看到有这样的一个目录那么紧接着呢我们就需要
[00:51] 需要把它导入到我们的idea里面那么我们现在有必要呢先给大家去先提一下它的这个pro所提供的一个目录结构啊那么像这个什么config目录我相信大家也闭目卧身了对吧mock还有一些public的一些这种目录然后src呢就是它的一些关键的一些源码的一些目录什么assist这个是我们的本地资源
[01:15] comment组件通用的一些组件放到这个里面来还有什么e2e然后还有就是layout等等这个大家应该就认识了好嘞好那么第二步我们就把它去导入到我们的ID2中那么把这个我们就先关掉然后我们把它导入进来在这个位置是不是就import projector导入一下找到这个code下面它然后点击OK然后我们去
[01:43] 创建一个这个source然后呢下一步然后呢这个没有问题然后再下一步然后呢这个也没有问题下一步他正在去搜然后呢点击finish完成去导入进来那么导入进来之后我们来看一下这就是导入进来之后那么大概呢有这么多一些文件和目录吧其实有一些是没用的大家可以看像一些没用的就可以把它就删掉了
[02:13] 但是呢我们现在先保留吧到后面的话我们再去做一些这种清理的工作好然后呢我们接着继续往下面看啊导入完成之后呢我们就需要给他做一些初始化和一些启动服务因为我们知道你现在拿到这个只是他的源码对吧那么他这个里面呢会依赖很多的一些这种包所以呢我们还需要做一些这种初始化的操作依然呢打开我们的控制台在这控制台里面呢我们去输入一些命令那么首先我们要输入的就是这个
[02:42] 替这个yan一个叫install去做一个安装那么我们就等待他的一个完成因为这个时间可能会比较长一点那么我就把这个视频呢先暂停一下好那么通过了300多秒就是近5分钟啊5分多一点的这个时间呢他终于呢就把一些相关的依赖的安装完成了那我们可以看到在这个工程里面已经多了这个node的一个modules里面有非常多的一些依赖啊
[03:13] 这个我们就不一去看了然后呢下面呢我们来通过这个t yarn来启动这个服务t yarn start然后呢走把它呢启动起来我们来看一下效果等待它的一个启动那么启动完成之后呢它呢会去打开一个窗口对吧然后我们来看一下效果等待它的一个启动那么这样我还是把视频呢先暂停一下
[03:47] 好那么我们来看一下这个服务呢就启动起来了花了一点时间大概花了一分钟的时间吧把它跑起来了好那我们来看一下这个页面当它跑起来之后它就会自动去打开这个页面那么跟我们刚刚看到的截图其实是一样的你可以看到它首先默认进入的是一个Deskboard就仪表盘这个页面
[04:10] 在这个里面呢有一些这种数据这种统计信息啊然后呢它有一些这种就是我们的图表的一些信息然后呢像有什么监控监控页面呢还有一些像这么工作台啊等等的是不是有很多的一些这种这种操作啊或者这种页面然后呢可以看到在这个位置啊是不是有一些这个表单的一些这种情况啊那么表单的这个页面我们后续是不是可以做一些这种参考
[04:39] 对吧还有这种列表页面啊什么标准哎还有这种标准的列表页面啊等等然后呢还有一些什么搜索结果页啊什么成功页啊失败页啊他都有一些这种模板的页面我们都是不都可以去使用啊还有一些什么异常的页面啊403呢404啊还有500啊啊等等然后还有个人主页啊然后呢在这个位置呢还有可以切换我们的这个
[05:07] 切换我们的这个国际化的语言然后呢可以切换成英语对吧切换成英语你可以看看list它叫search table就是搜索这样的一个表格然后呢你可以再把它切回来简体中文然后呢像这个位置呢有可以做一些什么个人的设置对吧还有一些等等一些情况一些这个数据等等然后呢像这个位置可以做搜索也可以去看一下它的一些
[05:37] 消息通知等等所以它是一个基本上功能比较全面的这样的一个后台的系统左边这个菜单还可以把它折叠起来可以看一下可以把它去做一个折叠效果还是做的非常不错的非常不错的所以我们将会基于这个项目去做我们项目的一个开发好那么关于这个部署和安装我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何从 GitHub 下载 Ant Design Pro 项目、在 IntelliJ IDEA 中导入、安装依赖并启动本地开发服务器，展示其管理后台的前端界面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 Ant Design Pro 的表格组件页面，包含分页和筛选功能，右侧有“自定义选择项”说明，提示“默认不显示下拉框，设为 true 时显示默认选择框”。
画面 2：在 Typora 中打开课程笔记，显示文件目录结构，包含“code”文件夹，其中可见“ant-design-pro-master.zip”。
画面 3：解压“ant-design-pro-master.zip”，显示解压后的文件夹结构，包含“code”、“docs”、“public”、“src”等目录。
画面 4：在 Typora 中展示 Ant Design Pro 的项目目录结构，包含“config”、“src”、“tests”等文件夹，并提示“第一步：导入项目到 IDEA 中”。
画面 5：在 IntelliJ IDEA 中选择“Import project from external model”，并选择“Maven”。
画面 6：在 IntelliJ IDEA 的“Import Project”窗口中，项目名称设置为“ant-design-pro-master”，并选择“Maven”。
画面 7：在 IntelliJ IDEA 中打开项目，终端显示多个依赖包的警告信息，如“antd-theme-webpack-plugin”、“less”、“request”等。
画面 8：在终端中执行“yarn start”命令，启动项目，显示“yarn run v1.12.1”和“cross-env APP_TYPE=site umi dev”。
画面 9：展示 Ant Design Pro 的仪表盘页面，包含图表和数据，如“¥ 15,781”、“转化率”等。
画面 10：展示 Ant Design Pro 的表单页面，包含“截止日期”、“目标描述”、“客户”、“负责人”等字段。
画面 11：展示 Ant Design Pro 的 403 错误页面，提示“抱歉，你无权访问该页面”，并有“返回首页”按钮。
画面 12：展示 Ant Design Pro 的个人中心页面，点击“个人中心”后弹出菜单，包含“个人设置”、“退出登录”等选项。
画面 13：展示 Ant Design Pro 的仪表盘页面，包含“总销售额 ¥ 126,560”、“访问量 8,846”、“支付次数 6,560”等数据。
画面 14：在 Typora 中展示课程笔记，提示“第三步：进行初始化以及启动”，并显示“yarn install”和“yarn start”命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4：
```
Ant Design Pro提供项目目录如下：
1 config # 配置，包含路由，构建配置
2 mock # 模拟数据
3 public # 静态资源
4 src # 业务源码
5 assets # 业务通用图片
6 layouts # 通用布局
7 models # 全局 data model
8 pages # 业务页面入口和常用模板
9 services # 后端接口服务
10 utils # 工具类
11 locales # 国际化资源
12 global.css # 全局 CSS
13 global.js # 全局 JS
14 tests # 测试工具
15 package.json # 依赖包
```

画面 6：
```
Project name: ant-design-pro-master
Project location: F:\code\ant-design-pro-master
```

画面 7：
```
+ warning antd-theme-webpack-plugin > antd-theme-generator > less > request > hawk > hoek@82.16.3: This version is no longer maintained. Please upgrade to the latest version.
+ warning antd-theme-webpack-plugin > antd-theme-generator > less > request > hawk > sntp > hoek@82.16.3: This version is no longer maintained. Please upgrade to the latest version.
+ warning antd-theme-webpack-plugin > antd-theme-generator > less > request > hawk > boom > hoek@82.16.3: This version is no longer maintained. Please upgrade to the latest version.
+ warning enzyme > rat selector-parser > nearley > nomnom@1.6.2: Package no longer supported. Contact support@npmjs.com for more info.
+ warning eslint > file-entry-cache > flat-cache > circular-json@0.3.3: CircularJSON is in maintenance only, flattened is its successor.
```

画面 8：
```
F:\code\ant-design-pro-master>yarn start
yarn run v1.12.1
$ cross-env APP_TYPE=site umi dev
```

画面 14：
```
第三步：进行初始化以及启动
1 yarn install #安装相关依赖
2 yarn start #启动服务
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 4：PPT 标题为“Ant Design Pro提供项目目录如下”，并列出目录结构。
画面 6：PPT 标题为“第一步：导入项目到 IDEA 中”，并提示“Import project from external model”。
画面 14：PPT 标题为“第三步：进行初始化以及启动”，并列出“yarn install”和“yarn start”命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

