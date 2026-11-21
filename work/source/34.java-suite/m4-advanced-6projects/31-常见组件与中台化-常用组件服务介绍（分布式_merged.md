# 31-常见组件与中台化-常用组件服务介绍（分布式 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好,那么接下来咱们继续来看我们这个分布式ID服务它的使用说明。

刚才我们是说了一下,在真正使用这个服务之前,咱们是不是需要先把它部署起来。

而这个部署其实比较简单,它只是依赖了一个MySQL数据库,对吧?

所以说你只需要把它依赖的MySQL数据库创建出来,把那些表创建出来就可以了,然后就可以正常启动这个服务了。

那么启动完这个服务之后,我们就需要来看一下这个服务启动好了,我作为第三方系统,对吧?

比如说我开发了一个系统,我想获得ID,对吧?

那么我就可以通过来干什么呢?调用你这个分布式ID服务来获取这个唯一的一个标识,对吧?

那么我们应该如何来做?其实比较简单。

第一步就是引入什么呢?引入我们这个client这个依赖。

其实这样的话,你就可以干什么呢?

把这个client是不是把它安装一下,安装到你本地的Maven仓库。

如果说你们团队协作的话,可能你的局域网环境还有你们自己公司的私服,对吧?

这个时候你可以把这个包把它安装到私服上去,这样的话整个公司就都可以去使用了。

那么这是安装,安装完之后,在你自己的项目里边就可以引入这个坐标,对吧?

引入这个坐标,你看这是引的我们这个distributed ID client。

把它引到你自己的项目当中去。

引进来之后呢,还需要来配置一下什么呢?

就是这么一个文件,叫做distributed ID-client.properties。

这个地方配置什么呢?其实就是配置我们这个服务,也就是我们刚才启动的这个server,对吧?

启动的这个server,它的IP还有端口。

这个呢,肯定就需要根据实际情况,对吧?

根据实际情况改成你自己的这个IP还有端口。

你比如说我现在这个服务是在我本地,

我这个端口号是多少呢?

我这个端口号的话,从这能够看到,我这个端口号是这个,18099,对吧?

是这个端口号。

所以说呢,到时候呢,你需要把这个地方是不是改成我们这个分布式ID服务,它的IP以及端口号。

好。

当然了,如果说我们部署了多个,对吧?

比如说我这个分布式ID服务呢,我部署的集群,那你这样的话,你就用这个什么呢,逗号进行分隔就可以了。

IP加上端口,对吧?

你部署了多个节点,用逗号分隔就可以。

好。

然后分隔完之后啊,我们就可以在自己的项目当中来调用什么呢?

调用这个类,它的这个静态方法。

而这个类在哪呢?

其实就是在咱们这个D3 Beauty的ID Client这个包里边。

它其实你可以把它看成就是一个工具类,对吧?

然后在这里边呢,你调用这些方法,它就可以来生成相应的这个ID。

那么只不过这些ID呢,它是不同类型的。

你像这个Auto Increment,

它是从服务端来获取什么呢?

自增型的ID。

然后在这儿呢,你需要传一个什么服务名。

然后呢,它其实本身呢,这个里边呢,还有本地生成雪花算法。

这个呢,其实就没有调服务。

然后这个是什么呢?

你看,Snowflake,然后From Server,

这就是从服务端是不是获取这个锁雪花算法等等。

所以说呢,我们直接呢,就可以去调用咱们这个Client端的。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

Client。

这里边呢

其实是有好几个静态方法

好几个静态方法

这些方法呢

有的呢

是从我们本地来获取

有的呢

是通过调用我们这个远程调这个server来获取

最终的目的就是生成一个什么呢

生成一个这个

这个唯一的标识

一会儿呢

我们可以给大家来演示一下这个效果

现在呢

咱们是只是对着讲义来说明了一下

对吧

应该如何操作

那一会儿呢

我们就可以把这个包呢

安装一下

然后我们创建一个新的项目

对吧

把它引进来

然后来看一下我们具体如何使用

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是对您提供的技术课程视频画面的结构化中文分析报告：

---

### 1) 视频摘要

本视频课程主要讲解了一个名为 `distributedid` 的分布式ID生成系统的客户端使用方法。讲师通过 IntelliJ IDEA 开发环境，结合 PPT 文档，演示了如何在 Java 项目中集成该客户端库，并通过配置文件和代码调用，实现三种不同模式的ID生成：本地自增ID、本地雪花算法ID、以及从远程服务端获取的雪花算法ID。课程内容侧重于实际操作和配置，旨在帮助开发者快速上手使用该分布式ID服务。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:05**: 视频开头，讲师在 IntelliJ IDEA 中展示项目结构，重点指向 `distributedid-client` 模块，并在代码编辑器中高亮显示 `DistributedId.java` 文件中的 `autoincrementId` 方法，介绍其功能是“本地直接生成ID，雪花算法”。
*   **00:05 - 00:10**: 讲师切换到 PPT 页面，展示“2.3.4. 使用说明”章节，讲解第一步：在项目的 `pom.xml` 中引入 `distributedid-client` 依赖。
*   **00:10 - 00:15**: 讲师在 PPT 上展示 `distributedid_client.properties` 配置文件的示例内容，包括服务器地址 `distributedid.server` 和超时时间设置。
*   **00:15 - 00:20**: 讲师在 PPT 上展示第三步：如何在 Java 代码中调用 ID 生成方法，分别演示了 `autoincrement`、`snowflake` 和 `snowflakeFromServer` 三种方式。
*   **00:20 - 00:25**: 讲师在 IntelliJ IDEA 中切换到 `application.yml` 文件，展示服务器和数据库的配置，以说明服务端的部署环境。
*   **00:25 - 00:30**: 讲师在 PPT 上再次强调 `distributedid_client.properties` 的配置项，并在代码示例中高亮显示 `DistributedId.autoincrement("your service name")` 的调用方式。
*   **00:30 - 00:35**: 讲师在 IntelliJ IDEA 中滚动查看 `DistributedId.java` 文件，展示 `snowflakeFromServer` 方法的实现，并在 PPT 上展示其对应的代码调用方式。
*   **00:35 - 00:40**: 讲师在 PPT 上展示 `DistributedId.java` 的类结构，包括 `clientFactory`、`snowflake` 和 `userMap` 等静态成员变量，解释其作用。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT 关键内容**:
    *   **章节标题**: “2.3.4. 使用说明”
    *   **第一步**: 引入依赖的 Maven 代码块：
        ```xml
        <dependency>
            <groupId>com.itcast.distributedid</groupId>
            <artifactId>distributedid-client</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        ```
    *   **第二步**: `distributedid_client.properties` 配置文件内容：
        ```
        #服务器地址
        distributedid.server=211.103.136.244:7315
        #部署多个的话，可自行添加
        #distributedid.server=211.103.136.244:7315,ip2:port,...
        #超时时间
        distributedid.readTimeout=5000
        distributedid.connectTimeout=5000
        ```
    *   **第三步**: Java 代码调用示例：
        ```java
        Long id = 0L;
        //从服务端获取自增型ID
        id = DistributedId.autoincrement("your service name");
        //本地生成雪花算法ID
        id = DistributedId.snowflake();
        //从服务端获取雪花算法ID
        id = DistributedId.snowflakeFromServer();
        ```

*   **代码关键内容**:
    *   **`DistributedId.java` 文件**:
        *   `public static Long autoincrementId(String bizType)` 方法：用于本地生成自增ID。
        *   `private static Snowflake snowflake = new Snowflake();`：用于本地生成雪花算法ID。
        *   `public static Long snowflakeFromServer()` 方法：用于从远程服务端获取雪花算法ID。
        *   `private static Map<String, Snowflake> userMap = new HashMap<>();`：用于管理不同业务类型的雪花算法实例。
        *   `public static List<Long> segment(String bizType, Integer batchSize)` 方法：用于按段模式生成ID。

---

### 4) 关键场景与演示描述

*   **场景一：项目结构与核心代码展示** (00:00-00:05)
    *   讲师在 IntelliJ IDEA 中打开项目，高亮显示 `DistributedId.java` 文件。
    *   通过代码注释 `//本地直接生成ID，雪花算法`，向观众说明 `autoincrementId` 方法的功能。
    *   通过代码注释 `//使用段模式返回单个ID`，向观众说明 `segment` 方法的功能。

*   **场景二：PPT 配置与调用方式讲解** (00:05-00:20)
    *   讲师切换到 PPT，讲解 `pom.xml` 中的依赖配置，强调需要引入 `distributedid-client`。
    *   讲师展示 `distributedid_client.properties` 文件，解释其配置项的作用，如服务器地址和超时时间。
    *   讲师在 PPT 上展示 Java 代码调用示例，分别演示了三种ID生成方式，并在代码中添加注释说明每种方式的用途。

*   **场景三：服务端配置与客户端调用对比** (00:20-00:35)
    *   讲师在 IntelliJ IDEA 中打开 `application.yml` 文件，展示服务端的配置，如 `server.port` 和 `datasource`。
    *   讲师在 PPT 上再次强调 `distributedid_client.properties` 的配置项，并在代码示例中高亮显示 `DistributedId.autoincrement("your service name")` 的调用方式。
    *   讲师在 IntelliJ IDEA 中滚动查看 `DistributedId.java` 文件，展示 `snowflakeFromServer` 方法的实现，并在 PPT 上展示其对应的代码调用方式。
    *   讲师在 PPT 上展示 `DistributedId.java` 的类结构，包括 `clientFactory`、`snowflake` 和 `userMap` 等静态成员变量，解释其作用。

---

以上是根据您提供的视频画面内容整理出的结构化报告。
