# 17-Seata-抢单分布式事务实现 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

接下来我们把分布式事物这块给实现一下

好了这块由于我们分布式事物它相对来说比较独立

那我们可以创建一个独立的工程

然后这个工程这一块谁需要去实现分布式事物

谁就可以直接依赖这个工程就可以了

好我们这一块先把这个工程给搭建一下

搭建一个相对独立的一个分布式事物的对应的模块

右键新建一个工程

工程就叫Secure Theta

好把工程名字输入一下点击下一步

那么这一块一配置之后

我们要引入相关的一个依赖包

那由于等会儿我们需要在这里配置数据源

而且是代理数据源

那这个代理数据源等会儿要跟我们持久层相关

所以我们这里要把MyBetis相关的包也给引入进来

那因此

我们找到MyBetis相关的包

这个给拷贝进来

在这一块

好这一块呢

简单说一下

它这里由于我们只需要保证编译的时候不出问题就可以了

所以我给它的一个作用范围是Provide

好接着还有一个Theta相关的包

这个可以给拷过来就行了

拷到这里

拷过来之后呢

我们紧接着去实现一下我们Theta相关的一些配置了

第一个首先是这一块

我们要配置一下代理数据源

那代理数据源这一块呢

我们来写一下

com.secure.theta.configure.datasource.configure

在这里写一个叫Spring

写个叫Configuration

然后我们在这里面开始去实现三个配置

第一个配置是配置我们

对应的一个Data Source

第二个配置呢

是要配置代理数据源

好第三个我们来说一下

第三个持久层

这一块持久层我们用的是MyBedis

那这一块MyBedis这一块有一个叫SuggestionFactory

它需要注入Data Source

那我们需要做什么事情呢

将注入的Data Source换成代理数据源

也就是第二个步骤这里配置的数据源

好那我们开始去实现一下相关的配置了

PublicDataSource

Data Source

LueDataSource

这一块我们用最的

最的Data Source

那这里就可以直接Lue最的Data Source了

好这一块呢

我们将会参考我们每个配置里面的一个数据源配置信息

也就是这个配置信息

这里面的Spring.DataSource这些配置信息

主要是参考这一块

所以我这里要写一个ConfigurationProperties

把这个Profix给加上去

Spring.DataSource

最后不要忘了把它交给Spring管理

好这一块配置了之后数据源有了

接下来我们开始配置我们的代理数据源

代理数据源呢

是我们Cita里面的叫

DataSourceProxy这一块哈

不要忘了是Cita包里面的

我们直接Lue个DataSourceProxy就行了

那不要忘了在这里把它交给容器管理啊

好这一块写了之后

还有一个地方

这里缺的是一个数据源

你需要把上面这个DataSource给注入进来就行了

那我们开始注入一下

最的DataSource把它注入进来给他

那么这一块我们这个代理数据源就搞定了

接着是持久层这一块数据源要更换

数据源呢你不能用他默认的数据源了

你要用代理数据源

这一块是SuccessingFactory

好我们这一块要Lue一个SuccessingFactoryBeam

选这个LueSuccessingFactoryBeam

然后这个时候他要有一个数据源的配置

这个数据源的配置呢

我们就需要用到代理数据源了

好我们先把它给返回

在上面这里不要忘了加一个bin

这里是这个对象点

getObject

抛一个异常出去

那么这个数据源就要换成代理数据源了

要用他了

所以这里我们要把它给注入进来

DataSourceProgress

行把它给拷过来就OK了

那目前为止代理数据源就创建好了

接着我们看第四个步骤

要配置微幅与C

与C的TC交互信息以及注册信息

那么这一块呢

我们就只需要在这里创建两个配置文件就可以了

那么这两个配置文件呢

在下面这里分别都有

第一个是注册的配置文件信息

叫register.configure

他的注册呢

可以注册到文件里面

Lacos, Eureka, Redis, DK, Console等等

好那我们这里就选择他默认的方式

叫文件去配置

行我们把这个注册的文件给创建一下

在这一块右键新建一个文件

叫register.configure

这里面的配置信息呢

我们就拷贝一下就好了

好我们重新粘

第一个是当前这一块注册用什么东西去注册

注册到哪里去

那注册到Lacos, Eureka都是可以的

我们这里呢选择默认的注册到文件里面去

哪个文件注册到哪里去

注册到Fielding Configure文件

因此这个文件是要有的

所以我们创建一下这个文件

那配置信息配置到哪里去

可以配置到文件里面

Lacos还有我们的DK

还有我们的Abro

还有我们的Console

就是这一块

行那我们这里选择的是注册到文件里面去

OK注册到文件里面

文件里面有什么内容呢

我们把这一段拷过来

首先我们看一下

在这一块注意哈

这一块其实就是我们与TC之间进行交互的一个配置

与TC之间进行交互呢

用的是我们的Laty

所以这一块是Laty相关的配置

我们就不管它了

后面这一块呢要着重关注这个Server配置就可以了

这个Server配置有一个Group

这个Group是什么呢

这个Group其实就是当前这一块

我们要参与分布式事务的哪些应用

它们是一个组

哪些组要参与分布式事务

就是这一块

这个组呢是

这个后面这个呢是组名

组名你可以随意去取

那我这里就取一个叫CitaSQLTransaction

那这一块一写之后

后面哪一个项目要参与分布式事务

那么你给它标记的组名得跟这个是保持一致的

好下面呢就是我们的Laty的配置了

下面有一个DefaultGroupList

这其实就是我们的一个CitaTC的地址

TC的地址这一块呢是IP加端口号就行了

IP加端口

这是这一个

行

这个呢大家一定要记住它是要改的

上面这个呢可改可不改

这是这一个

那后面呢我们其实就不用去关注了

后面这个不需要去更改了

默认的就行

好那我们这一块关于分布式事务这一块

它的一个抽取就搞定了

接着我们要看一下哪两个项目要参与分布式事务

一个是我们的一个是我们的故事

一个是我们的order

这两个要参与分布式事务

那它俩就要依赖刚才那个工程了

这个工程是要依赖的

好下面这里也要依赖的啊

两个都要依赖

这是一方面

接着我们再往这里看

这里配置了之后呢

紧接着还要去做另外一个事

在配置文件里面要告诉它

它是属于我们分布式事务哪个组

哪个组的

要跟它们对应的组绑定到一起去

哪个组呢

刚才这个文件里面有这个组名

组名叫Cita secure transaction

那么你这里这个组名就要跟它对应

那么以后它们这一块就是属于分布式事务的一组项目

一组将参与分布式事务

除了你这里要配置

那么上面这个故事呢

也是需要配置的

在这一块也得指定一下Cita

可以了

那到目前为止

这一块分布式事务在我们项目中去实现

分布式事务就搞定了

这个只是说参与了分布式事务哈

那具体分布式事务的实现在哪里实现呢

像刚才这一块是属于一些配置性东西

那如果你要实现分布式事务的话

你还需要在指定的方法上去添加一个注解

这个注解是什么注解呢

介绍一下注解就是我们最后这里说的

使用全局分布式事务的方法上添加注解

Global transaction

行添加一个注解

Global transaction

到目前为止分布式事务配置完成了

并且也已经实现了分布式事务的一个操作了

OK

这就是咱们秒杀项目里面

分布式事务的一个控制整体实现

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频课程是关于分布式事务框架 **Seata** 的实战配置与集成教程。讲师通过一个名为 `seckill` 的秒杀系统项目，详细演示了如何在 Spring Boot 项目中集成 Seata，以实现分布式事务的控制。核心内容包括：首先，安装并配置 Seata 的事务协调器（TC）服务；其次，在各个参与分布式事务的微服务（如订单服务、库存服务）的数据库中添加 `undo_log` 表；接着，配置数据源代理，将 MyBatis 的 `SqlSessionFactory` 与 Seata 的代理数据源绑定；最后，通过在业务方法上添加 `@GlobalTransactional` 注解来声明全局事务。整个过程旨在帮助开发者理解并实践 Seata 的核心机制。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，讲师介绍本节将讲解 Seata 的安装与配置。
*   **00:05 - 00:15**: 讲解 Seata 的 TC（事务协调器）安装。演示了使用 Docker 安装 Seata TC 的命令，并提供了官方下载地址。
*   **00:15 - 00:30**: 讲解如何在 Spring Boot 项目中添加 Seata 的依赖。展示了 `pom.xml` 文件中需要添加的依赖项，包括 `spring-cloud-starter-alibaba-seata`。
*   **00:30 - 00:45**: 讲解如何在数据库中创建 `undo_log` 表。展示了 Seata 的数据库初始化脚本，其中包含了 `PRIMARY KEY (id)` 和 `UNIQUE KEY ux_undo_log (xid, branch_id)` 等关键约束。
*   **00:45 - 01:00**: 讲解如何配置数据源代理。在 `DataSourceConfig.java` 中，首先创建一个 `DruidDataSource`，然后通过 `DataSourceProxy` 包装它，以实现对数据源的代理。
*   **01:00 - 01:15**: 讲解如何配置 `SqlSessionFactory`。在 `DataSourceConfig.java` 中，将 `SqlSessionFactoryBean` 的 `dataSource` 属性设置为代理数据源，从而在 MyBatis 中使用 Seata 的事务管理。
*   **01:15 - 01:30**: 讲解如何配置 Seata 的注册中心。展示了 `registry.conf` 配置文件，其中配置了 `file` 类型的注册中心，并设置了 `transport` 的相关参数。
*   **01:30 - 01:45**: 讲解如何配置 Seata 的服务端。展示了 `application.yml` 配置文件，其中配置了数据库连接信息、Nacos 注册地址、Redis 配置等。
*   **01:45 - 02:00**: 讲解如何在业务代码中使用 `@GlobalTransactional` 注解。展示了 `OrderServiceImpl` 中的 `add` 方法，该方法上添加了 `@GlobalTransactional` 注解，以声明这是一个全局事务。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文本内容**:
    *   **Seata 安装步骤**: 1. 在每个需要控制分布式事务的数据库中添加日志表 `undo_log`；2. 安装 TC；3. 配置数据源-代理数据源；4. 配置微服务与 Seata 的 TC 交互信息以及注册地址；5. 使用全局分布式事务的方法上添加注解 `@GlobalTransactional`。
    *   **Seata TC Docker 安装命令**: `docker run -d --name seata-server -p 8091:8091 -e SEATA_PORT=8091 seataio/seata-server:latest`
    *   **Seata 依赖配置**: `<dependency> <groupId>com.alibaba.cloud</groupId> <artifactId>spring-cloud-starter-alibaba-seata</artifactId> <version>0.0.1-SNAPSHOT</version> </dependency>`
    *   **数据库表结构**: `PRIMARY KEY (id), UNIQUE KEY ux_undo_log (xid, branch_id)`

*   **代码关键内容**:
    *   **`pom.xml` 依赖配置**:
        ```xml
        <dependency>
            <groupId>com.alibaba.cloud</groupId>
            <artifactId>spring-cloud-starter-alibaba-seata</artifactId>
            <version>0.0.1-SNAPSHOT</version>
        </dependency>
        ```
    *   **`DataSourceConfig.java` 配置**:
        ```java
        @Configuration
        public class DataSourceConfig {
            @Bean
            public DruidDataSource dataSource() {
                return new DruidDataSource();
            }
            
            @Bean
            public DataSourceProxy dataSourceProxy(DruidDataSource dataSource) {
                return new DataSourceProxy(dataSource);
            }
            
            @Bean
            public SqlSessionFactory sqlSessionFactory(DataSourceProxy dataSourceProxy) throws Exception {
                SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
                sqlSessionFactoryBean.setDataSource(dataSourceProxy);
                return sqlSessionFactoryBean.getObject();
            }
        }
        ```
    *   **`registry.conf` 注册中心配置**:
        ```properties
        transport {
            # tcp udt unix-domain-socket
            type = "TCP"
            #NIO NATIVE
            server = "NIO"
            #enable heartbeat
            heartbeat = true
            #thread factory for netty
            thread-factory {
                boss-thread-prefix = "NettyBoss"
                worker-thread-prefix = "NettyServerNIOWorker"
                server-executor-thread-prefix = "NettyServerBossHandler"
                share-boss-worker = false
                client-selector-thread-prefix = "NettyClientSelector"
                client-worker-thread-prefix = "NettyClientWorkerThread"
            }
        }
        ```
    *   **`application.yml` 服务端配置**:
        ```yaml
        server:
          port: 18085
        application:
          name: seckill-order
        datasource:
          driver-class-name: com.mysql.cj.jdbc.Driver
          url: jdbc:mysql://db-server:3306/seckill_general?useUnicode=true&characterEncoding=utf8
          username: root
          password: 123456
        cloud:
          config:
            file-extension: yaml
            server-address: nacos-server:8848
        alibaba:
          seata:
            tx-service-group: seckill
        redis:
          cluster:
        ```

---

### 4) 关键场景与演示描述

*   **场景一：安装 TC 服务** (00:05-00:15)
    *   **描述**: 讲师在屏幕上展示了 Docker 命令行界面，输入并执行了安装 Seata TC 的命令 `docker run -d --name seata-server -p 8091:8091 -e SEATA_PORT=8091 seataio/seata-server:latest`。同时，屏幕右侧的 PPT 显示了安装 TC 的步骤。

*   **场景二：添加 Seata 依赖** (00:15-00:30)
    *   **描述**: 讲师在 IDE 中打开 `pom.xml` 文件，将 Seata 的依赖项粘贴到 `<dependencies>` 标签内，并展示了依赖的 `groupId`、`artifactId` 和 `version`。

*   **场景三：配置数据库表** (00:30-00:45)
    *   **描述**: 讲师在 PPT 上展示了 Seata 的数据库初始化脚本，重点讲解了 `PRIMARY KEY (id)` 和 `UNIQUE KEY ux_undo_log (xid, branch_id)` 等关键约束，强调了这些表在分布式事务中的作用。

*   **场景四：配置数据源代理** (00:45-01:00)
    *   **描述**: 讲师在 `DataSourceConfig.java` 文件中，首先创建了一个 `DruidDataSource`，然后通过 `DataSourceProxy` 包装它，以实现对数据源的代理。

*   **场景五：配置 SqlSessionFactory** (01:00-01:15)
    *   **描述**: 讲师在 `DataSourceConfig.java` 文件中，将 `SqlSessionFactoryBean` 的 `dataSource` 属性设置为代理数据源，从而在 MyBatis 中使用 Seata 的事务管理。

*   **场景六：配置注册中心** (01:15-01:30)
    *   **描述**: 讲师在 `registry.conf` 文件中，配置了 `file` 类型的注册中心，并设置了 `transport` 的相关参数，如 `type`、`server`、`heartbeat` 等。

*   **场景七：配置服务端** (01:30-01:45)
    *   **描述**: 讲师在 `application.yml` 文件中，配置了数据库连接信息、Nacos 注册地址、Redis 配置等，以确保服务能够正常运行。
