# 17-构造个人详情报表：需求说明

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\17-构造个人详情报表：需求说明_【海量资源尽在 ubkz.com】.mp4
- 时长 5分12秒（音频 312s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经完成了这些报表的基本的一个操作其中我们看了一下就是数据填充分组报表还有我们chart图表以及我们的副子报表其实这几个报表呢其实考量的就是这个Jasper Studio咱们的一个应用重点其实就是看一下这个图形化界面工具如何去填充数据比如说呢可以使用map的parameter的形式也可以使用我们jdbc链接当然还可以使用我们的一个史
[00:30] 对象的数字集合那对于分组报表来说呢其实分组报表它也有自己的应用场景比如说呢我们想要以分组的形式展示出不同的数据那还有一个呢就是我们常见的一些图表比如说呢柄状图数状图等等等等它都支持当然最后我们又来了一个复子报表
[00:50] 那其实通过这些报表呢咱们已经涵盖了一个应用当中的基本上大部分报表的一个情况那这些我们都讲过了之后接下来的就是最后一项咱们完成整个用户档案下载的这个工作那首先呢在这边呢我已经把当前我自己的工程呢已经打开了那打开了之后在这边呢我先把这些工程呢都一个一个给它跑起来简单的和各位来做一个需求方面的一个交代
[01:19] 好了这边呢在我们启动的过程当中啊首先呢千万要注意我们已经配置了Eureka那我们启动的其实就是先把Eureka服务先启动起来OKEureka服务启动起来了之后接着我们把系统微服务也启动起来这边系统微服务OK当然了除了系统微服务之外呢还有一个啊就是我们这边要用到一个员工管理的一个微服务员工管理微服务也给它启动哎启动一把
[01:58] 好了这边程序让他去启动那接着呢我简单的和各位来聊一下就是我们这个个人信息的一个打印那其中呢我们之前看过一个就是员工的一个个人信息个人信息那我们要做的事情呢就是可以提供一个按钮点击按钮去下载员工的我们叫做pdfpdf详情资料就去完成这么一个需求
[02:35] 那我们这个员工PDF的详情资料呢其实对于我们来说呢都比较简单并且呢在今天的资料当中我也把所需要的咱们的这个PDF报表的基本的这个SML呢给它构造出来了那我们可以打开它或者把它引入到我们这个工程当中和各位简单的来看一下Control V引过来了我叫做Profile就是员工的详情资料
[03:06] 那还知道我们去创建一个PDF的时候呢首先的第一步是不是去把这个模板给它构造出来了那这个模板呢其实非常简单它不难但是呢比较繁琐当然了我这个还是做的比较简略的这么一个版本好了打开呢简单的来看一下那首先
[03:24] 对于我们而言左边是用户的一张头像信息那这边的有用户的名称电话公号和所属部门那底下就是教育信息他的最高学历他的毕业学校他的专业和毕业时间底下就是一个工作经历那其实跟我们的跟我们的程序展示出来的内容其实差不多了当然底下还有岗位的信息那这些内容我用什么进行构建的呢是这样的各位会看到里面的全部都是$P大括号的这种形式
[03:52] 所以各位就应该知道了我一会要往里填充数据的时候是不是全部把数据放到parameter也就是放到一个map当中给我传递过来那咱们看一下它的一个基本的一个效果这边preview可以自己去填充内容当然我就不填了咱们执行一把你会发现我要搞到的效果其实就是这样基本上就是员工的一个基本简历了OK那我现在的程序已经跑起来了那接下来咱们打开浏览器登录到我们的系统
[04:21] 一起来看一下我要完成的这个工程是什么样子456走刚才有一个登录失败可能是密码写错了好这边123456走好了各位来看现在呢登录进来之后这边有一个员工那员工呢其中可以查看一下员工的详细情况那这边呢比如说我要完成的功能就是在这边员工详细情面这边呢可以给他构建一个按钮
[04:50] 点击按钮去下载员工的PDF详情的这么一个报表文件OK好了这个就是跟各位来简单的聊了一下我们这个需求那其实需求比较清晰了这边搞一个按钮一点击按钮下载一个文件构造成刚才我们看到的PDF的这种形式

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iReport Studio 中设计和预览包含子报表的复杂报表，并结合后端 Java 项目结构与数据库实体类进行数据展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 iReport Studio 中“父子报表”章节的 PPT 内容，说明制作父报表和子报表的基本概念。
画面 2: 在 IntelliJ IDEA 中展示 `UserCompanyPersonal.java` 实体类代码，包含 JPA 注解和字段定义。
画面 3: 在 IntelliJ IDEA 中展示项目结构，选中 `EurekaServer` 类。
画面 4: 在 IntelliJ IDEA 中展示 `EurekaServer.java` 代码，包含 `@SpringBootApplication` 和 `@EnableEurekaServer` 注解。
画面 5: 在 IntelliJ IDEA 中展示项目结构，选中 `ihrm_system` 模块。
画面 6: 在 IntelliJ IDEA 中展示 `EmployeeApplication.java` 代码，包含 `@SpringBootApplication`、`@EntityScan` 和 `@EnableEurekaClient` 注解。
画面 7: 展示 Microsoft Visio 的空白绘图界面。
画面 8: 在 iReport Studio 中打开 `main.jrxml` 报表设计文件，显示“Main report”设计视图和“Report: main”属性面板。
画面 9: 在 iReport Studio 中编辑 `profile.jrxml` 报表，显示“学历”、“专业”、“毕业学校”、“毕业时间”等字段。
画面 10: 在 iReport Studio 中编辑 `profile.jrxml` 报表，选中“Band: Detail 1”并显示其尺寸为 155px。
画面 11: 在 iReport Studio 中预览 `profile.jrxml` 报表，显示“Page 1 of 1”。
画面 12: 在浏览器中显示 iHRM 后台登录页面，包含用户名和密码输入框。
画面 13: 在浏览器中显示 iHRM 后台的“个人详情”页面，包含员工照片和基本信息。
画面 14: 在 iReport Studio 中预览 `profile.jrxml` 报表，显示“教育信息”、“工作信息”、“岗位信息”等字段内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package com.ihrm.domain.employees;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonRootName;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonUnwrapped;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.annotation.JsonView;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml

