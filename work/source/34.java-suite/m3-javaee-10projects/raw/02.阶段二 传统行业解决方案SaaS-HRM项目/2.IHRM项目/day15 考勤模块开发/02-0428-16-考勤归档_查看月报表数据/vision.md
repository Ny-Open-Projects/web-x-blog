# 画面线理解：16-考勤归档：查看月报表数据

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\16-考勤归档：查看月报表数据_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:45, 01:57, 02:48, 03:18, 05:09, 06:22, 07:24, 09:05, 11:27, 11:53, 12:33, 13:44, 14:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:40:11

1) 这一组画面整体在讲什么（一句话）：
演示如何通过 Java 后端代码实现并查询员工考勤月报数据，涉及数据库查询、实体类定义、服务层逻辑和前端页面展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 SQL 查询语句，用于统计指定用户在指定日期的考勤记录，查询结果为 1 行。
画面 2: 前端页面显示员工考勤列表，用户可按部门、状态筛选，当前筛选条件为“test1”。
画面 3: 浏览器开发者工具显示前端请求后端 API `/attendances/reports?atteDate=201907` 的响应，状态码为 200 OK。
画面 4: IDE 中展示 `ArchiveMonthlyInfo` 实体类定义，包含 `id`, `userId`, `name`, `workNumber` 等字段。
画面 5: IDE 中展示 `AttendanceController` 控制器类，包含 `getReports` 方法用于获取月报数据。
画面 6: IDE 中展示 `AtteService.java` 文件，包含 `editAtte` 方法用于编辑考勤记录。
画面 7: IDE 中展示 `AtteService.java` 文件，`getReports` 方法中遍历用户列表并创建 `ArchiveMonthlyInfo` 对象。
画面 8: 前端页面显示月报生成界面，用户点击“新建报表”后，浏览器开发者工具显示请求 `/attendances/reports?atteDate=201907` 的状态码为 200 OK。
画面 9: SQL 查询语句，用于统计指定用户在指定日期的考勤记录，查询结果为 1 行。
画面 10: SQL 查询语句，用于统计指定用户在指定日期的考勤记录，查询结果为 1 行。
画面 11: IDE 中展示 `AtteService.java` 文件，`getReports` 方法中调用 `attendanceDao.save` 方法保存数据。
画面 12: IDE 中展示 `AttendanceDao.java` 文件，定义了 `findByUserIdAndDay` 方法，并使用 `@Query` 注解指定 SQL 查询。
画面 13: IDE 中展示项目结构和运行日志，显示 Spring Boot 应用启动并成功解析 Eureka 服务端点。
画面 14: 前端页面显示 201907 月人事报表，包含员工姓名、工号、部门、考勤等详细数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```sql
SELECT COUNT(*) FROM
(SELECT (CASE WHEN atts.att_status = 1 THEN 1 END) att,
       (CASE WHEN atts.att_status = 2 THEN 1 END) att,
       (CASE WHEN atts.att_status = 3 THEN 1 END) att,
       (CASE WHEN atts.att_status = 4 THEN 1 END) att,
       (CASE WHEN atts.att_status = 5 THEN 1 END) att
FROM acto_attendance WHERE user_id = 1 AND DAY LIKE '201907%') t
```

画面 4:
```java
@Entity
@EqualsAndHashCode(callSuper = true)
@Table(name = "atte_archive_monthly_info")
@Data
@AllArgsConstructor
public class ArchiveMonthlyInfo extends BaseEntity implements Serializable {
    @Id
    private String id;
    private String userId;
    private String atteArchiveMonthlyId;
    private String name;
    private String workNumber;
    private String mobile;
    private String attResolution;
    private String department;
    private String workCity;
    private String yearLeaveDays;
    private String sickLeaveDays;
}
```

画面 5:
```java
@RequestMapping(value = "/reports", method = RequestMethod.GET)
public Result getReports(String atteDate) throws Exception {
    return new Result(ResultCode.SUCCESS, atteService.getReports(atteDate));
}
```

画面 6:
```java
public void editAtte(Attendance attendance) {
    //1.查询考勤是否存在,更新
    Attendance vo = attendanceDao.findByUserIdAndDay(attendance.getUserId(), attendance.getDay());
    //2.如果不存在,设置对象id,保存
    if (vo == null) {
        attendance.setId(idWorker.nextId() + "");
    } else {
        attendance.setId(vo.getId());
    }
    attendanceDao.save(attendance);
}
```

画面 7:
```java
public List<ArchiveMonthlyInfo> getReports(String atteDate, String companyId) {
    //1.查询所有用户
    List<User> users = userDao.findByCompanyId(companyId);
    //2.循环遍历用户列表,统计每个用户当月的考勤记录
    List<ArchiveMonthlyInfo> list = new ArrayList<>();
    for (User user : users) {
        ArchiveMonthlyInfo info = new ArchiveMonthlyInfo(user);
        //3.查询当月的考勤记录
        attendanceDao.save(info);
        list.add(info);
    }
    return list;
}
```

画面 11:
```java
list.add(attendanceDao.save(info));
```

画面 12:
```java
@Query("SELECT att FROM Attendance att WHERE att.userId = ?1 AND att.day = ?2")
Attendance findByUserIdAndDay(String id, String day);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
