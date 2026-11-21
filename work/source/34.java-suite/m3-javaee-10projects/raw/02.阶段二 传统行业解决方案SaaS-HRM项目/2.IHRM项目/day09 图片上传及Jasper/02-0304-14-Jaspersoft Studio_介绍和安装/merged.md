# 14-Jaspersoft Studio：介绍和安装

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\14-Jaspersoft Studio：介绍和安装_【海量资源尽在 ubkz.com】.mp4
- 时长 6分44秒（音频 404s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的对这个开发的流程做了一个改述那我们都知道对于我们重点关注的就这么三点制作模板构造数据以及填充数据那这三个里面第一件事我们先来看一下它就是制作报表模板那制作报表模板可以借助Jasper Report官方提供的一个工具来完成那这个工具呢就是我们接下来要聊的模板工具Jasper Soft Studio
[00:32] 那先简单的对这个工具呢做一个介绍其实它就是Jasper Report这个公司提供的这么一个模板制作工具和我们这个Jasper Report配套使用那Jasper Report它是一套Java Lab包或者我们的Javajar 包通过Javajar 包在Java代码当中生成PDF那这个死丢丢工具它主要目的就是生成XML的模板代码或者对模板进行编译成
[01:02] JASPR文件的并且它还支持预览的一个操作所以对于这个工具是我们使用JASPR生成PDF必不可少的一个辅助工具这个辅助工具它是一个可视化的报表设计工具通过这个工具可以非常方便的以可视化的形式以拖拽的形式帮助我们去设计模板并且通过这个它还有很多的好处帮我们把模板编译
[01:33] 帮我们进行设计的一个预览那既然是一个工具就涉及到一个下载安装的这么一个过程那在讲义当中呢这边给各位准备了它的下载的官方网站的地址如果各位有兴趣的话去进行下载其实就可以了那其实这个资料呢也给各位都准备好了这边我想说一下如果有的朋友想去自己下载的话进入这个网站注意我们下载的是Jasper Soft Studio
[02:02] 下载的是这个当然了如果你不想去下载的话在我今天的资料当中有一个soft studio的安装包是我下载好的6.5版本的对于各位来说直接双击安装即可其实安装它比较简单就是傻瓜式无脑安装一路next点击下去直至安装成功就可以了
[02:29] 那我在这边呢已经把这个工具安装成功了那安装成功了之后我们打开它来看一下它的一个展示的效果OK就是Jazz Pro Support Studio这个打开相对来说有一点点慢啊各位耐心等待一下好了这边呢我已经把这个工具打开了那打开这个工具呢其实有的朋友立马就有的朋友就会说了这个工具很眼熟啊没错这个Jazz Pro
[03:02] soft studio它其实是基于Eclipse的引擎开发出来的所以如果之前你用过Eclipse这个工具其实对于各位来说使用起来就没有什么难度了在这边需要和各位简单的做一个工具里面的很多的这些比如说框框的一个介绍这些介绍在今天资料当中这个讲义当中都有
[03:27] 就是它的一个面板的一个说明这个面板呢一共分成了这么几块这么几块首先呢第一块就是左边叫做project那这一块呢是我们工程的一个面板也就是说呢你一会要创建一些自己的模板的时候可以以工程的形式体现出来那工程就浏览到这边OK那第一块内容我们看过了之后接着就是第二块继续往下移
[03:59] 叫做outline那这个outline代表的什么呢它其实指的是以竖形结构的形式以竖形结构的形式展示pdf当中的所有内容也就是展示我们模板当中的所有内容那除了这块之外那继续来看中间部分那中间部分呢其实是我们整个pdf相应的一块内容它是我们主要的一个编辑区域它能够通过拖拽通过定位
[04:30] 等等一些设计手段去设计我们PDF的一个模板好了那接下来这个主的设计区域底下呢各位会发现有三个按钮第一个design它是我们的设计视图设计视图那还有一个sourcesource指的是我们的源代码视图还有一个preview是我们的预览视图就这么三个视图那接下来除了中间这个部分之外还有右边那右边呢
[05:00] 其中第一个呢叫做blend那对于这个视图它究竟在做什么呢那其实通过这个视图呢它是我们一些按一些按钮那这些按钮是干嘛的是通过这些按钮以可视化的形式对我们的pdf进行编辑的比如说呢你想要填充一些静态的文字你拖住过来一个按钮过来那这边你就可以填写你自己想要的一些文字了
[05:35] 这个能理解吧比如说你想要图片拖拽过来一个其实就可以所以右边这边全部都是我们设计阶段的一些组件需要那些组件拖拽过来一个需要那些组件拖拽过来一个其实就可以了上边是一些基本的组件那底下是一些更加高级的一些组件这些组件里面比如说对于一个PDF来说可能有分页的一个支持它支持分页的一些内容那比如说呢底下总页数等等的一些内容比如说还有
[06:03] 当前时间那这个就不再多说了所以呢对于这个面板来说呢咱们做了一个简单的介绍我们重点关注的面板其实只有这么几块第一个主区域第二个就是这边的一些组件所以呢对于这个Studio工具
[06:23] 要想去使用还是比较简单的如果你有Eclipse基础的话我们关注的就是刚才和各位来聊的这几块如果说你对这个PDF工具如果说你对这个工具还是不太熟在这边讲义当中已经把这些基本的和各位有一个简单的说明关注一下咱们讲义当中的内容其实就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
介绍 JasperSoft Studio 报表工具的安装、界面组成及基本使用方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT第14页，标题为“4.3 开发流程概述”，子项包括“制作报表模板”、“模板解释”、“构造数据”，并引出“5 模板工具Jaspersoft Studio”章节。
画面2：展示PPT第15页，内容为“5.1 概述”，介绍JasperSoft Studio是基于Eclipse的报告设计器，支持多种数据源和输出格式。
画面3：展示PPT第15页，内容为“5.2 安装配置”，列出JasperReport官网下载页面的“Community Editions”选项，包括“JasperReports* Server CE v7.1.0”、“JasperReports* Library CE v6.7.0”、“Jaspersoft* Studio CE v6.6.0”和“iReport Designer CE v5.6.0”。
画面4：桌面截图，显示“黑马程序员”和“博学谷”标志，桌面上有“lhmm”和“test.html”等文件。
画面5：展示PPT第15页，标题为“5.3 面板介绍”，图示JasperSoft Studio界面，标注了“Project Explorer view”、“Report Editing Area”、“Designer Palette”、“Properties view”和“Outline view”。
画面6：展示JasperSoft Studio界面，详细标注了“Project Explorer view”、“Report Editing Area”、“Designer Palette”、“Properties view”和“Outline view”。
画面7：展示JasperSoft Studio界面，显示“Blank_A4.jrxml”报告设计界面，包含“Title”、“Page Header”、“Column Header”、“Detail 1”、“Column Footer”、“Page Footer”等区域。
画面8：在JasperSoft Studio界面中，选中一个矩形元素，显示其尺寸为“517 x 466”，位置为“R(0, (240, 240, 240))”。
画面9：在JasperSoft Studio界面中，显示“Blank_A4.jrxml”文件的XML代码，包含“<jasperReport>”、“<queryString>”、“<title>”、“<pageHeader>”、“<columnHeader>”、“<detail>”、“<columnFooter>”、“<pageFooter>”和“<summary>”等标签。
画面10：在JasperSoft Studio界面中，选中一个矩形元素，显示其尺寸为“14 x 26”，位置为“R(0, (240, 240, 240))”。
画面11：在JasperSoft Studio界面中，选中“Total Pages”元素，显示其尺寸为“351 x 120”。
画面12：在JasperSoft Studio界面中，选中“Total Pages”元素，显示其尺寸为“351 x 120”，并显示“Current Date”、“Time”、“Percentage”等选项。
画面13：展示PPT第15页，标题为“5.3 面板介绍”，图示JasperSoft Studio界面，标注了“Project Explorer view”、“Report Editing Area”、“Designer Palette”、“Properties view”和“Outline view”。
画面14：展示PPT第15页，标题为“5.4 基本使用”，内容包括“Report editing area”、“Repository Explorer view”、“Project Explorer view”、“Outline view”、“Properties view”、“Problems view”和“Report state summary”等面板的描述。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面9：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/jasperreports.xsd">
    <queryString>
        <![CDATA[]]>
    </queryString>
    <title>
        <band splitType="Stretch"/>
    </title>
    <pageHeader>
        <band height="70" splitType="Stretch"/>
    </pageHeader>
    <columnHeader>
        <band height="63" splitType="Stretch"/>
    </columnHeader>
    <detail>
        <band height="225" splitType="Stretch"/>
    </detail>
    <columnFooter>
        <band height="49" splitType="Stretch"/>
    </columnFooter>
    <pageFooter>
        <band height="54" splitType="Stretch"/>
    </pageFooter>
    <summary>
        <band height="42" splitType="Stretch"/>
    </summary>
    <jasperReports>
    </jasperReports>
</jasperReport>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面5：图示JasperSoft Studio界面，标注了“Project Explorer view”、“Report Editing Area”、“Designer Palette”、“Properties view”和“Outline view”。
画面6：图示JasperSoft Studio界面，标注了“Project Explorer view”、“Report Editing Area”、“Designer Palette”、“Properties view”和“Outline view”。
画面13：图示JasperSoft Studio界面，标注了“Project Explorer view”、“Report Editing Area”、“Designer Palette”、“Properties view”和“Outline view”。
画面14：内容包括“Report editing area”、“Repository Explorer view”、“Project Explorer view”、“Outline view”、“Properties view”、“Problems view”和“Report state summary”等面板的描述。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

