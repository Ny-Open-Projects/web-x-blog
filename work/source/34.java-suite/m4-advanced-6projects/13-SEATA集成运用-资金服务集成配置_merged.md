# 13-SEATA集成运用-资金服务集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来接着咱们去修改资金服务

去实现CETA主线的集成配置

之前咱们已经实现了交易服务的集成

那资金服务整体实现流程和交易服务的集成呢

基本上是一致的

咱们在这里就做一个快速实现

那回到工程当中

咱们首先去copy CETA客户端的配置信息

将这两个文件copy

然后放置在资金服务的资源目录下面

Binance

粘贴

这里直接copy过来之后

不需要做任何的调整和修改

因为在这里面并没有个性化的配置信息

接下来就去修改矿物文件增加CETA的依赖

那我们从交易服务里面做一个copy

选中CETA的主线依赖

把它放置Binance资金服务的下面

这里咱们之前已经配置好了

那就不需要再copy

接下来就去实现CETA的代码配置

从交易服务当中copy CETA的配置内

放在根据一个目录下面

这里面也不需要做任何调整

因为它会根据Spring Application Name的属性

自动读取服务的名称

最后就是修改数据源的配置

我们先从Lui的配置内当中

将CETA的数据源代理配置copy过来

把它放在资金服务的Lui的配置内当中

注意这个名称要配置正确

这个和业务数据源的名称是一致的

接下来就去修改业务数据源的具体配置

将Circle Session Factory里面的Data Source

做一个替换采用BitProxy Data Source

然后再去修改Transaction Manager里面的Data Source

好

那资金服务的CETA集成配置

咱们就已经实现完成

那这一讲话就先说到这里了

那这一讲话就先说到这里了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于“分布式事务”技术课程的第17讲，核心内容是将“资金服务”模块集成到“Seata”分布式事务框架中。讲师通过 IntelliJ IDEA 开发环境，演示了如何在项目中进行配置修改，包括：
- 在 `resources` 目录下创建并配置 `registry.conf` 和 `file.conf` 文件。
- 修改 `pom.xml` 文件，添加 Seata 的 Maven 依赖。
- 编写 Spring Boot 配置类 `SeataConfiguration`，用于初始化 Seata 的全局事务扫描器。
- 配置数据源代理，通过 `DataSourceProxy` 将业务数据源包装为支持 Seata 事务管理的数据源。
- 最终目标是使资金服务能够参与 Seata 的分布式事务管理，确保数据一致性。

---

### 2) 按时间顺序的章节（带时间点）

由于无法从画面中精确获取时间戳，以下章节基于画面内容和逻辑顺序进行划分：

- **00:00 - 00:15**: 课程导入与目标说明。讲师在 Typora 文档中展示了本讲的标题“3.3 资金服务集成 SEATA”，并概述了本讲将完成的三个主要步骤：工程配置修改、依赖支持、增加配置类。
- **00:16 - 00:35**: **工程配置修改**。讲师在 IDEA 中导航至 `bulls-stock-finance` 项目，演示在 `resources` 目录下创建 `registry.conf` 和 `file.conf` 文件，并展示了 `registry.conf` 文件中的配置内容，如 `eurekaUrl`、`redis`、`zk` 和 `file` 等配置项。
- **00:36 - 01:00**: **依赖支持**。讲师在 `pom.xml` 文件中添加 Seata 的 Maven 依赖，配置 `groupId` 为 `io.seata`，`artifactId` 为 `seata-all`，并使用 `${seata.version}` 作为版本号。
- **01:01 - 01:25**: **增加配置类**。讲师创建并编辑 `SeataConfiguration.java` 文件，使用 `@Configuration` 注解，并通过 `@Bean` 方法创建 `GlobalTransactionScanner` 实例，配置其 `applicationId` 和 `txServiceGroup`。
- **01:26 - 01:50**: **数据源代理配置**。讲师在 `DruidSystemDataSourceConfiguration.java` 文件中，通过 `@Bean` 方法创建 `DataSourceProxy`，将 `bizSystemDataSource` 代理为支持 Seata 事务的数据源。
- **01:51 - 02:15**: **事务管理器配置**。讲师在 `BizSystemDataSourceConfiguration.java` 文件中，配置 `SqlSessionFactory` 和 `TransactionManager`，并使用 `@Qualifier` 注解指定数据源，确保事务管理器与代理数据源的绑定。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

#### PPT / 文档内容

- **文档标题**: `Day17.md`，章节标题为“3.3 资金服务集成 SEATA”。
- **步骤清单**:
  1.  工程配置修改
  2.  依赖支持
  3.  增加配置类

#### 代码关键内容

- **`registry.conf` 文件配置**:
  ```properties
  namespace = public
  cluster = "default"
  eurekaUrl = "http://localhost:1001/eureka"
  application = "default"
  weight = "1"
  redis {
    serverAddr = "localhost:6381"
    db = "0"
  }
  zk {
    cluster = "default"
    serverAddr = "127.0.0.1:2181"
    session.timeout = 6000
    connect.timeout = 2000
  }
  file {
    name = "file.conf"
  }
  ```

- **`pom.xml` 依赖配置**:
  ```xml
  <!-- Seata 分布式事务依赖 -->
  <dependency>
    <groupId>io.seata</groupId>
    <artifactId>seata-all</artifactId>
    <version>${seata.version}</version>
  </dependency>
  ```

- **`SeataConfiguration.java` 配置类**:
  ```java
  @Configuration
  public class SeataConfiguration {
      @Value("${spring.application.name}")
      private String applicationId;

      @Bean
      public GlobalTransactionScanner globalTransactionScanner() {
          GlobalTransactionScanner globalTransactionScanner = new GlobalTransactionScanner(applicationId, "stock_trade_group");
          return globalTransactionScanner;
      }
  }
  ```

- **`DruidSystemDataSourceConfiguration.java` 数据源代理配置**:
  ```java
  @Bean("bizProxyDataSource")
  public DataSourceProxy bizProxyDataSource(@Qualifier("bizSystemDataSource") DataSource bizSystemDataSource) {
      return new DataSourceProxy(bizSystemDataSource);
  }
  ```

- **`BizSystemDataSourceConfiguration.java` 事务管理器配置**:
  ```java
  @Bean(name = "bizSystemTransactionManager")
  public PlatformTransactionManager bizSystemTransactionManager(@Qualifier("bizProxyDataSource") DataSource dataSource) {
      return new DataSourceTransactionManager(dataSource);
  }
  ```

---

### 4) 关键场景与演示描述

- **场景一：创建配置文件**。讲师在 IDEA 的项目结构中，右键点击 `resources` 目录，选择“新建” -> “文件”，分别创建 `registry.conf` 和 `file.conf` 文件，并在 `registry.conf` 中输入 Seata 的注册中心和配置中心信息。
- **场景二：添加 Maven 依赖**。讲师在 `pom.xml` 文件中，将光标定位到 `<dependencies>` 标签内，粘贴并格式化 Seata 的依赖配置，确保项目能识别并下载 Seata 的相关组件。
- **场景三：编写配置类**。讲师在 `src/main/java` 目录下创建 `SeataConfiguration.java` 文件，使用 `@Configuration` 注解声明其为 Spring 配置类，并通过 `@Bean` 方法创建 `GlobalTransactionScanner` 实例，配置其 `applicationId` 和 `txServiceGroup`。
- **场景四：配置数据源代理**。讲师在 `DruidSystemDataSourceConfiguration.java` 文件中，通过 `@Bean` 方法创建 `DataSourceProxy`，并传入 `bizSystemDataSource` 作为参数，将业务数据源包装为支持 Seata 事务管理的数据源。
- **场景五：配置事务管理器**。讲师在 `BizSystemDataSourceConfiguration.java` 文件中，通过 `@Bean` 方法创建 `PlatformTransactionManager`，并使用 `@Qualifier` 注解指定其绑定的数据源为 `bizProxyDataSource`，确保事务管理器能正确管理事务。

---

以上是根据视频画面进行的结构化技术课程分析，内容准确反映了讲师在视频中演示的技术要点和操作步骤。
