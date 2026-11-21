# 画面线理解：11-薪资模块：月报表-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\11-薪资模块：月报表-下_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:26, 00:36, 00:59, 01:08, 02:07, 02:18, 02:41, 05:05, 05:47, 05:55, 06:24, 06:40, 07:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:51:12

1) 这一组画面整体在讲什么（一句话）：
演示一个薪资计算服务的代码实现，包括从数据库查询、调用远程服务获取用户信息、计算薪资、社保公积金等，并最终在前端展示薪资报表。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 `ArchiveService.java` 中的 `findPage` 方法，用于分页查询薪资档案，循环中创建 `SalaryArchiveDetail` 对象并填充数据。
画面 2: 在 `ArchiveService.java` 中，继续循环，调用 `feignClientService` 获取用户社交信息、月度信息，并调用 `salaryService.findUserSalary` 获取用户薪资，然后设置到 `detail` 对象中。
画面 3: 展示 `SalaryArchiveDetail.java` 中的薪资计算逻辑，包括计算交通补贴、计算考勤扣款、计算应纳税工资等。
画面 4: 展示 `Settings.java` 类中定义的 `companyid`、`socialSecurityType`、`subsidyName` 等字段，用于存储企业设置信息。
画面 5: 继续展示 `Settings.java` 类，显示 `transportationSubsidyScheme`、`communicationSubsidyScheme`、`lunchAllowanceScheme` 等字段，用于存储补贴方案。
画面 6: 展示 `SalaryArchiveDetail.java` 中的交通补贴计算逻辑，根据 `transportationSubsidyScheme` 的值决定是否加补贴。
画面 7: 展示 `SalaryArchiveDetail.java` 中的考勤扣款计算逻辑，根据 `officialSalaryDays` 与 21.75 的比较决定是否扣款。
画面 8: 展示 `SalaryArchiveDetail.java` 中的应纳税工资计算逻辑，根据 `salaryByTax` 计算税额。
画面 9: 展示 `SalaryArchiveDetail.java` 中的 `getTax` 方法，用于根据薪资计算应缴税额。
画面 10: 展示 `SalaryArchiveDetail.java` 中的 `getTax` 方法内部逻辑，根据薪资分段计算税率和扣除额。
画面 11: 展示 `SalaryArchiveDetail.java` 中的 `getTax` 方法，显示税率计算的完整代码。
画面 12: 展示前端页面“工资报表”，显示员工薪资信息的表格。
画面 13: 展示前端页面“工资报表”，显示员工薪资信息的表格，包含姓名、手机号、工号、部门、在职状态、公积金个人、社保个人、社保企业等字段。
画面 14: 展示前端页面“设置”，显示员工的入职时间、工龄、社保方案等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
Page<Map> page = userSalaryDao.findPage(companyId, pageRequest: null);
for (Map map : page.getContent()) {
    //1.查询用户数据
    SalaryArchiveDetail detail = new SalaryArchiveDetail();
    detail.setUserId(map.get("user_id").toString());
    detail.setUserName(map.get("user_name").toString());
    detail.setSocialInfo(feignClientService.getSocialInfo(detail.getUserId()));
    detail.setMonthlyInfo(feignClientService.getAttInfo(detail.getUserId()));
    //2.获取用户薪资
    UserSalary userSalary = salaryService.findUserSalary(detail.getUserId());
    detail.setSalary(userSalary.getSalary());
    list.add(detail);
}
return list;
```

画面 2:
```java
Settings settings = settingsService.findById(companyId);
Page<Map> page = userSalaryDao.findPage(companyId, pageRequest: null);
for (Map map : page.getContent()) {
    //3.构造SalaryArchiveDetail
    SalaryArchiveDetail detail = new SalaryArchiveDetail();
    detail.setUserId(map.get("user_id").toString());
    detail.setUserName(map.get("user_name").toString());
    detail.setSocialInfo(feignClientService.getSocialInfo(detail.getUserId()));
    detail.setMonthlyInfo(feignClientService.getAttInfo(detail.getUserId()));
    //4.获取在岗用户的薪资
    UserSalary userSalary = salaryService.findUserSalary(detail.getUserId());
    detail.setSalary(userSalary.getSalary());
    detail.setSettings(settings);
    list.add(detail);
}
return list;
```

画面 3:
```java
money = money.add(settings.getLunchAllowanceAmount().multiply(this.officialSalaryDays));
if (settings.getTransportationSubsidyScheme() == -3) {
    money = money.add(settings.getTransportationSubsidyAmount().multiply(this.officialSalaryDays));
} else {
    money = money.add(settings.getTransportationSubsidyAmount().multiply(this.officialSalaryDays));
}
this.salaryChangeAmount = money;
//计算考勤扣款
BigDecimal attendanceMoney = this.currentSalaryTotalBase;
if (officialSalaryDays.compareTo(new BigDecimal(val: 21.75)) < 0) {
    attendanceMoney = this.currentSalaryTotalBase.divide(new BigDecimal(val: 21.75), scale: 2, ROUND_HALF_UP).multiply(this.officialSalaryDays);
} else {
    this.attendanceDeductionMonthly = "0";
}
//计算应纳税工资
this.currentSalaryTotalBase = attendanceMoney.add(money);
//计算(扣除社保和公积金部分)
this.salaryByTax = this.currentSalaryTotalBase.subtract(this.providentFundIndividual).subtract(this.socialSecurityIndividual);
```

画面 4:
```java
/**
 * 企业id
 */
private String companyId;
/**
 * 对应社保自然月
 */
private Integer socialSecurityType;
/**
 * 补贴方案名称
 */
private String subsidyName;
/**
 * 补贴备注
 */
private String subsidyRemark;
/**
 * 交通补贴类型
 */
private Integer transportationSubsidyScheme;
/**
 * 交通补贴金额
 */
private BigDecimal transportationSubsidyAmount;
/**
 * 通讯补贴计算类型：1：日，3：月
 */
private Integer communicationSubsidyScheme;
/**
 * 通讯补贴金额
 */
private BigDecimal communicationSubsidyAmount;
```

画面 5:
```java
/**
 * 交通补贴计算类型：1：日，3：月
 */
private Integer communicationSubsidyScheme;
/**
 * 通讯补贴金额
 */
private BigDecimal communicationSubsidyAmount;
/**
 * 午餐补贴计算类型
 */
private Integer lunchAllowanceScheme;
/**
 * 午餐补贴金额
 */
private BigDecimal lunchAllowanceAmount;
/**
 * 住房补贴计算类型
 */
private Integer housingSubsidyScheme;
/**
 * 住房补贴金额
 */
private BigDecimal housingSubsidyAmount;
```

画面 6:
```java
if (settings.getTransportationSubsidyScheme() == -3) {
    money = money.add(settings.getTransportationSubsidyAmount().multiply(this.officialSalaryDays));
} else {
    money = money.add(settings.getTransportationSubsidyAmount().multiply(this.officialSalaryDays));
}
```

画面 7:
```java
BigDecimal attendanceMoney = this.currentSalaryTotalBase;
if (officialSalaryDays.compareTo(new BigDecimal(val: 21.75)) < 0) {
    attendanceMoney = this.currentSalaryTotalBase.divide(new BigDecimal(val: 21.75), scale: 2, ROUND_HALF_UP).multiply(this.officialSalaryDays);
} else {
    this.attendanceDeductionMonthly = "0";
}
```

画面 8:
```java
//计算应纳税工资
this.currentSalaryTotalBase = attendanceMoney.add(money);
//计算(扣除社保和公积金部分)
this.salaryByTax = this.currentSalaryTotalBase.subtract(this.providentFundIndividual).subtract(this.socialSecurityIndividual);
```

画面 9:
```java
private BigDecimal getTax(BigDecimal salary) {
    //salary * 税率 - 速算扣除数
    BigDecimal easyNum = new BigDecimal(val: 0);
    BigDecimal stageNum = new BigDecimal(val: 0.03);
    if (salary.doubleValue() <= 3500) {
        return BigDecimal.ZERO;
    } else if (salary.doubleValue() > 1500) {
        easyNum = new BigDecimal(val: 105);
        stageNum = new BigDecimal(val: 0.1);
    } else if (salary.doubleValue() > 6000) {
        easyNum = new BigDecimal(val: 555);
        stageNum = new BigDecimal(val: 0.2);
    } else if (salary.doubleValue() > 9000) {
        easyNum = new BigDecimal(val: 1085);
        stageNum = new BigDecimal(val: 0.25);
    } else if (salary.doubleValue() > 15000) {
        easyNum = new BigDecimal(val: 2755);
        stageNum = new BigDecimal(val: 0.3);
    } else if (salary.doubleValue() > 30000) {
        easyNum = new BigDecimal(val: 5505);
        stageNum = new BigDecimal(val: 0.35);
    } else if (salary.doubleValue() > 55000) {
        easyNum = new BigDecimal(val: 18155);
        stageNum = new BigDecimal(val: 0.45);
    }
    salary = salary.multiply(stageNum);
    salary = salary.subtract(easyNum);
    return salary;
}
```

画面 10:
```java
if
