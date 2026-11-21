# 19-POI文件导入：总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\19-POI文件导入：总结_【海量资源尽在 ubkz.com】.mp4
- 时长 3分13秒（音频 193s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 由于今天的这个时间是有限那还留下最后一块内容呢咱们留待下一天内容再去讲解那我们先对今天咱们讲过的这些做一个简单的总结好了对于今天呢我们一起来看了这么几块内容首先呢第一个就是员工管理那对于这块员工管理的这块内容呢其实是我们的一些常见的一些需求那这些需求呢其实是大于我们的这些代码的那对于我们的代码都比较简单
[00:30] 那用户管理呢我们都有入职转正离职调岗等等这些功能这些功能其实看似比较高大上其实就是对数据库表的一些基本增伸改善操作当然了这边呢有很多个申请比如说转正比如说有离职比如说调岗那这些申请呢其实就是往表里面添加一条记录然后呢以状态的形式进行控制那后续由我们的工作流的处理平台把你这个状态给你修改成转正成功
[00:56] 或者离职成功或者是调管成功等等这些因为这个涉及到工作流向每一级部门的领导进行沟通的这么一个处理过程好了这第一块管理除了我们的业务之外还有一个就是我们用到了Eureka和我们这个Finn这两个组件这两个组件主要是为我们刚才的报表导出打基础的因为我们涉及到多个微服务之间的一个跨平台调用而Eureka其实是一个发现的一个组件它分为Server跟Client
[01:23] Server是统一的对我们的所有服务进行注册管理的那Client就是把服务注册到Reca的这么一个组件好了呢接下来就是这个Fend组件呢其实需要各位知道怎么去用它以及它的主要构成就是一个HTTP的一个客户端工具通过发送HTTP请求的形式来做的当然了对于我们这个呢由于它涉及到了一个Token的一个
[01:46] 我们叫做认证的这么一个处理所以我这边呢还有一个就是添加了一个过滤器通过这个过滤器去对我们的头进行一个补充好了员工管理说过了接着就是我们要聊了一个报表那对于报表报表两种形式我们之前也看过XLS2003版本二进制XLSX它是一个XML结构的存储数据量比较大而且呢它占用的内存比较小OK那两种呢这个工具我们看过了之后呢就是说这两种解析的
[02:15] 两种解析工具一个是GXL还有PUI我们用的是PUI来做的好了PUI也有很多的应用场景咱们今天都说过了剩下的事情我们搞了一个PUI的入门在这个入门当中希望各位要知道的是它的一个结构我们HSFHSSF是用来解析2007的是用来解析2003的XSF是用来解析2007的当然这边还有很多的API这些API跟我们的
[02:45] 手动操作一个Excel是一样的Workbook相当于我们创建了一个ExcelShare相当于我们创建了单元表的一个表格当然我习惯叫做以当前某一页肉是某一行Cell是一个格子字体和样式等等OK最后呢我们又来了一个叫做PUI报表的一个导入那对于这个导入而言其实里面的代码并不复杂各位可以把这个代码自己去实现一下OK好了这样一来我们今天的内容就已经简单的回顾过了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
本课程系统讲解了在Saas-HRM系统中，如何通过微服务架构（Feign）和POI技术实现员工管理功能及Excel报表操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程目录，当前选中“1 员工管理”下的“1.1 需求分析”。
画面2：展示“1.1 需求分析”和“1.2 数据库表概述”内容，列出涉及的数据库表及其说明。
画面3：聚焦于“1.2 数据库表概述”中的“em_transferposition”表（员工调岗申请表）。
画面4：展示“1.5 微服务调用组件Feign”章节，介绍Feign的背景和快速体验步骤。
画面5：继续展示“1.5.1 简介”和“1.5.2 快速体验”内容，包含在pom.xml中添加依赖和修改启动类的注解。
画面6：展示“1.5.1 简介”中关于FeignConfiguration类的Java代码，用于配置请求拦截器。
画面7：切换到“2 POI报表的概述”章节，介绍Excel报表开发的两种形式。
画面8：聚焦于“2.2 Excel的两种形式”表格，对比Excel 2003和Excel 2007的后缀、结构和特点。
画面9：展示“2.3 常见excel操作工具”内容，说明Java中常用的操作方式为JXL和POI。
画面10：继续展示“2.3 常见excel操作工具”内容，强调POI是当前主流。
画面11：展示“2.4 POI的概述”和“2.5 POI的应用场景”内容。
画面12：展示“3.2 POI结构说明”和“3.3 API介绍”内容，列出HSSF、XSSF等组件的功能。
画面13：继续展示“3.2 POI结构说明”和“3.3 API介绍”内容。
画面14：展示“3.4 基本操作”和“3.4.1 创建Excel”内容，列出API名称如Workbook、Sheet等，并展示一个Java类的开始代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
(1) 在hrm_system模块添加依赖
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-openfeign</artifactId>
</dependency>

(2) 修改hrm_system模块的启动类，添加注解
@EnableDiscoveryClient
@EnableFeignClients

(3) 在hrm_system模块创建com.ihrm.system.client包，包下创建接口

画面6：
@Configuration
public class FeignConfiguration {
    @Bean
    public RequestInterceptor requestInterceptor() {
        return new RequestInterceptor() {
            @Override
            public void apply(RequestTemplate template) {
                ServletRequestAttributes attributes = (ServletRequestAttributes)
                        RequestContextHolder
                                .getRequestAttributes();
                if (attributes != null) {
                    HttpServletRequest request = attributes.getRequest();
                    Enumeration<String> headerNames = request.getHeaderNames();
                    if (headerNames != null) {
                        while (headerNames.hasMoreElements()) {
                            String name = headerNames.nextElement();
                            String values = request.getHeader(name);
                            template.header(name, values);
                        }
                    }
                }
            }
        };
    }
}

画面14：
public class PoITest01 {

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2：
标题：1.1 需求分析
内容：企业员工管理是人事资源管理系统中最重要的一个环节，分为对员工入职、转正、离职、调岗，员工报表导入导出等业务逻辑。
标题：1.2 数据库表概述
表格：
| 数据库表名称 | 说明 |
| --- | --- |
| em_archive | 月度员工归档表 |
| em_positive | 转正申请表 |
| em_resignation | 离职申请表 |
| em_transferposition | 员工调岗申请表 |
| em_user_company_jobs | 员工岗位信息表 |
| em_user_company_personal | 员工详细信息表 |

画面7：
标题：2.1 需求说明
内容：在企业级应用开发中，Excel报表是一种最常见的报表需求。Excel报表开发一般分为两种形式：
- 为了方便操作，基于Excel的报表批量上传数据
- 通过java代码生成Excel报表。
标题：2.2 Excel的两种形式
表格：
| 后缀 | Excel 2003 | Excel 2007 |
| --- | --- | --- |
| 结构 | 二进制格式，其核心结构是复合文档类型的结构 | XML类型结构 |
| 单sheet数据量 | 行：65535；列：256 | 行：1048576；列：16384 |
| 特点 | 存储容量有限 | 基于xml压缩，占用空间小，操作效率高 |

画面9：
标题：2.3 常见excel操作工具
内容：
- JXL只能对Excel进行操作，属于比较老的框架，它只支持到Excel 95-2000的版本。现在已经停止更新和维护。
- POI是apache的项目，可对微软的Word,Excel,Ppt进行操作，包括office2003和2007,Excel2003和2007。poi现在一直有更新。所以现在主流使用POI。

画面12：
标题：3.2 POI结构说明
内容：
HSSF提供读写Microsoft Excel XLS格式档案的功能。
XSSF提供读写Microsoft Excel OOXML XLSX格式档案的功能。
HWP提供读写Microsoft Word DOC格式档案的功能。
HSLF提供读写Microsoft PowerPoint格式档案的功能。
HDGF提供读Microsoft Visio格式档案的功能。
HPBF提供读Microsoft Publisher格式档案的功能。
HSMF提供读Microsoft Outlook格式档案的功能。
标题：3.3 API介绍

画面14：
标题：3.4 基本操作
标题：3.4.1 创建Excel
表格：
| API名称 | 说明 |
| --- | --- |
| Workbook | Excel的文档对象，针对不同的Excel类型分为：HSSFWorkbook (2003) 和 XSSFWorkbook (2007) |
| Sheet | Excel的表单 |
| Row | Excel的行 |
| Cell | Excel的格子单元 |
| Font | Excel字体 |
| CellStyle | 格子单元样式 |

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

