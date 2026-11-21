# 19-搭建TMS项目开发环境（修改Nacos命名空间 — 课程文稿（声音线+画面线 合并稿）

> 说明：本稿由管线本地朴素合并生成（声音线中文稿为骨架，画面线理解作为补充附录）。配置外部融合 API 后可获得更连贯的讲稿。

## 一、声音线文稿（中文）

好 刚才呢

咱们已经把我们这个Maven的初始工程

已经导入到我们IDL开发工具当中来了

并且呢 我们刚才也

向大家展示了一下我们这个Maven工程

它的一个结构

以及每一个Maven工程它的定位

它到底是干什么用的 对吧

它的功能定位是什么

以及呢 他们之间的这个调用关系 对吧

应该是谁调用谁

那么这么一个调用的层次关系

好 那么接下来呢

我们还需要来看一下

咱们来看一下我们导入的这个初始工程

咱们可以打开我们这个

副工程的POM文件来看一下

然后呢 因为我们这个

Maven工程

其实本质上来说呢

都属于Spring Boot的应用

所以说呢 在我们这个副工程上面

你看我通过Parent的标签

是不是继承了一个副工程

这个副工程呢 就是由Spring Boot给我们提供的

就是Spring Boot Starter Parent

咱们使用Spring Boot开发呢

是不是都需要来继承这么一个副工程

这是由Spring Boot给我们提供的

然后呢 下边呢 你看

我们通过Models

来指定什么呢

聚合了这么多模块 对吧

这些模块呢 其实对应的就是上面这一堆

就是把这堆模块是不是进行了一个聚合

然后呢 我们可以

这是聚合 对吧

聚合下面的子模块

聚合下面的子模块

OK

然后你看通过Packaging等于POM

是不是说明当前这个工程

它的定位是一个副工程 对吧

然后下面这一堆呢

这是不是在我们Properties标签里面来指定每一个框架

对吧

它的版本号 在这来统一的指定

然后呢 通过Dependency Management

在这来指定什么呢

指定我们使用的Spring Cloud它的版本

但是具体这个版本号呢

你看我们是不是刚才在这定义的

使用的是这个版本

好

然后还有什么呢

还有这个SWAG的 对吧

SWAG的

好

这是咱们副工程的POM文件

然后呢

下面子工程的POM文件呢

我们可以随便打开一个来看一下

你看这个子工程呢

它继承了我们刚才这个品达TMS Java这个副工程

继承了它

然后呢

这个叫做数据聚合服务

对吧

这是描述了一下

然后接下来呢

我们在这个POM文件里面其实已经为大家整理好了

每一个这个Main文工程

它依赖的这些Main文作标其实都已经提供好了

所以大家在开发的时候呢

就不用自己再去调整我们这个POM文件了啊

也就是说我们POM文件其实都已经整理好了

大家直接开发我们的代码就可以了

你看这里面所依赖的这些Main文作标呢

其实还是比较多的

这是这个

其他的也都是类似的

咱们再打开这个

你看这个是我们的基础服务

对吧

基础服务

然后呢

这里边的Main文作标呢

也都调整好了

那我们现在呢

需要来调整一个什么东西呢

就是啊

大家还记得我们刚才呢

是不是已经把我们这个NUCLS配置中心给配置好了

这里边我们是不是导入了这么多的配置文件

当然我们在导入这个配置文件之前呢

咱们是不是创建了一个新的命名空间

对吧

创建了一个新的命名空间

就是我们这个品达TMS

而现在我们这个项目开发的时候呢

我就希望使用我当前新创建的这个命名空间下面的这些配置

对吧

这些配置下

你看从这能看到品达TMS

所以说呢

我们需要来修改一下我们相应的配置文件

比如说我们这个PDM文件呢

这个PG-Aggregation

对吧

然后呢

咱们来找一下

这是不是有我们这个配置文件

但是这个配置文件呢

是一个总的配置文件

真正细节的配置呢

其实是在另外一个配置文件

有哪个配置文件呢

你注意看下边是不是有这三个呀

到底用的是哪一个呢

你看我们这是不是通过profiles来指定什么呢

当前我们激活的是DEV

这就说明啊

我们应该使用的是这个配置文件

Bootstrap-DEV

对吧

这个咱们前面学过

这个Springboard

Springcloud

应该都知道啊

好

那就说我们当前需要使用到的是这个配置文件

而在这个配置文件里边

大家可以看到

我们是不是通过Springcloud-NUCLS

在这来指定什么呢

一个是Discovery

这是咱们的NUCLS的服务注册中心

对吧

来指定Server Address

服务的地址

然后呢

Group

还有什么呢

Namespace等等这些

还有Config

NUCLS呢

是不是既可以作为注册中心

也可以作为配置中心

好

然后这是呢

配置中心服务的地址

然后呢

这个快占名

这个配置文件快占名

对吧

然后呢

还有搜索的组

还有Namespace

现在呢

我们需要改什么呢

咱们需要把这个Namespace给改掉

但是这个Server Address呢

其实我

我当前呢

就不用改了

大家在下边练习的时候呢

需要去改

对吧

因为呢

我当前使用的就是这个地址

那么你在练习的时候呢

需要自己去安装NUCLS

那么你把这个地址呢

改成自己的啊

那个安装NUCLS的

IP地址就可以了

好

现在你看我这个6879 6342

对吧

那么对应的就是我们当前使用的这个NUCLS服务

所以这个IP呢

就不用改了

包括端口呢

8848对吧

我这都没有动

所以我当前这个地方就不用改了

我唯一需要改的就是这个Namespace

这两个Namespace

那么我们需要改成什么呢

我们前面自己创建的这个对吧

新创建的这个

咱们把这个命名空间ID呢

给它复制过来

好

把这个来复制一下

然后改成我们这个新的

这个地方还有下边

这个地方

这就表示我们要要读取配置的话呢

是不是就会从新的这个命名空间下边去读取

当然了

作为这个服务的注册中心对吧

我当我当我当前这个服务呢

启动好之后呢

他也就会注册到我们这个注册中心去

你看现在呢

他其实是看不到的

你看我们这个服务管理

然后呢

服务列表对吧

你看

在我们当前这个品达天马S这个命名空间下边还没有服务的啊

就是因为我们当前的这服务都没有启动呢

等你启动完之后呢

这里边就能看到了

这些呢

你看这是我们其实已经启动过的

是吧

在当前这个天马S这是以前创建的命名空间

这些服务呢

都已经启动好了

当然我们课上呢

使用的是后边咱们新创建的这个命名空间

好

所以说呢

我们把这个切换到新的命名空间就可以了

呃

然后上下边呢

这个简单提一下

你看这有NUCLS

也说我们Spring Boot呢

咱们这个项目要访问我们NUCLS是需要进行健全的

大家可能注意到啊

以前我们好像没有去写这个也好使

这是因为什么呢

我们当前使用的这个NUCLS呢

是新版本1.3的啊

那么我们在这个Main文工程当中来访问我们这个呃配置的话

NUCLS配置的话呢

需要来进行健全

所以说呢

我们在这需要输入什么呢

我们用户名密码好

那么这块呢

我们简单提一下就可以了

所以说呢

我们接下来呢

就需要什么呢

把其他的啊

其他的这些配置文件

其他模块的配置文件呢

那也都按照我们刚才提到的这个规则

把它改过来就可以了啊

这个使用的也是DV

就说明我们要用这个配置文件对吧

然后呢

其实这个配置呢

都是类似的啊

然后呢

我们把这个改造一下就可以了

当然我在这呢

就不再占用大家过多时间了

好

一会儿呢

我在底下把剩下的这些呢

也都改过来就可以了

好

这个呢

是我们这个把这个导入的初始工程对吧

然后呢

跟我们刚才创建的这个NUCLS呢

切换到我们新的这个NUCLS配置中心

主要就是修改他的这个命名空间的ID就可以了

---

## 二、画面线理解（PPT / 公式 / 图表 / 演示）

好的，这是根据您提供的视频画面进行的结构化分析：

---

### 1) 视频摘要

本视频为一个关于“品达物流TMS项目”的技术教程，主要演示了如何在 IntelliJ IDEA 中查看和理解一个基于 Spring Cloud 的微服务项目的 Maven 依赖和配置文件。视频内容涵盖了项目的整体结构、父工程的 `pom.xml` 文件、各个子模块的 `pom.xml` 文件、以及如何通过 Nacos 配置中心进行服务注册与配置管理。视频旨在帮助开发者理解项目的模块划分、依赖关系和运行环境配置。

---

### 2) 按时间顺序的章节（带时间点）

*   **00:00 - 00:03**: 视频开头，展示 IntelliJ IDEA 的主界面，项目名为 `pinda-tms-java`，并列出了项目中的各个模块。
*   **00:03 - 00:14**: 展示父工程 `pinda-tms-java` 的 `pom.xml` 文件，重点讲解了 `<modules>` 标签中定义的各个子模块，如 `pd-common`, `pd-base`, `pd-web` 等。
*   **00:14 - 00:33**: 继续展示 `pom.xml` 文件中的 `<properties>` 和 `<dependencies>` 部分，详细说明了项目所依赖的各个库的版本，如 Spring Cloud Hoxton.SR3、MyBatis Plus 3.3.0、Druid 1.1.23 等。
*   **00:33 - 00:45**: 切换到子模块 `pd-aggregation` 的 `pom.xml` 文件，展示其作为子模块的配置，包括 `artifactId` 和 `version`。
*   **00:45 - 01:17**: 在 `pd-aggregation` 的 `pom.xml` 文件中，详细展示了其依赖的其他模块，如 `pd-common`, `pd-service-oms-domain`, `pd-service-base-domain` 等。
*   **01:17 - 01:30**: 继续展示 `pd-aggregation` 的 `pom.xml` 文件，重点讲解了其依赖的第三方库，如 MyBatis Spring Boot Starter、MyBatis Plus、Druid、Commons IO 等。
*   **01:30 - 01:35**: 切换回项目根目录，展示 `pinda-tms-java` 的项目结构。
*   **01:35 - 01:42**: 打开 `pd-aggregation` 模块下的 `bootstrap.yml` 文件，展示其配置内容，包括 Tomcat、Servlet、Spring 应用名称、环境配置等。
*   **01:42 - 01:50**: 切换到浏览器，展示 Nacos 配置中心的界面，列出项目中各个模块的配置文件，如 `pd-user-dev.yml`, `pd-oms-dev.yml` 等。
*   **01:50 - 01:55**: 在 Nacos 服务列表中，展示项目中各个微服务的注册情况，如 `pd-netty`, `pd-auth-server`, `pd-web-driver` 等。
*   **01:55 - 02:00**: 展示项目文档 `m.pom.xml.md`，其中包含项目结构图和 Maven 配置说明。

---

### 3) 出现的 PPT / 公式 / 图表 / 代码的关键内容

*   **PPT / 文档内容**:
    *   **项目结构图**: 展示了用户端、网关、应用层和微服务层的调用关系。用户端（如手机App）通过网关访问应用层，应用层再调用微服务层。
    *   **Maven 配置说明**: 文档中提到项目使用了通用权限系统中的两个 jar 包，并给出了对应的 Maven 坐标。

*   **代码关键内容**:
    *   **父工程 `pom.xml`**:
        ```xml
        <modules>
            <module>pd-common</module>
            <module>pd-base</module>
            <module>pd-oms</module>
            <module>pd-user</module>
            <module>pd-work</module>
            <module>pd-web</module>
            <module>pd-dispatch</module>
            <module>pd-aggregation</module>
            <module>pd-druid</module>
            <module>pd-netty</module>
        </modules>
        ```
    *   **父工程 `pom.xml` 依赖部分**:
        ```xml
        <properties>
            <java.version>1.8</java.version>
            <spring-cloud.version>Hoxton.SR3</spring-cloud.version>
            <spring-boot.version>2.2.5.RELEASE</spring-boot.version>
            <swagger.version>2.9.2</swagger.version>
            <spring-cloud-alibaba.version>2.2.1</spring-cloud-alibaba.version>
            <druid.version>1.1.23</druid.version>
            <java.version>1.8</java.version>
            <shiro.version>1.4.0</shiro.version>
            <commons.lang.version>2.6</commons.lang.version>
            <commons.io.version>2.5</commons.io.version>
            <lombok.version>1.18.4</lombok.version>
            <commons.io.version>2.5</commons.io.version>
            <http-core.version>4.4.9</http-core.version>
            <httpclient.version>4.5.14</httpclient.version>
            <mybatis-spring-boot-starter.version>2.1.0</mybatis-spring-boot-starter.version>
            <mybatis-plus.version>3.3.0</mybatis-plus.version>
        </properties>
        ```
    *   **子模块 `pd-aggregation` 的 `pom.xml`**:
        ```xml
        <parent>
            <artifactId>pinda-tms-java</artifactId>
            <groupId>com.iteima</groupId>
            <version>1.0.0-SNAPSHOT</version>
        </parent>
        <artifactId>pd-aggregation</artifactId>
        <version>1.0.0-SNAPSHOT</version>
        <description>数据聚合服务</description>
        ```
    *   **`pd-aggregation` 的依赖部分**:
        ```xml
        <dependency>
            <groupId>com.iteima</groupId>
            <artifactId>pd-common</artifactId>
            <version>1.0.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>com.iteima</groupId>
            <artifactId>pd-service-oms-domain</artifactId>
            <version>1.0.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>com.iteima</groupId>
            <artifactId>pd-service-base-domain</artifactId>
            <version>1.0.0-SNAPSHOT</version>
        </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>${mybatis-spring-boot-starter.version}</version>
        </dependency>
        <dependency>
            <groupId>com.baidou</groupId>
            <artifactId>mybatis-plus</artifactId>
            <version>${mybatis-plus.version}</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>${druid.version}</version>
        </dependency>
        <dependency>
            <groupId>commons-io</groupId>
            <artifactId>commons-io</artifactId>
            <version>${commons.io.version}</version>
        </dependency>
        ```
    *   **`pd-aggregation` 的 `bootstrap.yml`**:
        ```yaml
        server:
          uri-encoding: UTF-8
          max-threads: 1000
          min-spare-threads: 30
          port: 8191
          connection-timeout: 50000ms
        servlet:
          # context-path: /
        spring:
          application:
            name: pd-aggregation
            # 环境 dev/test/prod
            profiles:
              active: dev
        main:
          allow-bean-definition-overriding: true
        ```

---

### 4) 关键场景与演示描述

*   **场景一：项目结构概览** (00:00-00:03)
    *   **描述**: 视频开始时，演示者在 IntelliJ IDEA 中打开了项目 `pinda-tms-java`，并展示了项目目录结构，包括 `pd-aggregation`, `pd-base`, `pd-common`, `pd-web` 等多个模块，为后续讲解奠定基础。

*   **场景二：父工程依赖管理** (00:03-00:33)
    *   **描述**: 演示者打开父工程的 `pom.xml` 文件，通过高亮和滚动，重点讲解了 `<modules>` 标签中定义
