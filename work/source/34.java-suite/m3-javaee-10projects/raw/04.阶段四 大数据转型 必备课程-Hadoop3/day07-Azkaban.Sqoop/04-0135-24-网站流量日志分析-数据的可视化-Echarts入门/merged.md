# 24-网站流量日志分析-数据的可视化-Echarts入门

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\24-网站流量日志分析-数据的可视化-Echarts入门【海量资源尽在 ubkz.com】.mp4
- 时长 5分41秒（音频 341s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习这个案例的最后一部分也就是数据的一个可视化我们在Hive的内部对数据做了一些分析并且把它的一些分析的结果通过scope导出到MySQL最后我们可以把MySQL的数据展现到一些web页面上然后来看它的一个最终的结果接下来我们来看如何去实现一个可视化
[00:30] 来看一下好那么实现可视化呢我们需要用一些可视化的工具在这里呢我们用的工具叫Eachas这个Eachas呢是使用率比较高的一种可视化工具这个工具呢我们来先来在官网上看一下它的一个简单的介绍来复制一下打开百度在这里我们来看一下Eachas看一下它的官网稍等好正在加载好这是Eachas的一个官网
[01:03] 在这个官网里边呢有很多的一些有很多的一些案例我们来看一下官方的实例好了我们打开这个实例了打开之后你会发现左边呢有一个列表有什么折线图注装图那这个呢比如说我们打一个折线图它呢就可以呢将我们的一些数据呢通过图形化的方式展示到页面上我点下这个折线图好点开我们来看一下右边呢是一个折线图
[01:34] 这个折线图是怎么去画出来的话你看左边左边有一个一个json格式的一个数据结构OK那么这个数据结构里边呢有x种这是一个x种还有y种还有它携带的一些数据好那么通过这三个参数呢它就可以把这个图呢给它画出来比如说在这个地方呢我可以改这个值比如说我改成820我改成900你看它这个图呢在变
[02:04] OK那么也就是说我们只要准备了这么一个json数据我们使用一掐锁就能够把这个图呢画出来我们的目的是干嘛呢来打开我们的数据库在数据库呢有个weblogview这里边有两张表这两张表的数据呢是从我们Hive分析之后呢导出来的我们需要呢将这个数据库两张表的数据呢把它通过一个图形化的一个界面呢把它展示出来
[02:33] 我们可以展示一个柱状图或者说折线图而数据呢就来自这两张表我们要做这么一件事情做这个事情之前呢我们来先了解一下一下子来我们可以自己做这么一个界面把这个图呢展现出来回到我们的ID好在ID里边呢有一个来看有一个我们的一个一个model在这里呢我已经给大家写好了好在这里我们来看一下
[03:01] 在我们的这里边有一个web项目这个web项目这个web项目里边我把其他的先合上先合上OK在这里呢有一个页面这个页面在web app下面web app下面有个index.jsp好这个页面那这个页面的话呢它其实就是一个简单的e-chars一个图形的表示方式你看我们要简单的去显示一个最简单的折线图怎么做呢
[03:30] 我们在这里写一个JSB在这个里边呢我们来写一个DIV标签这个DIV呢是用来显示那个折线图的宽和高分别是600和400那么在这里呢我要写一个JSDRIP的JS代码这个JS代码呢要写之前呢需要导入一个echars的一个JS文件OK导入之后呢我们如何去显示那个折线图需要做三步第一步我们
[04:00] 对一恰似要做一个初始化要做一个初始化就这句话第二呢我们要准备一个数据项这个数据项这是他的一个title题目还有呢X种Y种呢他没有还有呢他写的一些数据OK那么这是第二步第三步呢我们需要调一个方法用mychat就这个然后呢调一个方法叫set option把我们的option数据给他这个时候
[04:30] 我们就能显示出来折线图来这样子我把我这个代码呢部署到Tomcat上好我这里呢已经有一个web项目部署到Tomcat我们来访问一下好稍等那么访问的话因为它是个index的JSP默认的应该就是首页好了它已经把这个图呢展现出来了我们来看一下这就是我这个呃首页index它就是一个注装图在这里呢你看每一个注装图呢放上去之后呢
[04:59] 都有一个这个销量然后一个商品的名字后面上跟上一个数字OK这就是一个柱状图也就是说我们如果想显示一个柱状图是非常简单的我们只需要按照它的固定的一些固定的一些步骤来做重点是什么呢重点是我需要给它提供这些参数那么我们可以干嘛呢可以从数据库中把这些数据读出来放在这个位置
[05:28] 那么它显示的这个助长图或者说折线图是不是就按照我们的要求OK那这是我们的一个简单的对E-CHARDS的一个演示我们先把这个视频先暂停一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java Web 项目中集成 ECharts 图表库，通过配置数据和选项在前端页面展示柱状图。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PPT，标题为“七、模块开发---数据可视化”，子标题“1. ECharts 介绍”，内容介绍 ECharts 是由百度前端技术部开发的 JavaScript 数据可视化库，支持多种图表类型。
画面 2: 浏览器打开百度搜索结果页面，显示多个与 ECharts 相关的链接。
画面 3: 浏览器访问 ECharts 官网（https://echarts.baidu.com），点击“文档”菜单，展示官网导航结构。
画面 4: 浏览器打开 ECharts 官方示例页面，展示一个折线图的代码和图表，代码为：
```javascript
option = {
    title: {
        text: '折线图'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name: '销量',
        type: 'line',
        data: [820, 932, 901, 934, 1200, 1130, 1198]
    }]
};
```
画面 5: 数据库管理工具（SQLyog）界面，显示数据库表结构和 SQL 语句，SQL 语句为：
```sql
GRANT ALL PRIVILEGES ON . TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
FLUSH PRIVILEGES;
TRUNCATE emp_out;
```
画面 6: IntelliJ IDEA 项目结构视图，显示项目目录结构，包含 `weblog` 包下的 `Controller`、`Mapper` 和 `pojo` 子包。
画面 7: IntelliJ IDEA 项目结构视图，鼠标悬停在 `weblog` 包上，展示其子目录结构。
画面 8: IntelliJ IDEA 编辑器中打开 `index.jsp` 文件，显示 HTML 和 JavaScript 代码，代码为：
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<html>
<head>
<script src="js/echarts.min.js"></script>
<div id="main" style="..."></div>
</head>
<body>
<script type="text/javascript">
// 基于准备好的DOM，初始化Echarts实例
var mychart = echarts.init(document.getElementById('main'));
// 指定图表的配置项和数据
var option = {
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};
</script>
</body>
</html>
```
画面 9: IntelliJ IDEA 编辑器中，代码高亮显示，光标在 `xAxis` 的 `data` 数组中。
画面 10: IntelliJ IDEA 编辑器中，光标在 `yAxis` 的 `data` 数组中，代码为：
```javascript
yAxis: {},
data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
```
画面 11: IntelliJ IDEA 编辑器中，代码高亮显示，光标在 `series` 的 `data` 数组中。
画面 12: 浏览器显示 ECharts 图表页面，图表为柱状图，标题为“ECharts 入门示例”，显示数据。
画面 13: IntelliJ IDEA 编辑器中，代码高亮显示，光标在 `legend` 的 `data` 数组中。
画面 14: IntelliJ IDEA 编辑器中，代码高亮显示，光标在 `series` 的 `data` 数组中，数据为 `[5, 20, 36, 10, 10, 24]`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4:
```javascript
option = {
    title: {
        text: '折线图'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        name: '销量',
        type: 'line',
        data: [820, 932, 901, 934, 1200, 1130, 1198]
    }]
};
```
画面 5:
```sql
GRANT ALL PRIVILEGES ON . TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
FLUSH PRIVILEGES;
TRUNCATE emp_out;
```
画面 8:
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<html>
<head>
<script src="js/echarts.min.js"></script>
<div id="main" style="..."></div>
</head>
<body>
<script type="text/javascript">
// 基于准备好的DOM，初始化Echarts实例
var mychart = echarts.init(document.getElementById('main'));
// 指定图表的配置项和数据
var option = {
    title: {
        text: 'ECharts 入门示例'
    },
    tooltip: {},
    legend: {
        data: ['销量']
    },
    xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
};
</script>
</body>
</html>
```
画面 14:
```javascript
data: [5, 20, 36, 10, 10, 24]
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“七、模块开发---数据可视化”，子标题“1. ECharts 介绍”，内容介绍 ECharts 是由百度前端技术部开发的 JavaScript 数据可视化库，支持多种图表类型。
画面 3: ECharts 官网导航结构，包含“文档”、“下载”、“实例”、“工具”、“关于”等菜单项。
画面 8: 代码中包含 ECharts 的配置项和数据，用于生成柱状图。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

