# 画面线理解：15.Ant Design Pro入门之部署安装

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day02-Ant Design以及Ant Design Pro入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day02-Ant Design以及Ant Design Pro入门\15.Ant Design Pro入门之部署安装【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:20, 00:37, 00:55, 01:57, 02:20, 02:54, 03:37, 04:16, 04:35, 04:55, 05:28, 05:51, 06:03
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 20:22:18

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
