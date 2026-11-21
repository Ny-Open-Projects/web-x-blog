# 画面线理解：07-薪资模块：环境搭建-下(改)

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\07-薪资模块：环境搭建-下(改)_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 01:03, 02:02, 02:37, 03:18, 03:41, 04:48, 05:42, 06:33, 07:33, 08:33, 09:13, 09:47, 10:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:47:22

1) 这一组画面整体在讲什么（一句话）：
演示薪资模块的开发流程，包括创建实体类、数据访问层、服务层、控制器层，并最终启动项目并展示前端页面。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示薪资模块的前端页面，包含“开始年”输入框和“确定”按钮。
画面2：在IDEA中，打开项目结构，准备创建新包。
画面3：展示实体类 SalaryArchiveDetail 的代码，包含公司ID、是否设置、当前显示报表月份等字段。
画面4：展示项目文件夹结构，包含 CompanySettings.java、SalaryArchive.java 等文件。
画面5：展示 UserSalaryDao 接口代码，包含查询和分页方法。
画面6：展示 ArchiveService.java 服务层代码，包含对 ArchiveDao 和 IdWorker 的注入。
画面7：展示 SalaryService.java 服务层代码，包含对 UserSalaryDao、UserSalaryChangeDao 等的注入。
画面8：在IDEA中，展开项目结构，显示 salaries 模块下的 controller、service、dao 等包。
画面9：展示 CompanySettingsController.java 控制器代码，包含获取和保存企业设置、新建报表的方法。
画面10：展示 SalaryController.java 控制器代码，包含修改用户薪资、初始化薪资、查询列表的方法。
画面11：展示 SalariesApplication.java 启动类，包含 @SpringBootApplication 注解和 main 方法。
画面12：展示前端薪资列表页面，显示员工信息和操作按钮。
画面13：展示 SalariesApplication.java 启动类，包含 @Bean 注解的 IdWorker 实例。
画面14：展示前端薪资列表页面，显示“本月：入职/离职/调薪/中退”按钮和员工列表。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
@Entity(name = "sa_company_settings")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class CompanySettings implements Serializable {
    private static final long serialVersionUID = -262868884659248618L;
    @Id
    private String companyId;
    /**
     * 是否设置 0为未设置，1为已设置
     */
    private Integer isSettings;
    /**
     * 当前显示报表月份
     */
    private String monthAll;
}
```

画面5：
```java
package com.lhrm.salaries.dao;
import com.lhrm.salaries.entity.UserSalary;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import java.util.List;
public interface UserSalaryDao extends JpaRepository<UserSalary, Long>, JpaSpecificationExecutor<UserSalary> {
    @Query(value = "select bu.id,bu.username,bu.mobile,bu. bu_in_service_status inServiceStatus, bu.form_of_employment formOfEmployment, count(*) from bs_user bu where bu.id = ?1")
    Page<Map> findPage(String companyId, PageRequest page);
}
```

画面6：
```java
package com.lhrm.salaries.service;
import com.lhrm.salaries.dao.ArchiveDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
@Service
public class ArchiveService {
    @Autowired
    private ArchiveDao archiveDao;
    @Autowired
    private ArchiveDetailDao archiveDetailDao;
    @Autowired
    private IdWorker idWorker;
}
```

画面7：
```java
package com.lhrm.salaries.service;
import com.alibaba.fastjson.JSON;
import com.lhrm.common.entity.Result;
import com.lhrm.domain.wte.Bo.AtteSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserCompanyPersonal;
import com.lhrm.domain.wte.Bo.UserSalaryDetail;
import com.lhrm.domain.wte.Bo.UserSalary;
import com.lhrm.domain.wte.Bo.UserSalaryChange;
import com.lhrm.domain.wte.Bo.UserSalaryStatistics;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.UserSalaryStatisticsBO;
import com.lhrm.domain.wte.Bo.User
