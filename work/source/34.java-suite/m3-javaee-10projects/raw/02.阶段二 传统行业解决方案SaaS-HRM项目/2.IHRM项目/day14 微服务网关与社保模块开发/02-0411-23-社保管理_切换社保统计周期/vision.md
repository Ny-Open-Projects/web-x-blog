# 画面线理解：23-社保管理：切换社保统计周期

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\23-社保管理：切换社保统计周期_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:02, 00:38, 00:51, 01:33, 01:55, 02:34, 03:20, 03:52, 04:06, 04:30, 04:41, 05:00, 05:21, 05:39
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:25:54

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过前端点击“生成社保报表”按钮，触发后端接口，最终在数据库中更新企业社保设置并生成报表数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：在数据库管理工具中，查看 `ss_archive` 表的数据，其中 `company_id` 为 201908，`data_month` 为 201907。
画面2：在 iHRM 系统前端，显示“社保报表”页面，数据为 201907 月份，包含员工姓名、入职时间、学历等信息。
画面3：在浏览器开发者工具 Network 面板中，查看请求 URL 为 `/api/social_security/history/201908/newReport?type=1`，状态码为 200。
画面4：在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，其中 `@RequestMapping(value = "/settings", method = RequestMethod.POST)` 方法用于保存企业设置。
画面5：在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，其中 `@RequestMapping(value = "/settings", method = RequestMethod.POST)` 方法用于保存企业设置，代码中包含注释“修改企业设置”。
画面6：在浏览器开发者工具 Network 面板中，查看请求 URL 为 `/api/social_security/history/201908/newReport`，状态码为 404。
画面7：在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，其中 `@RequestMapping(value = "/settings", method = RequestMethod.POST)` 方法用于保存企业设置，代码中包含注释“修改企业设置”。
画面8：在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，其中 `@RequestMapping(value = "/settings", method = RequestMethod.POST)` 方法用于保存企业设置，代码中包含注释“修改企业设置”。
画面9：在浏览器开发者工具 Network 面板中，查看请求 URL 为 `/api/social_security/history/201908/newReport`，状态码为 404。
画面10：在数据库管理工具中，查看 `ss_archive` 表的数据，其中 `company_id` 为 201908，`data_month` 为 201907。
画面11：在 IntelliJ IDEA 中，查看项目结构，显示 `ihm_parent` 项目下的 `ihm_social_securities` 模块。
画面12：在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，其中 `@RequestMapping(value = "/settings", method = RequestMethod.POST)` 方法用于保存企业设置。
画面13：在 iHRM 系统前端，显示“社保报表”页面，状态码为 504。
画面14：在 iHRM 系统前端，显示“社保报表”页面，数据为 201909 月份，包含员工姓名、入职时间、社保城市等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4：
```java
@Autowired
private ArchiveService archiveService;

/**
 * 查询企业是否配置过社保
 */
@RequestMapping(value = "/settings", method = RequestMethod.GET)
public Result settings() {
    CompanySettings cs = companySettingsService.findById(companyId);
    return new Result(ResultCode.SUCCESS, cs);
}

// histories/201908/newReport
// 制作社保报表
// 功能统计周期
// 修改企业设置
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}
```

画面5：
```java
// histories/201908/newReport
// 制作社保报表
// 功能统计周期
// 修改企业设置
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}
```

画面6：
```java
// histories/201908/newReport
// 制作社保报表
// 功能统计周期
// 修改企业设置
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}
```

画面7：
```java
// histories/201908/newReport
// 制作社保报表
// 功能统计周期
// 修改企业设置
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}
```

画面8：
```java
// histories/201908/newReport
// 制作社保报表
// 功能统计周期
// 修改企业设置
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}
```

画面11：
```
ihm_parent
├── ihm_common
├── ihm_company
├── ihm_employee
├── ihm_gate
├── ihm_social_securities
│   ├── src
│   │   └── main
│   │       └── java
│   │           └── com
│   │               └── ihm
│   │                   └── social_securities
│   │                       └── client
│   └── pom.xml
└── pom.xml
```

画面12：
```java
@RequestMapping(value = "/settings", method = RequestMethod.POST)
public Result saveSettings(@RequestBody CompanySettings companySettings) {
    companySettings.setCompanyId(companyId);
    companySettingsService.save(companySettings);
    return new Result(ResultCode.SUCCESS);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无
