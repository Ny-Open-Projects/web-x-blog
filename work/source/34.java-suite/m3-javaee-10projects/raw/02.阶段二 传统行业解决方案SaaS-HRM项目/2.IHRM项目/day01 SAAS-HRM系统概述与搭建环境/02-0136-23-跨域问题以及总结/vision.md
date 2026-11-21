# 画面线理解：23-跨域问题以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\23-跨域问题以及总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:09, 00:18, 00:42, 00:59, 01:32, 01:42, 02:10, 02:20, 02:30, 02:46, 03:04, 03:13, 03:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:03:24

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
画面13：PPT 页面，展示技术架构图，包含前端、接口文档、后端和 swagger 组件。
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
package com.ihrm.common.controller;

import com.ihrm.common.entity.Result;
import com.ihrm.common.exception.CommonException;
import com.ihrm.domain.company.Company;
import com.ihrm.service.CompanyService;
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
内容：跨域是什么？浏览器从一个域名的网页去请求另一个域名的资源时，域名、端口、协议任一不同，都是跨域。我们是采用前后端分离开发的，也是前后端分离部署的，必然存在跨域问题。怎么解决跨域？很简单，只需要在 controller 类上添加注解 @CrossOrigin 即可！这个注解其实是 CORS 的实现。CORS(Cross-Origin Resource Sharing) 跨域资源共享是 W3C 出的一个标准，其意思是使用自定义的 HTTP 头部让浏览器与服务器进行沟通，从而决定请求或响应是应该成功，还是应该失败。因此，要想实现 CORS 进行跨域，需要对服务器进行一些设置，同时前端也需要做一些配置和分析。本文简单的对服务器的配置和前端的一些设置进行分析。

画面5：
结构：前端工程（椭圆形） → 后端微服务（矩形）

画面6：
结构：前端工程（椭圆形） → 后端微服务（矩形），中间标注“跨域问题”

画面13：
结构：前端（蓝色圆形） → 接口文档（橙色八边形） ← 后端（蓝色圆形），接口文档 → swagger（蓝色矩形）

5) 无
