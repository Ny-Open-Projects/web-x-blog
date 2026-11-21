# 画面线理解：17-考勤归档：实现数据归档

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\17-考勤归档：实现数据归档_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 01:13, 01:56, 03:17, 04:36, 05:34, 06:12, 06:39, 08:04, 08:41, 09:31, 10:10, 10:44, 11:04
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:41:01

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事系统中，通过后端 Java 代码实现“导出月度考勤报表”的功能，包括前端页面展示、控制器方法定义、服务层逻辑处理及数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：前端页面展示“201907月人事报表”，包含员工姓名、工号、部门、考勤数据等字段，页面有“导出”按钮。
画面 2：后端控制器 `AttendanceController.java` 中定义了 `/reports` 和 `/archive/item/archiveDate=201907` 的 GET 请求，用于获取报表数据。
画面 3：前端页面再次展示“201907月人事报表”，鼠标悬停在“调休”列。
画面 4：服务层 `ArchiveService.java` 中的 `getReports` 方法，用于获取月度报表数据。
画面 5：`ArchiveService.java` 中的 `saveArchive` 方法，用于保存归档数据，包含查询用户、统计考勤、创建归档对象等逻辑。
画面 6：`ArchiveService.java` 中的 `saveArchive` 方法，展示注释和代码结构。
画面 7：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置公司ID。
画面 8：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置归档年份和月份。
画面 9：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置部门ID。
画面 10：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置归档月份。
画面 11：在 `saveArchive` 方法中，为 `ArchiveMonthly` 对象设置总人数和全勤人数。
画面 12：控制器 `AttendanceController.java` 中定义了 `/archive/item/archiveDate=201907` 的 GET 请求，用于获取归档数据。
画面 13：数据库表 `archive_monthly_info` 的结构，包含 `id`, `company_id`, `department_id`, `archive_month`, `archive_year`, `total_people_num`, `full_attendance_people_num`, `is_archived` 等字段。
画面 14：数据库表 `archive_monthly_info` 的结构，与画面 13 相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
public Result importExcel(int page,int pagsize) throws Exception {
    Map map = attService.getAttDate(page,pagesize);
    return new Result(ResultCode.SUCCESS,map);
}

/**
 * 编辑用户的考勤记录
 */
@RequestMapping(value = "/id",method = RequestMethod.PUT)
public Result editAtte(Attendance attendance) throws Exception {
    attService.editAtte(attendance);
    return new Result(ResultCode.SUCCESS);
}

/**
 * 获取月度报表数据
 */
@RequestMapping(value = "/reports",method = RequestMethod.GET)
public Result reports(String attDate) throws Exception {
    List<ArchiveMonthlyInfo> list = attService.getReports(attDate,companyId);
    return new Result(ResultCode.SUCCESS,list);
}

/**
 * 数据归档
 */
@RequestMapping(value = "/archive/item/archiveDate=201907",method = RequestMethod.GET)
```

画面 4：
```java
public List<ArchiveMonthlyInfo> getReports(String attDate, String companyId) {
    List<User> users = userDao.findByCompanyId(companyId);
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        Map map = attendanceDao.statistByUser(user.getId(), s, attDate + "%");
        info.setStatisticsData(map);
        list.add(info);
    }
    return list;
}
```

画面 5：
```java
public static void saveArchive(String archiveDate) {
    //1.查询所有企业用户
    List<User> users = userDao.findByCompanyId(companyId);
    //2.循环遍历用户，统计每个用户的当月的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        //统计每个用户的考勤记录
        Map map = attendanceDao.statistByUser(user.getId(), s, attDate + "%");
        info.setStatisticsData(map);
        list.add(info);
    }
}
```

画面 6：
```java
private ArchiveMonthlyInfoDao archiveMonthlyInfoDao;
private UserDao userDao;
private Idworker idworker;

//数据归档
public void saveArchive(String archiveDate,String companyId) {
    //1.查询所有企业用户
    List<User> users = userDao.findByCompanyId(companyId);
    //2.循环遍历用户，统计每个用户的当月的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        //统计每个用户的考勤记录
        Map map = attendanceDao.statistByUser(user.getId(), s, attDate + "%");
        info.setStatisticsData(map);
        list.add(info);
    }
}
```

画面 7：
```java
archiveMonthly.setCompanyId(companyId);
```

画面 8：
```java
archiveMonthly.setArchiveYear(archiveDate.substring(0, 4)); //201908
archiveMonthly.setArchiveMonth(archiveDate.substring(5));
```

画面 9：
```java
archiveMonthly.setDepartmentId(departmentId);
```

画面 10：
```java
archiveMonthly.setArchiveMonth(archiveDate.substring(5));
```

画面 11：
```java
archiveMonthly.setTotalPeopleNum(users.size());
archiveMonthly.setFullAttendancePeopleNum(users.size());
archiveMonthly.setIsArchived(0);
```

画面 12：
```java
/**
 * 获取月度报表数据
 */
@RequestMapping(value = "/reports",method = RequestMethod.GET)
public Result reports(String attDate) throws Exception {
    List<ArchiveMonthlyInfo> list = attService.getReports(attDate,companyId);
    return new Result(ResultCode.SUCCESS,list);
}

/**
 * 数据归档
 */
@RequestMapping(value = "/archive/item/archiveDate=201907",method = RequestMethod.GET)
```

画面 13：
```sql
CREATE TABLE `archive_monthly_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `archive_month` varchar(255) DEFAULT NULL,
  `archive_year` varchar(255) DEFAULT NULL,
  `total_people_num` int(11) DEFAULT NULL,
  `full_attendance_people_num` int(11) DEFAULT NULL,
  `is_archived` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
