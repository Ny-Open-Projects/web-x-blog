# 30-常见组件与中台化-常用组件服务介绍（分布式 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们来看一下我们这个分布式ID服务它的使用说明,也就是说我现在如果想使用这个服务,对吧,那么具体我如何把它应用起来,要应用的话呢,首先呢,我们需要把这个分布式ID服务呢,先把它部署起来,其实部署的话呢,指的就是部署我们这个server,因为我们刚才也提到了,咱们这块啊,所涉及到的这个Main用工程啊,你看,其实主要的就是这么三个模块,

对吧,client,car,还有server,其中呢,服务模块呢,其实就是这个server,所以说呢,我们只要把这个服务把它跑起来就可以了,由于这块比较简单啊,所以关于它的代码呢,咱们就不再看了,那么我们就直接啊,把这个Main用工程把它引到我们的开发工具里面来,我这个提前呢,已经引过来了,大家可以看一下,那么引过来之后啊,我们需要来看一下,你要想把这个server把它跑起来,

那么需要依赖什么呢,它其实需要依赖我们的MySQL数据库,需要依赖我们的MySQL数据库,而这个MySQL数据库啊,是在哪配置的呢,咱们可以通过这儿来看一下,你看,我在这儿其实是配置了两个数据源,对吧,配置了两个数据源,然后呢,都是,我在这个呢,全都是用的我本地的MySQL数据库,然后呢,一个叫什么,Distributed ID1,Distributed呢,指的就是分布式ID,对吧,

因为我这儿是两个数据库啊,一个是1,一个是2,好,然后呢,所以说我们要想运行起来呢,首先需要在你本地创建这么两个数据库,这个呢,我已经创建完了,然后呢,创建完这个数据库之后啊,需要在这两个数据库里边去创建两张表,咱们可以来看一下,你看,这是Distributed ID1,然后这里边呢,有这么两张表,这两张表呢,其实都是为我们到时候呢,设计的,

生成这种什么呢,为一标识,服务的,好,这两个数据库里边,这两张表呢,其实都是完全一样的,完全一样的,它是为了提高这个性能,所以说呢,我们是分成了这么两个库,对吧,实际上呢,如果你只有一个库也没有关系,也是可以用的啊,那么我们在这儿呢,是生成这么,创建这么两个库,然后这两个表的结构呢,在咱们这个Dux,大家可以看到,这里边呢,我整理了一个Circle脚本,

你直接去执行一下这个Circle脚本,其实就是两个键表语句,对吧,Curriculable,那么这样的话呢,就可以把这两张表给创建出来,这两张表创建出来,好,这是它所依赖的环境,其实还是比较简单的,就依赖一个数据库,其他的呢,比如说什么Redis啊,或者是服务的注册中心,配置中心都没有使用到,所以它运行呢,是比较简单的,只需要把这个数据库,对吧,创建出来,把这两张表创建出来,

然后呢,我们就,

就可以来进行启动了,你看我这儿其实已经启动完成了,我这儿已经启动完成了,启动完成之后啊,它这里边,我们要想生成这个ID,对吧,你其实直接调用它的Controller的方法就可以了,你看它这里边是不是获取自增型的ID,对吧,然后呢,你直接调它这个接口就可以,然后呢,这个是获取什么雪花算法的ID,对吧,然后呢,这个是使用号段模式,其实这个号段模式对应的就是什么呢,就是我们刚才说的这个,

这个叫做,

在某一个,也就是这种趋势递增,对吧,趋势递增,在某一个段之内来生成,所以说呢,我们如果说把这个服务跑起来之后啊,你其实直接通过FIN接口,对吧,来调它这个,这几个方法就可以来生成了,那么我们还提供了另外一种方式,就是为了能让我们这个使用端,对吧,比如说我想调这个服务,那么方便使用,怎么做呢,

怎么做呢,你直接引入这个client,也就是我这个client呢,其实已经做了封装,对吧,已经做了封装,所以说呢,你直接调用我们这个distributed ID,你可以把它看成是一个工具类,这里边呢,封装的是一些工具方法,直接调这个工具方法,它其实底层呢,就会干什么呢,就会去调用我们的这个server,它会进行这个远程调用,通过FIN来进行调用,最终呢,调到我们这个接口,最终呢,把这个ID给获取出来,

大概就是这么一个过程啊,所以说我们在这呢,先来简单说一下,就是大家如果要使用的话,首先呢,需要先把我们这个系统,对吧,分布式ID,然后这个服务呢,把它部署完,好,刚才呢,我们是说了如何进行部署,

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频是一节关于“分布式ID生成”的技术课程，主要演示了如何使用一个名为 `distributedid` 的开源项目来实现分布式环境下的唯一ID生成。课程内容涵盖了项目的整体架构、核心功能（如自增ID、雪花算法ID）、配置方法以及客户端如何调用服务。讲师通过 IntelliJ IDEA 开发环境，逐步展示了项目结构、配置文件（如 `application.yml`）、数据库表结构（`sequence_id`）以及服务端和客户端的 Java 代码实现。视频旨在教授观众如何在实际项目中集成和使用该分布式ID服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 课程开场，讲师在 Typora 文档中展示“分布式ID生成”课程的目录结构，重点介绍了“使用说明”章节。
*   **00:05 - 00:15**: 讲师切换到 IntelliJ IDEA，展示项目 `distributedid` 的整体结构，包括 `d-client`、`d-core` 和 `d-server` 三个主要模块。
*   **00:15 - 00:30**: 讲师打开 `application.yml` 配置文件，讲解如何配置数据库连接（`datasource`）和服务器端口（`server.port`）。
*   **00:30 - 00:45**: 讲师展示数据库表结构文件 `distributedid.sql`，重点讲解 `sequence_id` 表的创建语句，用于支持自增ID功能。
*   **00:45 - 01:00**: 讲师回到 `application.yml`，演示如何配置多个数据源（`dsl, ds2`）。
*   **01:00 - 01:15**: 讲师进入 `IdController.java`，展示服务端提供的三个核心接口：`/increment`（自增ID）、`/snowflake`（雪花算法ID）和 `/segment`（分段ID）。
*   **01:15 - 01:30**: 讲师展示客户端代码 `DistributedId.java`，讲解如何通过 `IdGenMap` 获取不同类型的ID，并演示了 `snowflakeFromServer()` 方法的调用。
*   **01:30 - 01:45**: 讲师总结，强调了分布式ID生成的重要性，并鼓励观众动手实践。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **章节标题**: “2.3.4. 使用说明”
    *   **核心概念**: “单调递增”、“信息安全”、“分布式ID生成系统部署完成后，第三方系统接入即可直接获取ID”。
    *   **依赖配置**: 在 `pom.xml` 中添加 `distributedid-client` 依赖。
    *   **配置文件**: `distributedid_client.properties`，用于配置服务端地址。

*   **代码关键内容**:

    *   **服务端配置 (`application.yml`)**:
        ```yaml
        server:
          port: 18099
        servlet:
          context-path: /distributedid
        swagger:
          enable: true
        datasource:
          distributedid:
            names: dsl,ds2
            type: com.zaxxer.hikari.HikariDataSource
            dsl:
              driver-class-name: com.mysql.cj.jdbc.Driver
              url: jdbc:mysql://127.0.0.1:3306/distributedid?serverTimezone=Asia/Shanghai&characterEncoding=utf8
              username: root
              password: root
            ds2:
              driver-class-name: com.mysql.cj.jdbc.Driver
              url: jdbc:mysql://127.0.0.1:3306/distributedid2?serverTimezone=Asia/Shanghai&characterEncoding=utf8
              username: root
              password: root
        ```

    *   **数据库表结构 (`distributedid.sql`)**:
        ```sql
        CREATE TABLE `sequence_id` (
          `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增主键',
          `biz_type` char(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '业务类型',
          PRIMARY KEY (`id`) USING BTREE,
          UNIQUE INDEX `uniq_biz_type` (`biz_type`) USING BTREE
        ) ENGINE=InnoDB AUTO_INCREMENT=6 CHARACTER SET=utf8 COLLATE=utf8_general_ci ROW_FORMAT=COMPACT;
        ```

    *   **服务端控制器 (`IdController.java`)**:
        ```java
        @RestController
        @Api(tags = "分布式ID服务")
        public class IdController {
            @Autowired
            private String idGenMap;

            @GetMapping("/increment")
            public RestResponse<Long> autoincrement(@ApiImplicitParam(name = "bizType", value = "业务类型", required = true, dataType = "String") String bizType) {
                Long id = idGenMap.get("autoincrement").nextId(bizType);
                return RestResponse.success(id);
            }

            @GetMapping("/snowflake")
            public RestResponse<Long> snowflake() {
                Long id = idGenMap.get("snowflake").nextId(key: "");
                return RestResponse.success(id);
            }

            @GetMapping("/segment")
            public RestResponse<SegmentId> segment(@ApiImplicitParam(name = "bizType", value = "业务类型或者服务名", required = true, dataType = "String") String bizType) {
                SegmentId segmentId = idGenMap.get("segment").getNextSegmentId(bizType);
                return RestResponse.success(segmentId);
            }
        }
        ```

    *   **客户端工具类 (`DistributedId.java`)**:
        ```java
        public class DistributedId {
            private static IdGenClientFactory clientFactory = IdGenClientFactory.getInstance(null);

            public static Long autoincrementId(String bizType) {
                return clientFactory.getAutoincrementId(bizType);
            }

            private static Snowflake snowflake = new Snowflake();

            public static Long snowflake() {
                // ... 实现
            }

            public static Long snowflakeFromServer() {
                return clientFactory.getSnowflakeId();
            }

            public static List<Long> segment(String bizType, Integer batchSize) {
                // ... 实现
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示 (00:05-00:15)**:
    讲师在 IntelliJ IDEA 中打开项目，通过项目导航面板，向观众展示了 `distributedid` 项目的三个核心模块：`d-client`（客户端）、`d-core`（核心逻辑）和 `d-server`（服务端）。这为后续的代码演示奠定了基础。

*   **场景二：配置文件详解 (00:15-00:45)**:
    讲师打开 `application.yml` 文件，逐行讲解配置项。他特别强调了 `server.port` 用于设置服务端口，`datasource` 配置用于连接数据库，以及 `context-path` 用于设置API的访问路径。他还展示了如何配置两个数据源 `dsl` 和 `ds2`，以支持多库场景。

*   **场景三：数据库表结构 (00:30-00:45)**:
    讲师切换到 `distributedid.sql` 文件，高亮显示了 `sequence_id` 表的创建语句。他解释了该表用于存储自增ID的序列信息，其中 `id` 字段是自增主键，`biz_type` 字段用于区分不同业务类型的ID。

*   **场景四：服务端接口演示 (01:00-01:15)**:
    讲师进入 `IdController.java`，通过高亮和滚动，向观众展示了三个API接口：
    *   `/increment`: 用于获取自增ID。
    *   `/snowflake`: 用于获取雪花算法生成的ID。
    *   `/segment`: 用于根据业务类型获取分段ID。
    他解释了每个接口的注解和参数含义，强调了这些接口的易用性。

*   **场景五：客户端调用演示 (01:15-01:30)**:
    讲师展示 `DistributedId.java` 文件，重点讲解了客户端如何通过 `IdGenClientFactory` 获取服务端的ID生成器。他演示了 `snowflakeFromServer()` 方法，说明客户端可以直接调用服务端的雪花算法生成器，而无需自己实现。

*   **场景六：总结与实践 (01:30-01:45)**:
    讲师总结了分布式ID生成的重要性，并鼓励观众将所学知识应用到自己的项目中。他强调了该开源项目的易用性和扩展性，为观众提供了实践的方向。
