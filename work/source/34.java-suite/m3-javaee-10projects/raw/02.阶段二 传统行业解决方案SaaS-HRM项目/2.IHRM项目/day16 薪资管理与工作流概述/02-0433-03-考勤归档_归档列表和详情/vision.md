# 画面线理解：03-考勤归档：归档列表和详情

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\03-考勤归档：归档列表和详情_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:25, 02:16, 02:52, 03:11, 04:24, 04:52, 05:39, 06:32, 07:49, 08:43, 09:30, 10:08, 10:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:43:44

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 系统中实现考勤历史归档功能，包括前端页面展示、后端 Controller 层接口定义、Service 层业务逻辑和 Dao 层数据持久化操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示课程大纲，当前章节为“1.1 归档列表”，内容涉及 Controller 和 Service 层代码。
- Controller 层代码：
  ```java
  //查询年度归档
  @RequestMapping(value = "/reports/year", method = RequestMethod.GET)
  public Result findReports(String year) throws Exception {
      List<ArchiveMonthly> list = archiveService.findReportsByYears(year, companyId);
      return new Result(ResultCode.SUCCESS, list);
  }

  //查询月考勤明细
  @RequestMapping(value = "/reports/{id}", method = RequestMethod.GET)
  public Result findReportsById(String id) throws Exception {
      List<ArchiveMonthlyInfo> list = archiveService.findReportsById(id);
      return new Result(ResultCode.SUCCESS, list);
  }
  ```

画面 2：
- 前端页面显示“员工历史归档”，但请求返回 404 Not Found。
- 网络面板显示请求 URL 为 http://localhost:8080/api/attendances/reports/year/...，状态码 404。

画面 3：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/archive/item", method = RequestMethod.GET)` 和 `@RequestMapping(value = "/newReports", method = RequestMethod.GET)` 方法。

画面 4：
- 在 AttendanceController.java 中，光标位于 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法的注释上方。
- 代码中显示 `List<ArchiveMonthly> list = archiveService.findReportsByYear(year, companyId);`。

画面 5：
- 在 AttendanceController.java 中，光标位于 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法的注释上方。
- 代码中显示 `List<ArchiveMonthly> list = archiveService.findReportsByYear(year, companyId);`。

画面 6：
- 展示 ArchiveService.java 文件，其中包含 `for (User user : users) { ... }` 循环和 `public List<ArchiveMonthly> findReportsByYear(String year, String companyId) { ... }` 方法。

画面 7：
- 展示 ArchiveService.java 文件，其中包含 `for (User user : users) { ... }` 循环和 `public List<ArchiveMonthly> findReportsByYear(String year, String companyId) { ... }` 方法。

画面 8：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法。

画面 9：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法。

画面 10：
- 展示 AttendanceController.java 文件，其中包含 `@RequestMapping(value = "/reports/{id}", method = RequestMethod.GET)` 方法。

画面 11：
- 展示 ArchiveService.java 文件，其中包含 `public List<ArchiveMonthlyInfo> findMonthlyInfoByAid(String id) { ... }` 方法。
- 代码提示中显示 `findByArchiveMonthlyId(String atteArchiveMonthlyId)` 方法的多个重载选项。

画面 12：
- 前端页面显示“员工历史归档”列表，包含员工编号、姓名、工号、部门、手机和每日考勤状态。

画面 13：
- 展示项目结构，包含 `ihrm_parent` 和 `ihrm_attendance` 模块。
- 代码中显示 `@RequestMapping(value = "/reports/year", method = RequestMethod.GET)` 方法。

画面 14：
- 前端页面显示“员工历史归档”列表，包含员工编号、姓名、工号、部门、手机和每日考勤状态。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
//查询年度归档
@RequestMapping(value = "/reports/year", method = RequestMethod.GET)
public Result findReports(String year) throws Exception {
    List<ArchiveMonthly> list = archiveService.findReportsByYears(year, companyId);
    return new Result(ResultCode.SUCCESS, list);
}

//查询月考勤明细
@RequestMapping(value = "/reports/{id}", method = RequestMethod.GET)
public Result findReportsById(String id) throws Exception {
    List<ArchiveMonthlyInfo> list = archiveService.findReportsById(id);
    return new Result(ResultCode.SUCCESS, list);
}
```

画面 6：
```java
for (User user : users) {
    ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
    //统计每个用户的考勤记录
    Map map = attendanceDao.statsByUser(user.getId(), archiveDate + "%");
    info.setStatsData(map);
    info.setTid(idWorker.nextId());
    info.setAtteArchiveMonthlyId(archiveMonthly.getId());
    archiveMonthlyInfoDao.save(info);
}

//总人数
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttePeopleNum(users.size());
archiveMonthly.setIsArchived(0);

//根据年份，查询当年的所有考勤历史
public List<ArchiveMonthly> findReportsByYear(String year) {
    archiveMonthly;
}
```

画面 11：
```java
public List<ArchiveMonthlyInfo> findMonthlyInfoByAid(String id) {
    return_archiveMonthlyInfoDao.findByArchiveMonthlyId(id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
