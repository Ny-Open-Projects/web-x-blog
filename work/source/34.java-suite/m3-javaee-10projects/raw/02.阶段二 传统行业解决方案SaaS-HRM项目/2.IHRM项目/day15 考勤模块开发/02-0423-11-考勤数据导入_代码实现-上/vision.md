# 画面线理解：11-考勤数据导入：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\11-考勤数据导入：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:24, 01:58, 02:55, 03:30, 03:55, 04:42, 05:22, 06:33, 07:27, 09:03, 10:56, 11:36, 12:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:36:12

1) 这一组画面整体在讲什么（一句话）：
演示如何在Java项目中实现Excel考勤数据导入功能，包括服务层代码编写、数据模型定义、数据库操作及Excel解析工具的使用。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- IDE界面显示ExcelImportService.java文件，其中定义了@Autowired注入的AttendanceDao、AttendanceConfigDao和IdWorker。
- 方法importAttendanceExcel接收MultipartFile文件和companyId参数。
- 方法注释说明了处理Excel文件上传、解析、查询用户、构造考勤对象、判断迟到早退、检查重复记录等步骤。

画面2：
- 在importAttendanceExcel方法中，使用ExcelImportUtil工具类读取Excel文件，创建List<AtteUploadVo>集合。
- 代码中使用了rowindex=1，cellindex=0等参数。

画面3：
- 展示一个空白的流程图或架构图，包含三个椭圆形框，分别标注“系统微服务”、“考勤”和一个未命名的框。

画面4：
- IDE项目结构视图，显示了com.ihm.attendance包下的controller、dao、service等目录结构。
- 展示了AttendanceController、AttendanceDao、UserDao等类。

画面5：
- 显示ExcelImportService.java文件的import语句部分，包括了AttendanceConfigDao、UserDao、ExcelImportUtil、IdWorker等类的导入。

画面6：
- IDE项目结构视图，高亮显示了UserDao.java文件。
- 在ExcelImportService.java中，代码行显示了userDao.findByMobile方法的调用。

画面7：
- IDE界面显示了多个Java文件标签，包括Attendance.java、UserDao.java、ConfigController.java。
- 在ExcelImportService.java中，代码行显示了userDao.findByMobile方法的调用。

画面8：
- 在ExcelImportService.java中，代码行显示了attendance.setUser(user)的调用。
- 代码提示显示了Attendance类的setUser方法。

画面9：
- 在ExcelImportService.java中，代码行显示了attendance.setDay(attendance.setDay())的调用。
- 代码提示显示了Attendance类的setDay方法。

画面10：
- 在ExcelImportService.java中，代码行显示了attendance.setDay(attendance.setDay())的调用。
- 代码提示显示了Attendance类的setDay方法。

画面11：
- 展示了一个Excel表格，包含“员工姓名”、“手机号”、“工号”、“上班时间”、“下班时间”等列。
- 表格中显示了示例数据，如员工姓名“张三”，手机号“13800138002”，工号“123456”，上班时间“2019-7-1 8:30”，下班时间“2019-7-1 18:30”。

画面12：
- IDE界面显示了AtteUploadVo.java文件，其中定义了@Data和@ToString注解。
- 类中定义了多个私有字段，包括username、mobile、workNumber、inTime、outTime、attStatus等，并使用了@ExcelAttribute注解。

画面13：
- 展示了电脑桌面，显示了“黑马程序员”和“博学谷”的标志。
- 桌面上有多个快捷方式图标，如“Lemon”、“demo.xlsx”、“此电脑”、“回收站”、“优博方式”、“TUA客户”、“截图”、“记事本”等。

画面14：
- IDE界面显示了ExcelImportService.java文件，其中代码行显示了attendance.setDay(DateUtil.parseDate2String(atteUploadVo.getStartTime(), pattern))的调用。
- 代码注释说明了“判断是否迟到”、“判断是否早退”、“查询用户是否已有考勤记录，如果不存在，保存数据库”等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
private AttendanceDao attendanceDao;
@Autowired
private AttendanceConfigDao attendanceConfigDao;
@Autowired
private IdWorker idWorker;

/**
 * 处理考勤数据的文件上传
 * 参数：excel文件
 * 企业
 */
public void importAttendanceExcel(MultipartFile file, String companyId) {
    //1.导入的excel文件解析为vo的list集合
    //2.循环list集合
    //2.1 根据上传的手机号码查询用户
    //2.2 构造考勤对象
    //2.3 判断迟到，早退的状态
    //2.5 查询用户是否已经有考勤记录，如果不存在，保存数据库
}
```

画面2：
```java
public void importAttendanceExcel(MultipartFile file, String companyId) throws Exception {
    //1.导入的excel文件解析为vo的list集合
    List<AtteUploadVo> list = new ExcelImportUtil(AtteUploadVo.class).readExcel(file.getInputStream(), rowindex: 1, cellindex: 0);
    //2.循环list集合
    for (AtteUploadVo atteUploadVo : list) {
    }
}
```

画面4：
```
com.ihm.attendance
├── controller
├── dao
│   ├── ArchiveMonthlyDao
│   ├── ArchiveMonthlyInfoDao
│   ├── AttendanceDao
│   ├── AttendanceConfigDao
│   ├── DeductionDao
│   ├── DeductionTypeDao
│   ├── ExtraDutyRuleDao
│   ├── UserDao
├── service
│   ├── AttendanceServiceApplication
│   └── ShiroConfiguration
└── resources
    ├── ihm_attendance.ini
    └── pom.xml
```

画面5：
```java
import com.ihm.attendance.AttendanceConfigDao;
import com.ihm.attendance.AttendanceDao;
import com.ihm.attendance.entity.ResultCode;
import com.ihm.common.exception.CommonException;
import com.ihm.common.utils.ExcelImportUtil;
import com.ihm.common.utils.IdWorker;
import com.ihm.domain.att.vo.AtteUploadVo;
import com.ihm.domain.system.User;
import lombok.extern.log4j.Log4j2;
import org.apache.commons.lang.StringUtils;
import org.apache.poi.ss.usermodel.NSSerialNumber;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import java.io.IOException;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.List;
```

画面6：
```java
User user = userDao.findByMobile(atteUploadVo.getMobile());
```

画面7：
```java
attendance.setUser(user);
```

画面8：
```java
attendance.setDay(attendance.setDay());
```

画面9：
```java
attendance.setDay(attendance.setDay());
```

画面10：
```java
attendance.setDay(attendance.setDay());
```

画面12：
```java
package com.ihm.domain.att.vo;

import java.util.Date;

@Data
@ToString
public class AtteUploadVo {

    //员工姓名
    @ExcelAttribute(sort=0,format="String")
    private String username;
    //手机号
    @ExcelAttribute(sort=1,format="String")
    private String mobile;
    //工号
    @ExcelAttribute(sort=2,format="String")
    private String workNumber;
    //上班时间
    @ExcelAttribute(sort=3,format="Date")
    private Date inTime;
    //下班时间
    @ExcelAttribute(sort=4,format="Date")
    private Date outTime;
    //考勤状态
    @ExcelAttribute(sort=5,format="String")
    private String attStatus;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面3：
- 架构图包含三个椭圆形框，分别标注“系统微服务”、“考勤”和一个未命名的框。
- 未显示任何连接线或指向关系。

画面11：
- 表格包含“员工姓名”、“手机号”、“工号”、“上班时间”、“下班时间”等列。
- 表格中显示了示例数据，如员工姓名“张三”，手机号“13800138002”，工号“123456”，上班时间“2019-7-1 8:30”，下班时间“2019-7-1 18:30”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
