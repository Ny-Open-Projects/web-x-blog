# 画面线理解：01-回顾与内容介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\01-回顾与内容介绍_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 00:21, 01:09, 01:18, 01:27, 01:33, 02:14, 02:20, 02:23, 02:28, 02:36, 03:11, 03:49, 04:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:27:56

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 和 ZuuL 的 HR 系统中，社保模块的后端代码实现与前端界面操作，以及考勤模块的数据展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 桌面环境，显示“黑马程序员”和“博学谷”两个机构的标志。
画面 2: 打开画图程序，空白画布，准备绘制内容。
画面 3: IntelliJ IDEA 中打开 `UserSocialSecurityDao.java` 文件，展示一个继承自 `JpaRepository` 的接口，其中包含注释说明其功能，如“方法返回值”、“分页对象”、“sql语句”等。
画面 4: 在 `UserSocialSecurityDao.java` 文件中，高亮显示了 `@Query` 注解的 SQL 查询语句，用于查询社保数据。
画面 5: 在 IntelliJ IDEA 中，打开 `application.yml` 文件，位于 `ihrm_gate` 模块下，用于配置网关。
画面 6: 在 IntelliJ IDEA 中，打开 `LoginFilter.java` 文件，位于 `filter` 包下，展示了一个自定义的过滤器类。
画面 7: 在画图程序中，绘制了一个文本框，内容为“1.zuul网关”、“路由”、“过滤器”和“2.社保管理”、“考勤，薪资”。
画面 8: 在浏览器中打开 HR 系统的首页，显示“工作日历”和“绩效指数”等模块。
画面 9: 在浏览器中打开社保列表页面，显示员工社保信息，包括姓名、工号、部门、入职时间、离职时间、社保城市、公积金城市、社保基数、公积金。
画面 10: 在浏览器中打开社保详情页面，显示社保类型、社保基数、工龄比例等信息。
画面 11: 在浏览器中再次显示社保列表页面，鼠标悬停在“入职时间”列。
画面 12: 在 PDF 文档中，显示“1.1 归档历史列表”部分，包含 controller 和 service 层的代码。
画面 13: 在画图程序中，绘制了一个文本框，内容为“1.zuul网关”、“路由”、“过滤器”和“2.社保管理”、“考勤，薪资”。
画面 14: 在 PDF 文档中，显示“3 考勤管理”部分，包含考勤模块的介绍和数据表格。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```java
package com.ihrm.social.dao;
import ...
public interface UserSocialSecurityDao extends JpaRepository<UserSocialSecurity, String>, JpaRepository<UserSocialSecurity, String> {
    //方法返回值
    //分页对象
    //sql语句
    @Query(nativeQuery = true,
    value = "SELECT bu.id, bu.user_id, bu.username, bu.mobile, bu.work_number, bu.department_name, bu.time_of_entry, bu.time_of_dismissal, bu.participating_in_the_city, bu.suss_participating_in_the_city_id, bu.suss_provident_fund_city_id, bu.suss_social_security_base, bu.suss_provident_fund_city_id, bu.suss_provident_fund_base FROM bs_user bu LEFT JOIN ss_user_social_security suss ON bu.id = suss.user_id WHERE bu.id = ?1")
    Page<UserSocialSecurity> findPage(Pageable pageable);
}
```

画面 4:
```java
@Query(nativeQuery = true,
value = "SELECT bu.id, bu.user_id, bu.username, bu.mobile, bu.work_number, bu.department_name, bu.time_of_entry, bu.time_of_dismissal, bu.participating_in_the_city, bu.suss_participating_in_the_city_id, bu.suss_provident_fund_city_id, bu.suss_social_security_base, bu.suss_provident_fund_city_id, bu.suss_provident_fund_base FROM bs_user bu LEFT JOIN ss_user_social_security suss ON bu.id = suss.user_id WHERE bu.id = ?1")
Page<UserSocialSecurity> findPage(Pageable pageable);
```

画面 5:
```yaml
# application.yml
server:
  port: 8080
spring:
  application:
    name: ihrm-gate
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: lb://user-service
          predicates:
            - Path=/user/**
        - id: social-security-service
          uri: lb://social-security-service
          predicates:
            - Path=/social-security/**
```

画面 6:
```java
package com.ihrm.gate.filter;
import ...
@Component
public class LoginFilter extends ZuulFilter {
    @Override
    public String filterType() {
        return "pre";
    }
    @Override
    public int filterOrder() {
        return 2;
    }
    @Override
    public boolean shouldFilter() {
        return true;
    }
    @Override
    public Object run() {
        return null;
    }
}
```

画面 12:
```java
// 1.1 归档历史列表
// (1) controller
@GetMapping(value = "/historys/{year}/list", method = RequestMethod.GET)
public Result historiesList(@PathVariable(value = "year") String year) throws Exception {
    List<Archive> archiveList = archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, archiveList);
}
// (2) service
public List<Archive> findArchiveByYear(String companyId, String yearMonth) {
    return archiveDao.findByCompanyIdAndYearMonthLike(companyId, yearMonth);
}
```

画面 14:
```markdown
3 考勤管理

考勤模块是为了减轻手工考勤的繁杂工作，做到公平可信，建立严格的出勤制度，从而提高企业的执行效率、考勤统计数据设定自动转入新薪资模块，按照既定公式进行新薪资，可以为某些行业特殊的人员生产率报表提供可靠的数字。

| 序号 | 姓名 | 工号 | 部门 | 入职时间 | 离职时间 | 考勤类型 | 考勤状态 | 考勤备注 |
|------|------|------|------|----------|----------|----------|----------|----------|
| 1 | a01 | 1340000001 | 开发部 | 2018-01-01 | — | 正常 | 正常 | — |
| 2 | a02 | 1340000002 | 开发部 | 2018-01-01 | — | 正常 | 正常 | — |
| 3 | test001 | 1350000001 | 开发部 | 2018-01-01 | — | 正常 | 正常 | — |
| 4 | test002 | 1350000002 | 开发部 | 2018-01-01 | — | 正常 | 正常 | — |
| 5 | test003 | 1350000003 | 开发部 | 2018-01-01 | — | 正常 | 正常 | — |

3.1 数据导入

北京市昌平区建材城西路金燕龙办公一层 电话：400-618-9090
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 12:
标题：1.1 归档历史列表
内容：
(1) controller
- `@GetMapping(value = "/historys/{year}/list", method = RequestMethod.GET)`
- `public Result historiesList(@PathVariable(value = "year") String year) throws Exception {`
- `List<Archive> archiveList = archiveService.findArchiveByYear(companyId, year);`
- `return new Result(ResultCode.SUCCESS, archiveList);`
(2) service
- `public List<Archive> findArchiveByYear(String companyId, String yearMonth) {`
- `return archiveDao.findByCompanyIdAndYearMonthLike(companyId, yearMonth);`

画面 14:
标题：3 考勤管理
内容：
- 考勤模块是为了减轻手工考勤的繁杂工作，做到公平可信，建立严格的出勤制度，从而提高企业的执行效率、考勤统计数据设定自动转入新薪资模块，按照既定公式进行新薪资，可以为某些行业特殊的人员生产率报表提供可靠的数字。
- 表格数据：
  | 序号 | 姓名 | 工号 | 部门 | 入职时间 | 离职时间 | 考勤类型 | 考勤状态 | 考勤备注 |
  |------|------|------|------|----------|----------|----------|----------|----------|
  | 1 | a01 | 1340000001 | 开发部 | 2018-01
