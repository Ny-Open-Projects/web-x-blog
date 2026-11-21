# 23-智能调度服务（实现过程_环境搭建） — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来呢,咱们继续来看智能调度服务

前面呢,我们是说了一下智能调度服务它的数据模型,对吧

在这呢,一共涉及到了这么几张表

好,那接下来呢,下一个小节就是我们智能调度服务它的实现过程

整个这个实现过程啊,其实还是比较复杂的

通过我们前面再进行业务说明,大家也能感受到,对吧

那么这块呢,它的业务呢,是比较复杂的

那么对应的,我们要实现的,肯定也是比较复杂的

好,首先呢,我们先来看啊,咱们要操作的呢

也就是我们要编写的Maven工程啊,就是这个,叫做PD-Dispatch

好,当前这个工程呢,是一个空的,对吧

里边呢,什么东西都没有,只是创建了一个包结构

好,那么我们首先呢,需要来做一个基础环境的搭建

这块呢,会涉及到一些什么呢,比如说配置文件,对吧

还有相应的一些实体类

还有DTO啊,一些枚矩,还有MIPER,配置类,工具类,启动类等等这些

那么对于这一类的代码呢,我们就不在课上去手写了

这个会占用我们很多时间,对吧,而且没有什么基础含量

所以这块呢,这些呢,咱们就直接啊,在我们资料里边已经提前整理好

我们直接把它一次性导入就可以了

好,咱们来看一下,在咱们这个资料当中

你看,智能调度服务,基础环境

然后呢,这是有配置文件

这两个配置文件呢,我们直接复制进来就可以了

好,直接在这儿来复制一下

然后呢,我们把它放在咱们这个resource目录下边

好,直接粘贴在这个位置

简单大概,大概看一下就可以了啊

这配置呢,还是常规的配置,没什么区别

然后呢,它激活的是DEV,也就是说它使用的是这个配置文件

好,然后呢,还是一些常规的配置,对吧

那就是作为discovery了

还有config,配置中心

好,下面这些呢,也没什么特殊的

好,直接拿过来就可以了

好,这是配置文件

然后接下来呢,就是其他的一些实体类,对吧

一些实体类啊,DTO啊,等等这些

好,然后呢,我们直接从这边

你看,这是我们的Java代码

好,咱们整个呢,把这一堆啊,复制

复制一下

好,复制到我们这个品达这个目录下面来

好,直接在这儿粘

OK,稍等一下啊

好,那么,已经粘贴过来了

然后呢,我们可以大概来看一下咱们考进来的东西啊

首先呢,先来看这个entity,这是实体,对吧

实体类

那么这块呢,所涉及到的实体类呢,有这么几个

简单看一下

这是我们这个缓存,这个线路子表

对应的其实我们前面这些表呢,我们都说过了,对吧

PD,什么catchline,detail

这是这个线路子表

然后呢,这是不是就是我们这个缓存线路表

然后呢,这个是什么,那个使用表,对吧,使用表

这个前面咱们在这个数据模型这块呢,是不是都已经介绍过这些表了

然后呢,我们这些实体类呢,跟表呢,是有这么一个对应关系啊

包括这里面的属性跟表里面的字段,是不是都有对应关系

然后呢,这个是最多的那个什么关联表,对吧

有什么司机啊,车辆啊,车次啊,还有什么订单分类啊,等等这些

然后呢,这个呢,是就是我们这个订单分类啊,订单分类

对应的就是这张表,这个实体

然后呢,这个是订单分类跟我们这个订单的那个关联,对吧

那么对应的也是有这么一个实体类啊

然后这是关于我们这个定时任务,对吧,定时任务

这个映射的就是我们这张表,schedule job,对吧,这个定时任务,这张表

好

然后还有一个呢,就是咱们这个定时任务的日期表,对吧

日志表,日志表,好

OK,这是实体

因为我们前面这些表呢,都已经说过了

所以这个实体呢,就比较简单了

直接就是一个映射

然后呢,还有DTO

所涉及到的DTO呢,就比较多了,对吧,DTO比较多

你看这个呢,这是跟我们这个

进行这个路线规划的时候会使用到的DTO

路线规划的DTO

然后呢,这个是什么呢

这是我们这个

它继承了我们这个实体,对吧,catch line,DTO,entity

就是我们那个缓存线路子表

然后呢,它这里边扩展了这么两个,对吧

一个start agency

start agency

还有一个是end agency

就是一个是起始机构,一个是终点机构,等等

这里边呢,我们DTO到时候用到了再说吧

我们就不再一个一个去看了

DTO呢,它其实翻译过来就是数据传输对象,对吧

数据传输对象

一般呢,就是我们

在进行远程调用的时候呢

可能会把我们这个实体呢

进行一个封装,封装成DTO

来进行数据传输

然后呢,还有枚举,对吧

枚举

你看

叫schedule parameters

有什么线路,路线最近

什么成本最低,用时最少

中转次数最少,等等

这是我们定义成这个

枚举

然后呢,还有就是这个什么呢

我们这个定时任务

这个状态,对吧

它的状态就是这么两种啊

一个是暂停状态

还有一个是这个正常状态

分别用0还有1来表示

这么两个枚举

然后就是config,对吧

这就是我们的配置类啊

这个配置类呢

也都是常规的一些配置

这是关于我们这个

Jason的,对吧

还有这个swagger文档的

这些配置

包括这个什么mvc的配置啊

然后这个是mybedplus,对吧

因为要进行分页啊

所以需要把它配置上

然后呢

重点看的是这个

这个呢

就是关于我们这个定时任务的配置

对吧

但是这个代码呢

咱们前面在专门讲我们这个cause定时任务组件的时候呢

其实也说过了

也已经说过了

然后呢

在这儿再来强调一下

你看我们当前呢

是不是要创建这么一个叫做scheduler factory bit

通过它呢

可以来创建我们的调度工厂

对吧

创建我们这个

调度器啊

然后呢

这里边重点看的是谁呢

怎么体现出来我们这些任务要进行

这个定时任务要进行持久化呢

那么使用的就是这个

这个什么

org cause job store

对吧

叫class

那么它对应的就是这个

job store tx

这个是我们cause提供的

那这样的话呢

它就会将我们这些定时任务

由这个框架维护到我们相应的那套表结构当中

对吧

就是上面咱们再来看一下

这一堆表结构当中

但是下边呢

我们自己也有一个定时任务表

对吧

这个呢

就需要我们自己去维护

那么每一个组织机构呢

会对应这么一个定时任务啊

然后其他的呢

跟原先都是一致的

对吧

在这儿指定这个表明了他的前缀啊

然后呢

这个地方的还设置了一个什么呢

延时启动延时五秒钟再来启动啊

并不是说我们项目启动完之后

这定时任务马上就会启动

这个地方的是延时五秒

然后呢

才会去去启动啊

然后其他的基本上都是一样的

这是关于关于我们这个定时任务这个配置类

然后我们刚才导入的还有什么呢

还有就是这个Mapper对吧

Mapper的话呢

其实就是一些因为我们最终要操作那些表对吧

所以都会使用到Mapper啊

这个就比较简单了

都是继承了MapsPlus给我们提供的这个表呢

这个就比较简单了

我们的这个BaseMapper

然后呢

把相应的这个实体类是不是传进去就可以了啊

这是这几个Mapper

然后还有Utils对吧

这是一些工具类

这个到时候我们用到的时候呢

直接拿过来用就可以了

然后还有一个Future

这个Future里边的封装的其实是什么呢

是关于我们需要进行通过Fend进行远程调用的一些这个方法啊

比如说我现在呢

要远程调这个ORG API

这个这个Fend接口

那么你只要把这个接口给我传进来啊

把需要的参数传进来

然后他在这个内部呢

给我们去进行调用啊

这是对我们这个Fend进行了一个封装啊

然后呢

就是这个启动类的吧

这个启动类呢

就比较简单了

就是一个比较普通的启动类啊

这是我们导入的这个代码呢

咱们整体呢

过一下做到心里有数

然后一会儿呢

我们就需要干什么呢

来编写下一个就是关于这个定时任务的编写啊

那么这是关于这个定时任务的编写啊

那么这是关于这个定时任务的编写啊

那么这是关于这个定时任务的编写啊

咱们这个基础环境呢

我们就先说到这儿啊

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术课程分析。

---

### 1) 视频摘要

本视频是关于一个名为“品达物流TMS系统”（pd-dispatch）的Java后端项目的技术讲解。课程主要聚焦于“智能调度服务”模块，特别是“定时任务”功能的实现。讲师通过 IntelliJ IDEA 开发环境，逐步演示了如何配置项目、查看核心实体类（Entity）、定义调度参数枚举（ScheduleParams）、配置 Swagger 文档、自定义 Jackson 序列化/反序列化规则，以及编写和测试定时任务（ScheduleJob）的代码。视频内容旨在帮助开发者理解并实现一个基于 Spring Boot 和 Quartz 的定时任务调度系统。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 项目初始化与环境介绍。讲师展示了项目结构，包括 `pd-dispatch` 模块及其子模块（如 `pd-common`, `pd-web`），并打开了 `bootstrap-dev.yml` 配置文件。
*   **00:05 - 00:15**: 查看核心实体类。讲师浏览了 `entity` 包下的多个实体类，如 `CacheLineDetailEntity` 和 `ScheduleJobEntity`，并重点查看了 `ScheduleJobEntity` 的字段定义。
*   **00:15 - 00:25**: 查看数据传输对象（DTO）。讲师切换到 `AnalysisRoutePlanningDTO` 类，展示了其内部的 `Map` 结构和用于数据转换的 `for` 循环。
*   **00:25 - 00:35**: 定义调度参数枚举。讲师展示了 `ScheduleParams` 枚举类，其中定义了 `DISTANCE`、`COST`、`ESTIMATEDTIME` 等调度策略。
*   **00:35 - 00:45**: 配置 Swagger 文档。讲师查看了 `ConfigurationSupport.java` 文件，演示了如何通过 `addResourceHandlers` 方法配置 Swagger UI 的访问路径。
*   **00:45 - 00:55**: 自定义 Jackson 序列化配置。讲师展示了如何通过 `JacksonObjectMapper` 类自定义 JSON 序列化和反序列化规则，例如设置 `FAIL_ON_UNKNOWN_PROPERTIES` 和 `DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES`。
*   **00:55 - 01:05**: 编写定时任务。讲师展示了 `ScheduleJob` 类的代码，其中包含了 `JobExecutionContext` 和 `QuartzJobBean` 的导入。
*   **01:05 - 01:15**: 查看数据库表结构。讲师切换到 Navicat 数据库管理工具，展示了 `pd_dispatch` 数据库中的多个调度相关表，如 `QRTZ_TRIGGERS`、`QRTZ_JOB_DETAILS` 等。
*   **01:15 - 01:25**: 编写机构数据获取方法。讲师展示了 `PACompleteFuture.java` 文件中的 `agencyMapFuture` 方法，该方法使用 `CompletableFuture.supplyAsync` 和 `Stream` API 来异步获取机构数据。
*   **01:25 - 01:35**: 课程资料与文档。讲师展示了课程配套的 Markdown 文档，其中包含了“智能调度服务”的详细目录结构和代码示例。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 文档**:
    *   课程资料文档（Markdown 格式）：标题为“品达物流TMS项目”，包含“智能调度服务”、“定时任务”、“数据模型”等章节。
    *   代码示例：在文档中提供了 `ScheduleJob` 类的代码片段，用于演示定时任务的编写。

*   **代码关键内容**:

    *   **配置文件 `bootstrap-dev.yml`**:
        ```yaml
        discovery:
          server-addr: 68.79.63.42:8848
        config:
          server-addr: 68.79.63.42:8848
          group: pinda-tms
          namespace: 6107f553-3214-48d8-89c3-945f8446e3d9
        # Jackson时间格式化
        jackson:
          time-zone: ${spring.jackson.time-zone}
          date-format: ${spring.jackson.date-format}
        servlet:
          multipart:
            max-file-size: ${spring.servlet.multipart.max-file-size}
            max-request-size: ${spring.servlet.multipart.max-request-size}
            enabled: ${spring.servlet.multipart.enabled}
        ```

    *   **实体类 `ScheduleJobEntity.java`**:
        ```java
        @TableName("schedule_job")
        public class ScheduleJobEntity implements Serializable {
            @TableId(value = "id", type = IdType.INPUT)
            private String id;
            @TableField(fill = FieldFill.INSERT)
            private Long creator;
        }
        ```

    *   **枚举类 `ScheduleParams.java`**:
        ```java
        public enum ScheduleParams {
            DISTANCE("distance"),
            COST("cost"),
            ESTIMATEDTIME("estimatedTime"),
            TRANSFER("transfer");
            private String value;
            ScheduleParams(String value) { this.value = value; }
        }
        ```

    *   **配置类 `ConfigurationSupport.java`**:
        ```java
        @Override
        protected void addResourceHandlers(ResourceHandlerRegistry registry) {
            registry.addResourceHandler(...).addResourceLocations("/swagger-ui.html");
            registry.addResourceHandler(...).addResourceLocations("/webjars/**");
        }
        ```

    *   **自定义 Jackson 配置类 `JacksonObjectMapper.java`**:
        ```java
        class JacksonObjectMapper extends ObjectMapper {
            public JacksonObjectMapper() {
                this.configure(FALL_ON_UNKNOWN_PROPERTIES, false);
                SimpleModule simpleModule = new SimpleModule()
                    .addDeserializer(Enum.class, EnumDeserializer.INSTANCE);
                this.registerModule(simpleModule);
            }
        }
        ```

    *   **异步方法 `agencyMapFuture`**:
        ```java
        public static final CompletableFuture<Map<Long, Org>> agencyMapFuture(Api api, Integer agencyType, Set<String> ids, Long countId) {
            return CompletableFuture.supplyAsync(() -> {
                List<Long> idList = ids.stream().filter(item -> StringUtils.isNotBlank(item))
                    .mapToLong(id -> Long.valueOf(id)).boxed().collect(Collectors.toList());
                if (CollectionUtils.isEmpty(idList)) {
                    return new HashMap<>();
                }
                return result.getData().stream().collect(Collectors.toMap(Org::getId, org -> org));
            });
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与配置文件** (00:00-00:05)
    *   **描述**: 讲师在 IntelliJ IDEA 中打开了 `pd-dispatch` 项目，展示了其模块结构。随后，他双击打开 `src/main/resources/bootstrap-dev.yml` 文件，高亮显示了 `discovery` 和 `config` 配置块，说明了服务发现和配置中心的地址。

*   **场景二：实体类与数据库表结构** (00:05-00:15)
    *   **描述**: 讲师在项目中导航到 `entity` 包，依次查看了 `CacheLineDetailEntity` 和 `ScheduleJobEntity`。他特别强调了 `ScheduleJobEntity` 中的 `@TableName` 和 `@TableId` 注解，用于映射数据库表。随后，他切换到 Navicat 工具，展示了 `QRTZ_JOB_DETAILS` 和 `QRTZ_TRIGGERS` 等表的结构，说明了 Quartz 调度框架的数据库表。

*   **场景三：调度参数枚举** (00:25-00:35)
    *   **描述**: 讲师展示了 `ScheduleParams` 枚举类，其中定义了 `DISTANCE`、`COST`、`ESTIMATEDTIME` 等常量。他解释了这些枚举用于在调度任务中指定不同的优化策略。

*   **场景四：Swagger 文档配置** (00:35-00:45)
    *   **描述**: 讲师在 `ConfigurationSupport.java` 文件中，演示了如何通过 `addResourceHandlers` 方法配置 Swagger UI 的访问路径，解决了静态资源访问的问题。

*   **场景五：自定义 Jackson 配置** (00:45-01:05)
    *   **描述**: 讲师展示了如何自定义 `JacksonObjectMapper`，并设置了 `FAIL_ON_UNKNOWN_PROPERTIES` 为 `false`，以避免在反序列化时因未知属性而抛出异常。他还演示了如何注册自定义的 `SimpleModule` 来处理枚举类型。

*   **场景六：定时任务编写** (01:05-01:15)
    *   **描述**: 讲师展示了 `ScheduleJob` 类的代码，其中导入了 `org.springframework.scheduling.quartz.QuartzJobBean`。他解释
