# 画面线理解：02-POI导出人事报表：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day08 POI高级
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day08 POI高级\02-POI导出人事报表：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:44, 01:15, 01:53, 02:43, 03:35, 04:42, 06:02, 07:59, 09:47, 10:44, 12:20, 12:56, 13:51
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:05:08

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 Controller 层调用 Service 层，最终使用 Apache POI 库将员工档案数据导出为 Excel 文件。

2) 按时间顺序列出每张画面的要点：
画面1：展示 EmployeeController.java 中的 export 方法，用于导出员工档案，调用 archiveService.findSearch 方法获取数据。
画面2：展示 EmployeeReportResult.java 中的字段，用于封装导出的员工档案数据，包括银行账号、开户行、学历类型、毕业时间等。
画面3：展示 EmployeeReportResult.java 中的构造方法，用于合并个人基本信息和离职信息。
画面4：展示 EmployeeController.java 中的 save 方法，用于保存员工个人信息。
画面5：展示 UserCompanyPersonalService.java 中的 save 方法，调用 UserCompanyPersonalDao.save 方法保存数据。
画面6：展示 UserCompanyPersonalDao.java 中的 findByUserId 方法，用于根据用户 ID 查询员工个人信息。
画面7：展示 EmployeeReportResult.java 中的字段，包括用户名、部门名称、手机号、入职时间、离职原因等。
画面8：展示 UserCompanyPersonalDao.java 中的 findByReport 方法，用于根据公司 ID 和月份查询员工档案。
画面9：展示 EmployeeController.java 中的 export 方法，调用 userCompanyPersonalService.findDBReport 方法获取数据。
画面10：展示 EmployeeController.java 中的 export 方法，开始创建 Workbook 对象。
画面11：展示 Excel 文件界面，显示导出的员工档案数据，包含姓名、手机、入职时间等字段。
画面12：展示 EmployeeController.java 中的 export 方法，使用 Workbook 对象创建 Sheet。
画面13：展示 EmployeeController.java 中的 export 方法，使用 for 循环遍历数据并设置单元格值。
画面14：展示 EmployeeController.java 中的 export 方法，完成 Excel 文件的创建和下载。

3) 画面里出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字原样抄录）：
画面1：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) {
    //1.获取数据
    PageResult<EmployeeArchive> pr = new PageResult<>(searchPage.getTotalElements(), searchPage.getContent());
    return new Result(ResultCode.SUCCESS, pr);
}
```

画面2：
```java
private String providentFundAccount;
/** 银行卡号 */
private String bankCardNumber;
/** 开户行 */
private String openingBank;
/** 学历类型 */
private String educationalType;
/** 职业学校 */
private String graduateSchool;
/** 入学时间 */
private String enrollmentTime;
/** 毕业时间 */
private String graduationTime;
/** 专业 */
private String major;
```

画面3：
```java
public EmployeeReportResult(UserCompanyPersonal personal, EmployeeResignation resignation) {
    BeanUtils.copyProperties(personal, target: this);
    if(resignation != null) {
        BeanUtils.copyProperties(resignation, target: this);
    }
}
```

画面4：
```java
@RequestBody Map map) throws Exception {
    if (sourceInfo == null) {
        sourceInfo = BeanUtils.mapToBean(map, UserCompanyPersonal.class);
    }
}
```

画面5：
```java
@Service
public class UserCompanyPersonalService {
    @Autowired
    private UserCompanyPersonalDao userCompanyPersonalDao;

    public void save(UserCompanyPersonal personalInfo) {
        userCompanyPersonalDao.save(personalInfo);
    }

    public UserCompanyPersonal findById(String userId) {
        return userCompanyPersonalDao.findById(userId);
    }
}
```

画面6：
```java
public interface UserCompanyPersonalDao extends JpaRepository<UserCompanyPersonal, String>, JpaSpecificationExecutor<UserCompanyPersonal> {
    UserCompanyPersonal findByUserId(String userId);
}
```

画面7：
```java
package com.ihm.domain.employee.response;

import lombok.*;
import java.util.Date;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class EmployeeReportResult {
    private String userId;
    private String username;
    private String departmentName;
    private String mobile;
    private String timeOfEntry;
    private String companyId;
    private String cex;
    /** 出生日期 */
    private String dateOfBirth;
    /** 最高学历 */
    private String theHighestDegreeOfEducation;
    /** 国家地区 */
    private String nationalArea;
}
```

画面8：
```java
@Query(value = "SELECT new com.ihm.domain.EmployeeReportResult " +
        "LEFT JOIN EmployeeResignation er ON a.user_id = er.user_id " +
        "WHERE a.time_of_entry LIKE '%2018-02%' OR a.time_of_entry LIKE '%2018-03%'")
List<EmployeeReportResult> findByReport(String companyId, String month);
```

画面9：
```java
@RequestMapping(value = "/export/{month}", method = RequestMethod.GET)
public void export(@PathVariable String month) throws Exception {
    //1.获取数据
    List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
    //2.创建Excel
    Workbook wb = new XSSFWorkbook();
    //3.创建Sheet
    Sheet sheet = wb.createSheet();
}
```

画面10：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
```

画面11：
（无代码，为 Excel 文件界面）

画面12：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
```

画面13：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
//4.设置标题行
String[] titles = {"姓名", "手机", "入职时间", "离职原因", "离职时间"};
for (int i = 0; i < titles.length; i++) {
    Row row = sheet.createRow(i);
    Cell cell = row.createCell(i);
    cell.setCellValue(titles[i]);
}
```

画面14：
```java
//1.获取数据
List<EmployeeReportResult> list = userCompanyPersonalService.findDBReport(companyId, month);
//2.创建Excel
Workbook wb = new XSSFWorkbook();
//3.创建Sheet
Sheet sheet = wb.createSheet();
//4.设置标题行
String[] titles = {"姓名", "手机", "入职时间", "离职原因", "离职时间"};
for (int i = 0; i < titles.length; i++) {
    Row row = sheet.createRow(i);
    Cell cell = row.createCell(i);
    cell.setCellValue(titles[i]);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
（无 PPT 标题、架构图/流程图或表格数据）

5) 不要评价画面美观，不要输出与课程无关的内容。
（已遵守）
