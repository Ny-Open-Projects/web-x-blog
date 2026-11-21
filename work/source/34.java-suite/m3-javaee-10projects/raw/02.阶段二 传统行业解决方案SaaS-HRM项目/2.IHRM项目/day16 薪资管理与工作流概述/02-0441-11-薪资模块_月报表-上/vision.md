# 画面线理解：11-薪资模块：月报表-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\11-薪资模块：月报表-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:39, 01:05, 03:57, 04:40, 06:28, 08:35, 09:56, 10:23, 11:14, 12:09, 13:47, 14:21, 15:02, 15:34
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:50:18

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过 Spring Boot 后端代码实现“薪资归档”功能的前后端交互逻辑，包括控制器、服务层、数据访问层和数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面环境，显示“黑马程序员”和“博学谷”两个机构的Logo，用于课程开场。
画面2：在记事本中编辑一个 Vue.js 的 el-table-column 列配置代码，用于前端表格展示。
画面3：在浏览器中打开 iHRM 系统的“社保”模块页面，显示系统登录后的主界面。
画面4：在 IntelliJ IDEA 中打开项目结构，展示 iHRM 项目中与薪资归档相关的 controller、service、dao 等包结构。
画面5：在 ArchiveController.java 中，展示 historyDetail 方法的初步代码框架，包含注释说明请求参数。
画面6：在 ArchiveController.java 中，继续编写 historyDetail 方法，添加了 if (opType == 1) 的条件判断逻辑。
画面7：在 ArchiveController.java 中，对 else 分支进行注释说明，准备调用服务层方法。
画面8：在 ArchiveController.java 中，将 else 分支的代码改为调用 archiveService.find 方法。
画面9：在 Navicat for MySQL 中，查看并展示名为 “salary_archive” 的数据库表结构和部分数据。
画面10：在 ArchiveController.java 中，使用 Ctrl+空格自动补全 Java 类型，如 Long、String 等。
画面11：在 ArchiveService.java 中，展示 findSalaryArchive 和 findSalaryArchiveDetail 两个方法的定义。
画面12：在 ArchiveDao.java 中，定义了 JpaRepository 接口，用于查询 SalaryArchive 实体。
画面13：在 SalaryArchiveDetail.java 中，定义了实体类，包含 @Entity、@Data、@AllArgsConstructor 等注解。
画面14：在 ArchiveController.java 中，完成 historyDetail 方法的最终逻辑，调用服务层方法并返回结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```html
<el-table-column type="index" label="序号" center width="50"></el-table-column>
<el-table-column prop="username" label="姓名" width="150px"></el-table-column>
<el-table-column prop="workNumber" label="工号" width="150px"></el-table-column>
<el-table-column prop="departmentName" label="部门" width="150px"></el-table-column>
<el-table-column prop="identityStatus" label="身份状态" width="150px"></el-table-column>
<el-table-column prop="socialSecurityIndividual" label="公积金个人" width="150px"></el-table-column>
<el-table-column prop="socialSecurityEnterprise" label="公积金企业" width="150px"></el-table-column>
<el-table-column prop="totalSecurityProviderFundIndividual" label="公积金个人" width="150px"></el-table-column>
<el-table-column prop="currentBaseSalary" label="岗位工资" width="150px"></el-table-column>
<el-table-column prop="salaryChargeAmount" label="应扣金额" width="150px"></el-table-column>
<el-table-column prop="attendanceDurationMonthly" label="考勤天数" width="150px"></el-table-column>
<el-table-column prop="salaryFyTax" label="应纳税" width="150px"></el-table-column>
<el-table-column prop="tax" label="税" width="150px"></el-table-column>
<el-table-column prop="payment" label="实发工资" width="150px"></el-table-column>
```

画面4：
```
ihm_parent
├── ihm_common
├── ihm_company
├── ihm_employee
├── ihm_euroa
├── ihm_gate
├── ihm_salaries
│   ├── src
│   │   └── main
│   │       └── java
│   │           └── com.ihm.salaries
│   │               └── controller
│   │               │   └── ArchiveController.java
│   │               └── service
│   │               └── dao
│   └── resources
│       └── test
│       └── target
│       └── ihm_salaries.iml
│       └── pom.xml
└── ihm_social_security
```

画面5：
```java
package com.ihm.salaries.controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    public Result historyDetail() {
        return new Result();
    }
```

画面6：
```java
package com.ihm.salaries.controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    @RequestMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
    public Result historyDetail(@PathVariable String yearMonth, int opType) {
        return new Result(ResultCode.SUCCESS);
    }
```

画面7：
```java
package com.ihm.salaries.controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    @RequestMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
    public Result historyDetail(@PathVariable String yearMonth, int opType) {
        if (opType == 1) {
            // 1.单向opType参数:如果=1,自己勾选报表数据
        } else {
            // 2.如果=1,查询归档历史表
            // 2.1 查询主表数据
            // 2.2 根据主表的id,查询明细表的所有数据
        }
        return new Result(ResultCode.SUCCESS);
    }
```

画面8：
```java
package com.ihm.salaries.controller;

import org.springframework.web.bind.annotation.*;
import com.ihm.salaries.controller;

@RestController
@RequestMapping(value = "/salarys")
public class ArchiveController extends BaseController {
    // 制作薪资报表
    // 请求URL:/salarys/reports/201907?yearMonth=201907&opType=1
    // 参数：
    // 201907
    // 请求参数：opType(1:制作新的报表，其他:查询已归档的报表数据)
    @RequestMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
    public Result historyDetail(@PathVariable String yearMonth, int opType) {
        if (opType == 1) {
            // 1.单向opType参数:如果=1,自己勾选报表数据
        } else {
            // 2.如果=1,查询归档历史表
            // 2.1 查询主表数据
            // 2.2 根据主表的id,查询明细表的所有数据
            archiveService.find();
        }
        return new Result(ResultCode.SUCCESS);
    }
```

画面9：
```sql
SELECT * FROM salary_archive;
```

画面10：
```java
// Ctrl+空格自动补全
Long (java.lang)
lazy (org.springframework.context.annotation)
Lazy (org.springframework.data.util)
LinkageError (java.lang)
LeaveConfig (com.ihm.domain.attle.enum)
LambdaConversionException (java.lang.invoke)
LambdaDataFactory (java.lang.invoke)
Layout (com.sony.java.util)
LayoutStyle (java.awt)
Label (java.awt)
LabelPoem (java.awt)
Label (java.awt)
```

画面11：
```java
@Service
public class ArchiveService {
    @Autowired
    private ArchiveDao archiveDao; // 归档主表dao
    @Autowired
    private ArchiveDetailDao archiveDetailDao; // 归档明细dao
    @Autowired
    private UserSalaryDao userSalaryDao; // 员工薪资设置dao
    @
