# 画面线理解：12-考勤数据导入：代码实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\12-考勤数据导入：代码实现-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 03:06, 03:31, 04:03, 05:01, 06:02, 06:58, 08:15, 09:44, 10:54, 13:09, 13:54, 14:31, 14:54
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:36:51

1) 这一组画面整体在讲什么（一句话）：
在Java项目中，通过Excel导入考勤数据，根据用户手机、日期、上下班时间及公司/部门配置，判断并设置考勤状态（如休息、迟到、早退），并保存到数据库。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示`ExcelImportService.java`中`importAttendaceExcel`方法的循环体，用于处理Excel中每一行数据，构造`Attendance`对象并设置日期。
画面2：鼠标悬停在`application.yml`文件上，未展示具体内容。
画面3：展示`application.yml`中配置了`IdWorker`和`@Value`注入的假期和工作日配置。
画面4：展示`application.yml`中配置了`@Value`注入的假期和工作日配置。
画面5：展示`DateUtil`类的自动补全，用于后续日期比较逻辑。
画面6：在`if`判断语句中，使用`DateUtil`类的`isBetween`方法判断日期是否在假期或工作日。
画面7：在`else`分支中，使用`DateUtil`类的`isBetween`方法判断日期是否在假期或工作日。
画面8：在`else`分支中，调用`AttendanceConfigDao`的`findByCompanyIdAndDepartmentId`方法查询当前员工的上下班时间。
画面9：在`else`分支中，使用`DateUtil`类的`comparingDate`方法比较打卡时间与上下班时间。
画面10：在`else`分支中，使用`DateUtil`类的`comparingDate`方法比较打卡时间与上下班时间。
画面11：展示`Attendance`类的自动补全，用于后续设置考勤状态。
画面12：展示`AttendanceDao.java`文件，其中定义了`findByUserIdAndDay`方法。
画面13：在`else`分支中，使用`DateUtil`类的`comparingDate`方法比较打卡时间与上下班时间。
画面14：在`else`分支中，使用`DateUtil`类的`comparingDate`方法比较打卡时间与上下班时间。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
public void importAttendaceExcel(MultipartFile file, String companyId) throws Exception {
    //1.导入excel文件解析为vo的list集合
    List<AtteUploadVo> list = new ExcelImportUtil<AtteUploadVo>(AtteUploadVo.class).readExcel(file.getInputStream(), rowindex: 1, cellindex: 1);
    for (AtteUploadVo atteUploadVo : list) {
        //2.1 根据上传的手机号查询用户
        User user = userDao.findByMobile(atteUploadVo.getMobile());
        //2.2 构造考勤对象
        Attendance attendance = new Attendance(atteUploadVo,user);
        attendance.setDay(atteUploadVo.getAtteDate());
        //2.3 判断是否休假
    }
}
```

画面3：
```yaml
@Value("${atte.holidays}")
private String holidays;

@Value("${atte.workingDays}")
private String wordingDays;
```

画面5：
```java
import com.ihm.common.utils.DateUtil;
```

画面6：
```java
if (DateUtil.isBetween(atteUploadVo.getAtteDate(), 23)) {
    attendance.setAdtStatus(23); //休息
} else if (DateUtil.isBetween(atteUploadVo.getAtteDate(), 23)) {
    attendance.setAdtStatus(23);
}
```

画面8：
```java
AttendanceConfig ac = attendanceConfigDao.findByCompanyIdAndDepartmentId(companyId, user.getDepartmentId());
```

画面9：
```java
if (DateUtil.comparingDate(ac.getAfternoonStartTime(), atteUploadVo.getInTime())) {
    //第一个参数：规定时间，第二个参数：打卡时间
}
```

画面10：
```java
if (DateUtil.comparingDate(ac.getAfternoonStartTime(), atteUploadVo.getInTime())) {
    //第一个参数：规定时间，第二个参数：打卡时间
}
```

画面11：
```java
attendance.setAdtStatus(4); //早退
```

画面12：
```java
package com.ihm.atte.dao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface AttendanceDao extends JpaRepository<Attendance, Long>, JpaSpecificationExecutor<Attendance> {
    void findByUserIdAndDay(String id, String atteDate);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
