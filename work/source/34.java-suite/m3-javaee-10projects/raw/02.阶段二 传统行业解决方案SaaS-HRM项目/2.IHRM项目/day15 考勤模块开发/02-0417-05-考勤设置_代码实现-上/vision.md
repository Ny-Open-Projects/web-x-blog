# 画面线理解：05-考勤设置：代码实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day15 考勤模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day15 考勤模块开发\05-考勤设置：代码实现-上_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 01:14, 02:08, 03:07, 05:00, 05:50, 06:39, 07:15, 07:57, 09:12, 10:29, 11:29, 12:46, 14:11
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:31:11

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中创建并配置考勤模块，包括目录结构、配置文件、服务层和控制器层的代码编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 PPT 页面，标题为“2.3 环境搭建”下的“2.3.1 创建考勤模块”，并显示了项目目录结构，其中 `src/main/java/com.ihrm.attte` 包下包含 `client`、`controller`、`dao`、`service` 等子包，以及 `AttendanceApplication` 和 `ShiroConfiguration` 类。
画面2：显示记事本程序，空白页面，无内容。
画面3：在 IntelliJ IDEA 中打开 `SystemApplication.java`，代码中包含 Spring Boot 的配置注解，如 `@SpringBootApplication`、`@EnableDiscoveryClient`、`@EnableFeignClients`，并定义了 `main` 方法和两个静态方法 `getIdWorker()` 和 `getJwtUtils()`。
画面4：在 IntelliJ IDEA 中打开 `application.yml` 文件，内容为服务注册与配置，包括 Eureka 服务地址、端口、数据库连接信息（MySQL）、Redis 配置等。
画面5：在 IntelliJ IDEA 中，项目结构视图显示 `ihrm_common_model` 模块下的 `atte` 包，右侧为 IDE 的欢迎界面。
画面6：在 IntelliJ IDEA 中，项目结构视图显示 `ihrm_attendance` 模块下的 `dao` 包，同时弹出一个 PDF 文件窗口，显示了 `day15.pdf` 的内容。
画面7：在 IntelliJ IDEA 中打开 `AtteService.java`，代码中定义了 `@Service` 注解的类，包含多个 `@Autowired` 注入的 DAO 对象。
画面8：在 IntelliJ IDEA 中打开 `ReportService.java`，代码中定义了 `@Service` 注解的类，包含一个 `@Autowired` 注入的 `ArchiveMonthlyDao` 对象。
画面9：在浏览器中打开 `localhost:8080/#/attendances/index` 页面，显示了考勤状态的错误信息，状态码为 404。
画面10：在 IntelliJ IDEA 中打开 `ConfigController.java`，代码中包含 `@RestController` 注解，以及 `@RequestMapping` 注解。
画面11：在 IntelliJ IDEA 中打开 `ConfigController.java`，代码中定义了 `@RequestMapping(value = "/atte/item", method = POST)` 的方法。
画面12：在 SQLyog 中打开数据库表结构，显示了 `atte_attendance_config` 表的字段信息，包括 `company_id`、`department_id`、`create_date` 等字段。
画面13：在 IntelliJ IDEA 中打开 `ConfigController.java`，代码中定义了 `@RequestMapping(value = "/atte/item", method = POST)` 的方法，并注入了 `ConfigurationService`。
画面14：在 IntelliJ IDEA 中打开 `ConfigurationService.java`，代码中定义了 `@Autowired` 注入的多个 DAO 对象，并包含一个 `getAtteConfig` 方法，用于根据公司 ID 和部门 ID 查询考勤配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
创建考勤模块 ihrm_attendance
    ▼ ihrm_attendance
        ▼ src
            ▼ main
                ▼ java
                    ▼ com.ihrm.attte
                        ▼ client
                        ▼ controller
                        ▼ dao
                        ▼ service
                        ▼ AttendanceApplication
                        ▼ ShiroConfiguration
```

画面3：
```java
package com.ihrm.attte;
//配置springboot的包扫描
@SpringBootApplication(scanBasePackages = "com.ihrm")
//配置jpa注解的包
@EntityScan(value = "com.ihrm.domain.system")
@EnableFeignClient
@EnableDiscoveryClient
public class SystemApplication {
    /**
     * 启动方法
     */
    public static void main(String[] args) { SpringApplication.run(SystemApplication.class, args); }
    @Bean
    public IdWorker idWorker() { return new IdWorker(); }
    @Bean
    public JwtUtils jwtUtils() { return new JwtUtils(); }
    //不 session
    @Bean
    public OpenEntityManagerInViewFilter openEntityManagerInViewFilter() { return new OpenEntityManagerInViewFilter(); }
}
```

画面4：
```yaml
#注册到eureka的服务地址
eureka:
  service-url:
    defaultZone: http://127.0.0.1:8008/eureka/
  instance:
    preferIpAddress: true
    instance-id: ${spring.cloud.client.ip-address}:${spring.application.name}:${server.port}
#服务端口
server:
  port: 8005
#数据库配置
spring:
  application:
    name: ihrm social securitys #指定服务名
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/ihrm_attendance?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
    hikari:
      maximum-pool-size: 2
#redis配置
redis:
  host: 127.0.0.1
  port: 6379
  jpa:
```

画面7：
```java
package com.ihrm.attte.service;
import com.ihrm.attte.service;
@Service
public class AtteService {
    @Autowired
    private IdWorker idWorker;
    @Autowired
    private AttendanceDao attendanceDao;
    @Autowired
    private DeductionDictDao deductionDictDao;
    @Autowired
    private DaysMonthlyDao daysMonthlyDao;
    @Autowired
    private DepartmentDao departmentDao;
    @Autowired
    private UserDao userDao;
    @Autowired
    private AttendanceConfigDao attendanceConfigDao;
}
```

画面8：
```java
package com.ihrm.attte.service;
import com.ihrm.attte.dao.ArchiveMonthlyDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;
@Service
public class ReportService {
    @Autowired
    private ArchiveMonthlyDao archiveMonthlyDao;
}
```

画面10：
```java
package com.ihrm.attte.controller;
import org.springframework.web.bind.annotation.*;
@RestController
public class ConfigController {
}
```

画面11：
```java
package com.ihrm.attte.controller;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/cfg")
public class ConfigController extends BaseController{
    @RequestMapping(value = "/atte/item", method = POST)
    public Result atteConfig(String departmentId) {
        configurationService.getAtteConfig(companyId, departmentId);
    }
}
```

画面13：
```java
package com.ihrm.attte.controller;
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping("/atte/item")
public class ConfigController extends BaseController{
    @Autowired
    private ConfigurationService configurationService;
    @RequestMapping(value = "/atte/item", method = POST)
    public Result atteConfig(String departmentId) {
        configurationService.getAtteConfig(companyId, departmentId);
    }
}
```

画面14：
```java
private AttendanceConfigDao attendanceConfigDao;
private LeaveConfigDao leaveConfigDao;
private DeductionDictDao deductionDictDao;
private ExtraDutyConfigDao extraDutyConfigDao;
private ExtraDutyRuleDao extraDutyRuleDao;
private DayOffConfigDao dayOffConfigDao;
private IdWorker idWorker;
//查询考勤设置
public AttendanceConfig getAtteConfig(String companyId, String departmentId) {
    return attendanceConfigDao.findByCompanyIdAndDepartmentId(companyId, departmentId);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT 标题为“2.3 环境搭建”，子标题为“2.3.1 创建考勤模块”，并显示了项目目录结构。
画面10：PPT 中显示了 `ConfigController` 类的注解信息，包括 `@RestController`、`@RequestMapping` 等。
画面11：PPT 中显示了 `ConfigController` 类的注解信息，包括 `@RequestMapping(value = "/atte/item", method = POST)`。
画面12：SQLyog 中显示了 `atte_attendance_config` 表的字段信息，包括 `company_id`、`department_id`、`create_date` 等字段。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
