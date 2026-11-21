# 画面线理解：07.前台系统之工程搭建以及启动服务

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\07.前台系统之工程搭建以及启动服务【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:20, 01:53, 02:20, 02:48, 03:14, 03:57, 04:09, 05:11, 06:06, 06:25, 06:55, 08:07, 08:23, 08:41
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:09:49

1) 这一组画面整体在讲什么（一句话）：
讲解如何搭建并运行一个基于 React + semantic-ui 的前端项目，包括解压项目、安装依赖和启动服务。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：PDF文档第17页，标题“2、搭建前台系统”，内容说明前台系统采用React+semantic-ui实现移动端Web展示，后期可打包成App。
画面2：PDF文档第17页，标题“2.1、搭建工程”，内容说明第一步是将资料中的“haoke-web.zip”解压到项目目录，路径为“F:\code\itcast-haoke\itcast-haoke-web”。
画面3：桌面显示文件资源管理器，打开“itcast-haoke”文件夹，展示项目结构，包含多个子文件夹如“itcast-dubbo”、“itcast-graphql”等。
画面4：PDF文档第17页，标题“2.1、搭建工程”，内容重复说明第一步解压路径。
画面5：IntelliJ IDEA界面，显示“itcast-graphql-java-2”项目结构，代码编辑器中展示GraphQlSchema生成代码。
画面6：IntelliJ IDEA界面，显示“itcast-haoke-web”项目结构，编辑器中展示package.json文件内容。
画面7：IntelliJ IDEA界面，显示“itcast-haoke-web”项目结构，终端中显示当前路径“F:\code\itcast-haoke\itcast-haoke-web”。
画面8：IntelliJ IDEA界面，终端中执行“npm install”命令，显示安装依赖包的过程。
画面9：浏览器显示“localhost:9000”，页面为空白。
画面10：浏览器显示“localhost:9000”，页面显示登录界面，包含用户名和密码输入框及登录按钮。
画面11：浏览器显示“localhost:9000”，页面显示登录界面，右上角显示设备选择菜单，包括iPhone 6/7/8 Plus等选项。
画面12：PDF文档第15页，展示登录界面截图，与画面10内容一致。
画面13：PDF文档第17页，内容重复说明第一步解压路径。
画面14：PDF文档第14页，展示项目结构图，说明第三步执行命令初始化并导入依赖包，命令为“npm install”和“npm start”，输入地址为“http://localhost:9000/”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面5代码：
```java
// 生成Schema graphQLSchema = new SchemaGenerator().makeExecutableSchema();
// 根据Schema对象生成GraphQL对象
GraphQL graphQL = GraphQL.newGraphQL(graphQLSchema).build();
String query = "{user(id:100){id,name,age,card(cardNumber)}}";
ExecutionResult result = graphQL.execute(query);
System.out.println("query:" + query);
System.out.println(result.toSpecification());
```

画面6配置：
```json
{
  "name": "myhome",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "antd-mobile": "^2.1.10",
    "axios": "^0.18.0",
    "echarts": "^4.1.0",
    "echarts-for-react": "^2.0.13",
    "iscroll": "^5.2.0",
    "iscroll-luo": "^1.2.3",
    "nuka-carousel": "^4.2.3",
    "react": "^16.3.2",
    "react-avatar-editor": "^11.0.4",
    "react-dom": "^16.3.2",
    "react-image-gallery": "^0.8.12",
    "react-responsive-carousel": "^3.1.41",
    "react-router-dom": "^4.3.1",
    "react-scripts": "1.1.4",
    "react-touch-loader": "^1.1.4",
    "semantic-ui-css": "^2.3.2",
    "semantic-ui-react": "^0.81.2"
  },
  "scripts": {
  }
}
```

画面8命令：
```bash
> uglifyjs-webpack-plugin@0.4.6 postinstall F:\code\itcast-haoke\itcast-haoke-web\node_modules\uglifyjs-webpack-plugin
> node lib/post_install.js
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fs-events@1.2.4 (node_modules\fs-events):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fs-events@1.2.4: wanted {"os":"darwin","arch":"any"} (current: {"os":"win32","arch":"x64"})
```

画面14命令：
```bash
第三步，执行命令进行初始化和导入相关依赖包
1. npm install  #安装依赖
2. npm start  #启动服务
输入地址：http://localhost:9000/
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1标题：“2、搭建前台系统”。
画面2标题：“2.1、搭建工程”。
画面14标题：“第三步，执行命令进行初始化和导入相关依赖包”。
画面14结构：列出两个命令“npm install”和“npm start”，并注明输入地址“http://localhost:9000/”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
