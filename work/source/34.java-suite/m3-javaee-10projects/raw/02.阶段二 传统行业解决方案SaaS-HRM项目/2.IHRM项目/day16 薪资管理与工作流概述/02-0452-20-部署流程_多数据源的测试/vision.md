# 画面线理解：20-部署流程：多数据源的测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\20-部署流程：多数据源的测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:15, 00:42, 01:10, 01:34, 02:05, 02:31, 02:52, 03:09, 03:40, 05:29, 06:09, 06:31, 06:45, 07:28
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:57:45

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 JPA 实现对流程组（ProcUserGroup）的数据库操作，并通过 Activiti 流程引擎查询流程定义。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，打开 `AuditDataSourceConfig.java`，其中配置了数据源和实体管理器工厂，包含 Hibernate 的属性设置。
画面2：在 IDE 中复制 `ProcUserGroupDao.java` 文件，准备进行测试。
画面3：展示 `ProcUserGroup.java` 实体类，包含 `@Entity`、`@Table`、`@Id` 等注解，定义了实体字段。
画面4：展示 `AuditTest.java` 文件，导入了 Spring Boot 测试相关的依赖。
画面5：在 `AuditTest.java` 中添加 `@SpringBootTest` 和 `@RunWith(SpringRunner.class)` 注解。
画面6：在 `AuditTest.java` 中使用 `@Autowired` 注入 `ProcUserGroupDao`。
画面7：在 `AuditTest.java` 中编写测试方法 `test()`，调用 `findAll()` 方法并打印结果大小。
画面8：运行测试，控制台输出 Spring Boot 启动日志。
画面9：在 `AuditTest.java` 中添加注释说明测试内容。
画面10：在 `AuditTest.java` 中添加 `@Autowired` 注入 `RepositoryService`。
画面11：在 `AuditTest.java` 中编写测试方法 `testActiviti()`，调用 `repositoryService.createProcessDefinitionQuery().list()`。
画面12：运行测试，控制台输出 Activiti 流程引擎启动日志。
画面13：控制台输出 Activiti 流程定义查询结果。
画面14：测试成功，显示“1 test passed”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Qualifier("ihrmDataSource")
private DataSource ihrmDataSource;

@Bean
public LocalContainerEntityManagerFactoryBean ihrEntityManager() {
    LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
    em.setDataSource(ihrmDataSource);
    em.setPackagesToScan(new String[]{"com.ihrm.audit.entity"});
    em.setJpaVendorAdapter(new HibernateJpaVendorAdapter());
    HashMap<String, Object> properties = new HashMap<>();
    properties.put("hibernate.hbm2ddl.auto", env.getProperty("hibernate.hbm2ddl.auto"));
    properties.put("hibernate.dialect", env.getProperty("hibernate.dialect"));
    em.setJpaPropertyMap(properties);
    return em;
}

//平台事务管理器
@Bean
public PlatformTransactionManager ihrmTransactionManager() {
    JpaTransactionManager transactionManager = new JpaTransactionManager();
    transactionManager.setEntityManagerFactory(ihrmEntityManager().getEntityManagerFactory());
    return transactionManager;
}
```

画面3：
```java
package com.ihrm.audit.entity;

import org.springframework.data.jpa.domain.support.AuditingEntityListener;
import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "proc_user_group")
@Data
@org.springframework.data.jpa.domain.support.AuditingEntityListener
public class ProcUserGroup implements Serializable {
    @Id
    private String id;
    private String name;
    private String param;
    private String isql;
}
```

画面5：
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class AuditTest {
}
```

画面6：
```java
@Autowired
private ProcUserGroupDao procUserGroupDao;
```

画面7：
```java
@Test
public void test() {
    List<ProcUserGroup> list = procUserGroupDao.findAll();
    System.out.println(list.size());
}
```

画面10：
```java
@Autowired
private RepositoryService repositoryService;
```

画面11：
```java
@Test
public void testActiviti() {
    //测试activiti中的所有流程
    List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().list();
    System.out.println(list.size());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
