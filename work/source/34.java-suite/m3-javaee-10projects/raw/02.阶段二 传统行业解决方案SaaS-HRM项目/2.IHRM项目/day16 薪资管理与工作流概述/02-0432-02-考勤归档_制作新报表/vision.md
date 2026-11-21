# 画面线理解：02-考勤归档：制作新报表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\02-考勤归档：制作新报表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 00:54, 01:33, 01:54, 02:18, 02:34, 03:20, 03:42, 04:54, 06:06, 07:05, 07:28, 08:05, 08:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:43:01

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的人事考勤系统，重点讲解月度考勤报表的前端展示、后端控制器与服务层代码实现，以及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：前端页面显示“201907月人事报表”，包含员工姓名、工号、手机号、部门、考勤状态等字段，数据来自后端接口。
画面2：IDEA项目结构，展示项目根目录 `ihrm_parent` 及其子模块，如 `ihrm_attendance`、`ihrm_common` 等。
画面3：打开 `AttendanceController.java`，查看 `@RequestMapping(value = "/reports", method = RequestMethod.GET)` 方法，用于获取月度考勤报表。
画面4：前端页面显示“201907月人事报表”，数据加载完成，页面状态正常。
画面5：前端页面展示“201907月考勤明细”，显示员工每日考勤状态，弹窗提示“统计考勤时，异常状态优先正常状态”。
画面6：前端页面显示“201907月人事报表”，数据中某员工“正常”考勤次数为11，“迟到次数”为1，“早退次数”为1。
画面7：点击左侧菜单“社保”。
画面8：SQLyog 数据库管理工具，显示 `att_archive_monthly` 表结构，字段包括 `company_id`, `department_id`, `archive_year`, `archive_month`, `total_people_num`, `full_attend_people_num`, `late_num`, `early_leave_num`, `create`。
画面9：IDEA 中 `AttendanceController.java`，查看 `@RequestMapping(value = "/archive/item", method = RequestMethod.GET)` 方法，用于获取月度考勤明细。
画面10：IDEA 中 `AtteService.java`，查看 `@Autowired` 注解的 `excelImportService`、`atteService`、`archiveService` 字段。
画面11：IDEA 中 `AtteService.java`，查看 `getReports` 方法，其中包含 `UserDao.findUserByCompanyId` 查询用户，`attendanceDao.statsByUser` 获取考勤统计。
画面12：IDEA 中 `AtteService.java`，查看 `getReports` 方法，光标在 `companySettingsDoc.findById(companyId).isPresent()` 语句上，提示“expected”。
画面13：IDEA 项目结构，展开 `src/main/java/com/ihrm/attendance/service` 目录，显示 `AtteService.java` 文件。
画面14：前端页面显示“201907月考勤明细”，展示员工每日考勤状态，如“迟到”、“旷工”等。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3代码：
```java
/**
 * 获取月度考勤数据
 * /attendances/archive/item?archiveDate=201907
 */
@RequestMapping(value = "/reports", method = RequestMethod.GET)
public Result reports(String archiveDate) throws Exception {
    List<ArchiveMonthlyInfo> reports = atteService.getReports(archiveDate, companyId);
    return new Result(ResultCode.SUCCESS, reports);
}
```

画面9代码：
```java
/**
 * 获取月度考勤明细
 * /attendances/archive/item?archiveDate=201907
 */
@RequestMapping(value = "/archive/item", method = RequestMethod.GET)
public Result item(String archiveDate) throws Exception {
    archiveService.saveArchive(archiveDate, companyId);
    return new Result(ResultCode.SUCCESS);
}
```

画面11代码：
```java
/**
 * 获取月度考勤数据
 */
public List<ArchiveMonthlyInfo> getReports(String atteDate, String companyId) {
    //1.查询所有企业用户
    List<User> users = userDao.findUserByCompanyId(companyId);
    //2.循环所有用户，查询每个用户的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        Map map = attendanceDao.statsByUser(user.getId(), Integer.parseInt(atteDate.substring(0, 2)) + 1);
        System.out.println(user.getId() + " " + atteDate);
        info.setStatsData(map);
        list.add(info);
    }
    return list;
}
```

画面12代码：
```java
//处理报表，若companySetting中的月份序号为指定的月份
public void newReports(String yearMonth, String companyId) {
    companySettingsDoc.findById(companyId).isPresent();
}
```

画面8 SQL：
```sql
company_id department_id archive_year archive_month total_people_num full_attend_people_num late_num early_leave_num create
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
