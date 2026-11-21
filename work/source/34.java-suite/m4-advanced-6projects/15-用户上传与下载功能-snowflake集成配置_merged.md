# 15-用户上传与下载功能-snowflake集成配置 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

来,咱们接着呢

对Snowflake做项目的集成和使用

那么上一章节呢

咱们是实现了Global ID Generator

它作为一个工具类呢

放在Stockcom and Utils工程当中

那么接着的话呢

我们要在用户服务工程当中

去实现它的配置和使用

咱们就来从代码上做个实现

在Configure目录下面呢

我们去创建一个class

名称的话呢就叫Global System Configuration

我们看一下如何去集成和配置Snowflake呢

首先的话呢

我们要给它加上一个注解

然后呢我们就要去注入它的属性

这个属性的话呢

就包括Snowflake的工作中心ID

以及数据中心ID

通过value注入进来

读取配置文件当中的属性

Snowflake Worker ID

另外的话呢

就是它的数据中心的标识

上面呢是工作中心

Data Center ID

同样呢也将它属性录入进来

这个呢也叫Snowflake

Data Center ID

咱们呢加上对应的注释说明

这个呢就是Snowflake工作中心ID

这个呢就是Snowflake工作中心ID

之前呢咱们讲Snowflake工作机制上中呢

有提到对不对

它包括呢数据中心ID

以及呢工作中心ID

这个呢是Snowflake的数据中心ID

这样呢它就能够标识呢

每一个恢复节点

然后呢我们再将之前封装的

全局序列化生成器呢注入进来

先写它的方法

Public,Global,ID Generator

我们做一个判断

如果这个ID的话呢没有配置

或者是它为空的话呢

咱们就来采用它默认的方式进行创建

Global,ID Generator

如果说你有具体的值的话呢

那么就将这个值呢传递进去

通过构造方法传入进去

Work ID,ID Generator

然后呢这个生产ID

默认的话呢咱们可以看到

它会呢有一个数据中心的

会设定它有一个最大值

以及呢机器ID的最大的一个值

这样呢咱们就实现了

Global全局序列化ID的一个集成配置

咱们呢加上它的一个注释

这个呢是定义全局ID生成器

那么这两个值呢

咱们是不是应该

在工程配置文件当中去做配置呢

对不对

好

那么呢我们定义在最下面

将他们那个值呢拷贝回来

这个呢就是定义全局唯一ID的分布式的标识配置

因为呢微服务节点当中有很多个对不对

我们必须给它一个唯一的编号

这样呢他们所生成的ID才能保证了全局的唯一性

好那咱们呢回到讲义当中

如果是服务需要部署集群

按序列号呢去配置对应的值

这个呢不能随便配置

你必须要保证什么全局的唯一

每个服务配置的值呢不能重复

并且呢它的长度不能超过32

为什么呢

因为work ID和delta center ID呢

它只有预留了五位

那么最大值呢就是2.5次方

所以呢不能超过32位

这点呢大家要注意

如果说你是超过了32

这个呢是不生效的

它会去最大的ID

这个呢要明白清楚

好这样呢在用户服务工程当中

咱们呢就实现了这个工程呢

实现了snowflake的集成配置

那下面呢咱们就会做具体的运用

这一讲呢咱们就先讲到这里

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化技术分析。

---

### 1) 视频摘要

本视频片段是关于一个名为“bulls-stock”的Java Spring Boot项目的技术实现讲解。核心内容聚焦于如何在分布式系统中实现一个全局唯一的ID生成器，该方案基于Snowflake算法。讲师通过IDE（IntelliJ IDEA）展示了项目结构、配置文件（`bootstrap.yml`）和核心代码（`GlobalSystemConfiguration.java` 和 `GlobalIDGenerator.java`），详细说明了如何通过Spring Boot的`@Value`注解从配置文件中读取`workerId`和`datacenterId`，并用它们初始化一个Snowflake ID生成器。同时，视频也展示了如何配置Ceph存储服务用于文件上传，并处理相关的异常（如`ParamValidExceptionHandler`）。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 开场，展示项目结构和PPT大纲，引出“基于snowflake的全局分布式唯一ID”这一主题。
*   **00:05 - 00:15**: 展示用户服务模块的代码结构，重点指向`GlobalSystemConfiguration`类。
*   **00:15 - 00:30**: 在`GlobalSystemConfiguration`类中，使用`@Value("${snowflake.workerId}")`注解注入`workerId`，并定义`datacenterId`。
*   **00:30 - 00:45**: 在`GlobalSystemConfiguration`类中，定义并初始化`GlobalIDGenerator`实例，该实例会根据`workerId`和`datacenterId`进行配置。
*   **00:45 - 00:55**: 展示`GlobalIDGenerator`类的源码，其中定义了`workerIdBits`、`datacenterIdBits`、`sequenceBits`等关键常量，并计算了`workerIdShift`和`timestampLeftShift`。
*   **00:55 - 01:05**: 展示`bootstrap.yml`配置文件，其中配置了`snowflake`的`workerId`和`datacenterId`，并配置了Ceph存储的认证信息。
*   **01:05 - 01:15**: 讲解`workerId`和`datacenterId`的取值范围，强调它们只能是0-31（即5位二进制），最大值为`2^5`。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 大纲**:
    *   第2章 用户资料上传与下载功能
    *   3.3 基于snowflake的全局分布式唯一ID
    *   3.4 文件上传功能
    *   3.5 利用增强Token高效获取信息
    *   3.6 上传功能使用验证
    *   3.7 文件下载功能
    *   3.8 文件下载功能验证

*   **关键代码**:

    **`GlobalSystemConfiguration.java`** (配置类)
    ```java
    @Configuration
    public class GlobalSystemConfiguration {
        @Value("${snowflake.workerId}")
        private Long workerId;

        @Value("${snowflake.datacenterId}")
        private Long datacenterId;

        public GlobalIDGenerator globalIDGenerator() {
            if (null == workerId || null == datacenterId) {
                // 逻辑省略，用于初始化
            }
            return new GlobalIDGenerator(workerId, datacenterId);
        }
    }
    ```

    **`GlobalIDGenerator.java`** (ID生成器核心类)
    ```java
    private final static long workerIdBits = 5L; // 机器ID最大值
    private final static long datacenterIdBits = 5L; // 数据中心ID最大值
    private final static long sequenceBits = 12L; // 递增序列位数
    private final static long workerIdShift = sequenceBits; // 机器ID左移位数
    private final static long datacenterIdShift = sequenceBits + workerIdBits; // 数据中心ID左移位数
    private final static long timestampLeftShift = sequenceBits + workerIdBits + datacenterIdBits; // 时间毫秒左移位数
    ```

    **`bootstrap.yml`** (配置文件)
    ```yaml
    # 全局唯一ID分布式标识配置
    snowflake:
      workerId: 1
      datacenterId: 1

    # ceph swift 认证信息配置
    ceph:
      username: cephtester:subtester
      password: 654321
      authUrl: http://10.10.20.11:7480/auth/1.0
      defaultContainerName: user_datainfo
    ```

*   **关键公式/概念**:
    *   **Snowflake ID结构**: `timestamp + workerId + datacenterId + sequence`
    *   **取值范围**: `workerId` 和 `datacenterId` 均为5位二进制数，取值范围为0-31，最大值为 $2^5$。
    *   **ID生成逻辑**: 通过`workerId`和`datacenterId`的组合，确保在分布式系统中ID的全局唯一性。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构展示** (00:00-00:05)
    *   讲师在IDE中展示了项目`bulls-stock-user`的目录结构，重点指向`config`包下的`GlobalSystemConfiguration`类，为后续的ID生成器配置做铺垫。

*   **场景二：配置类开发** (00:15-00:30)
    *   讲师在`GlobalSystemConfiguration`类中，使用`@Value`注解从`bootstrap.yml`中注入`workerId`和`datacenterId`。他通过IDE的自动补全功能，展示了如何定义和初始化`GlobalIDGenerator`实例。

*   **场景三：ID生成器源码分析** (00:45-00:55)
    *   讲师切换到`GlobalIDGenerator`类，详细讲解了其中定义的几个关键常量：`workerIdBits`、`datacenterIdBits`、`sequenceBits`等。他解释了这些位数是如何用于计算`workerIdShift`和`timestampLeftShift`的，从而确定ID的各个部分。

*   **场景四：配置文件配置** (00:55-01:05)
    *   讲师在`bootstrap.yml`文件中，展示了如何配置`snowflake`的`workerId`和`datacenterId`，并配置了`ceph`存储服务的认证信息，为文件上传功能做准备。

*   **场景五：取值范围讲解** (01:05-01:15)
    *   讲师在PPT上强调，`workerId`和`datacenterId`的取值范围是0-31，最大值为$2^5$。他解释了这是为了确保在分布式系统中，每个服务实例的ID不会冲突。
