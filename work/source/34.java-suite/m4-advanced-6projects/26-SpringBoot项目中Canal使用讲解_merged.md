# 26-SpringBoot项目中Canal使用讲解 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

我们把这里保存一下

然后退出一下

再开始重启一下我们的cana

restart

cana

好重启之后呢

紧接着我们就开始做另外一个事情了

就是我们cana这一块啊

我就把它换成cana了

就不写mysec了

好

我们cana这一块啊

它监听到了这一个增量的数据

把增量的数据日子同步过来了

那么同步过来了之后呢

我的程序要获取这些数据

然后根据我的业务做一定的调整

那这个时候怎么办

我们可以写一个cana微服务

做什么事情呢

去订阅这个数据

订阅这个数据就可以了

好

我们来实现一下哈

那这一块我们要一个依赖

要有一个依赖

依赖第三方的

这一块呢

我们现在搭建这个cana微服务

这个cana微服务呢

主要是去读取监听到的一个变更的日子信息

那这个微服务咱取名叫cana

这就不说了

那这个项目呢

我们要依赖一个第三方的一个包

这个第三方的包用起来比较方便

等会儿我带你们去看一下

那这个第三方的包主要是去实现

对insert update delete相关的一个操作的一个增量数据监听

好

我们来看一下

第三方的这个包

它的一个用法哈

把这个地址打开

它也是我们github上的一个项目

我们打开看一下

在这一块呢

简单介绍一下哈

他这里还把我们看了又给介绍了一遍

咱就不再去说了

他的用法呢

比较简单

用法的话

直接在我们是不是不的项目里面引入他就可以了

引入这个依赖包

引入依赖包之后呢

这里有一些相关的属性要去配置

这些相关的属性

我们简单介绍一下

他这里有个看了点model

这个model这一块呢

其实就是标注你这块客户端所支持的一个类型

比如咱们这可以是简单的模式集群模式

这一可以卡卡模式

他默认是一个简单模式哈

可以不用写

因为有默认值

还有一个过滤器这块过滤器呢是一个简单模式的模式啊

你要过滤哪一些表

我们刚才不是配置过那个过滤吗

你可以自己在独立这儿配置

默认也可以不用写

还有一个就是你每次读取的消息的一个消息的一个数量哈

这里默认是每次读取一个就行了

还有一个消费超时时间

再就是我们看了这一块

如果以后有多个地址

那你可以写多个地址好

这个看了

这块注意一下这个看到设备的没有默认值是我们需要去写的

这个是必须的要写

还有个是第四个类型

第四个类型呢

其实就是咱这一块对应的一个对应的一个实例名称

我们刚才那里不是有一个一个占卜了吗

就是那个一个占卜了那个名字

好这里还有看到的用户名账号密码

这个可以不用写

group id这一块呢是针对咱们卡夫卡这一块的可以不用写

这一块是否是异部消息

这个呢

注意他默认其实就是异部消息

我们不用去管他

好

这个是针对卡夫卡的不用管

那也就是我们等会儿只需要配置这么几个点就行了

哪几个点呢

第一个首先是这个server地址要配置

实例这也要配置

这两个要配置

就行了

好

这个是我们要配置的

这些配置呢

直接在我们配置文件中配置是可以的

接着要用它怎么用

如果你当前这一块是支持jpg注解的话

那么这个时候可以直接用jpg注解

但如果你不是用jpg注解的话

他给你提供了一个相关的注解叫cannot table

取代以前jpg里面的table注解

这是这一块

好

那我们用的时候怎么用

用的时候需要实现这个接口in handler

in去handler

后面呢

写当前这个对应的加网并

这个加网并呢

其实就是你要跟哪个数据库数据对应的表建立一个关系的

这个加网并一定是数据库里面对应的一个表的一个映射信息

就这一块

而那个表的数据方式呢

如果发生变更

那么当前这个方法将会监听到哪个方法呢

比如增加会有映射的监听

修改会update的监听

删除会有delete进监听

那如果你想监听所有的表发生变化怎么办呢

在这里cannot table写过就行了

那么这个时候所有数据发生变化将会以map的形式推送过来

也会有映射的update delete

好

这是这一块

接着我们将使用一下这个工具来实现我们看了数据读取到我们当前微服里面来实现一个增量信息的一个消费

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的技术课程视频画面，进行的结构化中文输出：

---

### 1) 视频摘要

本视频课程主要讲解了如何使用 **Canal**（阿里巴巴开源的MySQL增量订阅&消费组件）来实现数据库的增量数据同步。课程内容涵盖了Canal的部署（通过Docker）、核心概念（如主从复制架构）、以及如何开发一个基于Spring Boot的微服务客户端来消费Canal监听到的数据库变更事件。讲师通过演示如何配置Canal、编写Java代码实现`EntryHandler`接口来处理`insert`、`update`、`delete`操作，并展示了如何使用`@CanalTable`注解来简化开发。整个课程旨在帮助开发者理解并实践Canal在分布式系统中的应用。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:30**: 课程开场，讲师介绍本节内容为“Canal微服务”，并展示终端界面，演示了在`conf`目录下查看配置文件（如`canal.properties`）的操作。
*   **00:30 - 01:00**: 讲师切换到绘图工具，展示了一个“主从复制”的架构图，图中包含MySQL主库、从库、以及一个“监听器”组件，用于说明Canal的工作原理。
*   **01:00 - 01:30**: 讲师切换到文档页面，展示课程大纲，重点指向“5.3 Canal微服务”章节，并介绍了该微服务的名称为`seckill1-canal`。
*   **01:30 - 02:00**: 讲师在GitHub页面上展示Canal的官方文档，重点讲解了如何通过Docker快速启动Canal服务，包括获取Docker镜像和运行脚本。
*   **02:00 - 02:30**: 讲师展示了一个系统架构图，该图描绘了“热点商品”相关的业务流程，包括用户认证、订单系统、库存系统等，用于说明Canal在实际业务场景中的应用。
*   **02:30 - 03:00**: 讲师进入GitHub的`canal-client`项目页面，介绍这是一个“易用的canal客户端”，并展示了其`README.md`文件中的“要求”和“特性”。
*   **03:00 - 03:30**: 讲师在代码页面中，详细讲解了`pom.xml`文件中的依赖配置，以及`canal.properties`配置文件中的关键属性，如`canal.mode`、`canal.server`等。
*   **03:30 - 04:00**: 讲师展示并讲解了`EntryHandler`接口的实现方法，包括`insert`、`update`、`delete`三个方法，并演示了如何通过`@CanalTable`注解来指定监听的表。
*   **04:00 - 04:30**: 讲师继续讲解`EntryHandler`的实现细节，展示了如何在`insert`方法中接收`User`对象，并在`update`和`delete`方法中接收`before`和`after`对象。
*   **04:30 - 05:00**: 讲师展示了如何使用`DefaultEntryHandler`来处理所有表的变更，并演示了如何通过`getMysql()`方法获取Canal的上下文信息。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT/图表**:
    *   **主从复制架构图**: 展示了MySQL主库和从库通过Canal进行数据同步的流程。
    *   **系统架构图**: 描绘了“热点商品”业务的完整流程，包括用户认证、订单、库存等模块。
    *   **课程大纲**: 明确了本节课程的结构和重点。
*   **代码**:
    *   **`pom.xml`依赖配置**:
        ```xml
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>canal-client</artifactId>
            <version>1.1.4</version>
        </dependency>
        ```
    *   **`canal.properties`配置**:
        ```properties
        canal.mode=simple
        canal.server=127.0.0.1:3306
        canal.destination=canal
        canal.user=canal
        canal.password=canal
        ```
    *   **`EntryHandler`接口实现**:
        ```java
        public class UserHandler implements EntryHandler<User> {
            @Override
            public void insert(User user) {
                log.info("新增 {}", user);
            }
            @Override
            public void update(User before, User after) {
                log.info("更新 {}", before, after);
            }
            @Override
            public void delete(User user) {
                log.info("删除 {}", user);
            }
        }
        ```
    *   **使用`@CanalTable`注解**:
        ```java
        @CanalTable(value = "t_user")
        @Component
        public class UserHandler implements EntryHandler<User> {
            // ... 方法实现 ...
        }
        ```
    *   **使用`DefaultEntryHandler`**:
        ```java
        @CanalTable(value = "all")
        @Component
        public class DefaultEntryHandler implements EntryHandler<Map<String, String>> {
            @Override
            public void insert(Map<String, String> map) {
                logger.info("Insert message {}", map);
            }
            @Override
            public void update(Map<String, String> before, Map<String, String> after) {
                logger.info("Update message {}", before, after);
            }
            @Override
            public void delete(Map<String, String> map) {
                logger.info("Delete message {}", map);
            }
        }
        ```

---

### 4) 关键场景与演示描述

*   **场景一：环境准备与配置**
    *   讲师在终端中执行`cd conf`命令，进入Canal的配置目录。
    *   讲师展示并解释了`canal.properties`文件中的关键配置项，如`canal.mode`、`canal.server`等，用于配置Canal监听的数据库。
*   **场景二：架构图展示**
    *   讲师在绘图工具中绘制并讲解了“主从复制”的架构图，说明Canal如何作为中间件，从MySQL主库读取binlog并同步到从库。
*   **场景三：微服务开发**
    *   讲师在GitHub页面上展示了`canal-client`项目的代码，重点讲解了`EntryHandler`接口的实现。
    *   讲师演示了如何编写一个`UserHandler`类，实现`insert`、`update`、`delete`方法，并通过`@CanalTable`注解指定监听的表。
*   **场景四：代码调试与运行**
    *   讲师在代码页面中，逐步演示了如何在`insert`方法中接收并打印`User`对象，在`update`方法中接收`before`和`after`对象。
    *   讲师展示了如何使用`DefaultEntryHandler`来处理所有表的变更，并通过`getMysql()`方法获取Canal的上下文信息。
*   **场景五：部署与启动**
    *   讲师在GitHub页面上展示了Canal的Docker部署文档，讲解了如何通过`docker pull`和`docker run`命令快速启动Canal服务。

---

以上是根据视频画面整理出的结构化信息，希望能帮助您更好地理解该技术课程的内容。
