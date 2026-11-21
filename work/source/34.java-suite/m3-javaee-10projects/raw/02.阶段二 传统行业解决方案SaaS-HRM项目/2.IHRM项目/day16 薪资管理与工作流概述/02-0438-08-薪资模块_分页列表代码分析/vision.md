# 画面线理解：08-薪资模块：分页列表代码分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\08-薪资模块：分页列表代码分析_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:29, 00:37, 00:50, 00:59, 01:29, 02:01, 02:27, 02:46, 03:17, 04:00, 04:38, 05:26, 05:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:47:58

1) 这一组画面整体在讲什么（一句话）：
演示如何在 iHRM 人事管理系统中，通过 Spring Boot + MyBatis-Plus 实现员工薪资分页查询功能，包括前端页面、后端 Controller、Service、DAO 层代码及数据库 SQL。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 iHRM 系统的员工薪资列表页面，包含筛选条件（聘用形式、员工状态、部门）和分页操作，页面 URL 为 /salaries/list?yearMonth=201907。
画面 2：展示 IntelliJ IDEA 中项目结构，主启动类 SalaryApplication.java，其中包含 @SpringBootApplication、@EntityScan、@EnableFeignClients 注解，以及一个 @Bean 注解的 IdWorker 实例。
画面 3：展示 SalaryController.java 中的 list 方法，用于处理分页查询请求，通过 PageResult pr = salaryService.findAll(page, pageSize, companyId); 返回分页数据。
画面 4：展示浏览器开发者工具 Network 标签页，显示对 localhost:8080 的请求，返回状态码 304（未修改），资源包括 app.js 和 profile。
画面 5：展示 Network 标签页中 Request Payload，包含分页参数 {page: 1, pageSize: 10}。
画面 6：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 7：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 8：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 9：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 10：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 11：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 12：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。
画面 13：展示 SQLyog 数据库管理工具，显示 user_salary 表的数据，包含 user_id、current_basic_salary、current_post_wage、fixed_basic_salary、fixed_post_wage、correction_of_basic_wage 等字段。
画面 14：展示 UserSalaryDao.java 中的 @Query 注解，定义了 nativeQuery 为 true 的 SQL 查询语句，用于分页查询。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
package com.ihrm.salarys;
import com.ihrm.salarys;
@SpringBootApplication(scanBasePackages = "com.ihrm")
@EntityScan(value = "com.ihrm.domain")
@EnableFeignClients
public class SalaryApplication {
    //启动方法
    public static void main(String[] args) { SpringApplication.run(SalaryApplication.class, args); }
    @Bean
    public IdWorker idWorker() { return new IdWorker(); }
}
```

画面 3：
```java
//查询列表
@PostMapping(value = "/list", method = RequestMethod.POST)
public Result list(@RequestBody Map map) {
    //1.获取请求参数
    Integer page = (Integer) map.get("page");
    Integer pageSize = (Integer) map.get("pageSize");
    //2.使用service查询
    PageResult pr = salaryService.findAll(page, pageSize, companyId);
    return new Result(ResultCode.SUCCESS, pr);
}
```

画面 6：
```java
@Query(nativeQuery = true,
        value = "select bu.id,bu.username,bu.mobile,bu.work_number workNumber, " +
                "bu.in_service_status inServiceStatus,bu.department_name departmentName,bu.department_id departmentId,bu.time_of_entry timeOfEntry, " +
                "bu.form_of_employment formOfEmployment,sauss.current_basic_salary currentBasicSalary,sauss.current_post_wage currentPostWage " +
                "from bs_user bu LEFT JOIN sa_user_salary sauss ON bu.id=sauss.user_id WHERE bu.company_id = ?1",
        countQuery = "select count(*) from bs_user bu LEFT JOIN sa_user_salary sauss ON bu.id=sauss.user_id WHERE bu.company_id = ?1")
Page<Map> findPage(String companyId, PageRequest pageRequest);
```

画面 13：
```sql
SELECT
    user_id,
    current_basic_salary,
    current_post_wage,
    fixed_basic_salary,
    fixed_post_wage,
    correction_of_basic_wage
FROM user_salary
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
