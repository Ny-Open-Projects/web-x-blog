# 12-SEATA集成运用-交易服务集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着在交易服务里面去实现CETA的集成配置

在做集成之前,咱们先说明一下

CETA对Double,Fint有着较好的支持

我们这里采用的是GRBC作为微服务的通讯方式

CETA呢,它暂时还没有很好的支持

但这个也没有关系

我们可以去做一些调整和修改

经过咱们的实际验证和测试

在代码当中做相应的调整也是可以正常使用的

因为CETA能够支持Double和Fint

实质上是在拦截器里面做的封装和支持

它会传递XAD,也就是失误的全局唯一标识

这样就做到失误的有效控制

在下面章节,我们会做具体的修改和实现

另外,CETA呢,它只支持MySQL数据库

到0.8版本已经可以支持MySQL和Olico

我们的业务数据源

采用的是MilDb

MilDb是基于MySQL实现的

MilDb是能够兼容MySQL协议

所以CETA呢,它是可以支持MilDb的

除此之外,其他数据库暂时无法支持

PGSQL是不支持的

我们目前业务上也暂时不需要

这个并没有影响

在机身当中,针对PGSQL的数据源呢

我们就可以不用做相应的调整

这点大家要清楚

下面我们就要去修改交易服务的工程配置

在Resource

目录下面增加register.config文件

以及下面的file.config文件

之前讲解CETA组件使用的时候呢

对这两个文件也做了讲解

而咱们就将内容拷贝过去

回到工程当中

在交易服务的Resource支援目录下面

首先增加register.config配置文件

将内容拷贝进来

这里是去标识和配置它的注册模式

这里是采用file模式

然后下面是config

它的配置信息的使用模式

这个呢也是file模式

采用file模式要指定对应的文件名称

名称为file.config

我们将它创建一下

这里面的配置内容

我们从讲义当中拷贝进来

选中拷贝

这里面的配置内容我们回顾一下

这个是数据传输的配置信息

下面是service的配置信息

这个是虚拟组别的名称

这个名称是service的配置信息

这个名称呢要和服务端的配置

以及工程的配置内当中的配置名称要保持一致

下面是cdash server服务端的连接地址

这里我们采用的是一个变量名称

采用变量名的目的

是可以变于多环境版本的配置管理

这样我们就可以不用针对于不同的环境

写不同的多份配置

如果是调整了环境

只需要在POM当中多环境的版本变量当中

预设好对应的配置

预设好对应的配置连接地址就可以

咱们接着再看下面的配置

这个是客户端的使用配置信息

下面是事务日志的存储配置

因为这个是作为客户端

所以我们呢就直接采用文件的模式

在实际生产环境当中

特别是多个节点的情况下面

最好呢还是要采用db模式

接下来我们在POM文件当中增加CETA的依赖支持

增加注释

CETA

全部是事务依赖组件

Dupensys

group id是io.ceta

ceta all

然后指定它的版本watch

我们去通过变量指定

ceta.watch

这个版本采用的是0.9.0

版本号不要写错

让它导入生效

接着要去增加配置类

new Java class

名称就叫ceta

configuration

上面添加注解

configuration

首先要去拿到服务的运行名称

这个通过属性注入进来

application

value

绑定对应的变量

sprint-application

-name

这个属性就是获取

服务的名称

它就会读取工程配置里面所定义的

服务名称

sprint-application-name

它定义的是stop deal

那么在这里面

它的值就是stop deal

这个是作为分目式事务

客户端的唯一标识

接着我们要去定义全局分目式事务的散热器

global

consection

consection

scanner

添加并注解

然后创建

global

consection scanner

新建对象

传递刚才所定义的applicationid

然后是事务分组名称

stock

shared

group

大家要注意这个分组名称

要跟fileconfig里面配置的分组名称一致

不叫stockshared group

然后返回该对象

global

consection scanner

然后我们要去修改数据源的配置

交易服务之前采用的是基于mybatties的方数据源

因为Seta0.9版本

是不支持pg-circle

所以我们不需要修改交易数据源

只需要修改业务数据源就可以

打开dll的数据源配置

原有的信息不做调整

我们增加Seta的代理数据源配置

public

datasource

proxy

它的包是在Seta下面

biz

proxy

定义datasource

这个是java.x.circle下面的包

将业务数据源

录入进来

datasource

这里增加注解

确保

读者对象

没有错误

我们将它扣逼过来

这个是业务数据源

然后创建

Seta的代理数据源

datasource

将业务数据源

录入进去

然后要去定义并的名称

名称就叫biz

proxy

datasource

添加注解

这个是Seta

分布式事物

业务数据源的配置

这里定义完成之后

我们要去修改业务数据源的配置

修改两个地方

一个是circle session factory

将这里改成

我们刚才所定义的

Seta的代理数据源

我们做一个copy

要确保名称正确

否则Seta生活使用的时候不能正常生效

另外要去修改

biz transaction manager

将这个名称呢

去做个替换

改成bizproxy

datasource

好

这两处修改完成之后

那咱们就完成了

交易服务

对Seta的集成配置

好

这一讲的内容

咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程为“分布式事务解决方案”系列中的第17讲，核心内容是**集成 SEATA 作为分布式事务管理器**。讲师通过一个名为 `bulls-stock-deal` 的 Spring Boot 项目，详细演示了如何在现有微服务架构中引入 SEATA，以实现对交易服务下单流程的分布式事务支持。课程内容覆盖了 SEATA 的基本原理、工程配置（包括注册中心、配置中心、数据源代理）、核心配置类的编写，以及如何通过注解和配置文件来启用和管理分布式事务。讲师强调了 SEATA 对 gRPC 的支持、对不同数据库（如 MySQL、Oracle、PostgreSQL）的兼容性，并展示了如何通过 `@GlobalTransactional` 注解来声明事务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:15**：课程开场，讲师介绍本讲主题为“交易服务集成 SEATA”，并简要说明 SEATA 的作用是解决分布式事务问题。
*   **00:16 - 00:30**：讲解 SEATA 的集成说明，包括其对 gRPC 的支持、对 MySQL 和 Oracle 的兼容性，以及对 PostgreSQL 的暂不支持。
*   **00:31 - 00:45**：演示如何在项目中创建 `registry.conf` 配置文件，用于配置服务注册中心（如 Nacos、Eureka）。
*   **00:46 - 01:00**：展示 `registry.conf` 文件的具体内容，包括 `nacos`、`eureka`、`redis`、`zk` 等注册中心的配置。
*   **01:01 - 01:15**：讲解如何在 `pom.xml` 中添加 SEATA 的依赖，并配置多环境（dev、uat）的 `seata.address`。
*   **01:16 - 01:30**：演示如何创建 `SeataConfiguration` 配置类，用于初始化 `GlobalTransactionScanner`。
*   **01:31 - 01:45**：讲解 `@GlobalTransactional` 注解的使用，以及如何通过 `@ConfigurationProperties` 注解绑定配置。
*   **01:46 - 02:00**：展示如何配置数据源代理，通过 `@Bean` 注解创建 `DataSourceProxy`，并将其注入到业务逻辑中。
*   **02:01 - 02:15**：讲解 `registry.conf` 中的 `service` 配置，包括 `vgroup_mapping` 和 `default.grouplist`。
*   **02:16 - 02:30**：总结本讲内容，强调 SEATA 的集成步骤和关键配置点。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**：
    *   **章节标题**：`3.2 交易服务集成 SEATA`。
    *   **集成说明**：
        *   SEATA 对 DUBBO、FEIGN 有较好支持，对 gRPC 有支持（需调整）。
        *   SEATA 0.8 版本支持 MySQL 和 Oracle，PostgreSQL 暂不支持。
    *   **工程配置修改**：
        *   在 `resources` 目录下增加 `registry.conf` 文件。
        *   配置 `nacos`、`eureka`、`redis`、`zk` 等注册中心。
        *   配置 `seata.address` 的多环境变量（dev、uat）。

*   **代码关键内容**：

    *   **`registry.conf` 配置文件**：
        ```properties
        registry {
            # file, nacos, eureka, redis, zk
            type = "file"
        }

        nacos {
            serverAddr = "localhost"
            namespace = "public"
            cluster = "default"
        }

        eureka {
            serviceUrl = "http://localhost:1001/eureka"
            application = "default"
            weight = "1"
        }

        redis {
            serverAddr = "localhost:6381"
            db = "0"
        }

        zk {
            cluster = "default"
            namespace = "127.0.0.1:2181"
        }
        ```

    *   **`pom.xml` 依赖配置**：
        ```xml
        <profiles>
            <profile>
                <id>dev</id>
                <activation>
                    <activeByDefault>true</activeByDefault>
                </activation>
                <properties>
                    <package.environment>dev</package.environment>
                    <seata.address>127.0.0.1:8091</seata.address>
                </properties>
            </profile>
            <profile>
                <id>uat</id>
                <properties>
                    <package.environment>uat</package.environment>
                    <seata.address>10.10.20.21:8091</seata.address>
                </properties>
            </profile>
        </profiles>
        ```

    *   **`SeataConfiguration.java` 配置类**：
        ```java
        @Configuration
        @EnableAutoConfiguration
        @EnableDiscoveryClient
        @SpringBootApplication
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

    *   **`DruidSystemDataSourceConfiguration.java` 数据源配置类**：
        ```java
        @Configuration
        @EnableConfigurationProperties
        public class DruidSystemDataSourceConfiguration {
            @Bean(name = "tradeSystemDataSource")
            @Primary
            @ConfigurationProperties(prefix = "spring.datasource.tradesystem")
            public DataSource tradeSystemDataSource() {
                return new DruidDataSource();
            }

            @Bean("bizProxyDataSource")
            public DataSourceProxy bizProxyDataSource(@Qualifier("bizSystemDataSource") DataSource bizSystemDataSource) {
                return new DataSourceProxy(bizSystemDataSource);
            }
        }
        ```

    *   **`registry.conf` 中的 `service` 配置**：
        ```properties
        service {
            #vgroup->rgroup
            vgroup_mapping.stock_trade_group = "default"
            #only support single node
            default.grouplist = "${seata.address}"
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与配置文件创建**
    *   **描述**：讲师在 IntelliJ IDEA 中打开项目 `bulls-stock-deal`，在 `resources` 目录下创建 `registry.conf` 文件，并展示其内容。他强调了该文件用于配置 SEATA 的服务注册中心，如 Nacos、Eureka 等。

*   **场景二：多环境配置与 Maven 依赖**
    *   **描述**：讲师在 `pom.xml` 文件中展示了如何通过 `<profiles>` 配置多环境（dev、uat），并为每个环境设置不同的 `seata.address`。他解释了如何通过 Maven 的 `profiles` 功能来动态切换配置。

*   **场景三：核心配置类 `SeataConfiguration`**
    *   **描述**：讲师创建并展示了 `SeataConfiguration` 类。他重点讲解了 `@Configuration`、`@EnableAutoConfiguration`、`@EnableDiscoveryClient` 等注解的作用，并演示了如何通过 `@Value` 注解获取应用名称，以及如何创建并返回 `GlobalTransactionScanner` 实例。

*   **场景四：数据源代理配置**
    *   **描述**：讲师在 `DruidSystemDataSourceConfiguration` 类中，通过 `@Bean` 注解创建了一个名为 `bizProxyDataSource` 的 `DataSourceProxy`。他解释了 `DataSourceProxy` 的作用是将原始数据源包装成支持分布式事务的代理数据源，并通过 `@Qualifier` 注解指定要代理的数据源。

*   **场景五：`registry.conf` 服务配置**
    *   **描述**：讲师在 `registry.conf` 文件中配置了 `service` 部分，包括 `vgroup_mapping` 和 `default.grouplist`。他解释了 `vgroup_mapping` 用于将业务组映射到具体的注册组，而 `default.grouplist` 用于指定 SEATA 服务的地址。

*   **场景六：集成说明与兼容性**
    *   **描述**：讲师在 PPT 上展示了 SEATA 的集成说明，强调了其对 gRPC 的支持、对 MySQL 和 Oracle 的兼容性，以及对 PostgreSQL 的暂不支持。他指出，即使对 PostgreSQL 不支持，也可以通过调整代码来使用 SEATA。

---

以上是根据视频画面整理出的结构化技术课程分析。
