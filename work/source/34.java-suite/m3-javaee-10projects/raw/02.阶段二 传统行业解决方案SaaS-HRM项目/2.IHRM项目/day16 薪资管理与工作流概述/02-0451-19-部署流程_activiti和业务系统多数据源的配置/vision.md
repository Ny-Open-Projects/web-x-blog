# 画面线理解：19-部署流程：activiti和业务系统多数据源的配置

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\19-部署流程：activiti和业务系统多数据源的配置_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:24, 01:03, 01:39, 02:02, 02:49, 05:17, 05:37, 06:54, 07:29, 07:57, 08:45, 09:27, 10:02, 10:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:57:12

1) 这一组画面整体在讲如何在 Spring Boot 项目中配置两个数据源（activiti 和 ihrm），并为 JPA 仓库配置 EntityManager 和 TransactionManager。

2) 按时间顺序列出每张画面的要点：
画面1：在 IntelliJ IDEA 中，选中并高亮显示 `application.yml` 文件，该文件位于 `src/main/resources/` 目录下，内容为 Spring Boot 的配置，包含 `spring.datasource`、`shrm`、`redis`、`jpa` 等配置项。
画面2：聚焦于 `application.yml` 文件内容，展示 `spring.datasource` 下的 `act` 数据源配置（用于 Activiti）和 `shrm` 数据源配置（用于业务）。
画面3：在绘图工具中，绘制一个名为“HRM 系统”的矩形框，右侧绘制一个名为“activiti数据库”的椭圆框。
画面4：在绘图工具中，在“activiti数据库”椭圆框下方新增一个名为“业务数据库”的椭圆框，并标注“ihrm”。
画面5：在绘图工具中，在“HRM 系统”框右侧添加文字“Activiti内置数据库操作”和“工作流数据库”，并添加文字“SpringDataJPA 开发”和“业务数据源”。
画面6：在文件资源管理器中，显示了包含“day/4”、“day/5”、“day/6”等文件夹的目录结构。
画面7：在 IntelliJ IDEA 中，选中并高亮显示 `AuditDatasourceConfig.java` 文件，该文件位于 `src/main/java/com/ihrm/audit/` 目录下。
画面8：聚焦于 `AuditDatasourceConfig.java` 文件内容，展示其配置两个数据源的代码。
画面9：在绘图工具中，从“HRM 系统”框引出两条线，分别指向“activiti数据库”和“业务数据库”，并在线上标注“1.配置两个DataSource(act,ihrm)”和“2.SpringDataJPA并发: entityManager transactionManager”。
画面10：在 IntelliJ IDEA 中，选中并高亮显示 `JpaRepositoriesConfig.java` 文件，该文件位于 `src/main/java/com/ihrm/audit/` 目录下。
画面11：聚焦于 `JpaRepositoriesConfig.java` 文件内容，展示其配置 `@EnableJpaRepositories` 注解和 `@Autowired` 注解的代码。
画面12：聚焦于 `JpaRepositoriesConfig.java` 文件内容，展示其配置 `@Bean` 注解的 `LocalContainerEntityManagerFactoryBean` 和 `PlatformTransactionManager` 的代码。
画面13：在 IntelliJ IDEA 中，弹出“New Package”对话框，提示输入新包名。
画面14：在 IntelliJ IDEA 中，选中并高亮显示 `JpaRepositoriesConfig.java` 文件，该文件位于 `src/main/java/com/ihrm/audit/` 目录下，文件内容与画面12相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```yaml
#spring配置
spring:
  application:
    name: ihrm-audit #指定服务名
  datasource:
    act:
      jdbc-url: jdbc:mysql://localhost:3306/act?useUnicode=true&characterEncoding=utf8&serverTimezone=GMT
      username: root
      password: 111111
      driver-class-name: com.mysql.jdbc.Driver
    shrm:
      jdbc-url: jdbc:mysql://localhost:3306/ihrm?useUnicode=true&characterEncoding=utf8&serverTimezone=GMT
      username: root
      password: 111111
      driver-class-name: com.mysql.jdbc.Driver
  redis:
    host: 127.0.0.1
    port: 6379
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
    activiti:
      history-level: full
      db-history-used: true
    eureka:
      client:
```

画面7：
```java
package com.ihrm.audit;

import com.ihrm.audit;
@Configuration
public class AuditDatasourceConfig extends AbstractProcessEngineAutoConfiguration {
    @Bean
    @Primary
    @ConfigurationProperties(prefix = "spring.datasource.act")
    @Qualifier("activitiDataSource")
    public DataSource activitiDataSource() {
        return DataSourceBuilder.create().build();
    }
    @Bean
    @ConfigurationProperties(prefix = "spring.datasource.ihrm")
    @Qualifier("ihrmDataSource")
    public DataSource ihrmDataSource() {
        return DataSourceBuilder.create().build();
    }
}
```

画面10：
```java
package com.ihrm.audit;

import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@Configuration
@EnableJpaRepositories(basePackages = "com.ihrm.audit.dao",
        entityManagerFactoryRef = "ihrmEntityManager",
        transactionManagerRef = "ihrmTransactionManager")
public class JpaRepositoriesConfig {
    @Autowired
    private Environment env;
    @Autowired
    @Qualifier("ihrmDataSource")
    private DataSource ihrmDataSource;
    @Bean
    @Primary
    public LocalContainerEntityManagerFactoryBean ihmEntityManager() {
        LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
        em.setDataSource(ihrmDataSource);
        em.setPackagesToScan(new String[]{"com.ihrm.audit.entity"});
        HibernateJpaVendorAdapter vendorAdapter = new HibernateJpaVendorAdapter();
        em.setJpaVendorAdapter(vendorAdapter);
        HashMap<String, Object> properties = new HashMap<>();
        properties.put("hibernate.hbm2ddl.auto", env.getProperty("hibernate.hbm2ddl.auto"));
        properties.put("hibernate.dialect", env.getProperty("hibernate.dialect"));
        em.setJpaPropertyMap(properties);
        return em;
    }
    @Bean
    @Primary
    public PlatformTransactionManager ihrmTransactionManager() {
        JpaTransactionManager transactionManager = new JpaTransactionManager();
        transactionManager.setEntityManagerFactory(ihrmEntityManager().getObject());
        return transactionManager;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面3：架构图包含“HRM 系统”指向“activiti数据库”。
画面4：架构图包含“HRM 系统”指向“activiti数据库”和“业务数据库”。
画面5：架构图包含“HRM 系统”指向“activiti数据库”和“业务数据库”，并标注“Activiti内置数据库操作”和“SpringDataJPA 开发”。
画面9：架构图包含“HRM 系统”指向“activiti数据库”和“业务数据库”，并标注“1.配置两个DataSource(act,ihrm)”和“2.SpringDataJPA并发: entityManager transactionManager”。

5) 不要评价画面美观，不要输出与课程无关的内容。
