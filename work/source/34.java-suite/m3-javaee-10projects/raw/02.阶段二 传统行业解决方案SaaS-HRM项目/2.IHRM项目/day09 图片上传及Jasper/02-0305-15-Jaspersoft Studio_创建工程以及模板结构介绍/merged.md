# 15-Jaspersoft Studio：创建工程以及模板结构介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\15-Jaspersoft Studio：创建工程以及模板结构介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 4分35秒（音频 276s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 把这个Jasper Studio安装好了之后接下来我们就可以通过Jasper Studio去创建一个基本的PDF模板那我们如何去做呢是这样的对于这个Jasper Studio它是以工程的形式来进行创建那我应该先去创建一个工程那如果各位有Eclipse基础的话那就比较简单了好了这边点击Fill找到这边的New好了我们可以创建一个Project来一个工程好了这个工程呢
[00:32] 可以让我们的选择选择什么就是找到Jasper ReportsJasper Reports ProjectOK点击Next在这边呢我们可以选择你工程的名称比如说呢我就叫做Test ReportsR-E-P-O-R-T-SOK接着点击Finish那工程创建出来之后那里面呢我们就可以去创建一个我们叫做PDF的模板
[01:00] 那这个模板怎么去创建也不难在这边右键创建一个Jasper ReportOK那创建一个Jasper Report这边呢有很多的模板它自带的一些模板可以让我们进行选择那其实这些模板呢咱们用它主要是用里面的一些样式比如说你想用这种好看的样式你就去选择就可以了当然我这边就用一个标准的A4打印纸的这么一种空白的一个样式来做了OK点击Next
[01:30] 那这边这边我们需要各位关注的是你这个创建的这个名称究竟是什么我们可以自己随便选择比如说呢就叫Test就Test好了接着点击Next注意这边呢Next之后它让你去进行一个选择那这个选择选择的是什么注意选择的是数据的填充方式
[01:53] 那我们的数据填充方式对于我来说我这边就用empty record就是说咱们第一个案例不填充任何数据主要是快速的看一下这个工具如何去使用就可以了OK接着点击finish好了这样一来呢咱们就已经创建了一个Jasper Report的这么一个基本的模板那在这个模板里面各位能够看到里面有一些比较浅的这么一些字那这些字呢它其实是通过把一个模板分成不同的区域
[02:22] 来让我们进行设计的那这个区域一共分为这么几块当然了这些区域你可以自己指定你不想要它删掉其实也可以那需要把这些区域呢和各位简单的介绍一下第一个就是title那title呢顾名之意它其实就是标题那这个标题呢在每一个一个pdf里面比如说以我这个讲义来举例以我这个讲义来举例那一个pdf里面首先标题部分那这个标题各位都知道了
[02:51] 一个PDF里面标题是不是只出现在第一页当中其实就可以啊没错吧OK那这个标题我们做过一个介绍那接下来还有一个叫做page header那这个page header指的是每页当中的一个头比如说我们这个讲义当中每页里面都出现了这么一个头能理解吧OK那除了这个之外接着最底下对应的一个是page footer那这个page footer是每页都要显示的这么一个尾
[03:19] 这两个是对应的那接着呢咱们继续再来还有column header那这个column header代表什么意思那它指的是如果说啊你这个pdf里面可能会以table也就是表格的形式来进行展示那进行表格形式展示的时候是不是一般都有一个表格头底下可能会有一个表格的一个尾啊那中间是不是就是我们表格所有的表格数据没错吧所以对于这个来说呢
[03:50] 指的是表格头底下表格尾中间指的是表格的数据当然了这个表格数据说的有点犯法其实除了表格数据呢你还可以填充真正PDF的正文这块内容叫做Detail那接下来最后一个SamuraiSamurai呢指的是统计摘要它指的是表格的一些表格的一些合计的一些字段那这个Samurai呢一般是出现在一个PDF里面最结束的最后这一页
[04:16] 比如说呢咱们讲义当中可能都有一个总结的一个部分总结的一个部分一般都是放到最后一页嘛能理解吧OK这个就是简单的和各位来看了一下如何去创建一个工程创建一个我们叫做JazportReport这么一个模板那以及里面这几块区域

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 JasperSoft Studio 创建并设计一个 JasperReports 报表，包括新建项目、选择模板、配置数据源和设计报表结构。

2) 按时间顺序列出每张画面的要点：
画面1：在 JasperSoft Studio 中，新建项目，项目名为 "Project..."。
画面2：项目中创建了一个名为 "jasperReport" 的报表文件。
画面3：在 "New Report Wizard" 中，选择 "Report Templates"，当前选中 "All" 分类。
画面4：在 "New Report Wizard" 中，选择 "Blank A4" 模板。
画面5：在 "New Report Wizard" 中，切换到 "Cherry" 模板分类，选中 "Cherry" 模板。
画面6：在 "New Report Wizard" 的 "Data Source" 页面，选择数据源 "Sample DB - Database JDBC Connection"。
画面7：进入报表设计界面，显示 "test.jrxml" 报表的结构，包含 Title、Page Header、Column Header、Detail 1、Column Footer、Page Footer、Summary 等区域。
画面8：切换到 PPT 页面，标题为 "4.3 开发流程概述"，子标题为 "5 模板工具Jaspersoft Studio"。
画面9：切换到 PPT 页面，标题为 "第9章 文件上传与PDF报表入门"，子标题为 "1 图片上传"。
画面10：在 PPT 页面中，展示 "data:text/plain,文本数据" 及其后跟的多种 data URI 格式。
画面11：在 PPT 页面中，选中 "data:text/html;base64,base64编码的html代码" 这一行。
画面12：在 PPT 页面中，展示完整的 data URI 格式列表，包括 text/plain、text/html、text/css、text/javascript、image/gif、image/png、image/jpeg、image/x-icon。
画面13：在 PPT 页面中，选中 "data:image/jpeg;base64,base64编码的jpeg图片数据" 这一行。
画面14：回到 JasperSoft Studio，显示 "test.jrxml" 报表设计界面，鼠标悬停在 "Page Footer" 区域。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
无

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：标题 "4.3 开发流程概述"，子标题 "5 模板工具Jaspersoft Studio"。
画面9：标题 "第9章 文件上传与PDF报表入门"，子标题 "1 图片上传"。
画面10：内容为 "data:text/plain,文本数据" 及其后跟的多种 data URI 格式。
画面11：选中 "data:text/html;base64,base64编码的html代码"。
画面12：完整列出 data URI 格式：
data:text/plain,文本数据
data:text/html,html代码
data:text/html;base64,base64编码的html代码
data:text/css,css代码
data:text/css;base64,base64编码的css代码
data:text/javascript,javascript代码
data:text/javascript;base64,base64编码的javascript代码
data:image/gif;base64,base64编码的gif图片数据
data:image/png;base64,base64编码的png图片数据
data:image/jpeg;base64,base64编码的jpeg图片数据
data:image/x-icon;base64,base64编码的icon图片数据
画面13：选中 "data:image/jpeg;base64,base64编码的jpeg图片数据"。
画面14：无 PPT 内容。

5) 不要评价画面美观，不要输出与课程无关的内容。
无

