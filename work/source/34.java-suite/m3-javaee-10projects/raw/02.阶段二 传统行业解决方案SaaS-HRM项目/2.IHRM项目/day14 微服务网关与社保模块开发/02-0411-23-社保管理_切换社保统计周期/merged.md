# 23-社保管理：切换社保统计周期

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\23-社保管理：切换社保统计周期_【海量资源尽在 ubkz.com】.mp4
- 时长 5分45秒（音频 345s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好了那到目前为止呢咱们今天的这个内容呢已经做成了这个归档这个报表咱已经搞定了其实到目前为止咱这个大部分内容就已经跟各位都说清楚了那这个归档呢如果我们搞定了之后呢接下来这边呢还有一项就是说如果这个7月份数据你呢已经归过档了那归档之后你如果想要做8月份的数据那怎么办咱们就需要点一下新建报表它会自动的
[00:29] 把我们的统计周期切换为下一个月那这个就是我们今天要做的最后一块功能那对于这个功能呢相对来说没有那么难好了各位来看我们一点这个新建报表他问我是否要新建7月的因为我是否要新建8月份报表因为7月份报表呢我们现在已经查明出来了那接着我一点击确定他会发送这么一个请求在这边就是new report
[00:58] 那对于这个请求呢咱们把它完善出来Ctrl C回到我们这个Controller部分注意这个方法呢很简单我简单说一下咱们在做什么就可以了这个就是制作新报表制作制作新报表那制作新报表呢其实就是切换我们的统计周期其实就这个含义就比如说之前是八月份现在我们切换统计周期就切换成了
[01:31] 9月份而已那新的月份他已经给我传递过来了那在我们这边就可以配置一个新的方法好了请求路径呢在这边这个路径我从其他地方拷一段过来吧OK后面呢有一个叫new report那接下来呢里面传递的参数呢也是从之前咱们写好的代码里拷一段过来OK好那接着我想说一下那我们这个切换新的周期干嘛呢注意很简单我们的主要目的就是
[02:23] 修改我们这个企业设置因为我们之前说过了在我们这一界面一点击是宝是不是它会统计一下我们当前这个数据库表的siting这个表当中究竟是几如果之前是7月份永远进来都是7月份那所以我们要做的事情就是把这个月份呢给它由07改成08月份其实就可以那这个代码呢写法也比较简单我们来试一下好了siting
[02:54] 注意直接Ctrl C拿过来就是根据企业去查询一下这个setting有没有那接着做一个判断if呢这个setting CS啊等于等于noneCS等于等于none是为了防止它出现一些问题等于CS等于new一个主要为了防止出问题所以我这边做一个额外的处理那接下来呢咱们在这边就可以CS点
[03:26] set company idsummon id设置进去cs.setdate month把这个date month传递过去那接下来cs.该设置都已经设置好了是吧我们可以点save直接把这cs传递过去那如果数据库里面存在这记录它就更新如果没有存在是不是就保存一条啊OK那这样一来咱们这个方法就已经
[03:54] 写好了接下来咱们重新启动一下这边都关掉我们来看好了这个启动还比较快我们启动成功了之后切换回我们的代码部分刷新一把回到我们这边社保回到社保我们现在是7月份社保没问题好了我们同时也归档了7月份数据接下来新建报表就应该变成了8月份同时我们这边数据库里面应该也有
[04:28] 07改成08我们一起来试一下新建报表走抱歉这边的请求方式刚才我们输忽略了找到刚才我们这个代码吧好了我们来看一下请求方式呢是一个put请求啊好了再来试一下好了这边呢请动成功了回到页面刷新社保点进去目前呢还是7月份那点到报表新建报表
[05:22] 确定新报表确定好了那接下来呢回到我们这边数据库来试一下刷新哦抱歉各位刚才点了两下是变成9月份了那接着找到社保那各位发现现在就是要是新月份的社保数据了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

