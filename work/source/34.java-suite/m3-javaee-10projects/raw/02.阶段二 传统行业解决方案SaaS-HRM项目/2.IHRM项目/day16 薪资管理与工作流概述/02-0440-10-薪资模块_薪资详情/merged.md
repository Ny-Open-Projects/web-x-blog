# 10-薪资模块：薪资详情

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\10-薪资模块：薪资详情_【海量资源尽在 ubkz.com】.mp4
- 时长 3分46秒（音频 226s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 我们这边已经看过了企业设置相关的这些内容那接下来呢还有一个小小的问题我们一起来看一下就是在这边可以有一个查看那这里面的查看的就是当前某一个员工他当月的这个薪资情况我们可以来试一下这边点击查看进去好了各位会发现这里面的显示内容还比较多比如说有用户的数据用户名以及他的入职时间
[00:26] 还有他的工资的相关情况当然底下还有设定的津贴以及企业的公积金还有他的出勤等等等等那对于这个界面是怎么做到的呢其实比较简单一点进来他会发送很多请求有查询用户API接口有查询他这个个人薪资接口有查询津贴接口有查询社保接口有查询我们出勤天数接口
[00:53] 那这个界面里面的大部分的数据呢我们都是已经有了其中还少一项是不是就是社保公积金这里面没有内容啊好了我们打开F12一起来看一下目前呢请求的这些接口好了这边请求了之后呢我们一起看一下他请求的接口还是比较多的比如说呢这边会去请求好了我们这边考勤模块的数据也会请求我们刚才咱们的福利津贴的这些数据
[01:23] 当然还会请求很多这边有一个报错的可以看到了其实这个是去考请求我们的社保模块那请求社保模块会传递一个我们的用户ID会传递一个年和月份这样一来呢它主要目的是去查询已归档的社保用户数据那这边给我们显示出来那我们这个接口呢现在还没有我们可以把这一段Ctrl Ccall一下
[01:52] 回到我们的代码当中注意现在是我们的社保模块里面补充一个新的方法那社保模块就在这儿我们打开找到对应的接口Controller好了我们现在要做到的是要根据用户ID还有根据考勤的年月去查询那各位发现其实我们这个接口呢在之前写过但是这个接口呢当时考虑的不足啊是因为我们要为了接口统一咱们应该返回应该全部都是这种
[02:20] 对象的形式, 导的形式所以我们直接在这个接口上进行改造就可以了那首先改造我们的UIL好了, 那第一个参数呢我们都知道代表的是userID因为它传递过来是一个地址参数这边改成我们的earMouse那由于这边传递过来的是地址参数的话我们就需要pass variablepass variable来进声明那声明好了之后我们返回这回返回的是一个rezoat所以我们这边呢得到一个对象叫做detail
[02:55] 那接着returnnew一个result那第一个success传进去那第二个detail传进去那这样一来我们这个接口改造就已经改造完成了那重新启动一下我们这个社保模块重启一下好了那接着回到我们的浏览器耐心等待它启动成功我们就能看到最终展示的这个效果好了页面上的我们重新刷新一下各位发现
[03:26] 中间这一块社保相关的数据是不是也已经给我们展示出来了那这样一来我们这个用户他的详情的这个这个薪资详情的这个页面我们也就已经都做好了OK这边数据该有都已经有

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中查看员工薪资详情，并通过浏览器开发者工具和 IntelliJ IDEA 调试器分析后端控制器代码，定位并修复因路径参数缺失导致的 404 错误。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 iHRM 系统的薪资列表页面，用户点击“详情”按钮查看员工 a01 的薪资详情。
画面 2: 展示员工 a01 的薪资详情页面，包含津贴、社保公积金等信息，右侧显示“请假日程”。
画面 3: 切换到浏览器开发者工具的 Network 标签页，显示请求列表，准备检查网络请求。
画面 4: 在 Network 标签页中，选中一个请求，显示请求失败，状态码为 404，请求 URL 为 /api/attendances/archive/...，并显示请求头信息。
画面 5: 在 IntelliJ IDEA 中，打开项目结构，定位到 `ihm_social_security` 模块下的 `Controller` 包。
画面 6: 在 IntelliJ IDEA 中，打开 `SocialSecurityController.java` 文件，查看 `historysDetail` 方法的代码。
画面 7: 在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，代码中 `@RequestMapping` 注解的路径为 `/social_security/historys/data`。
画面 8: 在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，代码中 `@RequestMapping` 注解的路径为 `/social_security/historys/archiveDetail/{userId}/{yearMonth}`。
画面 9: 在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，代码中 `@RequestMapping` 注解的路径为 `/social_security/historys/archiveDetail/{userId}/{yearMonth}`。
画面 10: 在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，代码中 `@RequestMapping` 注解的路径为 `/social_security/historys/archiveDetail/{userId}/{yearMonth}`。
画面 11: 在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，代码中 `@RequestMapping` 注解的路径为 `/social_security/historys/archiveDetail/{userId}/{yearMonth}`。
画面 12: 在 IntelliJ IDEA 中，查看 `SocialSecurityController.java` 文件，代码中 `@RequestMapping` 注解的路径为 `/social_security/historys/archiveDetail/{userId}/{yearMonth}`。
画面 13: 在浏览器中，刷新页面，显示员工 a01 的薪资详情页面，津贴和社保公积金数据已更新。
画面 14: 在浏览器中，查看员工 a01 的薪资详情页面，津贴和社保公积金数据已更新。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
```
ihm_parent
├── ihm_attendance
├── ihm_common
├── ihm_company
├── ihm_employees
├── ihm_eureka
├── ihm_gate
├── ihm_social_security
│   ├── src
│   │   └── main
│   │       └── java
│   │           └── com
│   │               └── ihm
│   │                   └── social
│   │                       └── Controller
│   │                           └── SocialSecurityController.java
```

画面 6:
```java
public Result historysDetail(@PathVariable String yearMonth) throws Exception {
    archiveService.archive(yearMonth, company.id);
    return new Result(ResultCode.SUCCESS);
}

// 查询历史列表
@RequestMapping(value = "/historys/{year}/list", method = RequestMethod.GET)
public Result historysList(@PathVariable String year) throws Exception {
    List<Archive> list = archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, list);
}

// 根据用户id查询某年某月的用户考勤明细
@RequestMapping(value = "/historys/data", method = RequestMethod.GET)
public ArchiveDetail historysData(String userId, String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面 7:
```java
@RequestMapping(value = "/historys/data", method = RequestMethod.GET)
public ArchiveDetail historysData(String userId, String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面 8:
```java
@RequestMapping(value = "/historys/archiveDetail/{userId}/{yearMonth}", method = RequestMethod.GET)
public ArchiveDetail historysData(@PathVariable String userId, @PathVariable String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面 9:
```java
@RequestMapping(value = "/historys/archiveDetail/{userId}/{yearMonth}", method = RequestMethod.GET)
public ArchiveDetail historysData(@PathVariable String userId, @PathVariable String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面 10:
```java
@RequestMapping(value = "/historys/archiveDetail/{userId}/{yearMonth}", method = RequestMethod.GET)
public ArchiveDetail historysData(@PathVariable String userId, @PathVariable String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面 11:
```java
@RequestMapping(value = "/historys/archiveDetail/{userId}/{yearMonth}", method = RequestMethod.GET)
public ArchiveDetail historysData(@PathVariable String userId, @PathVariable String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

画面 12:
```java
@RequestMapping(value = "/historys/archiveDetail/{userId}/{yearMonth}", method = RequestMethod.GET)
public ArchiveDetail historysData(@PathVariable String userId, @PathVariable String yearMonth) throws Exception {
    return archiveService.findUserArchiveDetail(userId, yearMonth);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

