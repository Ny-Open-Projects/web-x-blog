# 画面线理解：19-POI文件导入：总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\19-POI文件导入：总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:45, 01:05, 01:30, 01:49, 01:50, 01:57, 02:00, 02:11, 02:12, 02:21, 02:30, 02:38, 02:57
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:59:19

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
