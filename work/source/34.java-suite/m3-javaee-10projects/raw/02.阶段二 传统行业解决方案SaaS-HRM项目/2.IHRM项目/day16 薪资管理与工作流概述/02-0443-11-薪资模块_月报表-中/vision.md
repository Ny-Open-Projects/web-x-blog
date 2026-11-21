# 画面线理解：11-薪资模块：月报表-中

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\11-薪资模块：月报表-中_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 01:31, 02:50, 03:34, 04:33, 06:04, 07:57, 08:56, 09:58, 11:13, 12:30, 13:34, 14:27, 15:24
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:52:06

1) 这一组画面整体在讲什么（一句话）：
演示一个薪资报表系统的核心代码逻辑，包括控制器、服务层、数据访问层以及远程调用服务的实现，最终展示前端报表页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示薪资报表控制器（ArchiveController）中处理 /reports 接口的代码，根据 optype 参数决定返回当前月或历史数据。
画面2：展示前端页面中用于生成报表的 HTML 表格结构代码，定义了包括“姓名”、“工号”、“部门名称”、“在职状态”、“公积金个人”、“社保个人”、“社保企业”、“计算税”等列。
画面3：展示社保模块控制器（SocialSecurityController）中处理 /histories/list 接口的代码，用于查询用户社保历史数据。
画面4：展示服务层（ArchiveService）中用于根据 id 查询薪资明细的代码。
画面5：展示 Feign 客户端（FeignClientService）中用于调用远程服务获取考勤和社保数据的代码。
画面6：展示服务层（ArchiveService）中 getReports 方法的注释，说明其功能是计算薪资。
画面7：展示服务层（ArchiveService）中 getReports 方法的注释，说明其功能是计算薪资。
画面8：展示服务层（ArchiveService）中定义的私有成员变量，包括数据访问对象和远程调用服务。
画面9：展示服务层（ArchiveService）中 getReports 方法的注释，说明其功能是计算薪资。
画面10：展示实体类（SalaryArchiveDetail）中用于获取和设置薪资相关属性的方法，如 getSalaryBeforeTax、setSalaryAfterTax 等。
画面11：展示实体类（SalaryArchiveDetail）中设置薪资相关属性的方法，如 setSalaryAfterTax、setSocialSecurityEnterprise 等。
画面12：展示服务层（ArchiveService）中 getReports 方法的注释，说明其功能是计算薪资。
画面13：展示服务层（ArchiveService）中 getReports 方法的注释，说明其功能是计算薪资。
画面14：展示前端页面，显示“工资报表”功能，包含“查询/月份报表”和“新建报表”按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
/**
 * 薪资报表
 * 请求URL：/salaries/reports?yearMonth=201907&optype=1
 * 参数：
 *   地址参数：201907
 *   其他参数：optype(1:当前月的报表,其他:在该月已归档的报表)
 */
@GetMapping(value = "/reports/{yearMonth}", method = RequestMethod.GET)
public Result historyDetail(@PathVariable String yearMonth, int optype) {
    List<SalaryArchiveDetail> list = new ArrayList<>();
    //1.共用参数：如果optype=1，自己知道报表数据
    if (optype == 1) {
        //2.如果optype=1，查询当前月的记录
        //2.1 查询王宗数据
        SalaryArchive sa = archiveService.findSalaryArchive(yearMonth, companyId);
        //2.2 根据王宗的id，查询该月所有的数据
        if (sa != null) {
            list = archiveService.findSalaryArchiveDetail(sa.getId());
        }
        return new Result(ResultCode.SUCCESS, list);
    } else {
        //2.3 查询历史数据
        List<SalaryArchive> list = archiveService.findSalaryArchiveList(yearMonth, companyId);
        return new Result(ResultCode.SUCCESS, list);
    }
}
```

画面2：
```html
<el-table-column type="index" label="序号" width="50"></el-table-column>
<el-table-column prop="username" label="姓名" width="150px"></el-table-column>
<el-table-column prop="workNumber" label="工号" width="150px"></el-table-column>
<el-table-column prop="departmentName" label="部门名称" width="150px"></el-table-column>
<el-table-column prop="inServiceStatus" label="在职状态" width="150px"></el-table-column>
<el-table-column prop="socialSecurityIndividual" label="社保个人" width="150px"></el-table-column>
<el-table-column prop="socialSecurityEnterprise" label="社保企业" width="150px"></el-table-column>
<el-table-column prop="providerFundIndividual" label="公积金个人" width="150px"></el-table-column>
<el-table-column prop="providerFundEnterprises" label="公积金企业" width="150px"></el-table-column>
<el-table-column prop="currentBaseSalary" label="当月工资" width="150px"></el-table-column>
<el-table-column prop="salaryChangeAmount" label="调薪金额" width="150px"></el-table-column>
<el-table-column prop="salaryAfterTax" label="实发工资" width="150px"></el-table-column>
<el-table-column prop="salaryBeforeTax" label="应发工资" width="150px"></el-table-column>
<el-table-column prop="salaryStandard" label="工资标准" width="150px"></el-table-column>
<el-table-column prop="salaryCost" label="工资成本" width="150px"></el-table-column>
<el-table-column prop="payment" label="工资总额" width="150px"></el-table-column>
```

画面3：
```java
@GetMapping(value = "/histories/{year}/list", method = RequestMethod.GET)
public Result historyList(@PathVariable String year, @PathVariable String userId) throws Exception {
    List<Archive> list = archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, list);
}

@GetMapping(value = "/histories/archiveDetail/{userId}/{yearMonth}", method = RequestMethod.GET)
public Result historyData(@PathVariable String userId, @PathVariable String yearMonth) {
    ArchiveDetail detail = archiveService.findUserArchiveDetail(userId, yearMonth);
    return new Result(ResultCode.SUCCESS, detail);
}
```

画面4：
```java
public SalaryArchive findSalaryArchive(String yearMonth, String companyId) {
    return archiveDao.findByCompanyIdAndYearMonth(companyId, yearMonth);
}

public List<SalaryArchiveDetail> findSalaryArchiveDetail(String id) {
    return archiveDetailDao.findByArchiveId(id);
}
```

画面5：
```java
package com.ihrm.salaries.feign;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class FeignClientService {

    @Autowired
    private AttendanceFeignClient attendanceFeignClient;

    @Autowired
    private SocialSecurityFeignClient socialSecurityFeignClient;

    public ArchiveMonthlyInfo getAttendanceInfo(String userId, String yearMonth) {
        Result result = attendanceFeignClient.attendanceInfo(userId, yearMonth);
        ArchiveMonthlyInfo info = null;
        if (result.isSuccess()) {
            info = JSON.toJSONString(result.getData(), ArchiveMonthlyInfo.class);
        }
        return info;
    }

    public ArchiveDetail getSocialInfo(String userId, String yearMonth) {
        Result result = socialSecurityFeignClient.getSocialInfo(userId, yearMonth);
        ArchiveDetail info = null;
        if (result.isSuccess()) {
            info = JSON.toJSONString(result.getData(), ArchiveDetail.class);
        }
        return info;
    }
}
```

画面6：
```java
/**
 * 计算薪资 ：社保和考勤已经归档
 * @return
 */
```

画面7：
```java
/**
 * 计算薪资 ：社保和考勤已经归档
 * @return
 */
```

画面8：
```java
private ArchiveDetailDao archiveDetailDao; //档案明细dao
private UserSalaryDao userSalaryDao; //员工薪资dao
private IdWorker idWorker; //ID生成器
private SalaryService salaryService; //员工薪资service
private SettingsService settingsService; //福利设置service
private FeignClientService feignClientService;
```

画面9：
```java
/**
 * 计算薪资 ：社保和考勤已经归档
 * @return
 */
```

画面10：
```java
public BigDecimal getSalaryBeforeTax() {
    return this.salaryBeforeTax;
}

public BigDecimal getEntTotal() {
    return getProvidFundEnterprises().add(getSocialSecurityEnterprise());
}

public BigDecimal getPerTotal() {
    return getSocialSecurityIndividual().add(getProvidFundIndividual());
}

//设置用户属性
public void setUserInfo(Map map) {
    this.username = map.get("username").toString();
    this.departmentName = map.get("departmentName").toString();
    this.mobile = map.get("mobile").toString();
    this.userId = map.get("id").toString();
    this.workNumber = (String)map.get("workNumber").toString();
    this.inServiceStatus = map.get("inServiceStatus").toString();
}

//设置社保属性
public void setSocialInfo(ArchiveDetail socialInfo) {
    this.providFundIndividual = socialInfo.getProvidFundIndividual();
    this.providFundEnterprises = socialInfo.getProvidFundEnterprises();
    this.socialSecurityIndividual = socialInfo.getSocialSecurityIndividual();
    this.socialSecurityEnterprise = socialInfo.getSocialSecurityEnterprise();
    this.socialSecurityProvidFundEnterprises = socialInfo
