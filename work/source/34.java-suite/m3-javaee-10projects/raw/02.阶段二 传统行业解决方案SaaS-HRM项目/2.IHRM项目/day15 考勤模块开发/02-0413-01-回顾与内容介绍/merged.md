# 01-回顾与内容介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\01-回顾与内容介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 5分54秒（音频 355s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 各位朋友大家好那今天呢我们继续这个IHRM人力资源管理系统的学习那在昨天的内容呢和各位一起简单的来聊了一下咱们做网关好了这边呢我以一张图形的形式简单的记一下那在昨天内容呢咱们首先第一个讲的是一个叫做做网关做网关那这个做网关我们详细的
[00:32] 去解释了一下对住网关里面涉及到的两块核心功能比如说呢第一个就是它叫做路由那我们都知道住网关它的主要目的就是接收所有的请求把请求转发到不同的微服务上那除了这个住网关的这个路由功能之外它里面还有第二大功能就叫做过滤器那通过过滤器呢能够完成
[00:58] 统一的用户健全能够完成比如说我们的负载的一个平衡等等等等那我们自己写代码的时候也看过其实对于这个做网关而言呢没有各位想象的那么复杂其实呢就是遵守一定的代码编写的一些套路就可以了比如说我们这边需要搞一个我们的启动类出来在启动类上边我们需要注意一个开启网关功能那接着配置对应的一对
[01:28] ZOO相关的配置文件即可那如果你需要设计到过滤器咱们就写一个过滤器去继承ZOO filter是不是就可以了好了那这个ZOO网关我们看过了之后接下来呢昨天我们又来聊了第二块比较重要的内容就是叫做社保管理那这个社保管理呢是我们一个人力资源管理系统当中比较重要的一个环节那人力资源管理系统
[01:57] 里面涉及到的三个重要环节咱们完成了一个那除了这个社保我们是不是还应该有叫做考勤那除了考勤之外我们还应该有就是薪资那我们昨天完成的是社保管理里面的一小块功能我们可以打开我们的浏览器一起来看一下好了这边呢我已经把所有的系统呢全部都启动起来了这边点击登录进去哎我们完成了社保功能那在社保功能首先列表已经
[02:25] 搞定了并且在这边可以对用户的社保的数据呢咱们进行修改那同样的我们在边可以有月报表一个内容好了这个就是我们昨天和各位一起来看的这些点那么在昨天的同时也给各位留了一个小小的任务啊就是说啊咱们这个社保模块完成了这个月份的报表以及对当前月份报表的一个规档
[02:57] 那是不是还留了一个就是历史归档相关的这块内容没错吧OK好了这个是简单的和各位一起来说了一下我们昨天已经学过的这些支点那接着我们来看一下就是对于今天要跟各位咱们完成的这些功能那对于今天呢首先第一件事就是把昨天那个作业给它补充完整就是我们社保这边的归档相关的一些操作
[03:23] 那加上规档这些操作之后我们社保的模块呢就全部都完成了那接下来呢咱们就开始说了人力资源管理除了社保之外是不是还应该有对应的考勤因为加上社保加上考勤才能计算出一个员工他当月的这个薪资水平所以第二块呢我们要去玩考勤相关的那一个公司这个考勤简单的这边来说一下就一个公司的这个考勤
[03:51] 那考勤的其实是有很多的比如说呢有我们正常的初勤情况那这个初勤每个公司可能有不同的要求比如说有的公司早晨八点半要打卡上班下午五点半打卡下班那除了这个初勤之外呢还有就是休假那每个公司呢可能也有不同的休假的一些要求比如说在传统的在大部分公司周六周日是休假的但是在某些公司呢
[04:22] 可能是135要休息246要上班当然这个不太现实是吧OK但是这个意思各位应该能理解所以对于不同的公司这些出琴它的一些要求休假的一些要求等等等等我们都需要进行系统设置所以我们这边在做考琴之前要去做一个考琴相关的设置功能那这块设置包含了我们出琴等等等等
[04:47] 考勤设置搞定了之后接下来呢我们就开始玩这个考勤管理那其实说白了考勤管理就是查询一下在指定的月份全公司这些人的一些出勤记录那比如说张三周一周二周三周四他是迟到了还是正常上班还是旷工了等等那当然了这个考勤如果出现问题我们也可以对他进行修改
[05:13] 那修改了之后我们有考勤的一个归档那注意归档之后这个记录呢就不可以再去进行修改了其实跟我们这边社保是一样的那社保九月份我们制作完成并且归档那考勤九月份我们制作完成并且归档完成那这两个归档的记录就为我们做薪资提供了数据保障所以最后我们要去玩一下我们的薪资管理当了
[05:41] 今天的时间是有限的我们这个薪资管理呢只能完成一部分的这个功能OK好了这个就是跟各位简单的回顾了一下昨天的内容同时也说了一下我们今天要做的这些点

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面 12: 在 PDF 文档中，显示“1.1 归档历史列表”部分，包含 Controller 和 Service 层的代码。
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
        - id: user-Service
          uri: lb://user-Service
          predicates:
            - Path=/user/**
        - id: social-security-Service
          uri: lb://social-security-Service
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
// (1) Controller
@GetMapping(value = "/historys/{year}/list", method = RequestMethod.GET)
public Result historiesList(@PathVariable(value = "year") String year) throws Exception {
    List<Archive> archiveList = archiveService.findArchiveByYear(companyId, year);
    return new Result(ResultCode.SUCCESS, archiveList);
}
// (2) Service
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
(1) Controller
- `@GetMapping(value = "/historys/{year}/list", method = RequestMethod.GET)`
- `public Result historiesList(@PathVariable(value = "year") String year) throws Exception {`
- `List<Archive> archiveList = archiveService.findArchiveByYear(companyId, year);`
- `return new Result(ResultCode.SUCCESS, archiveList);`
(2) Service
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

