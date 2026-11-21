# 画面线理解：04-考勤归档：查询用户归档历史

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\04-考勤归档：查询用户归档历史_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:22, 02:08, 03:13, 03:57, 04:20, 04:41, 05:05, 05:43, 05:54, 06:11, 06:30, 07:16, 07:27, 07:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:44:25

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Spring Boot 后端代码实现员工考勤档案的查询与展示功能，并通过 Postman 进行接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 iHRM 系统前端页面，显示“员工历史归档”列表，包含年份筛选和数据表格。
画面 2: 在 IntelliJ IDEA 中查看 AttendanceController.java 文件，展示用于查询年份报表和用户月度详情的两个 GET 接口方法。
画面 3: 在 IntelliJ IDEA 中查看 AttendanceController.java 文件，展示用于查询用户月度详情的接口方法。
画面 4: 在 SQLyog 中查看数据库表结构，左侧显示数据库对象列表，右侧为空白。
画面 5: 在 IntelliJ IDEA 中查看 ArchiveMonthlyInfoDao.java 文件，展示根据归档ID查询的接口方法。
画面 6: 在 IntelliJ IDEA 中查看 ArchiveMonthlyInfoDao.java 文件，光标在方法名后，准备输入。
画面 7: 在 IntelliJ IDEA 中查看 ArchiveService.java 文件，展示用于查询用户月度详情的方法。
画面 8: 在 IntelliJ IDEA 中查看 AttendanceController.java 文件，光标在方法名后，准备输入。
画面 9: 展示桌面，显示“黑马程序员”和“博学谷”的标志。
画面 10: 在 Postman 中设置一个 POST 请求，目标地址为 127.0.0.1:9007/user/process/deploy。
画面 11: 在 Postman 中显示多个窗口的缩略图，包括 IntelliJ IDEA、SQLyog、浏览器等。
画面 12: 在 Postman 中设置一个 GET 请求，目标地址为 127.0.0.1:9007/attendance/archive/1063705899262277968/201907，请求体为 JSON 格式。
画面 13: 在浏览器开发者工具中查看网络请求，显示“2019-7月员工报表”的页面加载情况。
画面 14: 在 Postman 中查看 GET 请求的响应结果，显示 JSON 格式的数据，包含“success”、“code”、“message”等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
@GetMapping(value = "/reports/year", method = RequestMethod.GET)
public Result findReportsByYear(String year) throws Exception {
    List<ArchiveMonthly> list = archiveService.findReportsByYear(year,companyId);
    return new Result(ResultCode.SUCCESS,list);
}

// 查询归档详情
@GetMapping(value = "/reports/{id}", method = RequestMethod.GET)
public Result findInfosById(@PathVariable String id) throws Exception {
    List<ArchiveMonthlyInfo> list = archiveService.findMonthlyInfoByMid(id);
    return new Result(ResultCode.SUCCESS,list);
}

// 快速用户月度详情
// /archive/{userId}/{yearMonth}
@GetMapping("/archive/{userId}/{yearMonth}")
```

画面 3:
```java
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttePeopleNum(users.size());
archiveMonthly.setIsArchived(0);
atteArchiveMonthlyDao.save(archiveMonthly);

//根据年份，查询当年的所有考勤历史
public List<ArchiveMonthly> findReportsByYear(String year,String companyId) {
    return atteArchiveMonthlyDao.findByCompanyIdAndArchiveYear(companyId,year);
}

// 查询当月详情列表
public List<ArchiveMonthlyInfo> findMonthlyInfoByMid(String id) {
    return archiveMonthlyInfoDao.findByAtteArchiveMonthlyId(id);
}

//根据用户id和月度查询
public ArchiveMonthlyInfo findUserArchiveDetail(String userId, String yearMonth) {
    return archiveMonthlyInfoDao.findUserArchiveDetail(userId,yearMonth);
}
```

画面 5:
```java
package com.ihrm.attendance.dao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

public interface ArchiveMonthlyInfoDao extends CrudRepository<ArchiveMonthlyInfo,String>, JpaRepository<ArchiveMonthlyInfo,String> {

    //根据归档列表查询月度详情
    @Query("select a from ArchiveMonthlyInfo a where a.atteArchiveMonthlyId = :atteArchiveMonthlyId")
    List<ArchiveMonthlyInfo> findByAtteArchiveMonthlyId(String atteArchiveMonthlyId);

}
```

画面 7:
```java
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttePeopleNum(users.size());
archiveMonthly.setIsArchived(0);
atteArchiveMonthlyDao.save(archiveMonthly);

//根据年份，查询当年的所有考勤历史
public List<ArchiveMonthly> findReportsByYear(String year,String companyId) {
    return atteArchiveMonthlyDao.findByCompanyIdAndArchiveYear(companyId,year);
}

// 查询当月详情列表
public List<ArchiveMonthlyInfo> findMonthlyInfoByMid(String id) {
    return archiveMonthlyInfoDao.findByAtteArchiveMonthlyId(id);
}

//根据用户id和月度查询
public ArchiveMonthlyInfo findUserArchiveDetail(String userId, String yearMonth) {
    return archiveMonthlyInfoDao.findUserArchiveDetail(userId,yearMonth);
}
```

画面 8:
```java
@GetMapping(value = "/reports/{id}", method = RequestMethod.GET)
public Result findInfosById(@PathVariable String id) throws Exception {
    List<ArchiveMonthlyInfo> list = archiveService.findMonthlyInfoByMid(id);
    return new Result(ResultCode.SUCCESS,list);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
