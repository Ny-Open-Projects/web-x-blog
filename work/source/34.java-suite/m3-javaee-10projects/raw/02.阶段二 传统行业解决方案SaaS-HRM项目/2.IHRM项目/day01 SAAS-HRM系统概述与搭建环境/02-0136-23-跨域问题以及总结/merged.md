# 23-跨域问题以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\23-跨域问题以及总结_【海量资源尽在 ubkz.com】.mp4
- 时长 3分57秒（音频 237s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了到目前为止呢我们基本的这些都跟各位都说过了当然了还有最后一点叫做跨域处理那需要跟各位解释一下这跨域处理究竟是什么意思啊那我们刚才测试的时候看着好像没什么问题那这边以张图形的形式跟各位来聊一下我们这个SaaS平台的人力资源管理系统它是前后端分离那这边呢代表的是我们的前端工程那前端工程最终你部署
[00:33] 这时候可能会给它的一个域名让用户去访问比如说3w.abc.com那这个工程前端它会发送请求发送到我们的后端服务上这个代表的是我们的后端微服务那后端微服务其实就是我们公司的某一个服务器的一个地址或者这边只有它的IP那这个时候就有问题了
[01:03] 那前端是一个域名后面是一个IP可能他们根本就不是在一个IP段上并且前面是有域名后面没有域名所以你请求过程当中你请求过来必然会有一个问题就是跨域跨过了不同的域名或者跨P跨过了不同的网段那我们在微服务这一桩就应该想方设法的去把这个跨域问题给它解决掉那解决这个问题呢很简单
[01:33] 只需要找到我们的工程在我们的Controller最上方加一注解这个注解叫做eta cross orange这个注解主要目的就是解决跨域问题的OK那这样一来配置好了之后那你再去访问就没什么问题了OK那到目前为止呢咱们今天的所有内容就跟各位都讲过了
[02:07] 那对于我们今天呢,首先需要各位能够了解SaaS的一些基本概念,包括什么叫做IaaS,PaaS和SaaS,那其中SaaS和这三个这两个什么IaaS,PaaS它的区别,那对于我们现在完成的是一个基于SaaS的人力资源管理系统,那基于SaaS人力资源管理系统,
[02:31] 只要企业付费都能够用我们这个提供的平台完成各个企业的人力资源管理那我们怎么能把一个工程从无到有给它构造出来借助的是原型分析法构造出我们的原型那有了原型在我们成员看来他太关注细节我们成员先把整个的功能模块先给它构造出来我们借助的是UML用力图的形式以更加直观成员都能够认识的语言
[03:00] 来体现出系统的功能模块当然我们画用力图用了一个工具叫做Power Designer那这些基本的概念我们讲过了之后呢还需要各位要知道我们这个系统的一个架构前后端分离的方式前端分离的方式前端就是VOE生态圈后端Spring圈压筒那这些都搞定了之后希望各位自己能够去搭建一个环境实现出我们企业
[03:30] 基本微幅的增伤改查当然了在增伤改查都行过了之后呢这边有一个公共异常处理公共异常处理其实很简单借助两个注解配置到一个类上和方法上就能对企业就能对业务过程当中出现的所有异常做处理当然了也可能自定义常也可以去做那最后补充了一个跨域处理很简单一个注解ETA cross orange就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 SaaS-HRM 系统的架构设计与开发准备，包括跨域处理、原型分析法、UML 用例图、技术架构等内容。

2) 按时间顺序列出每张画面的要点：
画面1：展示 Java 代码，定义了自定义异常类 `CommonException`，并配置公共异常处理。
画面2：PPT 页面，标题为“5.4 跨域处理”，内容解释跨域问题及解决方案。
画面3：空白画布，准备绘制流程图。
画面4：画布上绘制了“前端工程 www.abc.com”的椭圆形节点。
画面5：在椭圆形节点右侧添加了“后端微服务”的矩形节点，并用箭头连接。
画面6：在前端与后端之间添加了“跨域问题”的文字标注。
画面7：IntelliJ IDEA 编辑器，展示 `CompanyController.java` 文件，其中包含 Spring MVC 注解和异常处理相关代码。
画面8：PPT 页面，标题为“5.4 跨域处理”，目录导航显示当前章节。
画面9：PPT 页面，标题为“1.1.3 SaaS（软件即服务）”，内容介绍 SaaS 概念。
画面10：PPT 页面，展示 SaaS-HRM 系统的原型界面截图，包含工作日历和导航栏。
画面11：PPT 页面，标题为“2.2 原型分析法”，内容解释原型分析法的概念。
画面12：PPT 页面，标题为“2.3.3 需求分析软件”，介绍 Power Designer 工具并列出使用步骤。
画面13：PPT 页面，展示技术架构图，包含前端、接口文档、后端和 Swagger 组件。
画面14：PPT 页面，标题为“5.4 跨域处理”，目录导航显示当前章节。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1：
```java
package com.ihrm.common.exception;

import com.ihrm.common.entity.ResultCode;
import lombok.Getter;

@Getter
public class CommonException extends RuntimeException {
    private static final long serialVersionUID = 1L;

    private ResultCode code = ResultCode.SERVER_ERROR;

    public CommonException() {
    }

    public CommonException(ResultCode resultCode) {
        super(resultcode.message());
        this.code = resultCode;
    }
}
```

画面7：
```java
package com.ihrm.common.Controller;

import com.ihrm.common.entity.Result;
import com.ihrm.common.exception.CommonException;
import com.ihrm.domain.company.Company;
import com.ihrm.Service.CompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/company")
public class CompanyController {

    @Autowired
    private CompanyService companyService;

    @GetMapping("/list")
    public Result list() {
        List<Company> list = companyService.list();
        return Result.ok(list);
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2：
标题：5.4 跨域处理
内容：跨域是什么？浏览器从一个域名的网页去请求另一个域名的资源时，域名、端口、协议任一不同，都是跨域。我们是采用前后端分离开发的，也是前后端分离部署的，必然存在跨域问题。怎么解决跨域？很简单，只需要在 Controller 类上添加注解 @CrossOrigin 即可！这个注解其实是 CORS 的实现。CORS(Cross-Origin Resource Sharing) 跨域资源共享是 W3C 出的一个标准，其意思是使用自定义的 HTTP 头部让浏览器与服务器进行沟通，从而决定请求或响应是应该成功，还是应该失败。因此，要想实现 CORS 进行跨域，需要对服务器进行一些设置，同时前端也需要做一些配置和分析。本文简单的对服务器的配置和前端的一些设置进行分析。

画面5：
结构：前端工程（椭圆形） → 后端微服务（矩形）

画面6：
结构：前端工程（椭圆形） → 后端微服务（矩形），中间标注“跨域问题”

画面13：
结构：前端（蓝色圆形） → 接口文档（橙色八边形） ← 后端（蓝色圆形），接口文档 → Swagger（蓝色矩形）

5) 无

