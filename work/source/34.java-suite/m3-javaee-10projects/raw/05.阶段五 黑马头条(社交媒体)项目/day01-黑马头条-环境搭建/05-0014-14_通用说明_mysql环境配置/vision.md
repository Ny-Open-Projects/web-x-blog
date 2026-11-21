# 画面线理解：14_通用说明_mysql环境配置

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day01-黑马头条-环境搭建
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day01-黑马头条-环境搭建\14_通用说明_mysql环境配置【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:15, 02:08, 04:05, 06:05, 07:47, 08:41, 10:50, 12:28, 14:16, 16:53, 18:42, 19:58, 21:34, 22:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 12:34:00

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中配置 MySQL 数据源和 MyBatis 的 SqlSessionFactory，包括读取配置文件、创建数据源、配置连接池和事务管理。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目结构，选中 `mysql-core-jdbc.properties` 配置文件，准备进行数据库配置。
画面 2：展示 `mysql-core-jdbc.properties` 文件内容，包含数据库连接 URL、用户名、密码、驱动等配置。
画面 3：展示 `MysqlCoreConfig.java` 文件，开始编写配置类，导入 Spring 注解。
画面 4：在 `MysqlCoreConfig` 类中，使用 `@Configuration` 注解，并通过 `@PropertySource` 注入 `mysql-core-jdbc.properties` 文件。
画面 5：在 `MysqlCoreConfig` 类中，定义 `HikariDataSource` 实例并设置数据库连接参数。
画面 6：展示 PPT 内容，标题为“6.5 通用属性说明”，子标题“6.5.2 mysql的环境配置”，并列出“6.5.2.1 数据库连接池”、“6.5.2.2 事务管理”、“6.5.2.3 MyBatis”等小节。
画面 7：在 `MysqlCoreConfig` 类中，继续编写 `SqlSessionFactoryBean` 的配置，设置数据源和包扫描路径。
画面 8：切换到 `heima-leadnews-model` 模块，展示其目录结构，选中 `mappers` 目录。
画面 9：在 `MysqlCoreConfig` 类中，配置 `SqlSessionFactoryBean` 的 `mapperLocations` 属性，用于指定映射文件位置。
画面 10：在 `MysqlCoreConfig` 类中，配置 `SqlSessionFactoryBean` 的 `configuration` 属性，用于设置 MyBatis 的全局配置。
画面 11：在 `MysqlCoreConfig` 类中，配置 `SqlSessionFactoryBean` 的 `mapperLocations` 属性，使用 `classpath*:/mappers/` 通配符。
画面 12：在 `MysqlCoreConfig` 类中，配置 `SqlSessionFactoryBean` 的 `configuration` 属性，设置 `logImpl` 为 `LOG4J2`。
画面 13：在 `MysqlCoreConfig` 类中，配置 `SqlSessionFactoryBean` 的 `configuration` 属性，设置 `mapUnderscoreToCamelCase` 为 `true`。
画面 14：在 `MysqlCoreConfig` 类中，添加一个 `getReversePassword` 方法，用于对密码进行反转操作。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```
# 日志级别
log.level=DEBUG
log.pattern=%d{DEFAULT} [%M] [%nlevel] [%c] %M %n%nMsg%n

# 本地只读
mysql.core.jdbc.url=jdbc:mysql://localhost:3306/heima_leadnews?autoReconnect=true&useUnicode=true
mysql.core.jdbc.username=root
mysql.core.jdbc.password=test
mysql.core.jdbc.driver=com.mysql.jdbc.Driver

mysql.core.root.mapper=mappers
mysql.core.alises.package=com.heima.model.**
mysql.core.tx.scan.package=execution(* com.heima.service.*(..))

# admin 用户
admin.username=admin
admin.password=admin

hostname.eureka.server=localhost
eureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka/
```

画面 3：
```
package com.heima.common.mysql.core;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MysqlCoreConfig {
    // 设置一个数据库的连接池
    @Autowired
    private MysqlCoreConfig mysqlCoreConfig;
```

画面 4：
```
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.jdbc.datasource.SimpleDriverDataSource;
import org.springframework.jdbc.datasource.TransactionAwareDataSourceProxy;
import org.springframework.jdbc.datasource.UnwrapDataSource;
import org.springframework.jdbc.datasource.lookup.DataSourceLookup;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactory;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactory;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactory;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactory;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean;
import org.springframework.jdbc.datasource.lookup.DataSourceLookupFactoryBeanFactoryBeanFactoryBeanFactoryBean
