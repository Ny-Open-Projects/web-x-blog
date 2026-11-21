# 08-薪资模块：分页列表代码分析

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\08-薪资模块：分页列表代码分析_【海量资源尽在 ubkz.com】.mp4
- 时长 5分55秒（音频 356s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好我们刚才呢已经把这个环境搭建好了那接下来呢咱们就简单的说一下里面涉及到的这几块功能刚才已经简单说过了进入到工资所涉及到的企业设置的一个表的数据操作先查询再更新好了那接下来呢进入到页面之后展示的是这个用户的所有列表那这个列表呢带分页那执行的是哪个方法我们回到咱们的代码当中一起来看一下那这边呢我要查询的其实就是
[00:30] 用户薪资的列表那用户薪资就在salary Controller当中我们一起来找到列表那在这边呢请求过来之后可以拿到配置拿到size那需要各位注意的是打开F12来看一下那刷新找到列表list那这个list请求过来之后是post请求那给我们封装成了这么一个参数
[01:00] 有配置有info等等那接下来呢对于我们而言那进行查询那查询的时候呢其实是这样的我们这边呢就需要把参数你request body的形式封装成一个map当然你想封装成实体类也可以那封装好了之后配置page size获取到两个分页参数那接着调用Service来进行查询进入到Service那Service查询很简单直接调用do那do接着我们来看一下
[01:29] 那DU这个时候呢咱们用到之前掌握或者之前学过的这么一个技术就是在SpringDataJPA当中以原生Circle的形式来进分页DataJPA使用本地Circle分页查询那这个查询呢就需要借助这个Query注解那Query注解当中有这么几个属性要跟各位来说一下简单的来回顾一下那首先呢第一个Navquery
[02:04] 处表示本地circle好了这个value代表的是我们查询的circle语句好了那接着还有一个countquerycountquery因为我们分页的时候分页的时候是不是应该要查询总记录数的circle语句所以
[02:25] 这样一来它自动的就会对我们进行封装这是我们这个query注解呢做了一个小小的解释那除了query注解之外还有需要跟各位说明的就是如果说你要使用这个本地circle进行分页我直接写到这里面了本地circle进行分页那我们查询的时候啊这边需要有这么一个参数这个是必须的这个参数是什么就是page request那page request里面
[02:54] 配置我们分页的基本数据包括了我们的起始页包括我们的页码还有每页查询条数那各位来看这个参数我们从哪传递过来的找到Service来看是我们自己构造了一个page request那page-1和page-7那这样一来它会自动的分页那对于里面这个sales语句呢它比较长了这个我就不再啰嗦了那它查的是什么现在来看我查询的是
[03:25] 员工薪资user salary以及BS user这两张表联合查询这两张表联合查询的一个结果那我们查询的是这样的BS user是所有的员工那这个user salary是这个员工的所有薪资那一个员工呢先在用户表里肯定有但是薪资表里未必有因为你刚入职可能还没有设置薪资没错吧所以我用了一个左外连接查询user的同时左外查询薪资
[03:55] 那各位来看伺候一句left join没错吧好了那接着这边呢还有一个小小的最后一个疑问就是我们的返回值返回值那这个返回值呢正常的逻辑我们需要构造构造实体类返回值那也就意味着配置里面装的其实是一个咱们的Java entity对象那为什么不这样写呢不构造一个实体类呢是这样的就是我们这边不构造实体类
[04:29] 是因为你如果说要去构造实体类你还需要去写一个对应实体类的这么一个DU那接着再去搞这一大堆才能这样查不知道各位有没有听懂那这边我再解释一下如果有一个新的实体类你这实体类显然不是我们刚才这个user salary因为user salary只有薪资它没有用户的用户名等等等等所以你如果想要构造实体类的话你就需要构造一个新的实体类
[04:56] 那在SpringDataJPG当中一个实体类要对应这么一个DU接口你构造新的就要写DU新的那才能给你封装对象所以我为了避免这个问题我直接返回一个map所以我们这边直接的就是返回map那这个返回map它的类型是什么样的注意它的key等于我们查询的字段名好了这个value就是对应的是这个值了所以我们构造出来了
[05:25] 注意查询之后得到的这么一行数据一行数据代表的是一个map集合那map集合key是user idvalue就是这个值那key代表的是current basebasicalaccelerate那value就是这个3应该能懂我意思吧所以一个map代表一条数据OK好了这个就是我们这个查询列表它的一个逻辑当然这个逻辑呢在我们之前学习社保的时候也用了一下基本上跟这个是一模一样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
    //2.使用Service查询
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

