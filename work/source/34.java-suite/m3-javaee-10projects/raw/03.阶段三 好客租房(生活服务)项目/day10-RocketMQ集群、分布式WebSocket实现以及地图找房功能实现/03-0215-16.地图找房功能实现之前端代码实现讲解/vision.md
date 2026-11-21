# 画面线理解：16.地图找房功能实现之前端代码实现讲解

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现
- 源文件：03.阶段三 好客租房(生活服务)项目\day10-RocketMQ集群、分布式WebSocket实现以及地图找房功能实现\16.地图找房功能实现之前端代码实现讲解【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:36, 01:06, 01:26, 01:50, 02:06, 02:40, 02:53, 03:12, 03:36, 03:50, 04:03, 04:19, 04:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 22:21:07

1) 这一组画面整体在讲什么（一句话）：
演示如何在前端项目中集成百度地图API，并改造数据加载方式以实现地图上的房源点位展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示PDF文档中“5.1、前端实现”章节，说明地图使用百度地图API，具体代码实现位于“maphouse.js”文件。
画面 2: 在IntelliJ IDEA中，通过“File”菜单选择“Open”来打开项目。
画面 3: 在IntelliJ IDEA中打开“itcast-haoke-manage-api-server”项目，查看“haoke.graphqls”文件中的GraphQL Schema定义，其中包含HouseResources类型。
画面 4: 在桌面打开“讲义.pdf”文件。
画面 5: 在IntelliJ IDEA的终端中执行命令启动前端项目：`myhome80.1.0 start F:\code\itcast-haoke\itcast-haoke-web` 和 `set PORT=9000 && react-scripts start`。
画面 6: 在浏览器中访问前端应用，显示登录页面，用户输入用户名和密码后点击“登录”按钮。
画面 7: 登录后页面显示“Loading”状态，等待数据加载。
画面 8: 在IntelliJ IDEA中查看“itcast-haoke-manage-api-server”项目的日志，显示Dubbo服务启动成功。
画面 9: 浏览器中前端应用加载完成，显示房源列表页面，包含房源图片和多个功能按钮。
画面 10: 在IntelliJ IDEA中打开“maphouse.js”文件，查看地图坐标数据。
画面 11: 在“maphouse.js”文件中，将静态的测试数据注释掉。
画面 12: 浏览器中前端应用成功加载百度地图，显示多个房源标记点。
画面 13: 在IntelliJ IDEA中打开“index.html”文件，查看其中包含的百度地图API脚本引用。
画面 14: 展示PDF文档中“5.2、改造数据的加载方式”章节，说明需要将静态数据改为加载后台数据的方式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```graphql
type HouseResources {
  id:Long!
  title:String
  estateId:Long
  buildingNum:String
  buildingUnit:String
  buildingFloorNum:String
  rent:Int
  rentMethod:Int
  paymentMethod:Int
  houseType:String
  coveredArea:String
  useArea:String
  floor:String
}
```

画面 5:
```bash
> myhome80.1.0 start F:\code\itcast-haoke\itcast-haoke-web
> set PORT=9000 && react-scripts start
Starting the development server...
```

画面 10:
```javascript
// 测试数据
var xy = [
  {
    'x': 116.350444,
    'y': 39.931645
  },
  {
    'x': 116.351684,
    'y': 39.9167
  },
  {
    'x': 116.357253,
    'y': 39.923152
  },
  {
    'x': 116.354954,
    'y': 39.935767
  },
  {
    'x': 116.36233,
    'y': 39.93839
  },
  {
    'x': 116.374249,
    'y': 39.93839
  }
];
```

画面 13:
```html
<link rel="shortcut icon" href="%PUBLIC_URL%/favicon.ico">
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0">
<script type="text/javascript" src="http://api.map.baidu.com/library/MapHouse/1.0.0/MapHouse-min.js">
<title>React App</title>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT标题为“5.1、前端实现”，副标题“地图使用的是百度地图api，具体代码实现：”，并展示目录结构图，其中“maphouse.js”被高亮。
画面 14: PPT标题为“5.2、改造数据的加载方式”，并显示公司地址和电话。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
